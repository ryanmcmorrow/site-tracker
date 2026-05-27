# Job Tracker Strategy

Accumulated learnings from each run to search smarter over time.

---

## Run: 2026-05-27

### General Notes
- Most company career pages (discord.com/jobs, stripe.com/jobs, careers.airbnb.com, anthropic.com/careers, openai.com/careers, databricks.com, builtinboston.com, greenhouse.io individual job boards) return **HTTP 403** to WebFetch. Do not attempt WebFetch on these.
- **Accessible via WebFetch**: careers.datadoghq.com (though some detail pages 404), dailyremote.com (403 too), nodesk.co (403).
- **Best strategy**: Use WebSearch with site-specific queries (site:greenhouse.io, site:careers.snowflake.com), then search job aggregators (remoterocketship.com, himalayas.app, workingnomads.com, jobgether.com) for details — but most also return 403. Rely on search result snippets for job details.
- **Most productive approach**: General WebSearch with company + title + year → aggregator links in results → snippet data.

---

## Run: 2026-05-27 (Second Pass)

### General Notes (Updated)
- explore.jobs.netflix.net returns **HTTP 403** to WebFetch.
- stripe.com/jobs/* returns **HTTP 403** to WebFetch. Must rely on search snippets.
- careers.airbnb.com returns **HTTP 403** to WebFetch.
- job-boards.greenhouse.io/* returns **HTTP 403** (not just boards.greenhouse.io).
- github.careers returns **HTTP 403** to WebFetch.
- cloudflare.com Greenhouse pages return **HTTP 403**.
- builtinsf.com returns **HTTP 403** to WebFetch.
- careers.datadoghq.com detail pages: some 404 (job removed = strong signal that role is gone).
- **Verification approach for 403 sites**: use search to find aggregator page snippets that describe the role's remote status. Key aggregators: Built In SF/NYC/Boston (indicates city if listed), ZipRecruiter (shows city), remoterocketship.com (confirms "remote - United States"), remotive.com (confirms remote), dailyremote.com.
- Built In SF or ZipRecruiter showing SF = NOT remote, exclude.
- remoterocketship.com or remotive.com listing = strong remote signal.

---

## Reddit

- **All Reddit staff/group PM roles are remote USA** — confirmed across multiple aggregators.
- Reddit posts heavily on greenhouse.io/reddit (new jobs) and boards.greenhouse.io/reddit (older jobs).
- Active job IDs found in run 1: 6478046, 6721235, 7858506, 7483888, 7724536, 7803856, 6718339.
- **New in run 2** (2026-05-27): job IDs 6486227 (Ranking/Core Experience), 6478066 (Reddit Pro), 7014057 (Compliance), 7311413 (Ranking & Data API), 7746309 (Ads API, confirmed active 5/4/2026), 6563939 (Ads Marketplace Supply).
- Reddit has many Staff PM roles across Consumer (Profiles, Answers, Subreddit Success, Reddit Pro, Ranking) and Ads (Monetization, Paid UA, Ads Business Manager, Finance Apps, Ads API, Ads Marketplace).
- "Senior Group Product Manager, Advertiser Optimization" (job 7858506) is Group-level — qualifies.
- Future runs: search `site:job-boards.greenhouse.io/reddit` to find new job IDs directly.
- Recommended query: `Reddit "staff product manager" OR "group product manager" remote 2026 site:greenhouse.io`
- Expect 10-15 open Reddit Staff PM roles at any given time; check job IDs against seen_jobs.

## Stripe

- **Multiple Staff PM roles, all remote USA** — Stripe defines remote as 35+ miles from any Stripe office.
- Jobs are on both stripe.com/jobs and job-boards.greenhouse.io/stripe.
- Active roles found (run 1): Dashboard (7913702), Apps & Extensibility Platform (7550590), Enterprise Industries (7812856), Support Experience (7920219), Payments (7819059), Web Presence & Platform (7169955).
- **New in run 2**: Seller Experience (7191708), Terminal - Global Payment Acceptance (7301942), Billing (6977801), Usage Based Billing (6894642), Local Processor Acquiring (7953691).
- Stripe consistently has 8-12 open Staff PM roles at any given time.
- **Exception**: Staff PM, Link Balance (7118153) — described as "office-assigned" with 50% in-office expectation. May be SF/NYC specific. Exclude until location clarified.
- Future runs: check stripe.com/jobs/search directly via search; look for new job IDs on site:stripe.com.
- Recommended query: `Stripe "staff product manager" remote "United States" 2026 site:stripe.com`

## Anthropic

- **Policy: all staff expected in office at least 25% of the time** — this meets the ≤25% exception.
- Roles qualify regardless of city since 25% in-office is within the exception criteria.
- Current roles (run 1): Lead PM Research (GH 4684257008), Lead PM Developer Services (GH 5021316008).
- **New in run 2**: Lead PM Claude Code (GH 4791979008) — actively confirmed on greenhouse.io.
- "Lead Product Manager" is Anthropic's equivalent of Staff/Group PM — qualifies on seniority.
- Offices are primarily San Francisco; some roles also list New York or Seattle.
- Note: Job IDs for Research/Developer Services may change if re-posted. Track by title+company slug.
- Future runs: check `Anthropic "lead product manager" site:greenhouse.io 2026`

## Discord

- Discord career pages (discord.com/jobs) return 403. Greenhouse pages also 403.
- Group PM, Machine Learning role from Oct/Nov 2024 — **expired/stale, do not re-report**.
- **New in run 2**: Staff PM, Growth & SEO (8348158002) — confirmed remote USA via remoterocketship.com.
- **Excluded SF-based roles**: Staff PM Commerce (8432341002) — San Francisco per ZipRecruiter and Built In SF. Staff PM Payments (8362678002) — Built In San Francisco, confirmed SF-based.
- Most Discord PM roles appear to be SF Bay Area on-site — verify carefully. If a role appears on Built In SF or ZipRecruiter with SF location, exclude it.
- Future runs: search `Discord "staff product manager" OR "group product manager" remote 2026 site:greenhouse.io` and cross-check with remoterocketship.com to confirm remote status.

## Google

- 137 Google PM jobs listed in "Boston" area on LinkedIn but this likely includes candidates in Boston applying to Google, not roles based in Boston.
- Google Cambridge, MA office exists — a few roles may be based there but hard to find specifically.
- Google generally requires on-site presence for PM roles.
- No qualifying remote or Boston-based Staff/Group/Director PM roles confirmed in any run.
- Future runs: search `site:google.com/about/careers "group product manager" OR "director" Boston Cambridge remote` and verify location.

## Netflix

- Group PM, Payments Product Journey — posted March 12, 2026 — **excluded**: role is based in Los Gatos, CA. Not Boston-compatible.
- **New in run 2**: Group PM, Security Platforms Engineering — **remote USA** — confirmed active via Netflix careers site and Glassdoor (May 2026). URL: explore.jobs.netflix.net/careers/job/790313768849...
- explore.jobs.netflix.net returns 403 to WebFetch. Use WebSearch with site:explore.jobs.netflix.net.
- Most Netflix PM roles are on-site in Los Gatos, LA, or NY. Remote roles are rare — search specifically for "USA - Remote" in titles.
- Future runs: query `Netflix "group product manager" OR "director" remote "USA" 2026 site:explore.jobs.netflix.net`

## OpenAI

- OpenAI PM roles are predominantly SF-based (on-site required).
- No qualifying Staff/Group/Director PM roles remote/Boston-compatible found in any run.
- Future runs: check `site:openai.com/careers "product manager"` for any new remote options.

## Airbnb

- Airbnb's official policy: employees can work from anywhere in the US (US Remote Eligible).
- **New in run 2**: Staff PM, AI Personalization (careers.airbnb.com/positions/7834495/) — US Remote Eligible. Active listing. $200K-$240K. Note: role title is "Staff Platform Manager, AI Personalization" on remotive but listed as "Staff Product Manager, AI Personalization" on careers.airbnb.com.
- careers.airbnb.com returns 403 to WebFetch. Use WebSearch + remotive for verification.
- Future runs: search `Airbnb "staff product manager" OR "staff platform manager" remote 2026 site:careers.airbnb.com` then verify via remotive.

## Meta

- Meta has Director of Product Management roles but remote policy unclear for senior roles.
- Director PM roles found: Content Integrity Trust & Safety, Ads Targeting & Countries Monetization, WhatsApp Growth — all appear to be Menlo Park or NYC based.
- No qualifying confirmed remote roles found in any run.
- Future runs: check metacareers.com for remote-flagged senior PM roles. Query: `site:metacareers.com "director product management" remote`.

## Microsoft

- Microsoft AI division requires 4 days/week in-office starting Jan 2026 for those within 50 miles of a Microsoft office — **significant blocker for remote**.
- Microsoft has offices in Burlington, MA (Greater Boston area) — roles based there would qualify.
- No confirmed Boston-based or fully-remote Principal Group PM roles found in any run.
- Future runs: search `Microsoft "principal group product manager" OR "group product manager" Boston Burlington remote 2026`.

## Databricks

- All Staff PM roles found are SF-based (San Francisco, CA) or Seattle — **not Boston-compatible**.
- Staff PM, AI Platform — SF; Staff PM, Databricks Notebooks — SF; Staff PM, Security — Seattle; Staff PM, Content Experience — Seattle.
- New role found in run 2: Staff PM (generic, job 7649409002) — location unknown.
- Future runs: check `site:databricks.com/company/careers "product manager" remote` — if remote PM roles appear, verify location.

## Snowflake

- All PM roles on careers.snowflake.com are on-site in Menlo Park, CA or Bellevue, WA — **not Boston-compatible**.
- Staff PM Developer Platform — Menlo Park (Jan 5, 2026).
- Toronto, Canada location appeared in run 2 — not US-based, excluded.
- Future runs: skip detailed Snowflake search unless checking for policy change.

## Datadog

- Datadog has a Boston office (Greater Boston Area) — some roles are Boston-based.
- Director PM roles found in run 2: Applied AI, Core Platforms, AI Observability, Security — ALL based in New York, NY (hybrid) — **not Boston-compatible**.
- careers.datadoghq.com detail pages: some return 404 (confirmed role removed). 404 = job closed.
- careers.datadoghq.com/product-management/ page loads but shows empty job list (JS-rendered, WebFetch can't read it).
- careers.datadoghq.com/remote/ page also shows empty job list to WebFetch.
- Future runs: use `site:careers.datadoghq.com "director" OR "staff product manager"` search. Look for Boston or Remote location indicators. Any NYC/hybrid result = exclude.

## GitHub

- GitHub uses github.careers (Taleo-based ATS) not greenhouse.io.
- **All GitHub Staff PM roles are fully remote in the United States**.
- Active roles confirmed in run 2:
  - Staff PM, Developer Experience (github.careers job 5124) — remote USA
  - Staff PM, Data Experience (boards.greenhouse.io/github/jobs/5265302) — remote USA
  - Staff PM, Repository Security and Governance — remote USA (remotive link)
- Additional roles mentioned in search results but without confirmed direct URLs: Staff PM, Copilot Platform.
- Future runs: search `GitHub "staff product manager" remote 2026 site:greenhouse.io OR site:github.careers` and `GitHub "staff product manager" remote site:remotive.com OR site:nodesk.co`.
- Salary range: $127,600–$372,300 for Staff PM.

## Cloudflare

- Cloudflare uses greenhouse.io for job postings (job-boards.greenhouse.io/cloudflare).
- greenhouse.io/cloudflare pages return 403 to WebFetch.
- **Senior Director of Product, App Performance** (GH 6951791) — listed on remoterocketship as "Austin, TX - hybrid" and on JobTarget as "San Francisco, CA". **NOT remote, excluded**.
- Most PM roles at Cloudflare appear to be Austin TX, NYC, or San Francisco office-based.
- Some remote Cloudflare PM roles exist (e.g., PM Cloud Email Security, remote US) but at senior/regular level, not Staff or Director.
- Future runs: search `Cloudflare "staff product manager" OR "director product management" remote 2026 site:greenhouse.io` and verify location via ZipRecruiter/Built In snippets.
