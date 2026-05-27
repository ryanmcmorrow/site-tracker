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

## Reddit

- **All Reddit staff/group PM roles are remote USA** — confirmed across multiple aggregators.
- Reddit posts heavily on greenhouse.io/reddit (new jobs) and boards.greenhouse.io/reddit (older jobs).
- Active job IDs found in this run: 6478046, 6721235, 7858506, 7483888, 7724536, 7803856, 6718339.
- Reddit has many Staff PM roles across Consumer (Profiles, Answers, Subreddit Success) and Ads (Monetization, Paid UA, Ads Business Manager, Finance Apps).
- "Senior Group Product Manager, Advertiser Optimization" (job 7858506) is Group-level — qualifies.
- Future runs: search `site:job-boards.greenhouse.io/reddit` to find new job IDs directly.
- Recommended query: `Reddit "staff product manager" OR "group product manager" remote 2026 site:greenhouse.io`

## Stripe

- **Multiple Staff PM roles, all remote USA** — Stripe defines remote as 35+ miles from any Stripe office.
- Jobs are on both stripe.com/jobs and job-boards.greenhouse.io/stripe.
- Active roles found: Dashboard (7913702, posted May 12 2026), Apps & Extensibility Platform (7550590, posted Apr 20 2026), Enterprise Industries (GH 7812856, posted Apr 22 2026), Support Experience (unknown date), Payments (7819059), Web Presence & Platform (posted Jan 5 2026 — likely stale by next run).
- Stripe consistently has 5–6 open Staff PM roles at any given time.
- Future runs: check stripe.com/jobs/search directly via search; look for new job IDs.
- Recommended query: `Stripe "staff product manager" remote "United States" 2026 site:stripe.com OR site:greenhouse.io`

## Anthropic

- **Policy: all staff expected in office at least 25% of the time** — this meets the ≤25% exception.
- Roles qualify regardless of city since 25% in-office is within the exception criteria.
- Current roles: Lead PM Research (GH 4684257008), Lead PM Developer Services.
- "Lead Product Manager" is Anthropic's equivalent of Staff/Group PM — qualifies on seniority.
- Offices are primarily San Francisco; some roles also list New York or Seattle.
- Future runs: check anthropic.com/careers/jobs?team=4002057008 (though it 403s, use search instead).
- Recommended query: `Anthropic "lead product manager" OR "staff product manager" site:greenhouse.io OR site:anthropic.com 2026`

## Discord

- Discord career pages (discord.com/jobs) return 403. Greenhouse pages also 403.
- Group PM, Machine Learning role found from Oct/Nov 2024 — **expired/stale, do not re-report**.
- Most Discord PM roles appear to be SF Bay Area on-site — check carefully before including.
- Staff PM Commerce and Staff PM Payments both appear SF Bay Area based — excluded.
- Future runs: search `Discord "product manager" remote 2026 site:greenhouse.io` and verify dates carefully.

## Google

- 137 Google PM jobs listed in "Boston" area on LinkedIn but this likely includes candidates in Boston applying to Google, not roles based in Boston.
- Google Cambridge, MA office exists — a few roles may be based there but hard to find specifically.
- Google generally requires on-site presence for PM roles.
- No qualifying remote or Boston-based Staff/Group/Director PM roles confirmed in this run.
- Future runs: search `site:google.com/about/careers "group product manager" OR "director" Boston Cambridge remote` and verify location.

## Netflix

- Group PM, Payments Product Journey — posted March 12, 2026 — **excluded**: role is based in Los Gatos, CA (West Coast on-site/hybrid). Not Boston-compatible.
- Netflix AI PM role paying $700K is fully remote but appears to be a different type of role (AI/Gen AI product, not standard PM title).
- Most Netflix PM roles are on-site in Los Gatos, LA, or NY.
- Future runs: check for remote Netflix roles specifically. Recommended query: `Netflix "product manager" remote "United States" 2026 site:explore.jobs.netflix.net`

## OpenAI

- OpenAI PM roles are predominantly SF-based (on-site required).
- Product Manager, Codex — SF only.
- Product Marketing Manager roles are remote but are marketing, not PM.
- No qualifying Staff/Group/Director PM roles remote/Boston-compatible found.
- Future runs: check `site:openai.com/careers "product manager"` for any new remote options.

## Airbnb

- Airbnb's official policy: employees can work from anywhere in the US.
- Senior Manager, Product Lead (Pilot Product) found but location/remote eligibility unverified (careers.airbnb.com 403s).
- Regular PM and PM (Stays, Destinations, LATAM, New Guest Experience) roles found — remote USA eligible.
- But none found at Staff/Group/Director level confirmed in this run.
- Future runs: search `Airbnb "staff product manager" OR "group product manager" OR "director" remote 2026`.

## Meta

- Meta has Director of Product Management roles but remote policy unclear for senior roles.
- One "Product Management, Director" role found on metacareers.com (job 816501496761265).
- Meta typically requires on-site presence at Menlo Park or NYC.
- No qualifying confirmed remote roles found.
- Future runs: check metacareers.com for remote-flagged senior PM roles.

## Microsoft

- Microsoft AI division requires 4 days/week in-office starting Jan 2026 for those within 50 miles of a Microsoft office — **significant blocker for remote**.
- Microsoft has offices in Burlington, MA (Greater Boston area) — roles based there would qualify.
- Principal Group PM roles exist but no confirmed Boston-based or fully-remote ones found.
- Future runs: search `Microsoft "principal group product manager" OR "group product manager" Boston Burlington remote 2026`.

## Databricks

- All Staff PM roles found are SF-based (San Francisco, CA) — **not Boston-compatible**.
- Staff PM, AI Platform — SF
- Staff PM, Databricks Notebooks — SF
- Staff PM, Content Experience — likely SF
- Databricks appears to have ~26 remote roles out of 471, but these are not PM level.
- Future runs: check `site:databricks.com/company/careers "product manager" remote` — if remote PM roles appear, verify location.

## Snowflake

- All PM roles on careers.snowflake.com are on-site in Menlo Park, CA or Bellevue, WA — **not Boston-compatible**.
- Staff PM Developer Platform — Menlo Park (Jan 5, 2026).
- No remote Staff/Group/Director PM roles found.
- 516 Snowflake jobs in Greater Boston on LinkedIn appear to be technical/sales, not PM.
- Future runs: skip detailed Snowflake search unless checking for policy change. Note in seen_jobs: excluded.

## Datadog

- Datadog has a Boston office (Greater Boston Area) — some roles are Boston-based.
- Director PM, Datadog Apps (Boston) found but the listing appears to be from November 2022 — **stale/expired**.
- careers.datadoghq.com detail page 404'd (job removed).
- Staff PM, Product Analytics found on LinkedIn but appears to be NYC-based.
- Future runs: check `careers.datadoghq.com/boston` and `careers.datadoghq.com/remote` for new senior PM openings.
- Datadog is worth monitoring for Boston/remote director-level PM roles — they have Boston presence.
