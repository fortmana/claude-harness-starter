---
name: fireflies
version: 0.1.0
status: alpha
summary: Poll Fireflies transcripts and turn them into standardized notes that match what matters to you
requires_modules: [obsidian-memory]
prerequisites: [python>=3.11]
python_packages: [requests, keyring]
secrets: [fireflies_api_key]
installs:
  skills: [meeting-review]
  claude_md_blocks: [fireflies.md]
  templates: []
  scripts: [poll.py, schedule_windows.ps1]
  scheduled_tasks: [ClaudeHarness-FirefliesPoll]
interview: interview.md
verify: verify.md
---

# fireflies

## What it does

Polls the Fireflies API for new transcripts, saves each locally as a JSON package, and processes them through a `meeting-review` skill whose output is generated from **your** answers to a short interview: meeting types, what you need from each meeting (decisions, action items, risks, and so on), date and name handling, where notes go, and what to skip. Processing runs inside Claude Code, so no separate Anthropic API key is needed.

## What it changes on your machine

- Creates a state folder (default `~/.claude-harness/fireflies/`) containing `poll.py`, `harness_secrets.py`, `pending/`, `processed/`, `last_run.json`, `excluded_ids.json`, and `poll.log`.
- Writes `~/.claude-harness/fireflies.toml` with your interview settings (no secrets).
- Installs Python packages from `requirements.txt` (`requests`, `keyring`).
- Copies one skill folder to `~/.claude/skills/meeting-review/` with your answers filled in.
- Appends one block to the CLAUDE.md file you choose.
- Stores your API key in the OS credential store under service `claude-harness`, name `fireflies_api_key`. You do this yourself; see below.
- **Opt-in only:** a Windows scheduled task `ClaudeHarness-FirefliesPoll` that runs `poll.py` on an interval. Not created unless you say yes.

## Setup notes

**Getting and storing your API key (never paste it into Claude)**

1. Sign in at app.fireflies.ai, open **Settings**, then the **MCP & API** screen, and copy your API key.
2. In **your own terminal** (not through Claude), run: `python harness_secrets.py set fireflies_api_key` from the state folder, and paste the key at the hidden prompt.
3. If you pasted the key anywhere else (a chat, a file), generate a new key in Fireflies and update the stored one.

BOOTSTRAP copies `core/secrets/harness_secrets.py` into the state folder next to `poll.py` because the module declares a secret.

**Whose meetings does it fetch?** The Fireflies API can return transcripts from meetings you did not attend. Set `my_email` in the interview so only meetings you organized or attended are kept. Use `python poll.py --exclude <id>` to permanently skip any transcript. Use `python poll.py --dry-run` to see what would be fetched.

**Sensitive content.** Transcripts may contain client-confidential or regulated data. Check your organization's policy before processing them, and keep outputs in locations you are approved to use.

**Scheduling (optional).**
- Windows: `schedule_windows.ps1 -ScriptDir <state folder> -IntervalMinutes 60`. Remove with `-Remove`.
- macOS/Linux: add a cron entry such as `0 * * * * /usr/bin/python3 ~/.claude-harness/fireflies/poll.py` (or a launchd job). Cron jobs cannot always reach the keyring; if so, set `FIREFLIES_API_KEY` in the job's environment through your OS's secure mechanism instead of a plain file.
- Only polling is scheduled. Run "process my meetings" in a Claude Code session to turn pending transcripts into notes.
- Unattended processing with `claude -p` is possible but out of scope for v0.1; it requires granting write permissions to a headless session, so treat it as an advanced, explicit opt-in.

## How to remove it

1. If scheduled: `schedule_windows.ps1 -Remove` (Windows) or delete the cron/launchd entry.
2. Delete the secret: `python harness_secrets.py delete fireflies_api_key`.
3. Delete `~/.claude/skills/meeting-review/` and the `## Fireflies Meetings` block from the CLAUDE.md it was added to.
4. Delete the state folder and `~/.claude-harness/fireflies.toml`, and remove the `fireflies` entry from `~/.claude-harness/installed.json`.
5. Notes already written to your vault are left untouched.
