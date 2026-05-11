---
name: skill-router
description: Activate at the START of EVERY user prompt — no matter how trivial. Two jobs per turn (1) match the request to 0-3 skills from the catalog and (2) pick the cheapest model that still delivers 10/10 quality. Triggers on ANY user input including one-word replies, casual chat, screenshots, links, file paths, code, "do X", "fix Y", "build me", "translate", "review", "watch this", or any substantive task. Token savings and model selection are non-negotiable — Gemini (free under AI Pro) preferred whenever quota allows.
---

# Skill Router — auto-select skills AND the cheapest 10/10 model per turn

This skill is the per-turn dispatcher. Two jobs:

1. **Skill match** — pick 0–3 skills from the catalog that fit the request
2. **Model match** — pick the cheapest model that still hits 10/10 quality

Priority order is fixed: **quality 10/10 is non-negotiable, token savings second**. Never downgrade the model if the task demands the bigger one — but never overspend either.

## Procedure (run on every prompt)

1. **Categorize** the request — trivial / medium / complex (use the model-match table below)
2. **Skill match** — pick the 1–3 most relevant skills, or **none** if the prompt is a one-word confirm / casual reply
3. **Model match** — pick the cheapest model that meets the bar (table below)
4. **Invoke** the selected skills via the `Skill` tool — no asking, no announcing
5. **If you're already on the right model and skill**, proceed silently. No need to narrate the routing.

If the prompt is one word ("ok", "yes", "done") or a casual ack, skip the skill step but still answer in the cheapest mode that fits.

## Model selection — cheapest 10/10 wins

| Task profile | Use this | Why |
|---|---|---|
| Trivial Q / one-liner / lookup / format / typo / one-word reply / confirm | **Haiku 4.5** OR `gemini -p` with **gemini-2.5-flash** | Same quality as bigger models on trivial tasks; ~10× cheaper than Sonnet, free under AI Pro for Gemini |
| Medium reasoning / single-file edit / structured task / data formatting / SEO rewrite | **Sonnet 4.6** OR `gemini -p` with **gemini-2.5-pro** | Best price/quality ratio; Gemini 2.5 Pro is free under AI Pro |
| Complex multi-file refactor / architecture / hard reasoning / production-critical code | **Opus 4.7** (current default) — keep going | The expensive one earns its keep when the task is hard |
| Second opinion on complex code | `/codex:adversarial-review` or `/codex:review` | GPT-5.5 catches what Claude misses; uses ChatGPT subscription, not Claude tokens |
| Translation / multimodal (video, audio, large PDFs) / >500k-token context scan | `gemini -p` (Gemini 2.5 Pro) | 1M context, multilingual depth, **free under AI Pro** — always prefer when AI Pro quota is healthy |
| Background long-running task | `/codex:rescue` or `/gemini:rescue` | Delegate while Claude keeps working in foreground |

**Rules:**
- **Default to Gemini whenever the task fits.** AI Pro covers it free; saves Claude quota for hard work.
- **Drop to Haiku/Flash freely.** Trivial tasks don't need Opus.
- **Never downgrade if quality demands the bigger model.** 10/10 quality is the floor.
- **If the user is on Opus 4.7 for a trivial task**, you don't need to switch models mid-session — but for the next session or batch job, route the appropriate way.

## When to skip skill-router entirely

For these prompts, skill-router consumes more tokens than it saves — answer directly in the current model:
- Pure ack: "ok", "yes", "done", "thanks", "got it"
- A typo in the previous prompt being corrected
- Continuing a task already routed correctly earlier in the turn

## Cluster map

### Strategy & ops (the orchestrators)

| Intent | Skill |
|---|---|
| Weekly SEO/AEO growth loop, GSC analysis, AI citation strategy | `seo-aeo-playbook` |
| Single-task SEO operations (audit, schema, llms.txt) | `anthropic-skills:seo-aeo-optimization`, `marketing:seo-audit` |
| Full marketing campaign | `marketing:campaign-plan` |
| Solo-founder grassroots launch | `organic-first-campaign` |
| Daily / weekly briefings | `sales:daily-briefing`, `legal:brief`, `enterprise-search:digest` |
| Build / refresh marketing context doc | `product-marketing-context` |

### Building / creating

