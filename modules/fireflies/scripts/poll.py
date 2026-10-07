"""Poll Fireflies for new transcripts and save each as a JSON package in pending/.

Usage:
    python poll.py                 # fetch new transcripts since the last run
    python poll.py --dry-run       # list what would be fetched; save nothing
    python poll.py --exclude <id>  # never fetch this transcript again

Configuration: ~/.claude-harness/fireflies.toml (written during setup)
    my_email             = "you@example.com"   # only keep meetings you organized or attended
    lookback_days        = 7                   # first run only
    skip_title_patterns  = ["lunch", "1:1 personal"]   # case-insensitive substrings
    state_dir            = ""                  # optional override

API key: stored with `python harness_secrets.py set fireflies_api_key` (run in your own terminal),
or the FIREFLIES_API_KEY environment variable. The key is never printed or logged.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
import time
import tomllib
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harness_secrets import require_secret  # noqa: E402

ENDPOINT = "https://api.fireflies.ai/graphql"
CONFIG_PATH = Path.home() / ".claude-harness" / "fireflies.toml"
FETCH_LIMIT = 50  # API page cap
DETAIL_SLEEP = 1.0  # seconds between detail calls (rate-limit courtesy)

LIST_QUERY = """
query Transcripts($fromDate: DateTime, $limit: Int, $skip: Int) {
  transcripts(fromDate: $fromDate, limit: $limit, skip: $skip) {
    id title date duration organizer_email
    meeting_attendees { displayName email name }
  }
}
"""

DETAIL_QUERY = """
query Transcript($id: String!) {
  transcript(id: $id) {
    id title date duration organizer_email
    meeting_attendees { displayName email name }
    sentences { speaker_name text start_time end_time }
    summary { gist action_items short_summary keywords overview }
  }
}
"""


def load_config() -> dict:
    cfg: dict = {}
    if CONFIG_PATH.exists():
        cfg = tomllib.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    state = cfg.get("state_dir") or str(Path.home() / ".claude-harness" / "fireflies")
    cfg["_state"] = Path(state)
    return cfg


def setup_logging(state: Path) -> logging.Logger:
    state.mkdir(parents=True, exist_ok=True)
    log = logging.getLogger("fireflies_poll")
    log.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s  %(levelname)-7s  %(message)s", "%Y-%m-%d %H:%M:%S")
    for h in (logging.FileHandler(state / "poll.log", encoding="utf-8"), logging.StreamHandler()):
        h.setFormatter(fmt)
        log.addHandler(h)
    return log


def gql(key: str, query: str, variables: dict) -> dict:
    resp = requests.post(
        ENDPOINT,
        json={"query": query, "variables": variables},
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
    body = resp.json()
    if "errors" in body:
        raise RuntimeError(f"GraphQL errors: {body['errors']}")
    return body.get("data", {})


def parse_date(raw) -> str:
    if raw is None:
        return ""
    if isinstance(raw, (int, float)):
        ts = raw / 1000 if raw > 1e10 else raw
        return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
    return str(raw)[:10]


def fmt_attendees(attendees: list | None) -> list[str]:
    out = []
    for a in attendees or []:
        name = a.get("displayName") or a.get("name") or ""
        email = a.get("email") or ""
        out.append(f"{name} <{email}>" if name and email else (email or name))
    return [x for x in out if x]


def load_excluded(path: Path) -> set[str]:
    if not path.exists():
        return set()
    try:
        return {e["id"] for e in json.loads(path.read_text(encoding="utf-8")) if e.get("id")}
    except Exception:  # noqa: BLE001
        return set()


def add_excluded(path: Path, tid: str) -> None:
    entries = []
    if path.exists():
        entries = json.loads(path.read_text(encoding="utf-8"))
    if not any(e.get("id") == tid for e in entries):
        entries.append({"id": tid, "added": datetime.now(timezone.utc).isoformat()})
        path.write_text(json.dumps(entries, indent=2), encoding="utf-8")


def is_mine(item: dict, my_email: str) -> bool:
    """True if my_email is the organizer or an attendee. No filter if my_email is unset."""
    if not my_email:
        return True
    me = my_email.lower()
    if (item.get("organizer_email") or "").lower() == me:
        return True
    return any((a.get("email") or "").lower() == me for a in item.get("meeting_attendees") or [])


def build_package(detail: dict) -> dict:
    summary = detail.get("summary") or {}
    lines = []
    for s in detail.get("sentences") or []:
        text = (s.get("text") or "").strip()
        if text:
            lines.append(f"{s.get('speaker_name') or 'Unknown'}: {text}")
    return {
        "id": detail.get("id"),
        "title": detail.get("title") or "",
        "date": parse_date(detail.get("date")),
        "duration_seconds": detail.get("duration") or 0,
        "organizer": detail.get("organizer_email") or "",
        "attendees": fmt_attendees(detail.get("meeting_attendees")),
        "transcript_text": "\n".join(lines),
        "ai_summary": {k: summary.get(k) or "" for k in ("gist", "action_items", "short_summary", "keywords", "overview")},
        "source": "fireflies",
    }


def fetch_list(key: str, from_date: str) -> list[dict]:
    items, skip = [], 0
    while True:
        page = gql(key, LIST_QUERY, {"fromDate": from_date, "limit": FETCH_LIMIT, "skip": skip}).get("transcripts") or []
        items.extend(page)
        if len(page) < FETCH_LIMIT:
            return items
        skip += FETCH_LIMIT
        time.sleep(DETAIL_SLEEP)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--exclude", metavar="ID")
    args = ap.parse_args()

    cfg = load_config()
    state: Path = cfg["_state"]
    log = setup_logging(state)
    pending, checkpoint, excl_path = state / "pending", state / "last_run.json", state / "excluded_ids.json"

    if args.exclude:
        add_excluded(excl_path, args.exclude)
        log.info("Excluded %s permanently", args.exclude)
        return 0

    key = require_secret("fireflies_api_key", "FIREFLIES_API_KEY")
    excluded = load_excluded(excl_path)
    skip_patterns = [p.lower() for p in cfg.get("skip_title_patterns", [])]
    my_email = cfg.get("my_email", "")

    if checkpoint.exists():
        from_date = json.loads(checkpoint.read_text(encoding="utf-8")).get("last_run")
    else:
        days = int(cfg.get("lookback_days", 7))
        from_date = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
        log.info("First run: looking back %d days", days)
    run_start = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

    try:
        items = fetch_list(key, from_date)
    except Exception as e:  # noqa: BLE001
        log.error("Failed to list transcripts: %s", e)
        return 1
    log.info("Found %d transcript(s) since %s", len(items), from_date)

    if not my_email:
        log.warning("my_email is not set: transcripts from other people's meetings may be included. "
                    "Set it in %s.", CONFIG_PATH)

    pending.mkdir(parents=True, exist_ok=True)
    saved = skipped = failed = 0
    for item in items:
        tid, title = item.get("id"), item.get("title") or ""
        if not tid or tid in excluded or (pending / f"{tid}.json").exists():
            skipped += 1
            continue
        if not is_mine(item, my_email):
            log.info("Skipped (not your meeting): %s", tid)
            skipped += 1
            continue
        if any(p in title.lower() for p in skip_patterns):
            log.info("Skipped (title rule): %s", tid)
            skipped += 1
            continue
        if args.dry_run:
            log.info("Would fetch: %s  %s  %s", tid, parse_date(item.get("date")), title)
            continue
        try:
            time.sleep(DETAIL_SLEEP)
            detail = gql(key, DETAIL_QUERY, {"id": tid}).get("transcript")
            if not detail:
                log.warning("No detail for %s", tid)
                failed += 1
                continue
            pkg = build_package(detail)
            (pending / f"{tid}.json").write_text(json.dumps(pkg, indent=2, ensure_ascii=False), encoding="utf-8")
            log.info("Saved %s  %s  (%s)", tid, pkg["title"] or "(no title)", pkg["date"])
            saved += 1
        except Exception as e:  # noqa: BLE001
            log.error("Error fetching %s: %s", tid, e)
            failed += 1

    if not args.dry_run and failed == 0:
        checkpoint.write_text(json.dumps({"last_run": run_start}, indent=2), encoding="utf-8")
    log.info("Done: %d saved, %d skipped, %d failed", saved, skipped, failed)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
