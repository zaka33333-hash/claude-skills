---
name: subagent-python-rpc
description: Pattern for collapsing multi-step tool pipelines into a single Python script that calls multiple tools/MCPs without round-tripping through the main agent's context. Inspired by Hermes Agent's "subagent + Python RPC" feature. Use when a task requires 3+ sequential tool calls that don't need the main agent to reason between steps (e.g. fetch URL → parse JSON → POST to webhook → log to file). Triggers on "automate this pipeline", "batch this", "save context tokens", "write a Python script that calls these tools", "subagent for X". Reduces cost + latency vs round-tripping each tool call through the model.
---

# Subagent + Python RPC pattern

## Why this exists

Every tool call in Claude Code costs:
- A round-trip to the model (latency)
- Tokens to encode the result back into context
- Reasoning capacity if the result is large

For pipelines where the model doesn't need to *think* between steps — just chain `fetch → transform → post → log` — paying that cost N times is wasteful. This skill encodes the pattern: write a single Python script that does the whole pipeline, run it once, return only the final result.

## When to use

✓ **Good fit:**
- Pipelines with 3+ sequential tool calls
- Each step's output feeds directly into the next, no model reasoning required
- Result is small (a status, a URL, a count) even if intermediate data is large
- Repeated the same way across many invocations (e.g. weekly reports)

✗ **Bad fit:**
- Steps that require the model to interpret intermediate results
- Branching logic that depends on what the model "decides" mid-pipeline
- One-off exploratory work

## Pattern

```python
#!/usr/bin/env python3
"""<pipeline-name>.py — N-step pipeline that runs as a single subprocess."""
import json
import subprocess
import sys
import urllib.request

def step1_fetch(url: str) -> dict:
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())

def step2_transform(data: dict) -> dict:
    # pure-python transform, no model needed
    return {"summary": len(data.get("items", []))}

def step3_post(transformed: dict, webhook: str) -> int:
    req = urllib.request.Request(
        webhook,
        data=json.dumps(transformed).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        return r.getcode()

def step4_log(status: int) -> None:
    Path("/tmp/pipeline.log").write_text(f"{datetime.now()} status={status}\n")

if __name__ == "__main__":
    data = step1_fetch(sys.argv[1])
    transformed = step2_transform(data)
    status = step3_post(transformed, sys.argv[2])
    step4_log(status)
    print(json.dumps({"status": status, "items": transformed["summary"]}))
```

The model's view: just `Bash(python pipeline.py <url> <webhook>)` → one call → small JSON result.

## When you need to call MCPs from Python

If your pipeline needs MCP tools (e.g. obsidian, gmail, claude-mem search), use the **MCP HTTP transport** if the server exposes one, or shell out to `claude -p` headlessly:

```python
result = subprocess.run(
    ["claude", "-p", f"Use mcp__obsidian__obsidian_simple_search with query: {q}",
     "--allowed-tools", "mcp__obsidian__obsidian_simple_search",
     "--output-format", "json"],
    capture_output=True, text=True,
)
data = json.loads(result.stdout)
```

This is a small subagent invocation — costs one round trip but gives you full MCP access from inside a script. Useful for "for each row in CSV, search Obsidian and write back" loops.

## Real-world examples (Star Toner)

1. **Weekly SEO digest pipeline** — fetch GSC top queries → diff vs last week → post to Slack via webhook → save to memory. 4 steps, runs in 5s, costs ~zero context.

2. **Customer email triage** — fetch unread Gmail → for each, check if customer in Shopify → tag urgency → draft reply via Claude subagent → leave in drafts. ~8 steps, current implementation rounds 8 times through the main agent — perfect candidate.

3. **Daily stand-up generator** — read last 24h of session JSONLs → extract decisions/blockers → write to Obsidian daily note. 3 steps, run as cron via `schedule` skill.

## Anti-pattern: don't reach for this for one-offs

Writing a 100-line Python script for a task you'll run once is *more* expensive than just round-tripping the tools through the model. Save this pattern for repeating workflows where the round-trip cost compounds.

## Comparison to existing skills/tools

| Tool | Use when |
|---|---|
| `Agent` tool (subagent) | One-off complex task, model reasoning needed throughout |
| `dispatching-parallel-agents` | Multiple independent investigations |
| `subagent-driven-development` | Long implementation plan with checkpoints |
| **`subagent-python-rpc`** | **Repeating pipeline, no mid-flow reasoning** |
| `loop` skill | Recurring on a clock, not just collapsing context |
| `schedule` skill | Cron-style scheduled remote agent |
| `ruflo-workflows:workflow-create` | Higher-level workflow templates |

## When to graduate to a real workflow engine

If you find yourself writing 5+ of these scripts, consider:
- `ruflo-workflows` — declarative workflow templates with parameterization
- `n8n` (workflow automation) — visual builder, runs as standalone service
- The `anthropic-skills:n8n-workflow-reviewer` skill helps audit those

Use this skill for the prototype phase. Graduate when the pattern stabilizes.
