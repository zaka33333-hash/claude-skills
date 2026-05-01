---
name: skill-router
description: Use this at the start of every non-simple prompt to identify which other skills should be invoked. Triggers on ANY substantive request — building, fixing, debugging, writing, designing, planning, auditing, optimizing, deciding, researching, or anything more than a one-line factual lookup. This is the meta-skill that scans the full installed-skills catalog and routes to the relevant skills (often combining several). Use when the user mentions a project, asks for a deliverable, shares a screenshot or link, says "do X" or "help me with Y", or otherwise gives a substantive task. Trigger on phrases like "what should I do", "how do I", "build me", "review this", "audit", "fix the", "plan for", "analyze", "write a", "design a", "help with", "what's wrong with", "why isn't", or sharing GSC/GA4/CSV/code/screenshots.
---

# Skill Router — auto-select and invoke skills per turn

This skill encodes the routing logic for matching a user's request to the right skill(s) from the installed catalog. It does NOT do the work itself — it picks the tools and dispatches.

## Procedure

For every non-simple prompt:

1. **Categorize** the request (build / fix / write / audit / plan / decide / debug / research / verify / etc.)
2. **Match** to a skill cluster below
3. **Select 1–3** most relevant skills (rarely more — overload reduces quality)
4. **Invoke directly** via the `Skill` tool — no asking, no announcing
5. **If two skills overlap heavily**, use the conflict-resolution table at the bottom

If the prompt is genuinely simple (one-line factual answer, casual chat, trivial command), skip this skill entirely. Overhead exceeds value.

## Cluster map

### Strategy & ops (the orchestrators)

| Intent | Skill |
|---|---|
| Weekly SEO/AEO growth loop, GSC analysis, AI citation strategy | `seo-aeo-playbook` |
| Single-task SEO operations (audit, schema, llms.txt) | `anthropic-skills:seo-aeo-optimization`, `marketing:seo-audit` |
| Full marketing campaign | `marketing:campaign-plan` |
| Solo-founder grassroots launch | `organic-first-campaign` |
| Daily / weekly briefings | `sales:daily-briefing`, `legal:brief`, `enterprise-search:digest` |

### Building / creating

| Intent | Skill |
|---|---|
| Distinctive web UI, avoiding "AI slop" | `frontend-design` (Anthropic original), `bencium-innovative-ux-designer` |
| Tactical UI components with shadcn/Tailwind | `ui-styling`, `web-design-guidelines` |
| Reference DB for design choices (palettes, fonts, styles) | `ui-ux-pro-max` |
| Comprehensive design suite (logo, CIP, branded assets) | `design` |
| Banners (social/ads/web hero) | `banner-design` |
| AI image/video prompts for scroll-stopping content | `scroll-stop-prompter` |
| Favicons, app icons, OG images | `web-asset-generator` |
| Generative art (p5.js) | `algorithmic-art` |
| Posters, static art | `canvas-design` |
| 3D asset prompts | `3d-asset-generator` |
| HTML presentations with Chart.js | `slides` |
| Pitch decks / .pptx files | `anthropic-skills:pptx` |
| Word docs | `anthropic-skills:docx` |
| Spreadsheets | `anthropic-skills:xlsx` |
| Multi-component claude.ai HTML artifacts (React/Tailwind/shadcn) | `anthropic-skills:web-artifacts-builder` |
| Theme application to artifacts | `anthropic-skills:theme-factory` |

### SEO / AEO tactical

| Intent | Skill |
|---|---|
| Schema markup / JSON-LD | `schema-markup`, `anthropic-skills:seo-aeo-optimization` |
| Programmatic SEO at scale | `programmatic-seo` |
| Site architecture / URL hierarchy | `site-architecture` |
| Backlinks via directories | `directory-submissions` |
| AEO-specific content optimization (FAQ schema, evidence panels) | `bencium-aeo` |
| Competitor alternatives pages ("X vs Y") | `competitor-alternatives` |
| Pull competitor ad library data | `competitive-ads-extractor` |
| Analytics tracking setup (GA4) | `analytics-tracking` |

### Conversion / CRO / experimentation

| Intent | Skill |
|---|---|
| Page conversion optimization | `page-cro` |
| Popup / modal / overlay optimization | `popup-cro` |
| Lead capture form optimization | `form-cro` |
| A/B test design | `ab-test-setup` |
| Pricing decisions | `pricing-strategy` |
| Lead magnet creation | `lead-magnets` |
| Free tool as lead gen | `free-tool-strategy` |

### Paid acquisition

| Intent | Skill |
|---|---|
| Google/Meta/LinkedIn ads strategy | `paid-ads` |
| Ad creative generation at scale | `ad-creative` |
| Competitor ad research | `competitive-ads-extractor` |

