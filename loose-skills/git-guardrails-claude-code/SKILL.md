---
name: git-guardrails-claude-code
description: Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.
---

# Setup Git Guardrails

Sets up a PreToolUse hook that intercepts and blocks dangerous git commands before Claude executes them.

## What Gets Blocked

- `git push` (all variants including `--force`)
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

When blocked, Claude sees a message telling it that it does not have authority to access these commands.

## Steps

### 1. Ask scope

Ask the user: install for **this project only** (`.claude/settings.json`) or **all projects** (`~/.claude/settings.json`)?

### 2. Create the hook script

Create the hook script at the target location based on scope:

- **Project**: `.claude/hooks/block-dangerous-git.sh`
- **Global**: `~/.claude/hooks/block-dangerous-git.sh`

The script content:

```bash
#!/bin/bash
# Block dangerous git commands
set -e

TOOL_INPUT="$(cat)"
COMMAND=$(echo "$TOOL_INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('command',''))" 2>/dev/null || echo "")

block() {
  echo "BLOCKED: $1" >&2
  exit 2
}

if echo "$COMMAND" | grep -qE '^git push( |$)'; then block "git push"; fi
if echo "$COMMAND" | grep -qE '^git reset --hard'; then block "git reset --hard"; fi
if echo "$COMMAND" | grep -qE '^git clean -f'; then block "git clean -f"; fi
if echo "$COMMAND" | grep -qE '^git branch -D'; then block "git branch -D"; fi
if echo "$COMMAND" | grep -qE '^git checkout \.'; then block "git checkout ."; fi
if echo "$COMMAND" | grep -qE '^git restore \.'; then block "git restore ."; fi
```

Make it executable with `chmod +x`.

### 3. Add hook to settings

Add to the appropriate settings file:

**Project** (`.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

**Global** (`~/.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

If the settings file already exists, merge the hook into existing `hooks.PreToolUse` array.

### 4. Ask about customization

Ask if user wants to add or remove any patterns from the blocked list. Edit the script accordingly.

### 5. Verify

Run a quick test to confirm the hook works correctly before considering the setup done.
