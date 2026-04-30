# claude-skills

A personal collection of Claude Code skills — local snapshot of `~/.claude/skills/` plus on-disk marketplace plugin skills, kept in sync with the live install.

## Structure

```
claude-skills/
├── loose-skills/       119 top-level skills installed in ~/.claude/skills/
├── plugin-skills/      52 skills extracted from installed marketplace plugins
├── Apple design language/   work-in-progress design assets
├── Zaka´s ai/               work-in-progress AI/skill experiments
└── scroll-stop-builder-skill/   in-development scroll-stopping content skill
```

The `loose-skills/` folder is the source of truth for everything that loads automatically into a Claude Code session as a top-level skill (no namespace prefix). The `plugin-skills/` folder is a flattened snapshot of skills bundled in installed Claude Code plugins — the naming convention is `<plugin>--<skill>` to disambiguate (e.g. `discord--access` and `imessage--access` would otherwise collide).

## Categories — `loose-skills/`

**Problem-solving & thinking (8)** — `when-stuck`, `inversion-exercise`, `scale-game`, `collision-zone-thinking`, `meta-pattern-recognition`, `simplification-cascades`, `preserving-productive-tensions`, `tracing-knowledge-lineages`

**Engineering workflow (12)** — `brainstorming`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `dispatching-parallel-agents`, `requesting-code-review`, `receiving-code-review`, `finishing-a-development-branch`, `using-git-worktrees`, `verification-before-completion`, `vanity-engineering-review`, `human-architect-mindset`

**Debugging & testing (7)** — `defense-in-depth`, `root-cause-tracing`, `test-driven-development`, `testing-anti-patterns`, `condition-based-waiting`, `webapp-testing`, `accesslint-audit-and-fix`

**Design & UI (10)** — `frontend-design`, `bencium-innovative-ux-designer`, `design`, `design-audit`, `design-system`, `ui-styling`, `ui-ux-pro-max`, `web-design-guidelines`, `typography`, `relationship-design`

**Marketing & growth (30)** — `seo-aeo-playbook`, `bencium-aeo`, `schema-markup`, `programmatic-seo`, `site-architecture`, `directory-submissions`, `analytics-tracking`, `paid-ads`, `ad-creative`, `competitive-ads-extractor`, `competitor-alternatives`, `content-strategy`, `content-research-writer`, `copy-editing`, `marketing-ideas`, `marketing-psychology`, `community-marketing`, `social-content`, `video`, `lead-magnets`, `lead-research-assistant`, `referral-program`, `pricing-strategy`, `product-marketing-context`, `free-tool-strategy`, `popup-cro`, `page-cro`, `form-cro`, `ab-test-setup`, `organic-first-campaign`

**Creative content (5)** — `algorithmic-art`, `canvas-design`, `banner-design`, `slides`, `scroll-stop-prompter`

**Assets & utilities (6)** — `web-asset-generator`, `image-enhancer`, `3d-asset-generator`, `file-organizer`, `invoice-organizer`, `changelog-generator`

**Communication (1)** — `adaptive-communication`

**Architecture decision-making (2)** — `negentropy-lens`, `renaissance-architecture`

**Memory & context (1)** — `remembering-conversations`

**Web scraping & research (12)** — `firecrawl`, `firecrawl-agent`, `firecrawl-search`, `firecrawl-scrape`, `firecrawl-crawl`, `firecrawl-map`, `firecrawl-download`, `firecrawl-interact`, `firecrawl-build-onboarding`, `firecrawl-build-scrape`, `firecrawl-build-search`, `firecrawl-build-interact`

**Plugin & MCP development (10)** — `agent-development`, `command-development`, `hook-development`, `mcp-integration`, `plugin-settings`, `plugin-structure`, `skill-development`, `build-mcp-server`, `build-mcp-app`, `build-mcpb`

**Setup & maintenance (4)** — `claude-automation-recommender`, `claude-md-improver`, `session-report`, `playground`

**Channel routing (6)** — `discord-access`, `discord-configure`, `imessage-access`, `imessage-configure`, `telegram-access`, `telegram-configure`

**Meta-skill (1)** — `skill-router` (auto-routes prompts to the right cluster of skills; full catalog at `loose-skills/skill-router/references/catalog.md`)

