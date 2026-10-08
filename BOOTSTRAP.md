# BOOTSTRAP — Instructions for Claude

You are setting up one or more modules from this repo for the user. Follow these steps in order. Be concise. **Until the user approves the plan in step 5, change nothing outside this repo: no installs, no files, no settings.** Hold answers in the conversation until then.

The install itself should feel like an installer: ask very little (a couple of base questions), use the module defaults for everything else, and then **offer** an optional tailoring conversation once things work.

## Ground rules

- Install only the modules the user selects, plus modules they require (offer, do not force).
- Never ask the user to paste an API key or secret into this chat. Give them the exact command to run in their own terminal (step 7). If a key appears in chat, tell them to rotate it.
- Never register scheduled tasks or edit Claude Code settings files without explicit opt-in for that specific action. Do not copy `schedule_*` scripts unless the user opts in to scheduling.
- Read only the selected modules' `MODULE.md` files (and the files they point to), not every module.
- Write user-specific values to `~/.claude-harness/`, never into the repo.
- Use forward slashes in paths you write into TOML, skills, and CLAUDE.md (for example `C:/Users/<you>/Vault`), even on Windows. In PowerShell commands you give the user, use `$HOME\.claude-harness\...` rather than `~`.
- Do not turn setup into a form. Never read a long list of questions at the user. Tailoring (step 9) works by showing a result and asking what they would change.

## Terms

- **`~`** is the user's home folder (`$HOME`; `%USERPROFILE%` on Windows).
- **State folder** is where a module keeps its scripts and downloaded data (for example `~/.claude-harness/fireflies/`). Explain it once in plain words: "where Claude keeps the scripts and downloaded transcripts."

## Files Claude writes under `~/.claude-harness/`

`<module>.toml` — one per module, built from the module's `defaults.toml` plus the user's answers and computed values:

```toml
[settings]            # real configuration read by scripts
my_email = "you@example.com"
state_dir = "C:/Users/<you>/.claude-harness/fireflies"
python = "C:/Python313/python.exe"

[placeholders]        # the text substituted into the module's skill and CLAUDE.md block
VAULT_PATH = "C:/Users/<you>/Documents/Vault"
OUTPUT_SECTIONS = """
1. **Summary** ...
"""
```

Use forward slashes or single-quoted literal strings for paths. Keep every `{{NAME}}` value in `[placeholders]` so installs are reproducible.

`installed.json`:

```json
{"modules": [{"name": "obsidian-memory", "version": "0.1.0", "installed": "YYYY-MM-DD"}]}
```

## Steps

