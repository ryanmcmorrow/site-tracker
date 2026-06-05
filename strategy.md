# Job Tracker Strategy Notes

## Last Updated: 2026-06-05

---

## Network Environment Constraints

**Critical:** This execution environment blocks all outbound requests except via WebSearch.
- All ATS API hosts return `403 Host not in allowlist` (Anthropic egress proxy enforcing allowlist)
- Blocked hosts include: `boards-api.greenhouse.io`, `job-boards.greenhouse.io`, `api.ashbyhq.com`, `api.lever.co`, `metacareers.com`, `careers.google.com`, `jobs.careers.microsoft.com`, `careers.snowflake.com`, `www.github.careers`, `cloudflare.com`
- **Workaround:** Use WebSearch for all companies. Greenhouse/Ashby/Lever pages surface clearly in Google results with correct ATS URLs.
- **Verification gap:** Cannot WebFetch individual job pages to confirm "Apply" button present; rely on WebSearch results from Google's index as a proxy for page validity.

---

## Per-Company Learnings

### Anthropic (Greenhouse token: anthropic)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/anthropic/jobs/{id}`
- Found ~12 open PM roles as of 2026-06-04; 10 additional (older) roles found 2026-06-05
- **Location note:** Anthropic is office-first (only ~8% of roles remote). Most PM roles list SF/NY/Seattle.
  - Confirmed remote-friendly: PM Revenue Platform (5077197008), PM Safeguards Privacy (5097486008), PM Growth (4124498008 — "Remote-Friendly, Travel-Required")
  - Company-wide policy: "at least 25% of the time in one of our offices" = floor of 25% in-office → meets location exception threshold
  - Older roles (4021723008–4557009008) found 2026-06-05 — likely open for longer; verify individual pages for in-office requirements
- Non-PM role found in feed: Analytics Data Engineering Manager, Product (5125387008) — excluded (not PM role)

### Airbnb (Greenhouse token: airbnb)
- API blocked — used WebSearch fallback
- **2026-06-04:** No Staff/Group/Director/Principal PM roles found.
- **2026-06-05:** Found Staff PM, AI Personalization (7834495) — confirmed "US Remote Eligible," salary $200K–$240K.
- URL pattern: `https://job-boards.greenhouse.io/airbnb/jobs/{id}`

### Reddit (Greenhouse token: reddit)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/reddit/jobs/{id}`
- **Excellent source:** Found 14+ Staff PM roles, all explicitly remote US-wide
- Reddit is aggressively hiring Staff PMs — will likely have new roles each cycle
- "Growth — New User Acquisition, Eastern Timezone" role explicitly prefers EST timezone — great Boston fit

### Discord (Greenhouse token: discord)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/discord/jobs/{id}`
- Found Staff PM and Group PM roles, all "San Francisco, CA or Remote (U.S.)" — qualifies
- **2026-06-05:** Found 2 additional Director of Product roles (5197403002, 5871614002) — both remote
- Note: "Director of Product Communications" (8542210002) was found but excluded — it's a communications role, not PM

### Databricks (Greenhouse token: databricks)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/databricks/jobs/{id}`
- Found ~5 Staff PM roles; location not explicitly confirmed as remote in search results
- Databricks.com page for Staff PM Network Security says "open to remote candidates" — suggests remote is available
- Verify location on individual pages; SF/Seattle are typical Databricks hubs

### Stripe (Greenhouse token: stripe)
- API blocked — used WebSearch fallback
- **Note:** Stripe jobs surface at `https://stripe.com/jobs/listing/{slug}/{id}` not `job-boards.greenhouse.io/stripe`
- All found Staff PM roles explicitly say "remote (35+ miles from a Stripe office)" — all qualify
- Found 9 Staff PM roles as of 2026-06-04; 2 more found 2026-06-05 (Link Balance 7118153, Enterprise Industries 7812856)
- Salary range: $194,800–$321,500 for Staff PM; Link Balance confirmed $214,300–$321,500

### Datadog (Greenhouse token: datadog)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/Datadog/jobs/{id}` (capital D in "Datadog" — must preserve case)
- Found: Director PM Applied AI (7616721), Staff PM OpenTelemetry (7555540)
- **Location concern:** Datadog HQ is NYC; found references to "New York, NY" for some roles
- User should verify if these offer remote or hybrid NYC (if hybrid NYC = not Boston compatible)

### OpenAI (Ashby slug: openai)
- API blocked — used WebSearch fallback
- **Result:** Only found standard PM roles (Product Manager, Codex; PM, API Agents; PM, Model Behavior) — all San Francisco
- No Staff/Group/Director/Principal PM roles surfaced in search
- OpenAI appears to use its own careers page (openai.com/careers) more prominently than Ashby job-board URLs
- Will retry with direct site:openai.com search in future runs

