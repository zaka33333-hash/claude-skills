---
name: seo-aeo-playbook
description: The "Claude as SEO/AEO growth operator" playbook — a weekly data-driven loop that turns Google Search Console exports, GA4 referral data, and competitor analysis into a prioritized opportunity list, then ships content + schema + performance fixes that earn AI Overview citations from ChatGPT, Perplexity, Gemini, and Google. Use whenever the user asks for a "weekly SEO review", "AEO strategy", "growth loop", "what should I work on this week", "find content gaps", "diagnose zero-click rankings", "audit my GSC data", "rank in ChatGPT", "get cited by AI Overviews", or shares a GSC/GA4/Ahrefs CSV. Also trigger when the user mentions Answer Engine Optimization, AI Overviews stealing traffic, llms.txt, the /about entity anchor, or wants to operationalize content production from first-party data instead of topic prompts. This is the strategic orchestrator that ranks above generic content writing — defer to focused skills (schema-markup, programmatic-seo, site-architecture, page-cro, bencium-aeo, analytics-tracking) for narrow tactical operations.
---

# SEO/AEO Growth Operator Playbook

Built from BadMenFinance's r/ClaudeAI methodology (96 articles → 1,000+ weekly clicks → 348 AI-referred sessions/month, $0 ads) — distilled into a reusable framework with the community's pushback baked in.

## Core principle

**Claude is the strategic analyst, not the writer.** The leverage is not in Claude's prose — it's in Claude's pattern-recognition over first-party data the user already owns but cannot process at scale (GSC exports, GA4 referrals, Lighthouse JSON, competitor URLs). Without that data, Claude regresses to generic AI slop.

The role contract:

