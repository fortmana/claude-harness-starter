"""Build a module's ~/.claude-harness/<module>.toml from its defaults plus overrides.

Usage:
    python build_toml.py <defaults.toml> <out.toml> [--set KEY=VALUE ...] [--ph KEY=VALUE ...]

    --set  sets a key in [settings]     (e.g. --set my_email=you@example.com)
    --ph   sets a key in [placeholders] (e.g. --ph VAULT_PATH=C:/Users/<you>/Vault)

Values are strings. A `--set` value that is valid JSON (a number, true/false, or a list)
is stored as that type, for example --set 'skip_title_patterns=["lunch"]'. Requires Python 3.11+.
Always writes forward-slash-safe, valid TOML so paths never need hand escaping.
"""
from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path


def dump_value(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, list):
        return "[" + ", ".join(dump_value(x) for x in v) + "]"
    s = str(v)
    if "\n" in s and '"""' not in s:
        return '"""\n' + s.replace("\\", "\\\\").strip("\n") + '\n"""'
    return json.dumps(s, ensure_ascii=False)


def dump_table(name: str, table: dict) -> str:
    out = [f"[{name}]"]
    out += [f"{k} = {dump_value(v)}" for k, v in table.items()]
    return "\n".join(out) + "\n"


def parse_pairs(pairs: list[str], typed: bool) -> dict:
    result = {}
    for p in pairs:
        key, _, raw = p.partition("=")
        if not key or not _:
            sys.exit(f"Bad argument (expected KEY=VALUE): {p}")
        value = raw
        if typed:
            try:
                parsed = json.loads(raw)
                if isinstance(parsed, (bool, int, float, list)):
                    value = parsed
            except json.JSONDecodeError:
                pass
        result[key] = value
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("defaults")
    ap.add_argument("out")
    ap.add_argument("--set", action="append", default=[], dest="settings")
    ap.add_argument("--ph", action="append", default=[], dest="placeholders")
    args = ap.parse_args()

    base = tomllib.loads(Path(args.defaults).read_text(encoding="utf-8"))
    settings = dict(base.get("settings", {}))
    placeholders = dict(base.get("placeholders", {}))
    settings.update(parse_pairs(args.settings, typed=True))
    placeholders.update(parse_pairs(args.placeholders, typed=False))

    text = dump_table("settings", settings) + "\n" + dump_table("placeholders", placeholders)
    tomllib.loads(text)  # refuse to write invalid TOML
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {out.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
