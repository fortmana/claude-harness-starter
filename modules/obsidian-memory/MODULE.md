---
name: obsidian-memory
version: 0.1.0
status: alpha
summary: An Obsidian vault Claude writes to, tags, files, and retrieves from consistently
requires_modules: []
prerequisites: [python>=3.11]
python_packages: []
secrets: []
installs:
  skills: [obsidian-note-router]
  claude_md_blocks: [obsidian-memory.md]
  templates: [meeting.md, decision.md, reference.md, person.md, daily.md, action-item.md, note.md]
  scripts: []
  scheduled_tasks: []
interview: interview.md
defaults: defaults.toml
tailor: tailor.md
verify: verify.md
---

# obsidian-memory

## What it does

Sets up a vault folder skeleton, a note-router skill that classifies, tags, names, and files notes, and a CLAUDE.md block with capture and retrieval rules. Claude uses its built-in file tools afterward, so no MCP server or Node.js is needed; Python is used only by the setup helper scripts. Writes are autonomous: Claude reports the path and tags afterward and confirms only before overwriting or deleting a note.

Setup asks one question (where the vault lives) and uses defaults for everything else. Afterward Claude offers an optional conversation to tailor the vault: it shows the default structure and you say what to change.

Consistent frontmatter and tags written at capture time are what make retrieval reliable. There is no search index to build.

## What it changes on your machine

- Creates (if missing) the default vault folders, and the seven note templates in `80 - Templates`. Existing notes are never moved or modified.
- Copies one skill folder to `~/.claude/skills/obsidian-note-router/` with your vault path and the module defaults filled in.
- Appends one block to the CLAUDE.md file you choose (`~/.claude/CLAUDE.md` for all sessions, or a project CLAUDE.md), with your vault path filled in.
- Writes your vault path and defaults to `~/.claude-harness/obsidian-memory.toml`.

Nothing else changes. No scheduled tasks, settings edits, packages, or secrets.

## Setup notes

1. Install Obsidian from obsidian.md and create (or choose) a vault; open it once so Obsidian initializes it.
2. Ask the base question in `interview.md` (vault location); take everything else from `defaults.toml`.
3. Show the user the install plan and wait for approval (BOOTSTRAP step 5). Nothing is written before this.
4. After approval: fill the `{{PLACEHOLDERS}}`, create any missing vault folders, copy templates from `templates/` into `80 - Templates`, copy the skill, and append the CLAUDE.md block. The default folders are `00 - Inbox`, `10 - Clients`, `20 - Internal`, `30 - Projects`, `40 - Reference`, `50 - Meetings`, `60 - People`, `70 - Daily Notes`, `80 - Templates`, `99 - Archive`.
5. Recommend a backup: the Obsidian Git plugin or a Git repo in the vault folder, since Claude can edit many files at once.
6. Run `verify.md` in a new session, then offer the optional tailoring conversation (`tailor.md`).

Optional extras (do not install unless asked): Obsidian Git, Dataview, and the Local REST API plugin (only needed for backlink-safe moves and live-app operations; not required for this module).

If the vault is in a cloud-sync folder, keep every search scoped to a subfolder; recursive scans from a sync root can force cloud-only files to download.

## Settings other modules depend on

- `fireflies` writes meeting notes into `50 - Meetings` and transcripts into `50 - Meetings/Transcripts`. If you rename or drop `50 - Meetings`, update the `fireflies` placeholders `NOTES_FOLDER` and `RAW_TRANSCRIPT_RULE` (see `tailor.md` step 3).

## How to remove it

1. Delete `~/.claude/skills/obsidian-note-router/`.
2. Remove the `## Obsidian Vault` block from the CLAUDE.md file it was added to.
3. Delete `~/.claude-harness/obsidian-memory.toml` and the `obsidian-memory` entry in `~/.claude-harness/installed.json`.
4. Your vault, notes, and templates are left untouched; delete them yourself if you want them gone.
