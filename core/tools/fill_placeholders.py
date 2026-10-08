"""Fill {{PLACEHOLDER}} tokens in a template from a module's TOML [placeholders] table.

Usage:
    python fill_placeholders.py <template> <module.toml> <output>

Exits non-zero (and writes nothing) if any {{TOKEN}} has no value, so a half-filled
skill is never installed. Requires Python 3.11+ (tomllib).
"""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

TOKEN = re.compile(r"\{\{([A-Z_]+)\}\}")


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__)
        return 2
    template, toml_path, out = map(Path, argv[1:])
    values = tomllib.loads(toml_path.read_text(encoding="utf-8")).get("placeholders", {})
    text = template.read_text(encoding="utf-8")
    missing = sorted({t for t in TOKEN.findall(text) if t not in values})
    if missing:
        print(f"Missing values in [placeholders]: {', '.join(missing)}")
        return 1
    filled = TOKEN.sub(lambda m: str(values[m.group(1)]).strip(), text)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(filled, encoding="utf-8")
    print(f"Wrote {out.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
