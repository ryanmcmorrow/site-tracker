import json, re, urllib.request
from datetime import date

GREENHOUSE = {
    'Anthropic': 'anthropic', 'Airbnb': 'airbnb', 'Reddit': 'reddit',
    'Discord': 'discord', 'Databricks': 'databricks', 'Stripe': 'stripe',
    'Datadog': 'datadog', 'Cloudflare': 'cloudflare',
}

ASHBY_OLD = {'OpenAI': 'openai'}   # format: {"jobPostings": [...], "locationName": ...}
ASHBY_NEW = {'Snowflake': 'snowflake'}  # format: {"jobs": [...], "location": ...}

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
    return not any(b in l for b in bad)

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

for company, slug in ASHBY_OLD.items():
    data = fetch(f'https://api.ashbyhq.com/posting-api/job-board/{slug}')
    if not data:
        print(f"FAILED: {company}")
        continue
    for j in data.get('jobPostings', []):
        if title_ok(j['title'], company) and loc_ok(j.get('locationName', '')):
            roles.append({
                'company': company,
                'title': j['title'],
                'location': j.get('locationName', ''),
                'url': j.get('externalLink', ''),
                'posted': j.get('publishedDate', ''),
            })

for company, slug in ASHBY_NEW.items():
    data = fetch(f'https://api.ashbyhq.com/posting-api/job-board/{slug}')
    if not data:
        print(f"FAILED: {company}")
        continue
    for j in data.get('jobs', []):
        if title_ok(j['title'], company) and loc_ok(j.get('location', '')):
            roles.append({
                'company': company,
                'title': j['title'],
                'location': j.get('location', ''),
                'url': j.get('jobUrl', j.get('applyUrl', '')),
                'posted': j.get('publishedAt', ''),
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

if len(new) > 50:
    print("WARNING: >50 new roles — possible state corruption. Aborting.")
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
