# obsidian-memory — verify

Report pass/fail honestly for each.

## File checks (run right after install, before restarting)

1. The vault path exists and contains the default folders, including `00 - Inbox` and `80 - Templates`.
2. `80 - Templates` contains `meeting.md`, `decision.md`, `reference.md`, `person.md`, `daily.md`, `action-item.md`, `note.md`.
3. `~/.claude/skills/obsidian-note-router/SKILL.md` exists and contains no unreplaced `{{...}}` placeholders.
4. The CLAUDE.md file that received the block contains the vault path and no unreplaced `{{...}}` placeholders.

## Behavior checks (after the user starts a new Claude Code session, so the skill and CLAUDE.md block are loaded)

| Test | Prompt | Expected |
|---|---|---|
| Capture | "Log this: met with <a client> today, agreed to move go-live to March. Send the contract by Friday." | Note filed under the client or an inbox note, correct frontmatter and tags, action item captured, path and tags reported, **no approval prompt** |
| Messy paste | Paste unstructured meeting notes: "clean this up and file it." | Structured meeting note from the template |
| Ambiguous | "Save this: check vendor pricing next week." | Filed to `00 - Inbox` with a reason and one follow-up question |
| Retrieval | "What did we decide about the go-live date?" | Finds the note by tag or folder, reads it, answers, cites the path |
| Safety | "Overwrite that note with ..." | Claude asks before overwriting |

Open the vault in Obsidian (reload with Ctrl+R / Cmd+R) and confirm the notes appear where Claude reported.
