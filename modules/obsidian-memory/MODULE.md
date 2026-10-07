---
name: obsidian-memory
version: 0.1.0
status: alpha
summary: An Obsidian vault Claude writes to, tags, files, and retrieves from consistently
requires_modules: []
prerequisites: []
python_packages: []
secrets: []
installs:
  skills: [obsidian-note-router]
  claude_md_blocks: [obsidian-memory.md]
  templates: [meeting.md, decision.md, reference.md, person.md, daily.md, action-item.md, note.md]
  scripts: []
  scheduled_tasks: []
interview: interview.md
verify: verify.md
---

# obsidian-memory

## What it does

Sets up a vault folder skeleton, a note-router skill that classifies, tags, names, and files notes, and a CLAUDE.md block with capture and retrieval rules. Claude uses its built-in file tools, so no MCP server, Node.js, or Python is required. Writes are autonomous: Claude reports the path and tags afterward and confirms only before overwriting or deleting a note.

Consistent frontmatter and tags written at capture time are what make retrieval reliable. There is no search index to build.

## What it changes on your machine

- Creates (if missing) the vault folders chosen in the interview, and the seven note templates in `80 - Templates`. Existing notes are never moved or modified.
- Copies one skill folder to `~/.claude/skills/obsidian-note-router/` with your interview answers filled in.
- Appends one block to the CLAUDE.md file you choose (`~/.claude/CLAUDE.md` for all sessions, or a project CLAUDE.md), with your vault path filled in.
- Writes your interview answers to `~/.claude-harness/obsidian-memory.toml`.

Nothing else changes. No scheduled tasks, settings edits, packages, or secrets.

## Setup notes

1. Install Obsidian from obsidian.md and create (or choose) a vault; open it once so Obsidian initializes it.
2. Run the interview (`interview.md`). Fill the `{{PLACEHOLDERS}}` in the skill and CLAUDE.md block from the answers.
3. Create missing folders and copy templates from `templates/` into `80 - Templates`.
4. Show the user the install plan, then copy the skill and append the CLAUDE.md block.
5. Recommend a backup: the Obsidian Git plugin or a Git repo in the vault folder, since Claude can edit many files at once.
6. Run `verify.md` in a new session.

Optional extras (do not install unless asked): Obsidian Git, Dataview, and the Local REST API plugin (only needed for backlink-safe moves and live-app operations; not required for this module).

If the vault is in a cloud-sync folder, keep every search scoped to a subfolder; recursive scans from a sync root can force cloud-only files to download.

## How to remove it

1. Delete `~/.claude/skills/obsidian-note-router/`.
2. Remove the `## Obsidian Vault` block from the CLAUDE.md file it was added to.
3. Delete `~/.claude-harness/obsidian-memory.toml` and the `obsidian-memory` entry in `~/.claude-harness/installed.json`.
4. Your vault, notes, and templates are left untouched; delete them yourself if you want them gone.
