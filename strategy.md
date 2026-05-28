# Job Tracker Strategy

Accumulated learnings from each run to search smarter over time.

---

## Run: 2026-05-28 (Fifth Pass)

### New Roles Found (4)
- **Reddit Staff PM, Growth — New User Acquisition, Eastern Timezone** (GH 6379485) — Remote USA, EST timezone preferred. Boston-compatible confirmed via Built In Boston listing. job-boards.greenhouse.io/reddit/jobs/6379485.
- **Google Group PM, Google Cloud** (129173606920790726) — Cambridge, MA listed as a preferred working location option. Confirmed via LinkedIn: "Google hiring...in Cambridge, Massachusetts." 12 years PM experience required. Salary $214K-$305K. google.com/about/careers job page.
- **Google Lead Group PM, Databases & Analytics, Google Cloud** (97142797563241158) — Cambridge, MA confirmed as preferred working location. Covers database and analytics products. 10 yr PM experience, 5 yr people mgmt required. Salary $227K-$320K.
- **Google Lead Group PM, Compute, Google Cloud** (106894634206012102) — Cambridge, MA confirmed. Leads compute and control plane for Google Cloud VMware Engine. Was previously "unconfirmed Cambridge" in strategy — now confirmed.

### Key Observations
- All ATS APIs (greenhouse, ashby, lever) still return HTTP 403. WebSearch + aggregator approach remains the only viable path.
- **Reddit Staff PM, Growth — New User Acquisition, Eastern Timezone** (6379485) is on the new job-boards.greenhouse.io URL style (not old boards.greenhouse.io), confirming it's an active recent posting.
- **Reddit Staff PM, Core Experience** (5345806) appeared on old boards.greenhouse.io — skip as likely stale.
- **Discord "Group Product Manager, Core Product"** — startup.jobs elevates title to "Group PM" but Greenhouse actual title is "Product Manager, Core Product" (IDs 8288128002 and 7982515002) — below Staff level. EXCLUDED.
- **Google Lead Group PM, Streaming Analytics** (82664694870876870) — confirmed locations are Sunnyvale, CA and Kirkland, WA only. NOT Cambridge. EXCLUDED.
- **Google Lead Group PM, Data Protection, Foundations** (126267683896206022) — primary location appears to be New York, not Cambridge. EXCLUDED.
- **Google Lead Group PM, Google Workspace** (90710050403689158) — Cambridge location not confirmed. Skip until confirmed.
- **Stripe** — no new Staff PM roles vs. previous run (all 14 prior roles still appear to be active).
- **Airbnb** — no new roles; same 4 qualifying + 2 excluded (Payments entity) as before.
- **Databricks Staff PM** (7649409002) — Amsterdam, Netherlands. EXCLUDED.
- **OpenAI** — no qualifying remote roles found.
- Many new Google Group PM / Lead Group PM roles exist on careers.google.com not yet checked for Cambridge: Group PM Lead End-to-End Workflows (123825865283773126), Group PM AI Infra (128346269826327238), Group PM ACI Infrastructure (135370941705134790), Group PM Cloud Foundations (130411359358591686), Lead Group PM Generative AI Cloud (82540556760031942), Lead Group PM YouTube Trust & Safety (124252434120745670). Check in future runs.

---

## Run: 2026-05-27 (Fourth Pass)

### New Roles Found (3)
- **Stripe Staff PM, Orchestration Lead** (7568296) — confirmed remote USA. Lead Stripe Orchestration, nascent enterprise product. URL: stripe.com/jobs/listing/staff-product-manager-orchestration-lead/7568296. Added to seen_jobs.
- **Reddit Staff PM, Contributor Experience (Core Experience Team)** (6434425) — confirmed remote USA via Working Nomads. job-boards.greenhouse.io (new URL format). Posted ~Nov 30, 2024, still active May 2026. Added to seen_jobs.
- **GitHub Staff PM, Copilot Platform** (job 4722) — confirmed remote USA. Multi-model strategy for GitHub Copilot. github.careers/benefits/jobs/4722. Different from job 5124 (Developer Experience). Added to seen_jobs.

