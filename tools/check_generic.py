"""Fail if the repo contains personal, company, or client-specific values.

Usage: python tools/check_generic.py
Patterns live in tools/generic_denylist.txt (one regex per line, # comments).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DENYLIST = Path(__file__).with_name("generic_denylist.txt")
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules"}
SKIP_FILES = {DENYLIST.name, Path(__file__).name}
TEXT_SUFFIXES = {".md", ".py", ".txt", ".toml", ".json", ".yml", ".yaml", ".ps1", ".sh", ".bat", ""}


def patterns() -> list[re.Pattern]:
    out = []
    for line in DENYLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(re.compile(line, re.I))
    return out


def main() -> int:
    pats = patterns()
    hits = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.name in SKIP_FILES:
            continue
        if SKIP_DIRS & set(path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for p in pats:
                if p.search(line):
                    hits.append(f"{path.relative_to(ROOT)}:{i}: matches /{p.pattern}/")
    if hits:
        print("\n".join(hits))
        print(f"\nFAIL: {len(hits)} non-generic value(s) found")
        return 1
    print("OK: no non-generic values found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
