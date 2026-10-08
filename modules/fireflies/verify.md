# fireflies — verify

Report pass/fail honestly.

## File checks (run right after install, before restarting)

1. `poll.py` and `harness_secrets.py` exist in the state directory, `pending/` and `processed/` exist, and `<python> -c "import requests, keyring"` succeeds (using the interpreter recorded in `fireflies.toml`; ignore harmless library warnings).
2. `~/.claude-harness/fireflies.toml` exists and `my_email` is set (warn if not).
3. `~/.claude/skills/meeting-review/SKILL.md` exists with no unreplaced `{{...}}` placeholders.
4. The CLAUDE.md block was added, has no unreplaced placeholders, and has exactly one `<!-- claude-harness:fireflies:start -->` / `<!-- claude-harness:fireflies:end -->` pair.
5. **Key stored.** Pause until the user confirms they stored the key themselves (see `MODULE.md`). If they have no key yet, skip checks 5 and 6 and the key-related security check, tell them to run those once the key is stored, and continue with the behavior checks. Otherwise confirm it exists without printing it: `<python> harness_secrets.py check fireflies_api_key`.
6. Dry run against the real API (safe, saves nothing): `python poll.py --dry-run`. Pass = it lists meetings or reports zero without an error. A 401 means the key is wrong; tell the user to re-run `harness_secrets.py set` themselves.

## Behavior checks (after the user starts a new Claude Code session)

The skill and CLAUDE.md block only load in a new session. No API key is needed for this test.

1. Copy `samples/sample_transcript.json` into `<state_dir>/pending/`.
2. Ask: "Process my pending meetings."
3. Expected: a note appears in the configured folder with the configured sections, the correct action items (Priya chases the vendor, due the Friday of that week; Sam drafts the checklist, due the following Wednesday), one decision (keep the current reporting tool for phase one), and one parked item (training budget). The package moves to `processed/`. Claude reports the path without asking approval.
4. Delete the sample note and the processed sample package afterward. (Changing the note's structure is the optional tailoring step in `tailor.md`, not part of this check.)

## Security checks

- The API key does not appear in any file under the state directory, the skill, CLAUDE.md, or the shell history Claude can see.
- `poll.log` contains transcript IDs and titles only.
