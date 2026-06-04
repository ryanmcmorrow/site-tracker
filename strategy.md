# Job Tracker Strategy Notes

## Last Updated: 2026-06-04

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
- Found ~12 open PM roles as of 2026-06-04
- **Location note:** Anthropic is office-first (only ~8% of roles remote). Most PM roles list SF/NY/Seattle.
  - Confirmed remote-friendly: PM Revenue Platform (5077197008), PM Safeguards (5097486008)
  - Other PM roles may require >25% in-office — user should verify individual pages
- Non-PM role found in feed: Analytics Data Engineering Manager, Product (5125387008) — excluded (not PM role)

### Airbnb (Greenhouse token: airbnb)
- API blocked — used WebSearch fallback
- **Result:** No Staff/Group/Director/Principal PM roles found in search results. Only regular PM and Senior Manager roles.
- Airbnb appears to not currently have senior PM openings at the Staff+ level. Check again next run.

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
- Found 9 Staff PM roles; may be more
- Salary range: $194,800–$321,500 for Staff PM

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

## Excluded Roles This Run
- Analytics Data Engineering Manager, Product @ Anthropic (not PM)
- Director of Product Communications @ Discord (not PM)
- Product Manager (non-senior) roles at all companies
- All Snowflake roles (CA office-required)
- All Airbnb — no qualifying titles found
- All OpenAI — no senior PM roles found
- All Microsoft — no specific role IDs found
- All Cloudflare — no qualifying roles found
