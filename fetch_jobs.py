import json, re, urllib.request
from datetime import date

GREENHOUSE = {
    'Anthropic': 'anthropic', 'Airbnb': 'airbnb', 'Reddit': 'reddit',
    'Discord': 'discord', 'Databricks': 'databricks', 'Stripe': 'stripe',
    'Datadog': 'datadog', 'Cloudflare': 'cloudflare', 'GitHub': 'github',
    'Snowflake': 'snowflake',
}

def slugify(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    return re.sub(r'\s+', '-', s.strip())

def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return json.loads(r.read())
    except Exception as e:
        print(f"SKIP {url}: {e}")
        return None

def title_ok(title, company):
    t = title.lower()
    if company == 'Anthropic':
        return 'product' in t and ('manager' in t or 'management' in t)
    senior = any(k in t for k in ['staff', 'group', 'director', 'principal'])
    pm = any(k in t for k in ['product manager', 'product management'])
    exclude = any(k in t for k in ['associate', 'intern', 'junior'])
    return senior and pm and not exclude

def loc_ok(loc):
    l = loc.lower()
    bad = ['on-site only', 'onsite only', 'in-office only']
    if any(b in l for b in bad):
        return False
    return True  # permissive — ATS data is clean, routine re-filters if needed

try:
    seen = json.load(open('seen_jobs.json'))
except Exception:
    seen = {}

roles = []

for company, token in GREENHOUSE.items():
    data = fetch(f'https://boards-api.greenhouse.io/v1/boards/{token}/jobs')
    if not data:
        print(f"FAILED: {company}")
        continue
    for j in data.get('jobs', []):
        if title_ok(j['title'], company) and loc_ok(j.get('location', {}).get('name', '')):
            roles.append({
                'company': company,
                'title': j['title'],
                'location': j.get('location', {}).get('name', ''),
                'url': j.get('absolute_url', ''),
                'posted': j.get('updated_at', ''),
            })

data = fetch('https://api.ashbyhq.com/posting-api/job-board/openai')
if data:
    for j in data.get('jobPostings', []):
        if title_ok(j['title'], 'OpenAI') and loc_ok(j.get('locationName', '')):
            roles.append({
                'company': 'OpenAI',
                'title': j['title'],
                'location': j.get('locationName', ''),
                'url': j.get('externalLink', ''),
                'posted': j.get('publishedDate', ''),
            })

data = fetch('https://api.lever.co/v0/postings/netflix')
if data:
    for j in data:
        if title_ok(j['text'], 'Netflix') and loc_ok(j.get('categories', {}).get('location', '')):
            roles.append({
                'company': 'Netflix',
                'title': j['text'],
                'location': j.get('categories', {}).get('location', ''),
                'url': j.get('hostedUrl', ''),
                'posted': str(j.get('createdAt', '')),
            })

new = []
for r in roles:
    jid = slugify(f"{r['company']}_{r['title']}_{r['location']}")
    if jid not in seen:
        r['job_id'] = jid
        new.append(r)

print(f"{len(new)} new / {len(roles)} matching / {len(seen)} previously seen")

if len(new) > 12:
    print("WARNING: >12 new roles — possible state corruption. Aborting.")
elif new:
    for r in new:
        seen[r['job_id']] = {
            'first_seen': date.today().isoformat(),
            'title': r['title'],
            'company': r['company'],
            'url': r['url'],
        }
    json.dump(seen, open('seen_jobs.json', 'w'), indent=2)
    json.dump({'date': date.today().isoformat(), 'roles': new}, open('pending_email.json', 'w'), indent=2)
    print(f"Wrote pending_email.json with {len(new)} roles")
else:
    print("No new roles")