1. **Detect environment.** Run `git --version` and `python --version` (on Windows also `python -c "import sys; print(sys.executable)"` to get the real interpreter path; record it with forward slashes, since it prints backslashes and may be an 8.3 short path). Report OS, Git, Python version and path, and whether `~/.claude` and `~/.claude/skills` exist (you create them in step 6 if missing). Do not install anything. If **Git** is missing, **stop now** and give the user the "Installing Git" instructions from `REQUIREMENTS.md`: they install it themselves, you wait, then re-run the detection. If **Python** is missing (typing `python` and having the Microsoft Store open means it is not installed), note it and continue to step 2; you stop for it in step 3 only if a selected module needs it. Never try to install Git or Python yourself.
2. **Choose modules.** List modules from `modules/*/MODULE.md` (skip `_template`) with their one-line summaries. Ask which the user wants. For each selection read `requires_modules`; if a required module is not selected (or installed per `installed.json`), explain why and offer to add it.
3. **Check prerequisites.** Compare each selected module's `prerequisites` and `python_packages` against step 1 and `REQUIREMENTS.md`. List what is missing. If a selected module needs Python and it is missing or older than required, **stop and give the user the "Installing Python" instructions from `REQUIREMENTS.md`**; they install it, you wait, then re-run the detection. Use the user's own Python by default (not a throwaway venv) because the user will run scripts such as key setup in their own terminal with the same interpreter. If they prefer a venv, record its interpreter as `python` in the module's settings and use it consistently.
4. **Base questions.** Read each selected module's `interview` file. It contains only the few questions that cannot be defaulted (for example vault location, your email). Ask them together in one short message, de-duplicating any overlap. Do not ask anything else; take everything else from the module's `defaults.toml`. Compute the rest (state folder, Python path), and reuse values from an installed module's toml by **copying them into the new module's `[placeholders]`**. Default the CLAUDE.md target to `~/.claude/CLAUDE.md`. Hold the answers; do not write files yet. You can ask these in the same message as the module choice when the user has already named their modules.
5. **Show the plan and get approval.** Keep it short. Per module: packages to install, files to create, skills to copy to `~/.claude/skills`, templates, CLAUDE.md blocks to append (and which file), and secrets the module needs (names only). Summarize the default behavior in a few lines (for example for meetings: "notes get a 3-sentence summary, decisions, action items, risks for client meetings, and a parking lot; you can reshape this after setup"). List scheduled tasks and settings edits as separate opt-ins. Wait for approval.
6. **Execute** only the approved steps:
   - Create `~/.claude/skills` if missing. When adding to an existing CLAUDE.md, append; never overwrite or reorder what is there. Create `~/.claude/CLAUDE.md` if it does not exist. Build `~/.claude-harness/<module>.toml` with `python core/tools/build_toml.py modules/<module>/defaults.toml <out.toml> --set key=value ... --ph NAME=value ...` (defaults first, then the user's answers and computed values such as `state_dir`, `python`, `my_email`, `STATE_DIR`, `VAULT_PATH`).
   - Fill every `{{PLACEHOLDER}}` from `[placeholders]` before copying anything, using `python core/tools/fill_placeholders.py <template> <toml> <output>` when Python is available (otherwise by hand). Never copy a file that still contains `{{...}}`.
   - Copy `templates/` files and scripts where the module's `MODULE.md` says. If a module declares `secrets`, also copy `core/secrets/harness_secrets.py` into the same folder as its scripts and `requirements.txt` into the state folder.
   - Install packages with the recorded Python: `<python> -m pip install -r requirements.txt`.
7. **File checks.** Run the file checks section of each module's `verify`. If a module needs a secret, **stop and give the user the exact command for their shell** (for example, PowerShell: `cd $HOME\.claude-harness\fireflies; & "<python>" harness_secrets.py set fireflies_api_key`, using the same Python recorded in settings). Wait until they confirm it is stored, then run the checks that need it. Report pass/fail honestly; never claim success on a failed check.
8. **Record.** Write or update `~/.claude-harness/installed.json`.
9. **Restart, then offer tailoring.** Tell the user to start a new Claude Code session (skills and CLAUDE.md load at session start) and run the behavior checks in each module's `verify`. Then, for each installed module that has a `tailor` file, **offer** (once) to help tailor it: "Want help tailoring this? I'll show you what the default looks like and you tell me what to change, or you can use it as is." If they say yes, follow that module's `tailor.md`. If they say no, stop and tell them they can ask any time. Point them to each module's "How to remove it" section.

## Updating a module

When the user asks to update, or the repo has a newer version (see `CHANGELOG.md` and each `MODULE.md` `version`):

1. Read `~/.claude-harness/installed.json` and compare versions. Summarize what changed from `CHANGELOG.md`.
2. Re-use the user's existing `~/.claude-harness/<module>.toml`; do not re-ask questions. Add any new `[placeholders]` or `[settings]` keys from the module's `defaults.toml`, and never overwrite values the user has set.
3. Show the plan (which installed skills and CLAUDE.md blocks will be replaced) and wait for approval. Replace the installed skill folder and the module's block in CLAUDE.md in place; do not append a duplicate block.
4. Re-run the module's file checks, update `installed.json`, and tell the user to start a new session.

## Adding a module later

Re-run this file. Read `installed.json`, skip installed modules, reuse existing `[placeholders]`, and run steps 2-9 for the new one.
