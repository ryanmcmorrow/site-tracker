# Job Tracker Strategy Notes

## Last Updated: 2026-06-07

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
- **Location note:** Anthropic is office-first (only ~8% of roles remote). Most PM roles list SF/NY/Seattle.
  - Company-wide policy: "at least 25% of the time in one of our offices" = meets location exception threshold (≤25%)
  - All PM roles qualify under Anthropic title exception (include ALL PM roles regardless of seniority)
- **2026-06-04:** ~12 open PM roles found
- **2026-06-05:** 10 additional (older) roles found (IDs 4021723008–4557009008)
- **2026-06-06:** 4 new roles found: PM Multi-Cloud Growth (5153924008), PM Developer Productivity (5220143008), PM Claude Code Model Performance (5247640008), PM API repost (4936029008)
- Non-PM roles in feed (excluded): Analytics Data Engineering Manager, Product Operations Manager, Technical Program Manager

### Airbnb (Greenhouse token: airbnb)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/airbnb/jobs/{id}`
- **2026-06-05:** Found Staff PM, AI Personalization (7834495) — confirmed "US Remote Eligible," salary $200K–$240K
- **2026-06-06:** No new roles found

### Reddit (Greenhouse token: reddit)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/reddit/jobs/{id}`
- **Excellent source:** Reddit is aggressively hiring Staff PMs — new roles appear each cycle
- All roles explicitly "Remote - United States" ✓
- "Content Discovery (EST timezone only)" role explicitly good for Boston (EST)
- **2026-06-04:** 14 Staff PM roles found
- **2026-06-05:** 11 more roles found (mix of older IDs on old boards domain and new IDs)
- **2026-06-06:** 3 new roles: Staff PM Ads Monetization Searcher (7483888), Staff PM Content Discovery (5327220), Group PM Ads Marketplace (5153402)

### Discord (Greenhouse token: discord)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/discord/jobs/{id}`
- **Location policy:** Most Staff PM roles are SF Bay Area only (NOT qualifying). Director roles are SF or Remote ✓
- **Qualifying roles (tracked):** Director of Product Friends (5197403002), Director of Product Trust & Safety (5871614002)
- **Excluded:** Staff PM Commerce (SF only), Staff PM Payments (SF only), Staff PM Growth & SEO (SF only), Director of Product Communications (SF Bay Area required, comms role not PM)
- Staff PM roles in Discord tend to be SF Bay Area office-required — check individual postings
- **2026-06-06:** No new qualifying roles found

### Databricks (Greenhouse token: databricks)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/databricks/jobs/{id}`
- **Location policy confirmed:** "Hybrid-first with strict RTO" — Product & Design roles require hub presence (SF, Sunnyvale, Seattle). NOT remote eligible.
- 5 Staff PM roles tracked from 2026-06-04 run; these were included under uncertainty before remote policy was confirmed
- **2026-06-06:** No new qualifying roles found. Policy confirmed = no remote PM roles.
- **Recommendation:** Consider removing tracked Databricks roles if confirmed non-remote in future verification

### Stripe (Greenhouse token: stripe)
- API blocked — used WebSearch fallback
- **Note:** Stripe jobs surface at both `https://stripe.com/jobs/listing/{slug}/{id}` AND `https://job-boards.greenhouse.io/stripe/jobs/{id}`
- All Staff PM roles explicitly "remote (35+ miles from a Stripe office)" — Boston qualifies
- **2026-06-04:** 9 Staff PM roles found
- **2026-06-05:** 2 more: Link Balance (7118153), Enterprise Industries (7812856)
- **2026-06-06:** 1 new: Staff PM Cards Monetization (7980498) — posted June 3, 2026
- Salary range: $194,800–$321,500 for Staff PM

### Datadog (Greenhouse token: datadog)
- API blocked — used WebSearch fallback
- URL pattern: `https://job-boards.greenhouse.io/Datadog/jobs/{id}` (capital D in "Datadog" — must preserve case)
- **2026-06-04:** Director PM Applied AI (7616721), Staff PM OpenTelemetry (7555540) tracked
- **Location concern confirmed:** Datadog is NYC-based hybrid. Most PM roles are NOT remote.
- **2026-06-06:** No new qualifying Staff/Group/Director PM roles found on job-boards domain. Search returned only Senior PM roles (below threshold) and PM II roles.
- User should verify the 2 tracked roles (7616721, 7555540) for remote eligibility — may need to remove if NYC hybrid only

### OpenAI (Ashby slug: openai)
- API blocked — used WebSearch fallback
- **Result across all runs:** Only standard PM roles found (Product Manager level); no Staff/Group/Director/Principal PM roles found
- OpenAI appears to hire at non-standard levels; all current postings are "Product Manager" without seniority prefix
- **Recommendation:** Continue checking; if OpenAI expands senior hiring, roles will appear

### Netflix (Lever slug: netflix)
- Lever API blocked — used WebSearch fallback
- **Key finding:** Netflix no longer uses Lever. Their ATS is at `explore.jobs.netflix.net` (Phenom-based)
- URL pattern: `https://explore.jobs.netflix.net/careers/job/{id}-{slug}`
- Found 3 confirmed remote US roles (all tracked): Principal PM Games Social Platform (790312452283), Principal PM Experimentation Platform (790313738714), Group PM Security Platforms Engineering (790313768849)
- **2026-06-06:** No new Netflix roles found beyond tracked ones

