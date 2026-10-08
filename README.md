# Claude Harness Starter

Opt-in modules that turn a plain Claude Code install into a setup that fits how you work. Pick the pieces you want; nothing installs by default.

## What is a "harness"?

Claude Code out of the box is a capable assistant with no memory of you. A **harness** is everything you add around it so it behaves consistently for your work:

| Layer | What it is | Example in this repo |
|---|---|---|
| **Skills** | Reusable instructions Claude follows when a task matches | `obsidian-note-router`, `meeting-review` |
| **CLAUDE.md** | Standing rules Claude reads at the start of every session | The "Obsidian Vault" and "Fireflies Meetings" blocks |
| **Memory** | A place Claude reads from and writes to between sessions | The Obsidian vault |
| **Scripts and schedules** | Code that fetches data or runs on a timer | The Fireflies poller |

Each module in this repo adds one useful capability and shows how these layers fit together. Start with one, use it for a week, then add the next. See [docs/concepts.md](docs/concepts.md) for a short explanation of each layer.

## Quick start

1. Check [REQUIREMENTS.md](REQUIREMENTS.md). You need Claude Code (signed in) and Git; modules like `fireflies` also need Python 3.11+. It has step-by-step install instructions for both.
2. Get this repo: clone it, or download it as a ZIP. The repo is private while under review, so if GitHub shows a 404, ask the maintainer for access first.
3. Open the folder in Claude Code (in Claude Desktop, use the Code tab).
4. Tell Claude: **"Follow BOOTSTRAP.md."**

You do not need to read `BOOTSTRAP.md`; it is the script Claude follows. [docs/example-session.md](docs/example-session.md) shows what the conversation looks like.

Claude asks which modules you want, asks a couple of short questions, shows exactly what it will change, and only then installs them. Some modules depend on others (for example `fireflies` writes into the `obsidian-memory` vault); Claude will offer to add what is needed.

**Platform:** Windows is the tested platform. macOS and Linux steps are included where they differ but have had less testing.

## Modules

| Module | What it gives you | Status |
|---|---|---|
| [`obsidian-memory`](modules/obsidian-memory/MODULE.md) | An Obsidian vault Claude writes to, tags, files, and retrieves from consistently | Alpha |
| [`fireflies`](modules/fireflies/MODULE.md) | Poll Fireflies transcripts and turn them into standardized notes that match what matters to you (needs `obsidian-memory`) | Alpha |

**Status meanings:** *planned* = designed, not installable yet. *alpha* = works end to end in testing; expect rough edges and changes. *stable* = used in practice; behavior will not change without a version bump.

Each module is self-contained, documents what it changes on your machine, and explains how to remove it. See [CONTRIBUTING.md](CONTRIBUTING.md) if you want to build your own.

## Where this goes next

A suggested order for growing your harness:

1. **Memory first** (`obsidian-memory`): Claude files and finds things the same way every time.
2. **Feed it data** (`fireflies`): something that produces notes automatically.
3. **Make it yours**: use the tailoring conversation each module offers, then write your own skills and CLAUDE.md rules.
4. **Build a module**: package a workflow you rely on so a colleague can install it the same way. [CONTRIBUTING.md](CONTRIBUTING.md) walks through it.

## How it works

- Every module has a `MODULE.md` manifest listing prerequisites, packages, secrets, and what it installs. See [`modules/_template/MODULE.md`](modules/_template/MODULE.md).
- `BOOTSTRAP.md` is written for Claude to execute.
- Shared building blocks (secrets handling, helper scripts) live in `core/`.
- Your own settings are written to `~/.claude-harness/`, never into this repo.
- To pick up a newer version of a module, see [CHANGELOG.md](CHANGELOG.md) and the "Updating a module" section of `BOOTSTRAP.md`.

## Security

API keys never go into Claude. See [SECURITY.md](SECURITY.md) before setting up any module that uses one.