### Key Observations
- Direct ATS API calls (boards-api.greenhouse.io, api.ashbyhq.com, api.lever.co) ALL return HTTP 403. WebSearch fallback is the only viable approach.
- **Discord Staff PM, Measurement & Signals** (8245255002) — Built In SF + Glassdoor confirm San Francisco location. EXCLUDED. Do not re-report.
- **Databricks Staff PM, Serverless Workspaces** (8420607002) — Seattle, WA on-site per Levels.fyi. EXCLUDED.
- **Databricks Staff PM Technical** (8394060002) — Amsterdam, Netherlands. Not US-based. EXCLUDED.
- **Anthropic Lead PM, Claude Code** (4791979008) — still active in search results. Confirmed in seen_jobs. Also found non-Lead PM roles (Claude Code Platform, Claude Code Enterprise, Consumer, Claude Experiences, Claude Code Growth) — all below Staff/Lead level, excluded.
- **Reddit Emerging Markets** (5139721) — boards.greenhouse.io OLD URL, no confirmed date, potentially very old (2023/early 2024). Skipped this run; monitor in future runs.
- **Stripe Orchestration Lead** — ID may appear as both 7568987 and 7568296 in different searches; use 7568296 (from direct stripe.com URL returned in specific search).
- Snowflake, Microsoft, Meta: no new qualifying roles. Skip detailed search unless criteria change.

---

## Run: 2026-05-27

### General Notes
- Most company career pages (discord.com/jobs, stripe.com/jobs, careers.airbnb.com, anthropic.com/careers, openai.com/careers, databricks.com, builtinboston.com, greenhouse.io individual job boards) return **HTTP 403** to WebFetch. Do not attempt WebFetch on these.
- **Accessible via WebFetch**: careers.datadoghq.com (though some detail pages 404), dailyremote.com (403 too), nodesk.co (403).
- **Best strategy**: Use WebSearch with site-specific queries (site:greenhouse.io, site:careers.snowflake.com), then search job aggregators (remoterocketship.com, himalayas.app, workingnomads.com, jobgether.com) for details — but most also return 403. Rely on search result snippets for job details.
- **Most productive approach**: General WebSearch with company + title + year → aggregator links in results → snippet data.

---

## Run: 2026-05-27 (Third Pass)

### General Notes (Updated)
- google.com/about/careers pages return **HTTP 403** to WebFetch. Must rely on WebSearch snippets.
- metacareers.com returns **HTTP 403** to WebFetch.
- **Google Cambridge discovery**: Multiple Google Group PM roles list "Cambridge, MA" as a preferred working location option. These qualify as "Based in Boston or Cambridge, MA" even though Google requires 3 days/week in-office — because the office IS in Boston area. Search specifically for Cambridge, MA Google roles.
- **Airbnb entity clarification**: Airbnb, Inc. (most roles) uses an "excluded states" model — broader eligibility, MA likely included. Airbnb Payments, Inc. (Payments/Evaluations/Automation, Business Host Payouts roles) uses an "approved states" model — MA is NOT in approved list. Exclude Airbnb Payments, Inc. entity roles for MA applicants.
- **Cloudflare Group PM Fraud** (boards.greenhouse.io/cloudflare/jobs/5714442) — posted ~Feb 2024, still indexed. Remote US available. Flag as potentially stale (>15 months). Do not re-report after this run unless Greenhouse page confirms still active.
- **Meta Director PM** — Glassdoor shows "Remote" but Meta currently requires 3-5 days/week in office. Do not include as qualifying remote role.
- **Stripe "Staff Product Manager, Link Balance"** — previously noted as "office-assigned" with 50% in-office. Confirmed to exclude.
- **Discord Group PM, Machine Learning** (7675546002) — new Greenhouse job ID found vs old stale URL. Built In SF still shows SF location. Multiple aggregators say closed. Treat as stale SF-based role, do not report.

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
- **New in run 3**: Compliance UX (7573905) — posted ~Feb 2026; Agentic Commerce (7303214).
- Stripe consistently has 10-14 open Staff PM roles at any given time.
- **Exception**: Staff PM, Link Balance (7118153) — "office-assigned" with 50% in-office expectation. Confirmed excluded.
- Future runs: check stripe.com/jobs/search directly via search; look for new job IDs on site:stripe.com.
- Recommended query: `Stripe "staff product manager" remote "United States" 2026 site:stripe.com`

