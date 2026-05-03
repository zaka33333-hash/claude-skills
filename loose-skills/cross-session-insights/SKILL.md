---
name: cross-session-insights
description: Generate a multi-day insights dashboard from Claude Code session history — hours spent per project, top skills/tools used, token usage, top pattern observations, daily activity heatmap. Triggers when the user asks "what did I work on this week", "show my usage", "weekly recap", "insights for last N days", "where did my time go", "session report" (multi-day version), or "audit my recent work". Output: HTML dashboard + concise summary.
---

# Cross-Session Insights Dashboard

Aggregates session JSONLs + claude-mem observations across N days into one dashboard. Fills the gap between `session-report` (single session) and `claude-mem:timeline-report` (whole-project narrative).

## When to use

- "What did I work on this week / month?"
- "How many hours have I been on Star Toner this month?"
- "What skills/tools am I actually using?"
- "Generate a weekly recap"
- "Where did my Claude time go for the last 7 days?"
- Time accounting / billing prep / quarterly reviews

## Procedure

1. **Run the script** with optional day window (default 7):
   ```bash
   python C:/Users/toner/.claude/skills/cross-session-insights/scripts/insights.py --days 7
   ```
   Other windows: `--days 1` (today), `--days 30` (this month), `--days 90` (quarter).

2. **Output:** HTML dashboard at `~/.claude/state/insights-{YYYY-MM-DD}.html` + a Markdown summary in stdout.

3. **Open the HTML** in browser:
   ```bash
   start C:/Users/toner/.claude/state/insights-2026-05-03.html  # Windows
   ```

4. **Push to Obsidian** (optional): if Obsidian + obsidian-mcp is connected, append the Markdown summary to a Daily Note via `mcp__obsidian__obsidian_append_content`.

## What it shows

| Section | Content |
|---|---|
| **Activity heatmap** | Per-day hours across the window |
| **Top projects** | Hours, % of total, last touched |
| **Top skills/tools** | Which skills + tools fired most. Reveals what you actually use. |
| **Tokens & cost** | Total tokens (in/out/cache), $ estimate |
| **Patterns surfaced** | Latest claude-mem observations (last N days) — captures decisions, fixes, learnings |
| **Idle days** | Days with no activity (vacation tracker) |

## Data sources

1. **Session JSONLs** at `~/.claude/projects/<project>/<session-id>.jsonl`
   - Timestamps, model, tokens, tool calls, message counts
2. **claude-mem observations** at `~/.claude-mem/claude-mem.db`
   - Patterns, decisions, learnings tagged by date/project/type
3. **Skill catalog** at `~/.claude/skills/skill-router/references/catalog.md`
   - Maps skill names to clusters

## Privacy note

Output is local-only HTML. No data leaves the machine. Safe to pin to your phone via OneDrive sync if you want a portable view.

## Cost note

Free — script aggregates existing local data, makes no API calls. Renders in <2 seconds for a year of sessions.
