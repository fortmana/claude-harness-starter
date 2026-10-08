# Contributing

For maintainers and anyone building a new module. Users who just want to install modules should start at the [README](README.md).

## Before every commit

```
pip install -r tools/requirements.txt
python tools/validate_manifests.py
python tools/check_generic.py
```

- `validate_manifests.py` checks every `modules/*/MODULE.md` manifest (required fields, status values, required sections, placeholders).
- `check_generic.py` fails if the repo contains personal, client, or company-specific values. Add new patterns to `tools/generic_denylist.txt`.

## Building a module

A module is a folder under `modules/<name>/`. Copy `modules/_template/` and fill it in.

1. **Scope it.** One module = one capability a person would say yes or no to. If it needs another module, list it in `requires_modules`.
2. **Write `MODULE.md`.** The frontmatter is the contract with `BOOTSTRAP.md`; the body must contain the sections "What it does", "What it changes on your machine", and "How to remove it". List *everything* that changes the user's machine. If it is not listed, it must not happen.
3. **Keep the interview tiny.** `interview.md` holds only questions that cannot be defaulted. Put every other choice in `defaults.toml`. Aim for one or two questions.
4. **Use placeholders for user values.** Write `{{NAME}}` in skills and CLAUDE.md blocks; BOOTSTRAP fills them from the user's `~/.claude-harness/<module>.toml`. Never hardcode a person, company, path, or client.
5. **Handle secrets the standard way.** Declare names in `secrets`, never values. Users store keys with `core/secrets/harness_secrets.py` in their own terminal. See [SECURITY.md](SECURITY.md).
6. **Make scheduling and settings edits explicit opt-ins.** Never on by default.
7. **Write `verify.md`.** File checks (run right after install) and behavior checks (run in a new session). Include one check that needs no real credentials, for example a bundled sample.
8. **Optionally write `tailor.md`.** A conversation that shows the default result and asks what to change. Never a form.
9. **Document removal.** Exact steps, including deleting secrets and scheduled tasks.
10. **Test it.** Run BOOTSTRAP in a fresh Claude Code session on a clean machine or folder and record what went wrong. Fix the module, not just your session.
11. **Update docs.** Add the module to the README table and `REQUIREMENTS.md`, and add a `CHANGELOG.md` entry.

## Module folder layout

```
modules/<name>/
  MODULE.md          manifest + human documentation
  interview.md       base questions only
  defaults.toml      [settings] and [placeholders] defaults
  tailor.md          optional tailoring conversation
  verify.md          file checks and behavior checks
  skills/            skill folders copied to ~/.claude/skills
  claude-md/         CLAUDE.md blocks appended on opt-in
  templates/         note or file templates
  scripts/           scripts copied to the state folder
```

## Cross-module settings

If your module relies on a value another module owns (for example `fireflies` files notes into the `obsidian-memory` folder `50 - Meetings`), say so in a "Depends on settings from other modules" section of your `MODULE.md`. List the module, the setting, and what to update if the user changes it. The owning module's `tailor.md` must tell Claude to update dependents.

## Versioning

Bump `version` in `MODULE.md` when behavior changes, and add a line to `CHANGELOG.md`. Use `0.x` while a module is `alpha`.