## Anthropic

- **Policy: all staff expected in office at least 25% of the time** — this meets the ≤25% exception.
- Roles qualify regardless of city since 25% in-office is within the exception criteria.
- Current roles (run 1): Lead PM Research (GH 4684257008), Lead PM Developer Services (GH 5021316008).
- **New in run 2**: Lead PM Claude Code (GH 4791979008) — actively confirmed on greenhouse.io.
- "Lead Product Manager" is Anthropic's equivalent of Staff/Group PM — qualifies on seniority.
- Offices are primarily San Francisco; some roles also list New York or Seattle.
- **Run 3 note**: Lead PM Research appeared with NEW job ID 4933813008 (vs old 4684257008). This is a re-post of the same role. Track by title+company slug, not job ID. Do NOT re-report same title unless meaningfully different.
- Future runs: check `Anthropic "lead product manager" site:greenhouse.io 2026`. Also search for "director" or "group" level roles as Anthropic grows.

## Discord

- Discord career pages (discord.com/jobs) return 403. Greenhouse pages also 403.
- Group PM, Machine Learning role from Oct/Nov 2024 — **expired/stale, do not re-report**.
- **New in run 2**: Staff PM, Growth & SEO (8348158002) — confirmed remote USA via remoterocketship.com.
- **Excluded SF-based roles**: Staff PM Commerce (8432341002) — San Francisco per ZipRecruiter and Built In SF. Staff PM Payments (8362678002) — Built In San Francisco, confirmed SF-based.
- Most Discord PM roles appear to be SF Bay Area on-site — verify carefully. If a role appears on Built In SF or ZipRecruiter with SF location, exclude it.
- Future runs: search `Discord "staff product manager" OR "group product manager" remote 2026 site:greenhouse.io` and cross-check with remoterocketship.com to confirm remote status.

## Google

- 137 Google PM jobs listed in "Boston" area on LinkedIn but this likely includes candidates in Boston applying to Google, not roles based in Boston.
- Google Cambridge, MA office exists and **multiple Group PM / Lead Group PM roles list Cambridge, MA as a preferred working location option**.
- Google requires 3 days/week in-office (hybrid). Cambridge, MA office = Boston area = QUALIFIES.
- **Confirmed qualifying roles (runs 3–5)**:
  - Group PM, Search (81599409300611782) — "Mountain View, CA or Cambridge, MA" — ACTIVE, salary $240K-$334K (run 3)
  - Group PM, Google Cloud (129173606920790726) — Cambridge, MA confirmed — salary $214K-$305K (run 5)
  - Lead Group PM, Databases & Analytics, Google Cloud (97142797563241158) — Cambridge, MA confirmed — salary $227K-$320K (run 5)
  - Lead Group PM, Compute, Google Cloud (106894634206012102) — Cambridge, MA confirmed (run 5; was unconfirmed in run 3)
