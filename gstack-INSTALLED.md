# gstack (Garry Tan's engineering-team-in-a-box)

**Status:** Installed at `~/.claude/skills/gstack/` (49 MB clone + ~253 MB Playwright runtime).
**Not mirrored to this repo** — too large; re-install from source on a new Mac.

## Install command (re-runnable)

```bash
# Prereqs
curl -fsSL https://bun.sh/install | bash          # Bun 1.3.10+ required
export PATH="$HOME/.bun/bin:$PATH"

# Install
git clone --single-branch --depth 1 \
  https://github.com/garrytan/gstack.git \
  ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup --prefix
```

The `--prefix` flag namespaces all 46 commands under `/gstack-*` to avoid
collision with existing skills.

## Highest-value commands (no overlap with existing tools)

| Command | What it does |
|---|---|
| `/gstack-autoplan` | CEO + design + engineering reviews in one pass before coding |
| `/gstack-design-consultation` | Builds a full design system from scratch (competitor research + creative direction) |
| `/gstack-design-shotgun` | Multiple visual mockup variants, iterate on feedback |
| `/gstack-design-html` | Finalize approved design to production HTML/CSS via Pretext |
| `/gstack-qa` | Full QA loop — finds bugs → atomic commits → regression tests → re-verifies |
| `/gstack-pair-agent` | Coordinate multiple AI agents in a shared browser session |
| `/gstack-canary` + `/gstack-benchmark` | Post-deploy monitoring + perf baselining |
| `/gstack-document-release` | Auto-update READMEs/ARCHITECTURE docs from your diff |
| `/gstack-retro` | Cross-tool weekly retrospective (Claude + Codex + Gemini) |
| `/gstack-setup-gbrain` + `/gstack-learn` | Cross-session persistent memory for your codebase |
| `/gstack-upgrade` | Stay on the latest gstack |
| `/gstack-health` | Health check the install |

## Duplicates (already covered by other tools — skip)

- `/gstack-review`, `/gstack-codex` (you have `/codex:review`, `/code-review`)
- `/gstack-ship`, `/gstack-land-and-deploy` (you have `shipping-and-launch`)
- `/gstack-browse` (you have `ruflo-browser`, `firecrawl-interact`, browser MCP)
- `/gstack-careful`, `/gstack-freeze`, `/gstack-guard` (you have `git-guardrails-claude-code`)
- `/gstack-cso` (you have `/security-review`, `ruflo-security-audit`)
- `/gstack-investigate` (you have `/codex:rescue`, `/gemini:rescue`, `diagnose`)
- `/gstack-office-hours`, `/gstack-plan-ceo-review`, `/gstack-plan-eng-review` (you have `brainstorming`, `to-prd`, `ruflo-sparc`)

## Repo

- https://github.com/garrytan/gstack — 95k+ stars, MIT, actively maintained by Garry Tan (YC)
