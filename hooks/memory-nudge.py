#!/usr/bin/env python3
"""
Memory-nudge hook — fires every N user prompts to remind Claude to scan recent
activity for new patterns/decisions/learnings worth persisting to the memory folder.

Wire as a UserPromptSubmit hook in settings.json:

  "hooks": {
    "UserPromptSubmit": [{
      "matcher": ".*",
      "hooks": [{
        "type": "command",
        "command": "python C:/Users/toner/.claude/hooks/memory-nudge.py"
      }]
    }]
  }

Counter persists at ~/.claude/state/memory-nudge-counter.json
Configurable interval via env: MEMORY_NUDGE_INTERVAL (default 20)
"""

import json
import os
import sys
from pathlib import Path

INTERVAL = int(os.environ.get("MEMORY_NUDGE_INTERVAL", "20"))
STATE = Path.home() / ".claude" / "state" / "memory-nudge-counter.json"


def load_state() -> dict:
    if not STATE.exists():
        return {"count": 0, "by_session": {}}
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        return {"count": 0, "by_session": {}}


def save_state(s: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(s, indent=2), encoding="utf-8")


def main() -> int:
    # Read hook payload from stdin (Claude Code JSON)
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except Exception:
        payload = {}

    session_id = payload.get("session_id") or payload.get("sessionId") or "unknown"
    state = load_state()
    state["count"] = state.get("count", 0) + 1
    state["by_session"][session_id] = state["by_session"].get(session_id, 0) + 1
    save_state(state)

    n = state["by_session"][session_id]
    if n > 0 and n % INTERVAL == 0:
        # Emit a system-reminder that Claude will see prepended to the prompt
        nudge = (
            f"<system-reminder>"
            f"Memory nudge — you're {n} turns into this session. "
            f"Before continuing, do a 30-second scan: are there 1-3 specific "
            f"new patterns, decisions, learnings, or workflow insights from "
            f"the last ~20 turns worth persisting to "
            f"~/.claude/projects/<project>/memory/ as feedback_*.md / pattern_*.md / "
            f"project_*.md / workflow_*.md? If yes, briefly tell the user what "
            f"you'd add and ask if they want them saved. If nothing new, skip silently."
            f"</system-reminder>"
        )
        # UserPromptSubmit hook: stdout JSON with additionalContext field gets injected
        out = {
            "decision": "approve",
            "additionalContext": nudge,
        }
        print(json.dumps(out))
        return 0

    # Pass-through; no nudge
    return 0


if __name__ == "__main__":
    sys.exit(main())