- **NOT Cambridge**: Group PM, Complex Journeys, Search — New York, NY or Mountain View, CA (not Cambridge)
- **NOT Cambridge**: Lead Group PM, Streaming Analytics (82664694870876870) — Sunnyvale, CA and Kirkland, WA only
- **NOT confirmed**: Lead Group PM, Data Protection, Foundations (126267683896206022) — appears NY-based
- **Not yet checked**: Group PM Lead, End-to-End Workflows (123825865283773126); Group PM AI Infra (128346269826327238); Group PM ACI Infrastructure (135370941705134790); Group PM Cloud Foundations (130411359358591686); Lead Group PM Generative AI Cloud (82540556760031942); Lead Group PM Google Workspace (90710050403689158)
- google.com/about/careers returns HTTP 403 to WebFetch. Use WebSearch with site:google.com/about/careers.
- Future runs: search `Google "Group Product Manager" "Cambridge, MA" 2026 site:google.com/about/careers` to find new Cambridge-eligible roles. Also check `site:careers.google.com "Cambridge" "Group Product Manager"`. Check the unverified roles listed above.
- Note: Google job IDs are very long (18-digit numbers). Track with slug "google-[level]-[title]-cambridge-ma".

## Netflix

- Group PM, Payments Product Journey — posted March 12, 2026 — **excluded**: role is based in Los Gatos, CA. Not Boston-compatible.
- **New in run 2**: Group PM, Security Platforms Engineering — **remote USA** — confirmed active via Netflix careers site and Glassdoor (May 2026). URL: explore.jobs.netflix.net/careers/job/790313768849...
- explore.jobs.netflix.net returns 403 to WebFetch. Use WebSearch with site:explore.jobs.netflix.net.
- Most Netflix PM roles are on-site in Los Gatos, LA, or NY. Remote roles are rare — search specifically for "USA - Remote" in titles.
- Future runs: query `Netflix "group product manager" OR "director" remote "USA" 2026 site:explore.jobs.netflix.net`

## OpenAI

- OpenAI PM roles are predominantly SF-based (on-site required).
- All PM roles found in run 3 are explicitly listed as San Francisco (e.g., Product Manager, Codex — SF; Product Operations Manager — SF).
- No qualifying Staff/Group/Director PM roles remote/Boston-compatible found in any run.
- Future runs: check `site:openai.com/careers "product manager"` for any new remote options. Low priority — skip if time-constrained.

## Airbnb

- Airbnb's official policy: employees can work from anywhere in the US (US Remote Eligible).
- **CRITICAL entity distinction**:
  - **Airbnb, Inc.** (most roles): Uses "excluded states" model — broader eligibility. Massachusetts is likely NOT excluded. These roles qualify.
  - **Airbnb Payments, Inc.** (payments-related roles): Uses "approved states" model with specific list. Massachusetts is NOT on the approved list. EXCLUDE these roles.
  - Payments roles that EXCLUDE MA: Business Host Payouts (7747440), Payments/Evaluations/Automation (7674658).
- Active roles (run 2): AI Personalization (7834495) — US Remote Eligible.
- **New in run 3** (all Airbnb, Inc. entity = MA likely OK):
  - Staff Platform Manager, Community Experience Platforms (7451574) — posted Apr 6, 2026
  - Staff Platform Manager, Trust and Safety (7740258) — posted Mar 24, 2026
  - Staff Platform Manager, Suspensions, Appeals & Enforcements (7445911)
  - Staff Platform Manager, Agent Products and Intelligence Platforms (7525175) — posted Jan 14, 2026
- careers.airbnb.com returns 403 to WebFetch. Use WebSearch + remoterocketship/remotive for verification.
- Future runs: search `Airbnb "staff product manager" OR "staff platform manager" remote 2026 site:careers.airbnb.com` and verify entity type (Airbnb, Inc. vs Airbnb Payments, Inc.) from job description.
- Airbnb has 5-8 open Staff PM/Platform Manager roles at any given time. Check for new position IDs each run.

## Meta

- Meta has Director of Product Management roles, but as of 2026 Meta requires 3-5 days/week in office for PM roles.
- Glassdoor shows one "Product Management, Director" role listed as "Remote" (job_details/816501496761265), but this is misleading — Meta remote PM roles are "rare exceptions" per industry sources.
- Director PM roles found: Content Integrity Trust & Safety, Ads Targeting & Countries Monetization, WhatsApp Growth — all appear to be Menlo Park or NYC based.
- metacareers.com returns 403 to WebFetch.
- No qualifying confirmed remote roles found in any run. Do not report Meta roles without explicit confirmation of Boston-compatible location.
- Future runs: check `site:metacareers.com "director product management" remote` but also verify via Glassdoor/LinkedIn that the role is actually flagged as remote (not just "can apply from anywhere").

