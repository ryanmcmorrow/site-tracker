# Job Tracker Strategy Log

## 2026-06-06 — All APIs Failed (Network Policy Block)

**Root cause:** The remote execution environment routes outbound traffic through Anthropic's egress gateway proxy. All external job board API domains are not in the proxy's allowlist. Response: `Host not in allowlist`.

This is a network-level restriction, not an API authentication issue.

**Failed companies (all):**
- Greenhouse: anthropic, airbnb, reddit, discord, databricks, stripe, datadog, cloudflare, github, snowflake — all 403 via WebFetch, "Host not in allowlist" via curl
- Ashby: openai — same error
- Lever: netflix — same error

**No roles fetched, no email sent, seen_jobs.json initialized as empty.**

**Resolution needed:** The environment's network policy must be updated to allowlist these domains:
- `boards-api.greenhouse.io`
- `api.ashbyhq.com`
- `api.lever.co`

Until that is done, no job data can be retrieved from this environment.
