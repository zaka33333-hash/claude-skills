---
name: telegram-gateway
description: Bridge Telegram messages to Claude Code so the user can chat with their agent from their phone. The bot receives a Telegram message, runs `claude -p "<message>"` headlessly with allowed-tools, and replies with the response. Triggers when the user asks "set up the telegram bot", "how do I message Claude from my phone", "build a telegram gateway", "send claude commands from telegram", "remote claude". Includes setup steps for BotFather, the Python bridge daemon, allowlist of authorized chat IDs, and systemd/Task Scheduler instructions for keeping it running.
---

# Telegram Gateway → Claude Code

Talk to your Claude Code from Telegram. Send a message → it runs through Claude headlessly → reply comes back. Inspired by Hermes Agent's messaging gateway.

## Architecture

```
You (Telegram app) ──┐
                     ↓
  Telegram Bot API ──→  bot.py daemon (long-poll)
                              ↓
                        subprocess: claude -p "<msg>" --output-format stream-json
                              ↓
                        Stream output back as Telegram messages
```

The bot daemon runs locally on your Windows machine (or a VPS / Raspberry Pi). Each incoming message spawns a `claude` CLI invocation with allowed tools and outputs streamed back.

## Setup steps

### 1. Create the bot via BotFather

1. Open Telegram, message `@BotFather`
2. `/newbot` → choose a name (e.g. "Toner Claude") and username (e.g. "toner_claude_bot")
3. BotFather replies with a **bot token** like `1234567890:ABCdefGHI...`
4. Save it.

### 2. Get your authorized chat ID

1. In Telegram, message your new bot anything
2. Visit `https://api.telegram.org/bot<TOKEN>/getUpdates` in browser
3. Find `"chat":{"id":123456789,...}` — that's your numeric chat ID
4. Save it. Only this chat ID will be allowed to talk to the bot.

### 3. Install Python deps

```bash
pip install python-telegram-bot
```

### 4. Set env vars

Create `~/.claude/state/telegram-gateway.env`:
```
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHI...
TELEGRAM_ALLOWED_CHAT_IDS=123456789,987654321
CLAUDE_BIN=C:/Users/toner/AppData/Roaming/npm/claude.cmd
CLAUDE_WORKDIR=C:/Users/toner/OneDrive/Desktop/Gemma
CLAUDE_ALLOWED_TOOLS=Read,Write,Edit,Bash,Glob,Grep,WebFetch,WebSearch,TodoWrite
```

### 5. Run the daemon

```bash
python C:/Users/toner/.claude/skills/telegram-gateway/scripts/bot.py
```

Now message your bot. First message kicks off a Claude session. Subsequent messages continue (with `--continue` flag).

### 6. Run on startup (Windows Task Scheduler)

Create scheduled task: trigger "At log on of <user>", action `python ...bot.py`. Or use NSSM to install it as a Windows service.

## Security model

- **Allowlist only.** Only chat IDs in `TELEGRAM_ALLOWED_CHAT_IDS` can send commands. Anyone else gets ignored.
- **No tool override.** The bot runs Claude with a hardcoded `--allowed-tools` list. Telegram messages cannot escalate.
- **Workdir locked.** `CLAUDE_WORKDIR` is fixed; commands can't `cd ../..`.
- **No file uploads accepted by default.** Audio/voice memos can be opt-in but require explicit handler (commented in bot.py).

## Common workflows once it's live

- *"What's the latest claude-mem observation?"* → bot runs claude → returns last memory entry
- *"Search my Obsidian for SEO crisis"* → uses obsidian MCP → returns matches
- *"Run a Star Toner SEO audit"* → fires the seo-aeo-playbook skill
- Voice: forward a WhatsApp/iPhone voice memo → bot transcribes via voice-memo-transcription skill → uses transcript as next prompt
- Photos: send a screenshot of an error → bot sends the image to claude → debug help

## Failure modes

| Symptom | Fix |
|---|---|
| Bot doesn't reply | Check `TELEGRAM_BOT_TOKEN` correct, bot is started, daemon running |
| "User not authorized" | Add chat ID to `TELEGRAM_ALLOWED_CHAT_IDS` |
| `claude: command not found` | Set `CLAUDE_BIN` to full path of claude.cmd / claude binary |
| Reply gets cut off | Telegram has 4096-char limit per message; bot splits long replies automatically |
| Daemon crashes | Wrap in `while true; python bot.py; sleep 5; done` or use systemd / NSSM |

## Cost

- Telegram Bot API: free
- Claude Code: same as desktop usage (your existing subscription / API key)
- VPS hosting (optional): $5/mo on Hetzner if you want it always-on without your laptop running

## Bridge to other platforms

Same pattern works for:
- **WhatsApp** — use [whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) or Twilio
- **Discord** — discord.py with same allowlist pattern
- **Slack** — Slack Bolt SDK
- **Signal** — signal-cli wrapper
- **iMessage** — sendmessage / Mac-only, requires macOS daemon

## Cross-reference

This skill complements the existing Claude Code plugins:
- `telegram-configure` — configures the cowork-style platform routing (different scope)
- `discord-configure`, `imessage-configure` — same family for other platforms
- `voice-memo-transcription` — pairs with this for voice → text → prompt pipeline