### Content writing

| Intent | Skill |
|---|---|
| Brainstorm content topics | `content-strategy`, `marketing-ideas` |
| Long-form article writing with research | `content-research-writer` |
| Edit / refresh existing copy | `copy-editing` |
| Channel-specific content | `marketing:content-creation`, `marketing:draft-content` |
| Social media content | `social-content` |
| Video content | `video` |
| Apply behavioral psychology | `marketing-psychology` |
| Brand voice review | `marketing:brand-review`, `brand-voice:enforce-voice` |

### Engineering — code work

| Intent | Skill |
|---|---|
| Architecture decision (ADR) | `engineering:architecture` |
| System design | `engineering:system-design`, `human-architect-mindset`, `renaissance-architecture` |
| Code review (general) | `engineering:code-review`, `requesting-code-review` |
| Automated PR review (5-agent) | `/code-review` slash command (from code-review plugin) |
| Receive code review feedback | `receiving-code-review` |
| Tech debt audit | `engineering:tech-debt`, `vanity-engineering-review` |
| Security review | `/security-review`, `security-guidance` plugin |
| Implementation planning | `writing-plans` → `executing-plans` |
| Phased plan with doc discovery (claude-mem variant) | `claude-mem:make-plan` → `claude-mem:do` |
| Subagent-driven dev (fresh agent per task) | `subagent-driven-development` |
| Map codebase into feature flowcharts | `claude-mem:pathfinder` |
| Token-optimized AST code search (vs full file Read) | `claude-mem:smart-explore` |
| Parallel-agent investigations | `dispatching-parallel-agents` |
| Git worktree for isolation | `using-git-worktrees` |
| Finish a feature branch | `finishing-a-development-branch` |
| Documentation | `engineering:documentation` |
| Standup updates | `engineering:standup` |

### Engineering — debugging

| Intent | Skill |
|---|---|
| Generic structured debug | `engineering:debug` |
| Trace deep error to root cause | `root-cause-tracing` |
| Validate at every layer (defense in depth) | `defense-in-depth` |
| Verify before claiming done | `verification-before-completion` |

### Engineering — testing

| Intent | Skill |
|---|---|
| Write tests first | `test-driven-development` |
| Avoid mock-testing anti-patterns | `testing-anti-patterns` |
| Async race condition fix | `condition-based-waiting` |
| Browser testing with Playwright | `webapp-testing` |
| Accessibility audit (WCAG) | `design:accessibility-review`, `accesslint-audit-and-fix` |
| Test strategy planning | `engineering:testing-strategy` |

### Engineering — incident & deploy

| Intent | Skill |
|---|---|
| Production incident workflow | `engineering:incident-response` |
| Pre-deploy verification | `engineering:deploy-checklist` |

### Plugin / MCP development

| Intent | Skill |
|---|---|
| Build an MCP server | `build-mcp-server`, `anthropic-skills:mcp-builder` |
| Build MCP UI app | `build-mcp-app` |
| Bundle MCP for distribution | `build-mcpb` |
| Create a Claude Code agent | `agent-development` |
| Create a slash command | `command-development` |
| Create a hook | `hook-development` |
| Configure MCP integration | `mcp-integration` |
| Plugin settings / structure | `plugin-settings`, `plugin-structure` |
| Skill development | `skill-development`, `anthropic-skills:skill-creator` |
| Hookify rule | `writing-hookify-rules` |

### Problem-solving / when stuck

| Intent | Skill |
|---|---|
| Don't know which technique to use | `when-stuck` (dispatcher) |
| Flip an assumption | `inversion-exercise` |
| Test at extremes (1000x bigger/smaller) | `scale-game` |
| One-insight-eliminates-many | `simplification-cascades` |
| Force unrelated concepts together | `collision-zone-thinking` |
| Pattern across 3+ domains | `meta-pattern-recognition` |

### Decision-making frameworks

| Intent | Skill |
|---|---|
| Architecture choices via entropy/decay lens | `negentropy-lens` |
| Multiple valid approaches; don't force resolution | `preserving-productive-tensions` |
| Trace why we use X (knowledge lineage) | `tracing-knowledge-lineages` |
| Renaissance vs derivative thinking | `renaissance-architecture` |

### Research / analysis