### Netflix (Lever slug: netflix)
- Lever API blocked — used WebSearch fallback
- **Key finding:** Netflix no longer uses Lever. Their ATS is at `explore.jobs.netflix.net` (Phenom-based)
- URL pattern: `https://explore.jobs.netflix.net/careers/job/{id}-{slug}`
- Found 3 confirmed remote US roles: Principal PM Games Social Platform, Principal PM Experimentation Platform, Group PM Security Platforms Engineering
- Los Gatos/LA roles excluded (on-site required outside Boston area)
- **Update Lever API call:** netflix slug on Lever returns empty — use WebSearch with explore.jobs.netflix.net

### Meta (WebSearch fallback)
- URL pattern: `https://www.metacareers.com/jobs/{id}` (verified correct format)
- Found: Principal PM Enterprise, Director PM Content Integrity, Director PM WhatsApp Growth
- **Location:** Meta has remote options for many roles; verify each posting for remote eligibility
- Login may be required to see full location details on metacareers.com

### Microsoft (WebSearch fallback)
- URL pattern: `https://jobs.careers.microsoft.com/global/en/job/{id}`
- **Result:** No specific qualifying roles found via WebSearch — general Microsoft PM listings came up but no role IDs
- Microsoft has many Principal PM roles but search didn't surface Boston/remote-specific ones
- Try `site:jobs.careers.microsoft.com "principal product manager" remote` in future runs

### Snowflake (WebSearch fallback)
- URL pattern: `https://careers.snowflake.com/us/en/job/{id}`
- **Result:** All found Principal PM roles are in San Mateo, CA or Menlo Park, CA — no remote roles found
- Snowflake appears to be largely office-based for PM roles — may be ineligible
- Monitor careers.snowflake.com for any remote-tagged roles in future

### GitHub (WebSearch fallback)
- URL pattern: `https://www.github.careers/careers-home/jobs/{id}` (confirmed correct)
- Found: Principal PM Agent Platform (5140), Principal PM (4884), Staff PM (4402)
- All listed as "United States" — likely remote-compatible (GitHub/Microsoft allows remote)
- Verify location on individual pages

### Cloudflare (WebSearch fallback)
- URL pattern: `https://cloudflare.com/careers/jobs/{id}`
- **Result:** No Staff/Group/Director/Principal PM roles surfaced in search results
- Cloudflare posts PM jobs on Greenhouse (found PM Intern posting there)
- Try `site:cloudflare.com/careers "product manager" senior` in future runs

---

## Title Filter Reference (non-Anthropic)
Include: Staff Product Manager, Group Product Manager, Director of Product Management, Principal Product Manager (or equivalent)
Exclude: Senior PM, Associate PM, or anything below Staff level

## Excluded Roles — Cumulative
- Analytics Data Engineering Manager, Product @ Anthropic (not PM)
- Director of Product Communications @ Discord (not PM)
- Product Manager (non-senior) roles at all companies
- All Snowflake roles (CA office-required)
- All OpenAI — no senior PM roles found (2026-06-04, 2026-06-05)
- All Microsoft — no specific role IDs found (2026-06-04, 2026-06-05)
- All Cloudflare — no qualifying roles found (2026-06-04, 2026-06-05)
- Datadog Group PM roles (Infrastructure/SDLC, Threat Management, Metrics) — hybrid but NYC-based; uncertain Boston compatibility
- Datadog Staff PM, AI — explicitly New York, NY; not Boston-compatible
- Reddit Staff PM Reddit Profiles (5888261) — older posting of same title as reddit-6478046; included 2026-06-05 for completeness

## 2026-06-05 New Discoveries (first pass, earlier in day)
- Airbnb re-entered tracker: Staff PM AI Personalization (7834495) — confirmed remote eligible
- Discord Director roles added: Friends (5197403002), Trust & Safety (5871614002) — both remote
- 10 older Anthropic PM roles (4021723008–4557009008) found — not in previous run's search results
- 9 older Reddit Staff PM roles (3464553–5888261) found — not in previous run's results; older IDs but still indexed
- 2 new Stripe Staff PM roles: Link Balance (7118153), Enterprise Industries (7812856)

## 2026-06-05 New Discoveries (second pass, current run)
- Anthropic PM Mobile (4933411008) — new role not found in earlier pass
- Reddit Principal PM - Ads Manager/Monetization (6762983) — new role
- Reddit Senior Group PM, Advertiser Optimization/Ads Marketplace (7858506) — new Group PM role
- Confirmed: Datadog all NYC-based hybrid, Microsoft 4 days/wk in-office → excluded from tracker
- Confirmed: Netflix migrated off Lever to explore.jobs.netflix.net (Phenom ATS)
- GitHub Staff PM (4402) at /careers-home/jobs/4402 confirmed valid URL; already tracked
- All WebFetch calls return 403 from execution environment — WebSearch-only verification strategy in effect
