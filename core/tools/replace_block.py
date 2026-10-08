"""Replace (or add) a module's marked block in a CLAUDE.md file.

Usage:
    python replace_block.py <CLAUDE.md> <module> <new_block.md>

The block is the text between `<!-- claude-harness:<module>:start -->` and
`<!-- claude-harness:<module>:end -->` (markers included in <new_block.md>). If the file has no
markers for the module, the block is appended. Writes LF line endings. Requires Python 3.11+.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__)
        return 2
    target, module, block_file = Path(argv[1]), argv[2], Path(argv[3])
    block = block_file.read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")
    start = f"<!-- claude-harness:{module}:start -->"
    end = f"<!-- claude-harness:{module}:end -->"
    if start not in block or end not in block:
        print(f"{block_file} must contain the {module} start and end markers")
        return 1
    text = target.read_text(encoding="utf-8").replace("\r\n", "\n") if target.exists() else ""
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if pattern.search(text):
        text = pattern.sub(lambda _: block, text, count=1)
    else:
        text = text.rstrip("\n") + ("\n\n" if text.strip() else "") + block
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip("\n") + "\n", encoding="utf-8", newline="\n")
    print(f"Updated {module} block in {target.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