| Intent | Skill |
|---|---|
| Distinctive web UI, avoiding "AI slop" | `frontend-design` (Anthropic original), `bencium-innovative-ux-designer` |
| Translate Figma designs into production code with 1:1 visual fidelity | `figma-implement-design` |
| Reverse-engineer design tokens (colors, type, spacing, shadows) from any public URL | `extract-design-system` |
| Tactical UI components with shadcn/Tailwind | `ui-styling`, `web-design-guidelines` |
| Reference DB for design choices (palettes, fonts, styles) | `ui-ux-pro-max` |
| Comprehensive design suite (logo, CIP, branded assets) | `design` |
| Banners (social/ads/web hero) | `banner-design` |
| AI image/video prompts for scroll-stopping content | `scroll-stop-prompter` |
| Math/algorithm explainer videos (3Blue1Brown style, Manim CE) | `manim-video` |
| Infographics: 21 layouts × 21 styles (bento-grid, hand-craft, etc.) | `baoyu-infographic` |
| Kinetic typography / DOM-free text-as-geometry (Cheng Lou's pretext) | `pretext` |
| Favicons, app icons, OG images | `web-asset-generator` |
| Generative art (p5.js) | `algorithmic-art` |
| Custom interactive D3.js visualizations / SVG charts | `d3-viz` |
| Posters, static art | `canvas-design` |
| 3D asset prompts | `3d-asset-generator` |
| Interactive HTML playgrounds (single-file explorers) | `playground` |
| AI-first interfaces with memory + trust evolution | `relationship-design` |
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
| Build / leverage online communities for growth | `community-marketing` |
| Referral / affiliate / word-of-mouth program | `referral-program` |
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
| Strip AI-isms from prose (de-AI scrub before publish) | `humanizer` |
| Channel-specific content | `marketing:content-creation`, `marketing:draft-content` |
| Social media content | `social-content` |
| Video content | `video` |
| Apply behavioral psychology | `marketing-psychology` |
| Brand voice review | `marketing:brand-review`, `brand-voice:enforce-voice` |
| Marketing performance report (KPIs, wins/misses) | `marketing:performance-report` |
| Brand-voice discovery / guidelines / enforcement | `brand-voice:discover-brand` → `brand-voice:guideline-generation` → `brand-voice:brand-voice-enforcement` |

### Engineering — code work

| Intent | Skill |
|---|---|
| Architecture decision (ADR) | `engineering:architecture` |
| System design | `engineering:system-design`, `human-architect-mindset`, `renaissance-architecture` |
| Code review (general) | `engineering:code-review`, `requesting-code-review` |
| Automated PR review (5-agent) | `/code-review` slash command (from code-review plugin) |
| Code-review skill (PR/diff focused review) | `code-review:code-review` |
| Review changed code for reuse / quality / efficiency | `simplify` |
| Receive code review feedback | `receiving-code-review` |
| Tech debt audit | `engineering:tech-debt`, `vanity-engineering-review` |
| Security review | `/security-review`, `security-guidance` plugin |
| Implementation planning | `writing-plans` → `executing-plans` |
| Concise plan from a prompt (single-message output) | `create-plan` |
| Gated SPEC → PLAN → TASKS → IMPLEMENT (human approval per phase) | `spec-driven-development` |
| Verify code against official docs (detect stack → fetch → cite) | `source-driven-development` |
| Find deepening opportunities / refactor shallow → deep modules | `improve-codebase-architecture` |
| Large multi-file migrations / framework upgrades (Composio CLI, batched PRs) | `codebase-migrate` |
| Sunset old systems / Strangler / Adapter / feature-flag migrations | `deprecation-and-migration` |
| Optimize agent context (CLAUDE.md tiers, scope, trust levels) | `context-engineering` |
| Get a higher-level map of the area before editing | `zoom-out` |
| Next.js patterns — RSC, route handlers, file conventions, async APIs, metadata | `next-best-practices` |
| React/Next.js performance optimization (Vercel Engineering) | `vercel-react-best-practices` |
| Stripe integration — API choice (Checkout vs PaymentIntents), Connect, Billing, webhooks | `stripe-best-practices` |
| Postgres / Supabase — schema, RLS, indexing, query optimization | `supabase-postgres-best-practices` |
| Phased plan with doc discovery (claude-mem variant) | `claude-mem:make-plan` → `claude-mem:do` |
| Subagent-driven dev (fresh agent per task) | `subagent-driven-development` |
| Collapse multi-step pipelines into one Python script (zero-context-cost) | `subagent-python-rpc` |
| Map codebase into feature flowcharts | `claude-mem:pathfinder` |
| Token-optimized AST code search (vs full file Read) | `claude-mem:smart-explore` |
| Parallel-agent investigations | `dispatching-parallel-agents` |
| Git worktree for isolation | `using-git-worktrees` |
| Finish a feature branch | `finishing-a-development-branch` |
| Documentation | `engineering:documentation`, `ruflo-docs:*` (auto-maintained) |
| Git diff risk scoring + reviewer suggestion | `ruflo-jujutsu:*` |
| ADR / architecture decision record | `engineering:architecture`, `ruflo-adr:*` |
| Domain-driven design scaffolding (contexts, aggregates, events) | `ruflo-ddd:*` |
| SPARC 5-phase methodology with quality gates | `ruflo-sparc:*` |
| Local LLM routing (Ollama, etc.) | `ruflo-ruvllm:*` |
| Sandboxed WebAssembly agents | `ruflo-wasm:*` |
| Background timer-scheduled tasks (12 auto-triggered workers) | `ruflo-loop-workers:*`, `loop`, `schedule` |
| Standup updates | `engineering:standup` |

### Engineering — debugging

| Intent | Skill |
|---|---|
| Generic structured debug | `engineering:debug` |
| Disciplined hard-bug loop (reproduce → minimise → hypothesise → instrument → fix) | `diagnose` |
| Trace deep error to root cause | `root-cause-tracing` |
| Validate at every layer (defense in depth) | `defense-in-depth` |
| Verify before claiming done | `verification-before-completion` |
| Sentry issue diagnosis (pull events / breadcrumbs / suspect commits via Composio) | `sentry-triage` |
| GitHub Actions PR check failures — pull logs, summarise, plan + fix | `gh-fix-ci` |

### Engineering — testing

| Intent | Skill |
|---|---|
| Write tests first | `test-driven-development` |
| Avoid mock-testing anti-patterns | `testing-anti-patterns` |
| Async race condition fix | `condition-based-waiting` |
| Browser testing with Playwright | `webapp-testing` |
| Live browser testing via Chrome DevTools MCP (DOM / console / network / perf) | `browser-testing-with-devtools` |
| Accessibility audit (WCAG) | `design:accessibility-review`, `accesslint-audit-and-fix` |
| Test strategy planning | `engineering:testing-strategy` |
| Auto-find missing tests + generate them | `ruflo-testgen:*` |
| Browser automation testing (Playwright agent) | `ruflo-browser:*`, `webapp-testing` |

### Engineering — incident & deploy

| Intent | Skill |
|---|---|
| Production incident workflow | `engineering:incident-response` |
| Pre-deploy verification | `engineering:deploy-checklist` |
| CI/CD pipeline setup (GitHub Actions, quality gates, branch protection) | `ci-cd-and-automation` |
| Husky pre-commit hooks + lint-staged + Prettier + typecheck | `setup-pre-commit` |
| Block dangerous git commands via PreToolUse hook (push, reset --hard, etc.) | `git-guardrails-claude-code` |
| Pre-launch checklist + feature-flag rollout + rollback plan | `shipping-and-launch` |
| Database schema migrations (safe rollouts) | `ruflo-migrations:*` |
| Structured logs / traces / metrics | `ruflo-observability:*` |
| CVE scans + vulnerability fixes | `ruflo-security-audit:*`, `/security-review` |

### Plugin / MCP development

| Intent | Skill |
|---|---|
| Build an MCP server | `build-mcp-server`, `mcp-builder`, `anthropic-skills:mcp-builder` |
| Build MCP UI app | `build-mcp-app` |
| Bundle MCP for distribution | `build-mcpb` |
| Create a Claude Code agent | `agent-development` |
| Create a slash command | `command-development` |
| Create a hook | `hook-development` |
| Configure MCP integration | `mcp-integration` |
| Plugin settings / structure | `plugin-settings`, `plugin-structure` |
| Skill development | `skill-development`, `anthropic-skills:skill-creator` |
| Build Claude API / Anthropic SDK apps (with prompt caching) | `claude-api` |
| Hookify rule | `writing-hookify-rules` |
| Scaffold + validate + publish your own plugin | `ruflo-plugin-creator:*` |

### GitHub / PR & issue workflows

| Intent | Skill |
|---|---|
| Address PR review/issue comments via gh CLI on the current branch | `gh-address-comments` |
| Fix failing GitHub Actions checks on the PR | `gh-fix-ci` |
| Break a plan/PRD/spec into vertical-slice issues (tracer bullets) | `to-issues` |
| Synthesize current context into a PRD and publish to issue tracker | `to-prd` |
| Triage issues through state machine (`needs-triage` → `ready-for-agent` etc.) | `triage` |
| Scaffold per-repo agent config (issue tracker, label vocab, CONTEXT.md/ADR layout) | `setup-matt-pocock-skills` |

### Plan stress-testing & idea refinement

| Intent | Skill |
|---|---|
| Refine a rough idea via structured divergent → convergent thinking | `idea-refine` |
| Stress-test a plan via relentless interview (one question at a time) | `grill-me` |
| Stress-test a plan against existing CONTEXT.md / ADRs and update docs inline | `grill-with-docs` |

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
| Typed JSON access to 90+ real websites (Google, Amazon, Reddit, GitHub, etc.) | `openweb` |
| Autonomous recursive research up to PhD depth, with source tiering and disk checkpoints | `recursive-research` |
| Scrape JS-heavy page | `firecrawl-scrape` |
| Crawl entire site/section | `firecrawl-crawl` |
| Map all URLs on a site | `firecrawl-map` |
| Browser automation in scrape | `firecrawl-interact`, `firecrawl-agent` |
| Search past Claude conversations | `remembering-conversations` |
| Library docs lookup (current versions) | `context7` (MCP), `firecrawl-build-onboarding` |
| Cross-source unified search (multi-MCP) | `enterprise-search:search`, `enterprise-search:search-strategy`, `enterprise-search:knowledge-synthesis`, `enterprise-search:source-management` |
| Design optimal RAG system for given data | `anthropic-skills:rag-architect` |
| Download entire site as local files (markdown / screenshots) | `firecrawl-download` |
| Integrate firecrawl scrape/search/interact into product code | `firecrawl-build-scrape`, `firecrawl-build-search`, `firecrawl-build-interact` |
| Data-driven analysis (CSV / DB) | `data:analyze`, `data:explore-data` |
| SQL writing across dialects | `data:sql-queries`, `data:write-query` |
| Data visualization (Python — matplotlib/seaborn/plotly) | `data:create-viz`, `data:data-visualization` |
| Build interactive HTML dashboard (charts/filters/tables) | `data:build-dashboard` |
| Statistical analysis (descriptive, trends, outliers) | `data:statistical-analysis` |
| QA an analysis before sharing | `data:validate-data` |
| Extract company-specific data context from analysts | `data:data-context-extractor` |
| Competitor research | `marketing:competitive-brief`, `product-management:competitive-brief`, `sales:competitive-intelligence` |
| Lead research | `lead-research-assistant`, `sales:account-research` |
| Customer research | `customer-support:customer-research`, `design:user-research` |
| Live store data (Shopify) | `mcp__shopify-mcp__*` (31 tools) |
| Passive domain reconnaissance (subdomains, SSL, WHOIS, DNS, no API keys) | `domain-intel` |
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
| Language-specific (Python / JS / Go) security best-practice review | `security-best-practices` |
| Generate dev handoff specs from a design | `design:design-handoff` |
| Audit / extend design system | `design:design-system`, `design-system` |
| UX copy review (microcopy, errors, CTAs) | `design:ux-copy` |
| Synthesize user research into themes | `design:research-synthesis` |
| PII detection / prompt-injection blocking / safety scanning | `ruflo-aidefence:*` |
| Offensive red-team / LLM jailbreak techniques (Parseltongue, GODMODE, ULTRAPLINIAN) | `godmode` |

### Communication & coordination

| Intent | Skill |
|---|---|
| Detect ambiguous intent | `adaptive-communication` |
| Stakeholder update | `product-management:stakeholder-update`, `operations:status-report` |
| Customer email response | `customer-support:draft-response` |
| Sales outreach | `sales:draft-outreach`, `apollo:prospect` |
| Ultra-terse output mode (drops filler / articles / hedging — ~75% fewer tokens) | `caveman` |
| Draft / rewrite / condense email (cold outreach, replies, escalations) | `email-draft-polish` |
| Customer-support ticket triage (Zendesk/Intercom/Help Scout) — categorise, draft reply | `support-ticket-triage` |
| Talk to Claude from your phone (Telegram bot bridge to Claude Code CLI) | `telegram-gateway` |
| Lead enrichment from name / company / LinkedIn / email | `apollo:enrich-lead` |
| Bulk-add leads to Apollo outreach sequence | `apollo:sequence-load` |
| Customer support ticket triage / KB article / escalation | `customer-support:ticket-triage`, `customer-support:kb-article`, `customer-support:customer-escalation` |
| Email sequence | `marketing:email-sequence` |
| Brainstorming session | `brainstorming`, `product-management:product-brainstorming` |
| Self-interview / clarify thinking | `inversion-exercise` (adjacent) |

### File / asset management

| Intent | Skill |
|---|---|
| Organize files / find dupes | `file-organizer` |
| Invoice & receipt organization | `invoice-organizer` |
| Image quality enhancement | `image-enhancer` |
| Transcribe voice memos / audio → text (Whisper API + faster-whisper + whisper.cpp fallback) | `voice-memo-transcription` |
| Generate changelog from git | `changelog-generator` |
| Analyse meeting transcripts for communication patterns / filler words / interruptions | `meeting-insights-analyzer` |
| Open / view / annotate / sign / fill-form a PDF (interactive) | `pdf-viewer:open`, `pdf-viewer:view-pdf`, `pdf-viewer:annotate`, `pdf-viewer:sign`, `pdf-viewer:fill-form` |
| PDF read / extract / manipulate (programmatic) | `anthropic-skills:pdf` |

### Documentation / project memory

| Intent | Skill |
|---|---|
| Initialize / improve CLAUDE.md | `init`, `claude-md-improver` |
| Recommend Claude Code automations | `claude-automation-recommender` |
| Session usage report | `session-report` |
| Memory consolidation | `anthropic-skills:consolidate-memory` |
| Two-tier memory system | `productivity:memory-management` |
| Shared TASKS.md task management | `productivity:task-management`, `productivity:start`, `productivity:update` |
| Read/write Obsidian notes (Gemma vault) | `mcp__obsidian__*` (CRUD via Local REST API plugin on port 27124) |
| Search past Claude sessions semantically | `claude-mem:mem-search`, `mcp__plugin_claude-mem_mcp-search__*` |
| Build AI-queryable knowledge base from observations | `claude-mem:knowledge-agent` |
| Project narrative / "Journey Into [Project]" report | `claude-mem:timeline-report` |
| Multi-day usage dashboard (hours, projects, skills, tokens, $) | `cross-session-insights` |
| Save / restore agent memory across sessions (ruflo) | `ruflo-rvf:*` |
| Fast vector DB for agent memory (HNSW-indexed) | `ruflo-agentdb:*` |
| Hybrid search + graph hops + diversity ranking | `ruflo-rag-memory:*` |
| Entity relationship maps / knowledge graphs | `ruflo-knowledge-graph:*` |
| GPU-accelerated Graph RAG (103 tools, ruvector) | `ruflo-ruvector:*` |

### Operations workflow

| Intent | Skill |
|---|---|
| Operational runbook | `operations:runbook` |
| Process documentation | `operations:process-doc` |
| Risk assessment | `operations:risk-assessment` |
| Vendor evaluation | `operations:vendor-review`, `legal:vendor-check` |

### Claude Code harness configuration

| Intent | Skill |
|---|---|
| Configure settings.json / hooks / permissions / env vars | `update-config` |
| Compress LLM context via 49 MCP tools, AST-aware reads, 90+ shell patterns (auto-installs) | `lean-ctx` |
| Customize keyboard shortcuts / chord bindings | `keybindings-help` |
| Reduce permission prompts (auto-allowlist common Bash/MCP) | `fewer-permission-prompts` |
| Run prompt on recurring interval | `loop` |
| Cron-scheduled remote agents | `schedule`, `anthropic-skills:schedule` |
| Cowork setup wizard | `anthropic-skills:setup-cowork` |

### Specialized / niche

| Intent | Skill |
|---|---|
| Apply Anthropic's official brand colors + typography | `anthropic-skills:brand-guidelines` |
| Review n8n workflows for errors / inefficiencies | `anthropic-skills:n8n-workflow-reviewer` |
| Full-stack client acquisition + delivery (improvised-intelligence) | `anthropic-skills:improvised-intelligence` |
| Excel / Google Sheets formulas, pivots, array formulas, dialect translation | `spreadsheet-formula-helper` |
| Competition math (IMO/Putnam/USAMO/AIME) | `math-olympiad` |
| IoT device management (trust scoring, anomaly detection, fleets) | `ruflo-iot-cognitum:*` |
| Algo trading agents (4 agents, backtesting, 112+ tools) | `ruflo-neural-trader:*` |
| Market data ingestion / OHLCV vectorization / pattern detection | `ruflo-market-data:*` |
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
| Cross-machine agent collaboration (zero-trust mTLS) | `ruflo-federation:*` |
| Dynamic agent behavior / cognitive patterns | `ruflo-daa:*` |

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

### Multi-model orchestration (token-saving routing)

| Intent | Skill |
|---|---|
| Auto-route between Claude / Codex / Gemini based on phrase + context (driver / reviewer / senses pattern) | `three-brain` |
| Manually invoke Codex for review or rescue | `codex:review`, `codex:adversarial-review`, `codex:rescue` |
| Manually invoke Gemini for long-context exploration or multimodal | `cc-gemini-plugin:gemini`, `gemini:rescue` |
| Delegate bulk translation to Gemini (free under AI Pro, saves Claude tokens) | call `gemini -p` directly from Bash |

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