| Human owns | Claude owns |
|---|---|
| What to measure, when to publish, business intent | Why a metric is broken (file path + line numbers + root cause) |
| Outcome verification (curl, PSI re-run, GSC delta check) | Specific fix (Lovable prompt, schema patch, CSS edit) |
| Live SERP spot-checks (Claude can't see them) | The article structure that earns AI extraction |
| The "is this true for my brand?" judgment | Prioritized opportunity list ranked by expected impact |

Two non-negotiables:

1. **Bring your own data.** No GSC + GA4 = no leverage. The 2–4 week wait to accumulate real query data is the cost of entry.
2. **Verify every claim with first-party evidence.** Run the curl, re-export the CSV, check the GSC delta. Don't trust your memory or Claude's narrative.

## The 7-step order of operations

This is the canonical sequence. Don't skip ahead — each step gates the next.

1. **Wire up the data.** Verified GSC property + GA4 with `chatgpt.com`, `gemini.google.com`, `perplexity.ai`, `claude.ai` as referral filters. (See `analytics-tracking` skill for setup.)
2. **Fix the technical floor before writing content.** SSR if SPA, llms.txt at root, AI-permissive robots.txt, /about entity anchor with Organization+Person+AboutPage schema. Without this, content ranks but doesn't get cited.
3. **Wait 2–4 weeks** for GSC to accumulate enough query data for pattern detection.
4. **Export the four GSC CSVs** (Queries, Pages, Countries, Devices) + GA4 referral data + any Ahrefs/Semrush exports. Dump into Claude.
5. **Per article, enforce the extractable template** (Quick Answer block → question H2s → comparison tables → FAQ schema → internal links). One article a day at most for solo operators; quality > velocity.
6. **Verify weekly with first-party data.** GSC click delta, GA4 AI-referrer count, PSI score on changed URLs. Loop back to step 4.
7. **Manual SERP spot-checks** for top 20 queries weekly to catch AI Overview cannibalization that Claude can't see (the polcititch correction — see "Honest blind spots" below).

## The weekly data-input loop

This is the heart of the playbook. Every Monday (or whatever cadence the user picks), run this:

### What to dump into Claude

- **GSC > Performance > Queries** CSV (date range: last 28 days, then last 3 months for trend)
- **GSC > Performance > Pages** CSV (same date ranges)
- **GSC > Coverage / Indexing** CSV — finds unindexed articles
- **GA4 > Reports > Acquisition > Traffic acquisition** filtered by Source containing AI engines
- **Ahrefs / Semrush** keyword + backlink exports if available
- **Top 5 competitor URLs** (let Claude crawl their sitemaps)

### What to ask Claude to find

Run Claude through this exact prioritization, in order:

1. **High-impression, zero-click queries.** Title/meta is failing — easiest fix, fastest impact. Rewrite titles using the format: `[Number] Best [Topic] in [Year] (Tested & Ranked)` or `Where Does [X] Store [Y]?` (question format).
2. **Position 1–3 with zero clicks.** AI Overviews stealing traffic. Pivot strategy: become the source AI Overviews cite, not chase a higher rank that no longer exists.
3. **Content gaps where competitors rank and you don't.** Each gap = one article assignment.
4. **Keyword cannibalization** — multiple pages competing for the same query. Decision: consolidate into one canonical, or differentiate with schema/intent.
5. **Unindexed articles.** Generate IndexNow ping commands for Bing/Yandex; for Google, generate the manual GSC URL Inspection list.

### The output Claude should produce

Not prose. A weekly action plan in this exact shape:

```
## Week of [DATE] — Top 5 actions, ranked by expected impact

1. [Action] — [Specific URL/file/query]
   Why: [data-grounded reason, with metric]
   Expected impact: [metric + estimate]
   Time to ship: [hours]
   How to verify: [exact command/check]

2. ...

## What to measure next week
- [Specific GSC/GA4 deltas to check]
```

Claude writes the prompts to fix things; the human runs them and verifies.

## The article structure template

Every article — without exception — uses this structure. Drift from it = lower extractability for AI engines.

```markdown
[Quick Answer block — 40 to 60 words, plain text, directly answers the article's main question]

## H2 phrased as a question
[3-paragraph max body. Lead with the direct answer in the first sentence so it's extractable. Then context.]

## Another H2 phrased as a question
[Same structure]

## Comparison table (when relevant)
| Option | Key trait | When to pick |
|---|---|---|
| ... | ... | ... |

## FAQ
**Q: [exact phrasing of a query users type]**
A: [40–80 word direct answer]

[Repeat 3–5 times — these become FAQPage schema]

[Internal links to 3–5 related articles, contextual not footer]
```

**Why each element earns extraction:**

- **Quick Answer block**: AI Overviews + ChatGPT extract from the first 60–80 words. Direct answer first, context second.
- **Question H2s**: AI engines match user queries to question-format headings preferentially. "Where Does Claude Code Store Skills?" beats "Skill Locations."
- **Comparison tables**: Easy structured extraction. Perplexity in particular cites tables.
- **FAQ section**: Mirrored by FAQPage schema for double extraction (visible content + machine-readable schema).
- **Internal links**: Build topical authority + give Claude something to cross-reference when re-analyzing the corpus.

## Schema layer by page type

This is the AEO infrastructure. Every page type gets its mapped schemas, no exceptions. Defer to the `schema-markup` skill for implementation specifics; the table below is the strategic layout.

| Page type | Required schemas |
|---|---|
| Homepage | Organization · WebSite (with SearchAction) · FAQPage (10–15 Q&As) |
| Article | Article · FAQPage · HowTo (when applicable) · BreadcrumbList · Organization |
| Product/Skill/Service | SoftwareApplication or Product (with pricing) · BreadcrumbList · conditional FAQPage |
| /about | Organization · AboutPage · Person — **load-bearing, not optional** |
| Category/Collection | CollectionPage · BreadcrumbList |
| FAQ standalone | FAQPage |

**Critical pitfall:** duplicate FAQPage schema breaks GSC validation. If the site is React-based, audit whether components emit FAQ schema client-side AND the SSR layer emits it server-side. Pick one (SSR-only is the safe default). Verify with `curl -s [URL] | grep -c FAQPage` — should return 1, not 2+.

## Technical foundation (must-haves)

These are not optimizations — they are prerequisites. A site missing any of them will not get cited by AI engines no matter how good the content is.

1. **SSR if you're on a React/Vue/SPA framework.** A client-rendered SPA serves empty HTML to crawlers and AI bots. For Lovable/Vercel/Netlify, this means an Edge Function (Netlify) or Server Components (Next.js App Router). The OP attributes "most of 150+ page-1 rankings" to fixing this single issue.
2. **`llms.txt` at root.** Plain text file. States: site purpose, key URLs, what to extract from each. Treat it as the README for LLMs.
3. **AI-permissive robots.txt.** Explicitly allow `GPTBot`, `ClaudeBot`, `Google-Extended`, `PerplexityBot`, `CCBot`, `anthropic-ai`. If you're blocking these, you're invisible to the engines you want to be cited by.
4. **`/about` page with full entity schema.** Organization + Person + AboutPage schema. AI engines need to know who you are before citing you. Include founder name, location, founding date, contact, social profiles linked via `sameAs`.
5. **Core Web Vitals on green.** LCP < 2.5s, CLS < 0.1, INP < 200ms. Generate WebP images at correct render dimensions, not 1920px logos rendered at 112px. Lazy-load below-fold sections. Defer analytics to `window.load`.

For perf debugging, paste the raw PageSpeed Insights JSON output into Claude — it diagnoses to file/line and writes the prompts to fix.

## AEO citation tracking

There's no perfect tool for this in 2026. Triangulate three signals:

1. **GA4 referral data**, filtered by source containing: `chatgpt.com`, `gemini.google.com`, `perplexity.ai`, `claude.ai`, `you.com`, `phind.com`. This is your AI-referred traffic count.
2. **Manual weekly spot-checks** — pick top 20 queries from GSC, paste each into ChatGPT, Perplexity, Gemini, Google AI Overview. Note whether your domain is cited. Log in a spreadsheet weekly to track citation rate over time.
3. **Cross-reference zero-click GSC queries vs. AI engine outputs.** A query ranking position 1 with zero clicks + cited by ChatGPT = you're winning the new game. Position 1 with zero clicks + NOT cited = AI Overview is eating you and you have no upside; deprioritize that page or restructure for extraction.

**Market gap to flag to the user:** there is no automated spot-check tool yet. If the user is technical, this is a worthwhile internal tool to build (Playwright + the four AI engines + a query list).

## Honest blind spots (the polcititch correction)

The strongest credible critique of this playbook, raised by user `polcititch` in the comments:

> "claude will confidently flag 'high impression, zero click' opportunities but has no visibility into whether those queries are already locked up by AI overviews or featured snippets, which in 2026 is basically most of them. so you end up optimizing for clicks that don't exist anymore regardless of where you rank."

**This is real.** Claude's gap analysis can produce false positives. The mitigation is the manual SERP spot-check (step 7 of the order of operations). For any query Claude flags as "high-impression, zero-click — fix the title", verify the live SERP first:

- Is there an AI Overview? → reframe content for citation, not click.
- Is there a featured snippet held by a competitor? → out-snippet them with a tighter Quick Answer block.
- Neither? → title rewrite is the right move.

Skipping this step compounds wasted effort.

## Kill criteria — when this playbook does NOT apply

Don't force this on:

- **Pre-traffic sites with no GSC data yet.** The loop bootstraps from GSC; without it you're guessing. Spend the first 2–4 weeks just publishing baseline content + technical setup, then start the loop.
- **Brand/transactional intent dominant** (e.g., "buy [brand X]"). The playbook is informational-query optimized.
- **YMYL niches with low AI Overview triggering** — medical, legal, financial advice often suppress AI Overviews due to liability. The AEO premise softens.
- **Hyperlocal-only intent** (e.g., "plumber in [tiny town]") — Google Business Profile and Maps win, not blog content.
- **Anyone who can't verify outcomes themselves.** If the user can't run curl, read PageSpeed JSON, or interpret GSC, they'll ship broken changes and not know it. The vibe-coding risk is real (RealEstatePirate's comment).
- **Editorial brands whose value IS the prose voice.** Extraction-optimized writing reads flat by design — strip context to lead with the answer. Brands selling prose quality should not adopt this template wholesale.