| Intent | Skill |
|---|---|
| Web search with content extraction | `firecrawl-search`, WebSearch |
| Scrape JS-heavy page | `firecrawl-scrape` |
| Crawl entire site/section | `firecrawl-crawl` |
| Map all URLs on a site | `firecrawl-map` |
| Browser automation in scrape | `firecrawl-interact`, `firecrawl-agent` |
| Search past Claude conversations | `remembering-conversations` |
| Library docs lookup (current versions) | `context7` (MCP), `firecrawl-build-onboarding` |
| Data-driven analysis (CSV / DB) | `data:analyze`, `data:explore-data` |
| Competitor research | `marketing:competitive-brief`, `product-management:competitive-brief`, `sales:competitive-intelligence` |
| Lead research | `lead-research-assistant`, `sales:account-research` |
| Customer research | `customer-support:customer-research`, `design:user-research` |
| Live store data (Shopify) | `mcp__shopify-mcp__*` (31 tools) |
| Shopify API/Liquid docs | `mcp__shopify-dev-mcp__*` |
| Search Obsidian vault notes | `mcp__obsidian__simple_search`, `mcp__obsidian__complex_search` |

### Verification / QA

| Intent | Skill |
|---|---|
| Before claiming work done | `verification-before-completion` |
| UI design quality | `design-audit`, `design:design-critique`, `web-design-guidelines` |
| Brand consistency | `marketing:brand-review`, `brand-voice:enforce-voice` |
| Accessibility | `accesslint-audit-and-fix`, `design:accessibility-review` |
| Schema integrity | `schema-markup`, manual curl checks |
| Typography correctness | `typography` |
| Vanity/over-engineering check | `vanity-engineering-review` |

### Communication & coordination

| Intent | Skill |
|---|---|
| Detect ambiguous intent | `adaptive-communication` |
| Stakeholder update | `product-management:stakeholder-update`, `operations:status-report` |
| Customer email response | `customer-support:draft-response` |
| Sales outreach | `sales:draft-outreach`, `apollo:prospect` |
| Email sequence | `marketing:email-sequence` |
| Brainstorming session | `brainstorming`, `product-management:product-brainstorming` |
| Self-interview / clarify thinking | `inversion-exercise` (adjacent) |

### File / asset management

| Intent | Skill |
|---|---|
| Organize files / find dupes | `file-organizer` |
| Invoice & receipt organization | `invoice-organizer` |
| Image quality enhancement | `image-enhancer` |
| Generate changelog from git | `changelog-generator` |

### Documentation / project memory

| Intent | Skill |
|---|---|
| Initialize / improve CLAUDE.md | `init`, `claude-md-improver` |
| Recommend Claude Code automations | `claude-automation-recommender` |
| Session usage report | `session-report` |
| Memory consolidation | `anthropic-skills:consolidate-memory` |
| Two-tier memory system | `productivity:memory-management` |
| Read/write Obsidian notes (Gemma vault) | `mcp__obsidian__*` (CRUD via Local REST API plugin on port 27124) |
| Search past Claude sessions semantically | `claude-mem:mem-search`, `mcp__plugin_claude-mem_mcp-search__*` |
| Build AI-queryable knowledge base from observations | `claude-mem:knowledge-agent` |
| Project narrative / "Journey Into [Project]" report | `claude-mem:timeline-report` |

### Operations workflow

| Intent | Skill |
|---|---|
| Operational runbook | `operations:runbook` |
| Process documentation | `operations:process-doc` |
| Risk assessment | `operations:risk-assessment` |
| Vendor evaluation | `operations:vendor-review`, `legal:vendor-check` |
| Reusable multi-step task templates (parameterized) | `ruflo-workflows:*` |
| Run agents autonomously in a loop (delegated, not turn-based) | `ruflo-autopilot:*` |
| Token usage budgets / cost alerts | `ruflo-cost-tracker:*` |

### Multi-agent orchestration

| Intent | Skill |
|---|---|
| Coordinate multiple agents as a team (parallel work) | `ruflo-swarm:*` (hierarchical / mesh / adaptive topologies) |
| Agents that learn from past success patterns | `ruflo-intelligence:*` |
| Break large goals into trackable plans | `ruflo-goals:*` |
| Foundation server / health checks / plugin discovery | `ruflo-core:*` |

## Common combinations (pre-mapped)

When the user asks about the following situations, fire these in order:

| User asks | Fire these (in order) |
|---|---|
| "Audit my SEO" | `anthropic-skills:seo-aeo-optimization` (audit) → `seo-aeo-playbook` (interpret findings) |
| "What should I work on this week" (with GSC data) | `seo-aeo-playbook` (weekly opportunity scan) |
| "Write a blog article on X" | `content-research-writer` → `seo-aeo-playbook` (article structure) |
| "Build a landing page" | `frontend-design` → `ui-ux-pro-max` → `typography` → `accesslint-audit-and-fix` |
| "Plan paid ad campaign" | `paid-ads` → `ad-creative` → `competitive-ads-extractor` → `page-cro` |
| "Debug this bug" | `engineering:debug` → `root-cause-tracing` → `verification-before-completion` |
| "Build a new feature" | `brainstorming` → `writing-plans` → `executing-plans` → `verification-before-completion` |
| "Review my code before merging" | `engineering:code-review` (manual) or `/code-review` (PR auto) |
| "Stuck on this problem" | `when-stuck` (dispatcher routes) |
| "Schema for this page" | `schema-markup` |
| "Research my competitor" | `firecrawl-scrape` → `marketing:competitive-brief` → `competitive-ads-extractor` |
| "Generate a Shopify product report" | `mcp__shopify-mcp__get-products` → `data:analyze` |
| "Pull the most recent orders" | `mcp__shopify-mcp__get-orders` |
| "Live page indexing audit" | `seo-aeo-playbook` (Week 1 procedure) |
| "Make a video / scroll-stopping post" | `scroll-stop-prompter` (or `video` skill) |
| "Find / read / write a note in my vault" | `mcp__obsidian__simple_search` → `mcp__obsidian__get_file_contents` → `mcp__obsidian__patch_content` (or `append_content`) |
| "Save this to my Obsidian" | `mcp__obsidian__append_content` (or create new note via Local REST API) |
| "Add audio / music / SFX to a rendered video" | `video-processing-editing` (FFmpeg automation) |
| "Cut, trim, or concatenate video clips" | `video-processing-editing` |

## Conflict resolution — when two skills both seem to fit

| Tension | Pick |
|---|---|
| Strategic playbook vs single-task tactical | Whichever the user is actually asking for. Strategic if "what should I work on", tactical if "do X". |
| `frontend-design` vs `bencium-innovative-ux-designer` | They're nearly identical; `frontend-design` wins as the canonical Anthropic version. |
| `engineering:code-review` vs `/code-review` slash | Slash command for live PR auto-review with GitHub integration; the `engineering:` skill for ad-hoc diff review. |
| `marketing:seo-audit` vs `seo-aeo-playbook` | seo-audit for one-time deliverable; playbook for the ongoing operator workflow. |
| `bencium-aeo` vs `anthropic-skills:seo-aeo-optimization` | Anthropic's is broader; bencium is FAQ-schema/evidence-panel focused. Anthropic wins by default. |
| `design` (the comprehensive suite) vs specific design skills | Use the specific skill (banner-design, slides, etc.) when the task is narrow; `design` when the user wants the multi-asset CIP-level treatment. |
| `firecrawl-scrape` vs WebFetch | firecrawl for JS-heavy pages, paywalled, or when WebFetch fails; WebFetch for fast simple HTML. |
| `webapp-testing` vs Playwright MCP | webapp-testing skill teaches the patterns; Playwright MCP executes the actual browser. Use both. |

## Anti-patterns

Don't:

- Fire 5+ skills for one prompt. Pick the 1–3 that genuinely matter.
- Re-invoke a skill already loaded earlier in the same turn. Its content is already in context.
- Use a skill that's "close" but not actually a fit — it loads pages of irrelevant instructions and degrades the response.
- Default to the most prominent / first-to-mind skill. Scan the catalog deliberately each turn.
- Use this routing skill on simple lookups. The overhead breaks fast factual answers.
- Override user preferences encoded in `feedback_*.md` memory files. Memory rules > skill instructions.

## Interaction with feedback memories

This skill complements (does not replace) the user's standing memory rules:

- `feedback_proactive_skill_use.md` — sets the active-scan-not-passive-match principle. This skill IS the active scan made concrete.
- `feedback_quality_bar_10_of_10.md` — skills serve quality. If a skill's instructions would degrade output, ignore those instructions.
- `feedback_dont_overfit_star_toner.md` — don't reflexively anchor to Star Toner. Pick skills based on the task, not the project.
- `feedback_context_discipline.md` — don't dump big tool outputs into context. Save to disk, summarize back.
- `feedback_seo_aeo_first.md` — for any web deliverable, SEO/AEO is the floor.
- `feedback_mobile_first_perf.md` — for any Star Toner or perf-sensitive web work, mobile-first is the floor.

## When to skip this skill entirely

- One-line factual lookup ("what's 2+2", "what time is it in Tokyo", "is Python installed")
- Casual chat ("ok", "thanks", "got it")
- Trivial command (`ls`, `git status`, `which X`)
- Reading or showing a single file the user named
- Continuing a conversation already routed correctly earlier (don't re-route mid-task)

## Catalog reference

For a full alphabetized index of every installed skill with a one-line description and trigger phrases, see `references/catalog.md`.