**Other (4)** — `example-command`, `example-skill`, `math-olympiad`, `writing-hookify-rules`

## Categories — `plugin-skills/` (marketplace plugins)

**Plugin development** — `plugin-dev--agent-development`, `plugin-dev--command-development`, `plugin-dev--hook-development`, `plugin-dev--mcp-integration`, `plugin-dev--plugin-settings`, `plugin-dev--plugin-structure`, `plugin-dev--skill-development`

**MCP server development** — `mcp-server-dev--build-mcp-server`, `mcp-server-dev--build-mcp-app`, `mcp-server-dev--build-mcpb`

**Channel routing** — `discord--access`, `discord--configure`, `imessage--access`, `imessage--configure`, `telegram--access`, `telegram--configure`

**Setup & maintenance** — `claude-code-setup--claude-automation-recommender`, `claude-md-management--claude-md-improver`, `session-report--session-report`, `playground--playground`, `frontend-design--frontend-design`, `skill-creator--skill-creator`

**Other** — `hookify--writing-rules`, `math-olympiad--math-olympiad`, `example-plugin--example-command`, `example-plugin--example-skill`

## Notable skills

- **`seo-aeo-playbook/`** — Custom-built SEO/AEO growth-operator playbook with a 7-step order of operations, weekly data-driven loop, and the polcititch correction baked in. Bundled `STRATEGY.md` documents the 4-cadence usage (setup, weekly, monthly, quarterly).
- **`skill-router/`** — Custom-built meta-skill. Auto-scans the full installed-skills catalog at the start of every non-simple prompt, picks 1–3 most relevant, invokes them. Bundled `references/catalog.md` is an alphabetized index of all 118 loose skills with one-line summaries. Acts as the orchestrator that fires other skills.
- **`accesslint-audit-and-fix/`** — Accessibility audit→edit→verify loop. Static fallback works without an MCP server; live-DOM mode requires the AccessLint MCP.
- **`ui-ux-pro-max/`** — UI/UX reference DB with 50+ styles, 161 color palettes, 57 font pairings, 99 UX guidelines, 25 chart types across 10 stacks.

## Origin

Each skill comes from one of these sources, kept distinct so attribution stays clean:

- Anthropic (`anthropic-skills:*` marketplace + `anthropics/skills` repo) — frontend-design, canvas-design, algorithmic-art, webapp-testing, etc.
- Anthropic Cowork plugins — engineering, marketing, design, sales, finance, legal, operations, HR, product-management, customer-support, data, brand-voice, apollo, enterprise-search, pdf-viewer, productivity (these load via plugin namespaces, not stored as files in this repo)
- obra/superpowers-skills — when-stuck, inversion-exercise, scale-game, etc. (excludes redundant ones already covered by Cowork plugins)
- nextlevelbuilder/ui-ux-pro-max-skill — ui-ux-pro-max, design, design-system, slides, banner-design, ui-styling
- bencium/bencium-marketplace — bencium-aeo, bencium-innovative-ux-designer, organic-first-campaign, design-audit, vanity-engineering-review, etc.
- accesslint/claude-marketplace — accesslint-audit-and-fix
- vercel-labs/agent-skills — web-design-guidelines
- ComposioHQ/awesome-claude-skills — competitive-ads-extractor, content-research-writer, image-enhancer, etc.
- coreyhaines31/marketingskills — paid-ads, schema-markup, programmatic-seo, page-cro, etc.
- Custom-built — seo-aeo-playbook

## Maintenance

This repo is a snapshot. The live skills run from `~/.claude/skills/`. To refresh the snapshot after installing or updating skills:

```bash
cd "C:/Users/toner/OneDrive/Desktop/claude skills"
rsync -a --delete "$HOME/.claude/skills/" loose-skills/
git add . && git commit -m "Sync skills snapshot $(date +%Y-%m-%d)"
git push
```

A future improvement would be a sync script + cron / scheduled task that automates this.

## License

This repository contains skills authored by multiple parties. Each skill folder retains its original `LICENSE.txt` where present (Anthropic Apache 2.0, MIT, Elastic-2.0, etc.). The aggregation and the few custom-built skills (e.g. `seo-aeo-playbook/`) are under MIT unless noted otherwise.
