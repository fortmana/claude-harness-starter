---
name: fireflies
version: 0.0.1
status: planned
summary: Poll Fireflies transcripts and turn them into standardized notes that match what matters to you
requires_modules: [obsidian-memory]
prerequisites: [python>=3.10]
python_packages: [requests, keyring]
secrets: [fireflies_api_key]
installs:
  skills: [meeting-review]
  claude_md_blocks: [fireflies.md]
  scripts: [poll.py]
  scheduled_tasks: [fireflies-poll]
---

# fireflies

## What it does

Polls the Fireflies API for new transcripts, saves them locally, and processes them through a meeting-review skill that is generated from your answers to a short interview (meeting types, what you need out of each meeting, formatting, destination, and what to skip). Processing runs through Claude Code, so no separate Anthropic API key is needed.

## What it changes on your machine

To be completed when the module is built: poll script and local state folders, one skill folder in `~/.claude/skills`, one CLAUDE.md block, and (opt-in) one scheduled task. Your API key is stored only in the OS credential store.

## Setup notes

Get your API key at app.fireflies.ai, then Settings, then MCP & API. Store it by running `python harness_secrets.py set fireflies_api_key` in your own terminal. Never paste it into Claude.

Known caveat: the API key may return transcripts beyond your own meetings. The module ships an exclusion list, and you should review what it pulls. Check your organization's policy before processing client-confidential or regulated content.

## How to remove it

To be completed when the module is built.
