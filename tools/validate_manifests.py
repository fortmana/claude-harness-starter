"""Validate every modules/*/MODULE.md manifest.

Usage: python tools/validate_manifests.py
Exit code 1 if any manifest is invalid. Requires PyYAML (maintainer tool only).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "modules"

REQUIRED = {
    "name": str,
    "version": str,
    "status": str,
    "summary": str,
    "requires_modules": list,
    "prerequisites": list,
    "python_packages": list,
    "secrets": list,
    "installs": dict,
}
INSTALL_KEYS = {"skills", "claude_md_blocks", "templates", "scripts", "scheduled_tasks"}
PLACEHOLDER = re.compile(r"\{\{([A-Z_]+)\}\}")
STATUSES = {"planned", "alpha", "stable"}
REQUIRED_SECTIONS = ["What it does", "What it changes on your machine", "How to remove it"]
SECRET_LIKE = re.compile(r"(sk-[A-Za-z0-9]{10,}|[A-Fa-f0-9]{32,}|Bearer\s+\S+)")


def load(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("missing YAML frontmatter")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def check(path: Path, all_names: set[str]) -> list[str]:
    errs: list[str] = []
    try:
        meta, body = load(path)
    except Exception as e:  # noqa: BLE001
        return [f"{path}: {e}"]
    mod_dir = path.parent
    is_template = mod_dir.name == "_template"

    for key, typ in REQUIRED.items():
        if key not in meta:
            errs.append(f"missing key '{key}'")
        elif not isinstance(meta[key], typ):
            errs.append(f"'{key}' must be {typ.__name__}")
    if errs:
        return [f"{path}: {e}" for e in errs]

    if not is_template and meta["name"] != mod_dir.name:
        errs.append(f"name '{meta['name']}' must match folder '{mod_dir.name}'")
    if meta["status"] not in STATUSES:
        errs.append(f"status must be one of {sorted(STATUSES)}")
    unknown = set(meta["installs"]) - INSTALL_KEYS
    if unknown:
        errs.append(f"unknown installs keys: {sorted(unknown)}")
    for dep in meta["requires_modules"]:
        if dep not in all_names:
            errs.append(f"requires unknown module '{dep}'")
    for s in meta["secrets"]:
        if SECRET_LIKE.search(str(s)):
            errs.append("secrets must list names, not values")
    for sec in REQUIRED_SECTIONS:
        if f"## {sec}" not in body:
            errs.append(f"missing section '## {sec}'")
    if meta["status"] != "planned" and not is_template:
        for ref in ("interview", "verify"):
            if meta.get(ref) and not (mod_dir / meta[ref]).exists():
                errs.append(f"'{ref}' file '{meta[ref]}' not found")
        inst = meta["installs"]
        for skill in inst.get("skills", []):
            if not (mod_dir / "skills" / skill / "SKILL.md").exists():
                errs.append(f"skill '{skill}' missing skills/{skill}/SKILL.md")
        for blk in inst.get("claude_md_blocks", []):
            if not (mod_dir / "claude-md" / blk).exists():
                errs.append(f"claude_md_block '{blk}' missing in claude-md/")
        for tpl in inst.get("templates", []):
            if not (mod_dir / "templates" / tpl).exists():
                errs.append(f"template '{tpl}' missing in templates/")
        for scr in inst.get("scripts", []):
            if not (mod_dir / "scripts" / scr).exists():
                errs.append(f"script '{scr}' missing in scripts/")
        # every {{PLACEHOLDER}} used by the module must be defined in the interview
        interview = (mod_dir / meta["interview"]).read_text(encoding="utf-8") if meta.get("interview") else ""
        used = set()
        for f in list((mod_dir / "skills").rglob("*.md")) + list((mod_dir / "claude-md").glob("*.md")):
            used |= set(PLACEHOLDER.findall(f.read_text(encoding="utf-8")))
        for ph in sorted(used):
            if "{{" + ph + "}}" not in interview:
                errs.append(f"placeholder {{{{{ph}}}}} is used but not defined in {meta.get('interview', 'an interview')}")
    return [f"{path}: {e}" for e in errs]


def main() -> int:
    manifests = sorted(MODULES.glob("*/MODULE.md"))
    names = {p.parent.name for p in manifests if p.parent.name != "_template"}
    errors: list[str] = []
    for p in manifests:
        errors.extend(check(p, names))
    if errors:
        print("\n".join(errors))
        return 1
    print(f"OK: {len(manifests)} manifest(s) valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
