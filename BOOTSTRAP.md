# BOOTSTRAP — Instructions for Claude

You are setting up one or more modules from this repo for the user. Follow these steps in order. Be concise. **Until the user approves the plan in step 5, change nothing outside this repo: no installs, no files, no settings.** Hold interview answers in the conversation until then.

## Ground rules

- Install only the modules the user selects, plus modules they require (offer, do not force).
- Never ask the user to paste an API key or secret into this chat. Give them the exact command to run in their own terminal (step 7). If a key appears in chat, tell them to rotate it.
- Never register scheduled tasks or edit Claude Code settings files without explicit opt-in for that specific action. Do not copy `schedule_*` scripts unless the user opts in to scheduling.
- Read only the selected modules' `MODULE.md` files, not every module.
- Write user-specific answers to `~/.claude-harness/`, never into the repo.
- Use forward slashes in paths you write into TOML, skills, and CLAUDE.md (for example `C:/Users/<you>/Vault`), even on Windows. In PowerShell commands you give the user, use `$HOME\.claude-harness\...` rather than `~`.

## Terms

- **`~`** is the user's home folder (`$HOME`; `%USERPROFILE%` on Windows).
- **State folder** is where a module keeps its scripts and downloaded data (for example `~/.claude-harness/fireflies/`). Say "state folder" to the user and explain it once in plain words: "where Claude keeps the scripts and downloaded transcripts."

## Files Claude writes under `~/.claude-harness/`

`<module>.toml` — one per module:

```toml
[settings]            # real configuration read by scripts
my_email = "you@example.com"
state_dir = "C:/Users/<you>/.claude-harness/fireflies"
python = "C:/Python312/python.exe"

[placeholders]        # the text substituted into the module's skill and CLAUDE.md block
VAULT_PATH = "C:/Users/<you>/Documents/Vault"
CLIENT_TAGS = "`client/acme` `client/northwind`"
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

1. **Detect environment.** Report OS, Python version and path, Git, and whether `~/.claude` and `~/.claude/skills` exist (you will create them in step 6 if missing). Do not install anything.
2. **Choose modules.** List modules from `modules/*/MODULE.md` (skip `_template`) with their one-line summaries. Ask which the user wants. For each selection read `requires_modules`; if a required module is not selected (or installed per `installed.json`), explain why and offer to add it.
3. **Check prerequisites.** Compare each selected module's `prerequisites` and `python_packages` with step 1. List what is missing. Use the user's own Python by default (not a throwaway venv) because the user will run scripts such as key setup in their own terminal with the same interpreter. If they prefer a venv, record its interpreter as `python` in the module's settings and use it consistently.
4. **Interview.** Read the selected modules' `interview` files and ask all of their questions together in one round (skip questions already answered by an installed module's toml; reuse its placeholders). Do not fill in answers for the user. Hold the answers; do not write files yet.
5. **Show the plan and get approval.** Present, per module: packages to install, files to create, skills to copy to `~/.claude/skills`, templates, CLAUDE.md blocks to append (and which CLAUDE.md file), the text you generated for each placeholder that shapes output (for example the "What to produce" section of a skill, so the user can correct it), and secrets the module needs (names only). List scheduled tasks and settings edits as separate opt-ins. Wait for approval.
6. **Execute** only the approved steps:
   - Create `~/.claude/skills` if missing. Write `~/.claude-harness/<module>.toml`.
   - Fill every `{{PLACEHOLDER}}` from `[placeholders]` before copying anything, using `python core/tools/fill_placeholders.py <template> <toml> <output>` when Python is available (otherwise by hand). Never copy a file that still contains `{{...}}`.
   - Copy `templates/` files and scripts where the module's `MODULE.md` says. If a module declares `secrets`, also copy `core/secrets/harness_secrets.py` into the same folder as its scripts and `requirements.txt` into the state folder.
   - If folders from the default set were renamed, added, or dropped, edit the skill's folder table, routing rules, and CLAUDE.md block consistently.
   - Install packages with the recorded Python: `<python> -m pip install -r requirements.txt`.
7. **File checks.** Run the file checks section of each module's `verify`. If a module needs a secret, **stop and give the user the exact command for their shell** (for example, PowerShell: `cd $HOME\.claude-harness\fireflies; <python> harness_secrets.py set fireflies_api_key`, using the same Python recorded in settings). Wait until they confirm it is stored, then run the checks that need it. Report pass/fail honestly; never claim success on a failed check.
8. **Record.** Write or update `~/.claude-harness/installed.json`.
9. **Restart and behavior checks.** Tell the user to start a new Claude Code session (skills and CLAUDE.md load at session start), run the behavior checks in each module's `verify`, and point them to each module's "How to remove it" section.

## Adding a module later

Re-run this file. Read `installed.json`, skip installed modules, reuse existing `[placeholders]`, and run steps 2-9 for the new one.
