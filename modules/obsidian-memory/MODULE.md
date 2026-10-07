---
name: obsidian-memory
version: 0.0.1
status: planned
summary: An Obsidian vault Claude writes to, tags, files, and retrieves from consistently
requires_modules: []
prerequisites: []
python_packages: []
secrets: []
installs:
  skills: [obsidian-note-router]
  claude_md_blocks: [obsidian-memory.md]
  scripts: []
  scheduled_tasks: []
---

# obsidian-memory

## What it does

Sets up a vault folder skeleton, a note-router skill that classifies, tags, names, and files notes, and a CLAUDE.md block with capture and retrieval rules. Claude uses its built-in file tools, so no MCP server or Node.js is required. Writes are autonomous; Claude reports the path and tags afterward and confirms only before overwriting or deleting a note.

## What it changes on your machine

To be completed when the module is built: vault folders and templates, one skill folder in `~/.claude/skills`, and one appended CLAUDE.md block.

## Setup notes

Content source: the v2.0 Obsidian + Claude Memory Setup Guide. Interview covers vault path, clients and projects, tools and topics, and sensitivity rules.

## How to remove it

To be completed when the module is built.
