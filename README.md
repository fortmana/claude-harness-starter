# Claude Harness Starter

Opt-in starter modules for getting useful Claude Code setups running quickly. Pick the pieces you want; nothing installs by default.

## Quick start

1. Check [REQUIREMENTS.md](REQUIREMENTS.md): you need Claude Code (signed in) and Git; modules like `fireflies` also need Python 3.11+. It includes step-by-step install instructions for Git and Python.
2. Clone this repo (or download it as a ZIP) and open that folder in Claude Code (in Claude Desktop, use the Code tab).
3. Tell Claude: **"Follow BOOTSTRAP.md."**

See [docs/example-session.md](docs/example-session.md) for what the conversation looks like.

Claude asks which modules you want, interviews you once, shows exactly what it will change, and only then installs them. Some modules depend on others (for example `fireflies` writes into the `obsidian-memory` vault); Claude will offer to add what is needed.

## Modules

| Module | What it gives you | Status |
|---|---|---|
| [`obsidian-memory`](modules/obsidian-memory/MODULE.md) | An Obsidian vault Claude writes to, tags, files, and retrieves from consistently | Alpha |
| [`fireflies`](modules/fireflies/MODULE.md) | Poll Fireflies transcripts and turn them into standardized notes that match what matters to you | Alpha |

More modules will be added over time. Each is self-contained, documents what it changes on your machine, and explains how to remove it.

## How it works

- Every module has a `MODULE.md` manifest listing prerequisites, packages, secrets, and what it installs. See [`modules/_template/MODULE.md`](modules/_template/MODULE.md).
- `BOOTSTRAP.md` is written for Claude to execute and for you to read.
- Shared building blocks (secrets handling, conventions) live in `core/`.

## Security

API keys never go into Claude. See [SECURITY.md](SECURITY.md) before setting up any module that uses one.

## Contributing / maintaining

Run `pip install -r tools/requirements.txt`, then `python tools/validate_manifests.py` and `python tools/check_generic.py` before committing. The repo must contain no personal, client, or company-specific values.
