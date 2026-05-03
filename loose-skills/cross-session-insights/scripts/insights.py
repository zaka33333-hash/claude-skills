#!/usr/bin/env python3
"""
Cross-session insights dashboard.

Aggregates ~/.claude/projects/<project>/<session>.jsonl + ~/.claude-mem/claude-mem.db
across the last N days. Outputs HTML dashboard + Markdown summary.

Usage:
  python insights.py --days 7
  python insights.py --days 30 --out custom.html
"""

import argparse
import json
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

PROJECTS_DIR = Path.home() / ".claude" / "projects"
MEM_DB = Path.home() / ".claude-mem" / "claude-mem.db"
STATE_DIR = Path.home() / ".claude" / "state"


def parse_iso(s: str) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def project_name(folder: str) -> str:
    """Decode `C--Users-toner-OneDrive-Desktop-Gemma` → readable name."""
    parts = folder.replace("--", "/", 1).split("-")
    # Take last meaningful segment
    return parts[-1] if parts else folder


def aggregate_sessions(days: int) -> dict:
    """Walk all session JSONLs in window. Return per-project + per-day stats."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    by_project: dict[str, dict] = defaultdict(
        lambda: {
            "sessions": 0,
            "messages": 0,
            "tokens_in": 0,
            "tokens_out": 0,
            "tokens_cache_read": 0,
            "tools": Counter(),
            "skills": Counter(),
            "first_seen": None,
            "last_seen": None,
            "hours": 0.0,
        }
    )
    by_day: dict[str, dict] = defaultdict(lambda: {"messages": 0, "minutes": 0.0})

    if not PROJECTS_DIR.exists():
        return {"by_project": {}, "by_day": {}, "total": {}}

    for proj_dir in PROJECTS_DIR.iterdir():
        if not proj_dir.is_dir():
            continue
        proj = project_name(proj_dir.name)
        for jsonl in proj_dir.glob("*.jsonl"):
            session_start: datetime | None = None
            session_end: datetime | None = None
            try:
                with open(jsonl, encoding="utf-8") as f:
                    msgs_in_session = 0
                    for line in f:
                        try:
                            obj = json.loads(line)
                        except Exception:
                            continue
                        ts = parse_iso(obj.get("timestamp", ""))
                        if not ts or ts < cutoff:
                            continue
                        if not session_start:
                            session_start = ts
                        session_end = ts

                        p = by_project[proj]
                        msgs_in_session += 1
                        p["messages"] += 1
                        if not p["first_seen"] or ts < p["first_seen"]:
                            p["first_seen"] = ts
                        if not p["last_seen"] or ts > p["last_seen"]:
                            p["last_seen"] = ts

                        # Token usage in assistant messages
                        msg = obj.get("message", {}) or {}
                        usage = msg.get("usage", {}) or {}
                        p["tokens_in"] += usage.get("input_tokens", 0) or 0
                        p["tokens_out"] += usage.get("output_tokens", 0) or 0
                        p["tokens_cache_read"] += usage.get("cache_read_input_tokens", 0) or 0

                        # Tool calls
                        for content in (msg.get("content") or []):
                            if isinstance(content, dict):
                                if content.get("type") == "tool_use":
                                    p["tools"][content.get("name", "?")] += 1

                        # Day bucket
                        day = ts.date().isoformat()
                        by_day[day]["messages"] += 1
            except Exception:
                continue

            if session_start and session_end and msgs_in_session > 0:
                duration_min = max(1, (session_end - session_start).total_seconds() / 60)
                by_project[proj]["sessions"] += 1
                by_project[proj]["hours"] += duration_min / 60
                day = session_start.date().isoformat()
                by_day[day]["minutes"] += duration_min

    total = {
        "messages": sum(p["messages"] for p in by_project.values()),
        "tokens_in": sum(p["tokens_in"] for p in by_project.values()),
        "tokens_out": sum(p["tokens_out"] for p in by_project.values()),
        "tokens_cache_read": sum(p["tokens_cache_read"] for p in by_project.values()),
        "hours": sum(p["hours"] for p in by_project.values()),
        "sessions": sum(p["sessions"] for p in by_project.values()),
    }
    return {"by_project": dict(by_project), "by_day": dict(by_day), "total": total}


def aggregate_observations(days: int) -> list[dict]:
    """Pull recent claude-mem observations for the window."""
    if not MEM_DB.exists():
        return []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    out: list[dict] = []
    try:
        conn = sqlite3.connect(f"file:{MEM_DB}?mode=ro", uri=True)
        conn.row_factory = sqlite3.Row
        # Try common observation tables
        for tbl in ("observations", "memories", "obs"):
            try:
                cur = conn.execute(f"SELECT * FROM {tbl} ORDER BY created_at DESC LIMIT 200")
                for row in cur:
                    d = dict(row)
                    ts = d.get("created_at") or d.get("timestamp") or ""
                    parsed = parse_iso(str(ts))
                    if parsed and parsed >= cutoff:
                        out.append(d)
                if out:
                    break
            except sqlite3.Error:
                continue
        conn.close()
    except Exception:
        pass
    return out[:100]


def estimate_cost(tokens_in: int, tokens_out: int, tokens_cache: int) -> float:
    # Sonnet 4.5 approx pricing (USD per 1M tokens)
    return (
        tokens_in / 1_000_000 * 3.00
        + tokens_out / 1_000_000 * 15.00
        + tokens_cache / 1_000_000 * 0.30
    )


def build_html(data: dict, observations: list[dict], days: int) -> str:
    by_project = sorted(
        data["by_project"].items(),
        key=lambda kv: kv[1]["hours"],
        reverse=True,
    )
    by_day = sorted(data["by_day"].items())
    total = data["total"]
    cost = estimate_cost(total["tokens_in"], total["tokens_out"], total["tokens_cache_read"])

    # Top skills + tools across all projects
    all_tools: Counter = Counter()
    for p in data["by_project"].values():
        all_tools.update(p["tools"])
    top_tools = all_tools.most_common(15)

    proj_rows = "\n".join(
        f"""<tr>
              <td>{p}</td>
              <td>{stats['sessions']}</td>
              <td>{stats['hours']:.1f}h</td>
              <td>{stats['messages']:,}</td>
              <td>{stats['tokens_in']+stats['tokens_out']:,}</td>
              <td>{stats['last_seen'].strftime('%b %d') if stats['last_seen'] else '—'}</td>
            </tr>"""
        for p, stats in by_project[:20]
    )

    day_rows = "\n".join(
        f"""<tr><td>{d}</td><td>{stats['minutes']/60:.1f}h</td><td>{stats['messages']}</td></tr>"""
        for d, stats in by_day[-30:]
    )

    tool_rows = "\n".join(
        f"""<tr><td><code>{t}</code></td><td>{c}</td></tr>""" for t, c in top_tools
    )

    obs_rows = "\n".join(
        f"""<li><b>{o.get('type','?')}</b> — {(o.get('content') or o.get('text') or '')[:140]}</li>"""
        for o in observations[:30]
    )

    max_minutes = max((s["minutes"] for s in data["by_day"].values()), default=1)
    heatmap = "".join(
        f'<div title="{d}: {s["minutes"]/60:.1f}h" '
        f'style="background:rgba(159,191,16,{min(1, s["minutes"]/max_minutes)});'
        f'width:18px;height:18px;display:inline-block;margin:1px;border-radius:3px;"></div>'
        for d, s in by_day
    )

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Insights · last {days} days</title>
<style>
  :root {{ --bg:#0a0a0c; --bg2:#121214; --txt:#fff; --muted:#99a1af; --acc:#bff549; --cyan:#00d4ff; }}
  body {{ background:var(--bg); color:var(--txt); font-family:'Manrope',-apple-system,system-ui,sans-serif; max-width:1200px; margin:40px auto; padding:0 24px; }}
  h1 {{ font-size:42px; letter-spacing:-0.02em; margin:0 0 8px; }}
  h2 {{ font-size:22px; margin:40px 0 16px; color:var(--acc); letter-spacing:-0.01em; }}
  .sub {{ color:var(--muted); margin-bottom:32px; }}
  .stats {{ display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin:32px 0; }}
  .stat {{ background:var(--bg2); border:1px solid #222; border-radius:12px; padding:20px; }}
  .stat .num {{ font-size:34px; font-weight:700; letter-spacing:-0.02em; color:var(--acc); }}
  .stat .lbl {{ color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:0.08em; margin-top:4px; }}
  table {{ width:100%; border-collapse:collapse; background:var(--bg2); border-radius:12px; overflow:hidden; }}
  th,td {{ padding:10px 14px; text-align:left; border-bottom:1px solid #222; font-size:14px; }}
  th {{ background:#1a1a1d; color:var(--muted); font-size:11px; text-transform:uppercase; letter-spacing:0.06em; }}
  code {{ background:#1a1a1d; padding:2px 6px; border-radius:4px; color:var(--cyan); font-size:12px; }}
  ul {{ list-style:none; padding:0; }}
  ul li {{ background:var(--bg2); padding:10px 14px; margin:6px 0; border-radius:8px; border-left:3px solid var(--acc); font-size:13px; }}
  .heat {{ background:var(--bg2); padding:20px; border-radius:12px; line-height:1; }}
</style></head><body>
<h1>Insights</h1>
<div class="sub">Last {days} days · generated {datetime.now().strftime('%Y-%m-%d %H:%M')}</div>

<div class="stats">
  <div class="stat"><div class="num">{total['hours']:.1f}h</div><div class="lbl">Total time</div></div>
  <div class="stat"><div class="num">{total['sessions']}</div><div class="lbl">Sessions</div></div>
  <div class="stat"><div class="num">{(total['tokens_in']+total['tokens_out'])/1000:.0f}k</div><div class="lbl">Tokens</div></div>
  <div class="stat"><div class="num">${cost:.2f}</div><div class="lbl">Est. cost</div></div>
</div>

<h2>Activity heatmap</h2>
<div class="heat">{heatmap}</div>

<h2>Top projects</h2>
<table><thead><tr><th>Project</th><th>Sessions</th><th>Hours</th><th>Messages</th><th>Tokens</th><th>Last</th></tr></thead>
<tbody>{proj_rows}</tbody></table>

<h2>Top tools used</h2>
<table><thead><tr><th>Tool</th><th>Calls</th></tr></thead><tbody>{tool_rows}</tbody></table>

<h2>Daily breakdown</h2>
<table><thead><tr><th>Date</th><th>Hours</th><th>Messages</th></tr></thead><tbody>{day_rows}</tbody></table>

<h2>Recent observations (claude-mem)</h2>
<ul>{obs_rows or '<li>(no observations in window)</li>'}</ul>
</body></html>
"""


def build_markdown_summary(data: dict, days: int) -> str:
    total = data["total"]
    cost = estimate_cost(total["tokens_in"], total["tokens_out"], total["tokens_cache_read"])
    by_project = sorted(
        data["by_project"].items(), key=lambda kv: kv[1]["hours"], reverse=True
    )
    lines = [
        f"## Insights — last {days} days",
        "",
        f"- **{total['hours']:.1f}h** across **{total['sessions']}** sessions",
        f"- **{(total['tokens_in']+total['tokens_out'])/1000:.0f}k tokens** (~**${cost:.2f}** estimated)",
        "",
        "### Top projects",
    ]
    for p, s in by_project[:8]:
        lines.append(f"- **{p}** — {s['hours']:.1f}h ({s['sessions']} sessions, {s['messages']} msgs)")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--days", type=int, default=7)
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    data = aggregate_sessions(args.days)
    obs = aggregate_observations(args.days)

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    out_path = args.out or (
        STATE_DIR / f"insights-{datetime.now().strftime('%Y-%m-%d')}.html"
    )
    out_path.write_text(build_html(data, obs, args.days), encoding="utf-8")
    print(build_markdown_summary(data, args.days))
    print(f"\n📊 Dashboard: {out_path}")
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