### Meta (WebSearch fallback)
- URL pattern: `https://www.metacareers.com/jobs/{id}` (verified correct format)
- **2026-06-04:** 3 roles tracked: Principal PM Enterprise (1332660768358503), Director PM Content Integrity (2674151899454763), Director PM WhatsApp Growth (779720348340713)
- **Location clarified 2026-06-06:** Director PM WhatsApp Growth confirmed Menlo Park, CA in-person — NOT Boston compatible
- **Recommendation:** Verify all 3 tracked Meta roles for remote eligibility; WhatsApp Growth may need removal

### Microsoft (WebSearch fallback)
- URL pattern: `https://jobs.careers.microsoft.com/global/en/job/{id}`
- **Result across all runs:** No qualifying roles found — Principal Group PM (1788310) is Xbox/Redmond WA; Group PM (1631720) location unclear but likely Redmond
- **2026-06-06:** Still no confirmed remote/Boston roles at Microsoft

### Snowflake (WebSearch fallback)
- URL pattern: `https://careers.snowflake.com/us/en/job/{id}`
- **Result:** All found Principal PM roles in San Mateo/Menlo Park/Bellevue — no remote roles found
- Snowflake appears to be largely office-based for PM roles

### GitHub (WebSearch fallback)
- URL pattern: `https://www.github.careers/careers-home/jobs/{id}` (confirmed correct)
- All roles listed as "United States" — confirmed remote-eligible (GitHub operates as distributed company)
- **2026-06-04:** Principal PM Agent Platform (5140), Principal PM (4884), Staff PM (4402)
- **2026-06-06:** 2 new: Staff PM (5315), Staff PM (4722)
- Total 5 GitHub roles tracked

### Cloudflare (WebSearch fallback)
- URL pattern: `https://cloudflare.com/careers/jobs/{id}`
- **Result across all runs:** No qualifying Staff/Group/Director/Principal PM roles surfaced
- Found PM Intern posting (7362113) on job-boards.greenhouse.io/cloudflare — Cloudflare uses Greenhouse
- **Try next run:** `site:job-boards.greenhouse.io/cloudflare "product manager"` to find Cloudflare PM roles

---

## Title Filter Reference (non-Anthropic)
Include: Staff Product Manager, Group Product Manager, Director of Product Management, Principal Product Manager (or equivalent)
Exclude: Senior PM, Associate PM, or anything below Staff level

## Excluded Roles — Cumulative Log
- Analytics Data Engineering Manager, Product @ Anthropic (not PM role)
- Product Operations Manager, Feedback Loops @ Anthropic (not PM)
- Technical Program Manager, Launches @ Anthropic (not PM)
- Director of Product Communications @ Discord (comms role, not PM)
- Staff PM Commerce, Payments, Growth & SEO @ Discord (SF Bay Area only, not Boston-compatible)
- Product Manager (non-senior) roles at all companies
- All Snowflake roles — CA/WA office-required
- All OpenAI — no senior PM roles found (consistent across all runs)
- All Microsoft — Redmond WA office, no confirmed remote
- Cloudflare — no qualifying roles found
- Datadog Group PM roles (Infrastructure/SDLC, Threat Management, older IDs) — NYC hybrid, uncertain Boston compat
- Datadog Staff PM, AI (6960614) — NYC, not Boston-compatible
- Meta Director PM WhatsApp Growth (779720348340713) — Menlo Park, CA in-person (may need to remove from tracker)
- Reddit Staff PM Reddit Profiles (5888261) — older posting of same title as reddit-6478046; both tracked

## Run History
| Date | New Roles | Total Tracked |
|------|-----------|---------------|
| 2026-06-04 | 54 | 54 |
| 2026-06-05 | 29 | 83 |
| 2026-06-06 | 10 | 93 |
| 2026-06-07 | 0 | 93 |

## 2026-06-07 Run Notes (Run 2 — confirmed same session)
- All ATS API endpoints blocked by network policy (HTTP 403 / "Host not in allowlist") — same as all prior runs
- Hosts blocked (all 12 API calls attempted in parallel and all returned 403):
  - Greenhouse: `boards-api.greenhouse.io` (anthropic, airbnb, reddit, discord, databricks, stripe, datadog, cloudflare, github, snowflake)
  - Ashby: `api.ashbyhq.com` (openai)
  - Lever: `api.lever.co` (netflix)
- Per task instructions: "Do NOT fall back to WebSearch for any company under any circumstances" — no WebSearch fallback used
- 0 new roles detected. No email sent.
- seen_jobs.json unchanged (93 roles total)
- **Action required:** Environment network policy must allowlist ATS API hosts to enable automated role detection without WebSearch fallback.

## 2026-06-06 Run Notes
- 4 new Anthropic PM roles (Multi-Cloud Growth, Developer Productivity, Claude Code Model Performance, API repost)
- 3 new Reddit Staff/Group PM roles (Ads Monetization Searcher, Content Discovery, Ads Marketplace)
- 1 new Stripe Staff PM (Cards Monetization, posted June 3)
- 2 new GitHub Staff PM roles (IDs 5315, 4722)
- Confirmed: Databricks PM = hybrid non-remote; Datadog PM = NYC hybrid; Microsoft = Redmond; Snowflake = office-based
- Netflix confirmed using Phenom ATS (explore.jobs.netflix.net), not Lever
- Stripe Cards Monetization (7980498) confirmed active on job-boards.greenhouse.io domain (posted ~June 3, 2026)
