# Changelog

Per-module versions are in each `MODULE.md`. Tag each entry with the module and version it applies to, for example `[fireflies 0.1.1]`; repo-wide entries use `[repo]`. To update an installed module, see "Updating a module" in `BOOTSTRAP.md`.

## Unreleased

- Python 3.11+ is now required for every module (setup helper scripts need it).
- `build_toml.py`: new `--base` (update a toml without re-typing values) and `--ph-from` (reuse a placeholder from another module's toml).
- CLAUDE.md blocks are wrapped in `claude-harness:<module>:start/end` markers. "Updating a module" now has a no-op rule, a diff, and a backup before replacing.
- BOOTSTRAP creates the state folder subfolders a module lists (`fireflies`: `pending/`, `processed/`).
- Tailoring no longer asks the user's name; it is taken from `my_email`.
- Doc fixes: stale `defaults.toml` comments, `obsidian-memory` setup order and explicit folder list, `fireflies` verify wording.

- README: added "What is a harness?", status definitions, suggested growth path, and platform note.
- Added `CONTRIBUTING.md` (maintainer commands and how to build a module) and `docs/concepts.md`.
- Added "Depends on settings from other modules" sections to the module manifests and template.
- Added "Updating a module" to `BOOTSTRAP.md`.
- Added `core/tools/README.md`.

## 0.1.0 — `obsidian-memory`, `fireflies`

- Initial alpha release of both modules, BOOTSTRAP, secrets helper, validators, and the example session.
