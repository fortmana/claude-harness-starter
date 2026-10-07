---
name: example-module
version: 0.1.0
status: planned            # planned | alpha | stable
summary: One sentence on what this module gives the user
requires_modules: []       # modules that must be present, e.g. [obsidian-memory]
prerequisites: []          # system-level, e.g. [python>=3.10, git]
python_packages: []        # installed from this module's requirements.txt
secrets: []                # names only, never values, e.g. [example_api_key]
installs:
  skills: []               # folders under this module's skills/ copied to ~/.claude/skills
  claude_md_blocks: []     # files under this module's claude-md/ appended on opt-in
  scripts: []              # files under this module's scripts/
  scheduled_tasks: []      # always requires explicit opt-in
interview: interview.md    # questions that parameterize the module (or omit)
verify: verify.md          # steps proving it works
---

# example-module

## What it does

Plain-language description for the user.

## What it changes on your machine

List every file created, package installed, settings edit, and scheduled task. Nothing may change the machine that is not listed here.

## Setup notes

Anything Claude or the user needs beyond the manifest (for example, where to retrieve a key on the provider's website).

## How to remove it

Exact steps to uninstall: delete skills, remove CLAUDE.md block, unregister tasks, delete the keyring entry, remove local config.
