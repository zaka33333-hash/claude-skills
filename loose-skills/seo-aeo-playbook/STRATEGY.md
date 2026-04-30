# SEO/AEO Skill Usage Strategy

How to use `seo-aeo-playbook` (strategy) and `anthropic-skills:seo-aeo-optimization` (tactics) together. From now on this is the standing operating procedure for any web project.

## Core mental model

You don't need to remember which skill to call. Trigger it by need:

- **"What should I work on?" / "Why isn't this working?"** → fires `seo-aeo-playbook` (the analyst)
- **"Audit this URL" / "Generate schema" / "Write llms.txt" / "Run PageSpeed on this"** → fires `anthropic-skills:seo-aeo-optimization` (the executor)

Both can fire in the same turn. Strategy decides what to do; tactics generate the deliverable.

## The two-skill split

| Surface | Skill |
|---|---|
| Why a metric is broken; what to prioritize this week | `seo-aeo-playbook` |
| Run a live audit on a URL with curl/PSI/Python | `anthropic-skills:seo-aeo-optimization` |
| Decide whether to fix titles vs reframe for AI extraction | `seo-aeo-playbook` |
| Generate a schema JSON-LD file from a template | `anthropic-skills:seo-aeo-optimization` |
| Plan the weekly cadence + verification rituals | `seo-aeo-playbook` |
| Write llms.txt scaffold | `anthropic-skills:seo-aeo-optimization` |
| Triangulate AI citation tracking signals | `seo-aeo-playbook` |
| Spawn parallel competitor subagents | `anthropic-skills:seo-aeo-optimization` |

## Setup ritual — Week 0 (any new project)

Before publishing any new content, in this order:

1. **Wire data**: GSC verified + sitemap submitted + GA4 with `chatgpt.com|gemini.google.com|perplexity.ai|claude.ai|copilot.microsoft.com` referral filter
2. **Run a baseline audit** with `anthropic-skills:seo-aeo-optimization` → run `audit.sh` on the homepage + 3 representative pages → save report
3. **Fix the technical floor** based on the audit report, in this priority:
   1. SSR if the site is a SPA (highest ROI)
   2. AI-permissive `robots.txt`
   3. `llms.txt` at root (use Anthropic's `generate_llms_txt.py`)
   4. `/about` page with `Organization + Person + AboutPage` schema
   5. Page-type → schema mapping deployed (FAQPage, Article, etc.)
   6. Core Web Vitals on green
4. **Don't write content yet.** GSC needs 2–4 weeks of query data before the analyst loop is meaningful. Use the wait to publish baseline content (≤1 article/week, structured per the article template in `seo-aeo-playbook`).

## Weekly ritual — 30 minutes every Monday

The whole loop, every week:

```
1. Export — 5 min
   - GSC > Performance > Queries (last 28 days CSV)
   - GSC > Performance > Pages (last 28 days CSV)
   - GSC > Indexing CSV
   - GA4 > Acquisition filtered by AI engines (CSV)

2. Prompt — paste into Claude with the "Weekly opportunity scan" template from seo-aeo-playbook
   → Claude runs the 5-pattern prioritization, returns top 5 actions

3. Manual SERP check — 10 min
   For Claude's top 5 actions, paste each query into ChatGPT, Perplexity,
   Google AI Overview. Confirm whether the gap is actionable or already
   locked up by AI Overviews (the polcititch correction).

4. Ship — Tuesday/Wednesday
   For each surviving action, fire the relevant focused skill:
   - title rewrite → just edit, no skill needed
   - article missing → /article-structure prompt
   - schema fix → seo-aeo-optimization for the JSON-LD
   - perf fix → seo-aeo-optimization for the curl/PSI run
   - CRO opportunity → /page-cro

5. Verify — Thursday
   Run the verification rituals table from seo-aeo-playbook.
   Don't claim done without curl/PSI/GSC delta evidence.
```

## Monthly ritual — 60 minutes (first Friday of each month)

What the weekly cadence misses:

- **AI citation rate spot-check** — top 20 queries across 5 engines, log to a spreadsheet, compare month-over-month. This is the closest thing to "AEO ranking" that exists.
- **Schema integrity sweep** — `curl -s [URL] | grep -c FAQPage` across 10 random pages. Catch duplicate-schema regressions early.
- **GA4 AI-referrer trend** — month/month delta, broken down by source.
- **Core Web Vitals regression check** — run PSI on the 5 highest-traffic pages.
- **Indexing audit** — anything from the last 4 weeks not indexed → IndexNow ping + GSC URL Inspection.

Output: a 10-line monthly diff to log somewhere.

## Quarterly ritual — strategic re-orientation

Once a quarter, step out of the weekly loop and ask:

- Is the playbook still right for this site? (Re-check kill criteria — has the site shifted to brand-intent or YMYL?)
- Are AI citations growing as a share of traffic? If yes, double down on AEO. If no after 6 months, the niche may not trigger AI Overviews — pivot.
- Are there new AI engines worth tracking? (you.com, phind.com — already on the watch list)
- Re-export competitor sitemaps; spawn the parallel subagent audit pattern from `anthropic-skills:seo-aeo-optimization`.
- Decide on next quarter's content theme based on cumulative gap analysis.

## What you keep doing yourself

Don't delegate these to Claude — they require human judgment or human-in-the-loop verification:

- The publish/don't-publish call on every article (the brand voice judgment)
- Live SERP spot-checks (Claude can't see them)
- The "is this even our buyer?" filter on keyword opportunities
- Final approval before any schema goes live (a wrong schema is worse than no schema)
- The annual "is search even our channel?" question

## Red flags — when to abort the playbook

Stop if any of these are true:

- 8+ weeks of weekly loops with no measurable lift in clicks OR AI citations → niche may not respond; pivot strategy
- The site shifts to brand-led acquisition (referral, social, paid) > 80% — search is no longer the leverage
- You can't verify outcomes yourself (PSI, GSC, curl) — shipping blind is worse than not shipping
- Schema validation errors compounding instead of decreasing — pause and audit, don't add more

## Cadence summary card

| Frequency | Time | What |
|---|---|---|
| One-time | ~4 hours | Setup ritual (data wiring + technical floor) |
| Weekly (Monday) | 30 min | Export → prompt → SERP check → ship plan |
| Weekly (Tue–Thu) | varies | Ship + verify |
| Monthly | 60 min | AI citation rate, schema sweep, GA4 trend |
| Quarterly | 2 hours | Strategic re-orientation, competitor re-audit |

That's it. The weekly loop is where 80% of the value is. Don't skip the manual SERP check.
