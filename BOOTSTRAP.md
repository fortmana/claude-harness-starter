# BOOTSTRAP — Instructions for Claude

You are setting up one or more modules from this repo for the user. Follow these steps in order. Be concise. **Do not install anything or edit any file outside this repo until the user approves the plan in step 5.**

## Ground rules

- Install only the modules the user selects, plus modules they require (offer, do not force).
- Never ask the user to paste an API key or secret into this chat. Direct them to run the module's key-setup script in their own terminal. If a key appears in chat, tell them to rotate it.
- Never register scheduled tasks or edit Claude Code settings files without explicit opt-in for that specific action.
- Read only the selected modules' `MODULE.md` files, not every module.
- Write user-specific answers to `~/.claude-harness/<module>.toml`, never into the repo.

## Steps

1. **Detect environment.** Report OS, Python version, Git, and the Claude Code config directory (`~/.claude`). Do not install anything.
2. **Choose modules.** List modules from `modules/*/MODULE.md` (skip `_template`). Ask which the user wants (multi-select). For each selection, read its `requires_modules`; if a required module is not selected, explain why and offer to add it.
3. **Check prerequisites.** For each selected module, compare `prerequisites` and `python_packages` against what step 1 found. List what is missing.
4. **Interview.** For each selected module that declares an `interview` file, ask those questions (batch them in one message where possible). Save answers to `~/.claude-harness/<module>.toml`.
5. **Show the plan and get approval.** Present, per module: packages to install, files to create, skills to copy into `~/.claude/skills`, CLAUDE.md blocks to append, scheduled tasks to register, and secrets the module needs (names only). Mark scheduled tasks and settings edits as separate opt-ins. Wait for approval.
6. **Execute** only the approved steps for the selected modules.
7. **Verify.** Run each module's `verify` steps. Report pass/fail honestly; do not claim success on a failed check.
8. **Record.** Write `~/.claude-harness/installed.json` with module names, versions, and install date so later "add module" runs know what is present.
9. **Tell the user** to start a new Claude Code session (skills and CLAUDE.md load at session start) and point them to each module's "How to remove it" section.

## Adding a module later

Re-run this file. Read `~/.claude-harness/installed.json`, skip installed modules, and run steps 2-9 for the new one.
