#!/usr/bin/env python3
"""
Telegram -> Claude Code bridge daemon.

Run: python bot.py
Env (or ~/.claude/state/telegram-gateway.env):
  TELEGRAM_BOT_TOKEN
  TELEGRAM_ALLOWED_CHAT_IDS  (comma-separated)
  CLAUDE_BIN                 (default: claude)
  CLAUDE_WORKDIR             (default: cwd)
  CLAUDE_ALLOWED_TOOLS       (comma-separated, default: Read,Write,Edit,Bash,Glob,Grep,WebFetch)

Requires: pip install python-telegram-bot
"""

import asyncio
import logging
import os
from pathlib import Path

# Auto-load env file if present
ENV_FILE = Path.home() / ".claude" / "state" / "telegram-gateway.env"
if ENV_FILE.exists():
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())

try:
    from telegram import Update
    from telegram.ext import (
        Application,
        CommandHandler,
        ContextTypes,
        MessageHandler,
        filters,
    )
except ImportError:
    raise SystemExit("Missing dep. Install: pip install python-telegram-bot")

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ALLOWED = {
    int(x) for x in os.environ.get("TELEGRAM_ALLOWED_CHAT_IDS", "").split(",") if x.strip()
}
CLAUDE_BIN = os.environ.get("CLAUDE_BIN", "claude")
WORKDIR = os.environ.get("CLAUDE_WORKDIR", str(Path.cwd()))
ALLOWED_TOOLS = os.environ.get(
    "CLAUDE_ALLOWED_TOOLS",
    "Read,Write,Edit,Bash,Glob,Grep,WebFetch,WebSearch,TodoWrite",
).replace(",", " ")

if not TOKEN:
    raise SystemExit("TELEGRAM_BOT_TOKEN not set")
if not ALLOWED:
    raise SystemExit("TELEGRAM_ALLOWED_CHAT_IDS not set (comma-separated chat IDs)")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger("tg-claude")

# Per-chat session continuity
sessions: dict[int, bool] = {}


def split_for_telegram(text: str, limit: int = 4000) -> list[str]:
    """Telegram hard limit is 4096; we use 4000 for safety."""
    chunks = []
    while text:
        if len(text) <= limit:
            chunks.append(text)
            break
        cut = text.rfind("\n", 0, limit)
        if cut < limit // 2:
            cut = limit
        chunks.append(text[:cut])
        text = text[cut:]
    return chunks


async def run_claude(prompt: str, chat_id: int) -> str:
    """Spawn the Claude CLI as a sub-process and return its stdout."""
    args = [CLAUDE_BIN, "-p", prompt, "--allowed-tools", *ALLOWED_TOOLS.split()]
    if sessions.get(chat_id):
        args.insert(1, "--continue")
    try:
        proc = await asyncio.create_subprocess_exec(
            *args,
            cwd=WORKDIR,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout_b, stderr_b = await asyncio.wait_for(proc.communicate(), timeout=600)
        out = (stdout_b or b"").decode("utf-8", errors="replace").strip()
        err = (stderr_b or b"").decode("utf-8", errors="replace").strip()
        sessions[chat_id] = True
        if proc.returncode != 0 and not out:
            return f"[claude exited {proc.returncode}]\n{err[:1000]}"
        return out or err or "(empty response)"
    except asyncio.TimeoutError:
        return "[claude timed out >10min]"
    except Exception as e:
        return f"[bridge error: {e}]"


async def handle_msg(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_chat:
        return
    chat_id = update.effective_chat.id
    if chat_id not in ALLOWED:
        log.warning(f"unauthorized chat: {chat_id}")
        await ctx.bot.send_message(chat_id, "Not authorized.")
        return
    text = (update.message and update.message.text) or ""
    if not text:
        return
    log.info(f"msg from {chat_id}: {text[:80]}")
    await ctx.bot.send_chat_action(chat_id, "typing")
    reply = await run_claude(text, chat_id)
    for chunk in split_for_telegram(reply):
        await ctx.bot.send_message(chat_id, chunk, parse_mode=None)


async def cmd_new(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_chat:
        return
    chat_id = update.effective_chat.id
    if chat_id not in ALLOWED:
        return
    sessions.pop(chat_id, None)
    await ctx.bot.send_message(chat_id, "New session started.")


async def cmd_status(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_chat:
        return
    chat_id = update.effective_chat.id
    if chat_id not in ALLOWED:
        return
    state = "active" if sessions.get(chat_id) else "fresh (no continuation)"
    await ctx.bot.send_message(
        chat_id,
        f"status\n  workdir: {WORKDIR}\n  session: {state}\n  tools: {ALLOWED_TOOLS}",
    )


def main() -> None:
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("new", cmd_new))
    app.add_handler(CommandHandler("reset", cmd_new))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))
    log.info(f"bot starting; workdir={WORKDIR}; allowed chats={sorted(ALLOWED)}")
    app.run_polling()


if __name__ == "__main__":
    main()