## Specific prompt templates

These are the verbatim prompt shapes to feed Claude. Adapt the bracketed parts.

### Weekly opportunity scan

```
Attached: GSC Queries CSV (last 28 days), GSC Pages CSV, GA4 acquisition CSV, indexing status CSV.

Find, in priority order:
1. Queries with > [threshold, default 1000] impressions and CTR < 1% — title/meta problem.
2. Queries ranking position 1–3 with < 5 clicks — AI Overview cannibalization candidate.
3. Pages with > 500 impressions but no rankings on the queries listed in [competitor sitemap].
4. Multiple URLs ranking on the same query — cannibalization to consolidate.
5. URLs with zero impressions in 90 days — indexing problem.

Output: top 5 actions for this week with metric, expected impact, time-to-ship, and verification command.
Do not write content. Do not suggest "create more content." Find what's broken first.
```

### Article structure enforcement

```
Topic: [topic]
Primary query: [primary query phrased as a question]
Target length: 1200–1800 words

Use the SEO/AEO playbook article template:
- Quick Answer block (40–60 words, plain text, top of page, before any H2)
- 4–6 H2s, each phrased as a question that real users would type
- Lead each H2 section with the direct answer in the first sentence
- Comparison table where it makes sense
- FAQ section with 3–5 Q&As (these become FAQPage schema)
- 3–5 contextual internal links to: [list]

Do not write fluff intro paragraphs. Lead with the answer.
```

