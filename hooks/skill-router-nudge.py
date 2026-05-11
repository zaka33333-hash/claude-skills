#!/usr/bin/env python3
"""
Skill-router nudge hook — fires on EVERY UserPromptSubmit to remind Claude to:
  1. Consult the skill-router skill to match the request to the right skill(s)
  2. Pick the cheapest model that still delivers 10/10 quality

Wire as a UserPromptSubmit hook in settings.json:

  "hooks": {
    "UserPromptSubmit": [{
      "matcher": ".*",
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/skill-router-nudge.py"
      }]
    }]
  }

Disable temporarily by setting SKILL_ROUTER_NUDGE_OFF=1 in env.
"""

import json
import os
import sys


def main() -> int:
    # Allow ad-hoc disable without removing the hook
    if os.environ.get("SKILL_ROUTER_NUDGE_OFF") == "1":
        return 0

    # Read (and ignore body of) hook payload to keep stdin drained
    try:
        json.loads(sys.stdin.read() or "{}")
    except Exception:
        pass

    nudge = (
        "<system-reminder>"
        "Activate skill-router for THIS prompt — no matter how trivial. "
        "Two-step process: "
        "(1) **Skill match.** Scan ~/.claude/skills/skill-router/SKILL.md and references/catalog.md; "
        "pick the 1-3 most relevant skills (or none, if the prompt is a one-word confirm / casual reply). "
        "(2) **Model match.** Pick the CHEAPEST model that still hits 10/10 quality on the chosen task. "
        "Priority order — quality is non-negotiable, tokens are secondary: "
        "  • Trivial Q / one-liner / lookup / format / typo fix → Haiku 4.5 OR `gemini -p` with gemini-2.5-flash (free under AI Pro). "
        "  • Medium reasoning / single-file edit / structured task → Sonnet 4.6 OR `gemini -p` with gemini-2.5-pro (free under AI Pro). "
        "  • Complex multi-file refactor / architecture / hard reasoning / production-critical → Opus 4.7 (current default) OR `/codex:adversarial-review` for second-opinion. "
        "  • Translation / multimodal / >500k-token context → delegate to Gemini via `gemini -p` (FREE on AI Pro — always prefer when quota allows). "
        "  • Background long jobs → `/codex:rescue` or `/gemini:rescue`. "
        "Default to Gemini whenever the task fits and AI Pro quota is healthy (we save Claude tokens for hard work). "
        "If you're already on the right model and skill, just proceed silently — no need to announce the routing. "
        "Disable this nudge for one session with `export SKILL_ROUTER_NUDGE_OFF=1`."
        "</system-reminder>"
    )

    print(json.dumps({"decision": "approve", "additionalContext": nudge}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