## Microsoft

- Microsoft AI division requires 4 days/week in-office starting Jan 2026 for those within 50 miles of a Microsoft office — **significant blocker for remote**.
- Microsoft has offices in Burlington, MA (Greater Boston area) — roles based there would qualify.
- No confirmed Boston-based or fully-remote Principal Group PM roles found in any run.
- Future runs: search `Microsoft "principal group product manager" OR "group product manager" Boston Burlington remote 2026`.

## Databricks

- Most Staff PM roles are SF-based (San Francisco, CA) or Seattle — **not Boston-compatible**.
- Staff PM, AI Platform — SF; Staff PM, Databricks Notebooks — SF; Staff PM, Security — Seattle; Staff PM, Content Experience — Seattle.
- **Run 3 note**: Staff PM, Network Security (6454355002) — primary location SF, but Databricks says "open to remote candidates in other locations." Borderline case. Excluded for now due to primary SF listing, but worth monitoring.
- Additional roles found (run 3, all SF-excluded): New Product (6971388002), Next Gen Analytics (7332973002), Technical (7625294002), Senior Staff PM (6845707002), Content Experience (8041821002).
- Staff PM, Data Security appears to be the same role as Network Security under a different name/ID — same 6454355002 base ID.
- Future runs: search `site:databricks.com/company/careers "product manager"` — if any role explicitly says "remote" without SF caveat, investigate further.

## Snowflake

- All PM roles on careers.snowflake.com are on-site in Menlo Park, CA or Bellevue, WA — **not Boston-compatible**.
- Staff PM Developer Platform — Menlo Park (Jan 5, 2026).
- Toronto, Canada location appeared in run 2 — not US-based, excluded.
- Future runs: skip detailed Snowflake search unless checking for policy change.

## Datadog

- Datadog has a Boston office (Greater Boston Area) — some roles are Boston-based.
- Director PM roles found in run 2: Applied AI, Core Platforms, AI Observability, Security — ALL based in New York, NY (hybrid) — **not Boston-compatible**.
- **Run 3**: Staff PM, Product Analytics (5901346) — Built In NYC + Glassdoor confirm New York, NY hybrid. EXCLUDED.
- careers.datadoghq.com detail pages: some return 404 (confirmed role removed). 404 = job closed.
- careers.datadoghq.com/product-management/ and /remote/ pages show empty job list to WebFetch (JS-rendered).
- Future runs: use `site:careers.datadoghq.com "director" OR "staff product manager"` search. Look for Boston or Remote location indicators. Any NYC/hybrid result = exclude. Monitor for any remote/Boston-based new PM roles.

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

- Cloudflare uses greenhouse.io for job postings (job-boards.greenhouse.io/cloudflare and boards.greenhouse.io/cloudflare).
- greenhouse.io/cloudflare pages return 403 to WebFetch.
- **Senior Director of Product, App Performance** (GH 6951791) — Austin, TX hybrid, excluded.
- **Group Product Manager, Fraud** (boards.greenhouse.io/cloudflare/jobs/5714442) — Remote US available (Austin, Champaign, SF, Washington DC, or Remote-US). **POTENTIALLY STALE** — posted ~Feb 2024. Still indexed on Greenhouse and aggregators as of May 2026. Reported in run 3.
- Most PM roles at Cloudflare appear to be Austin TX, NYC, or San Francisco office-based.
- Future runs: search `Cloudflare "group product manager" OR "director product" remote 2026` and also check `Cloudflare site:greenhouse.io "product manager" remote`. If Fraud role (5714442) still appears in search results, do NOT re-report (already in seen_jobs). Verify it's still open before including any new Cloudflare roles.
- Note: boards.greenhouse.io (old URL style) is used for older Cloudflare postings vs job-boards.greenhouse.io (new style).