### PageSpeed performance triage

```
Attached: PageSpeed Insights JSON for [URL].

Identify the top 3 opportunities by impact on LCP/CLS/INP. For each:
- Root cause (specific file, bundle, asset)
- Concrete fix
- Verification command (curl, PSI re-run trigger, etc.)

Then write the [Lovable / Next.js / Shopify Liquid] prompt to ship the fix.
```

### Schema audit

```
Attached: HTML source of [URL] (or list of URLs).

Audit:
1. Which schema types are present? List them.
2. Are any duplicated (most commonly FAQPage emitted both client-side and server-side)?
3. Are required schemas missing for this page type? (Reference the playbook's page-type → schema map.)
4. Generate the patch.
```

## Verification rituals

After every change, before claiming success — run these:

| What changed | Verification command/check |
|---|---|
| Schema patch | `curl -s [URL] \| grep -A 50 'application/ld+json'` — confirm presence and uniqueness |
| Title rewrite | Re-pull GSC CTR after 14 days; expect lift if SERP is click-eligible |
| Performance fix | Re-run PSI; LCP/CLS/INP delta visible immediately |
| Content publish | URL Inspection in GSC → "Request Indexing" within 1 hour |
| llms.txt / robots.txt | `curl -s [domain]/llms.txt` and `curl -s [domain]/robots.txt` to confirm reachable |
| AEO citation attempt | 7-day spot-check across ChatGPT/Perplexity/Gemini for the target query |

Don't claim work is done without running the corresponding check. Echoing the `verification-before-completion` skill: evidence before claims, always.

## What this playbook is NOT

To prevent scope creep:

- It's not an SEO audit — for that, use the `marketing:seo-audit` skill.
- It's not for generating content at scale — see `programmatic-seo`.
- It's not for site restructure — see `site-architecture`.
- It's not for narrow schema fixes — see `schema-markup`.
- It's not for ad copy or paid acquisition — see `paid-ads`, `ad-creative`.
- It's not for AEO content drafting in isolation — see `bencium-aeo`.

This skill is the **weekly orchestrator** that decides which of the above to invoke and when, based on what the data says is broken.
