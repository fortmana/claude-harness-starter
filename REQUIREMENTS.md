# Requirements

What you need before running `BOOTSTRAP.md`, and what each module adds. Windows is the tested platform.

## Before you start (once per machine)

| Need | Why | Check it | If missing |
|---|---|---|---|
| **Claude Code** (Claude Desktop's Code tab, the CLI, or an IDE extension), signed in | Runs the setup | You can start a Code session in a folder | Install from claude.ai/download |
| **Git for Windows** | Claude Desktop's Code tab on Windows requires it, and it is how you clone this repo | In PowerShell: `git --version` | See "Installing Git" |
| **Python 3.11 or newer** (install the latest, currently 3.13) | Fireflies scripts, key storage, repo tools. Not needed for `obsidian-memory` alone | In PowerShell: `python --version` | See "Installing Python" |
| **Obsidian** (free) | Opens and browses the vault; Claude writes the files directly | Launch it | Install from obsidian.md (or your company portal) |
| **Access to this repo** | It is private while under review | You can open it on GitHub | Ask the maintainer |

Node.js is **not** required. No MCP server is used.

### Installing Git

If your company uses ManageEngine Endpoint Central:

1. Right-click the **Endpoint Central icon in the system tray** (bottom right, near the clock; you may need to click the `^` to show hidden icons).
2. Choose **Self Service Portal**.
3. Find **Git** (Git for Windows) and click **Install**. Accept the default options.
4. **Fully quit and reopen Claude Desktop** so it sees Git.
5. Verify in a new PowerShell window: `git --version`.

Otherwise download Git for Windows from git-scm.com and accept the defaults (keep "Git from the command line and also from 3rd-party software" selected).

### Installing Python

1. Open the **Microsoft Store**, search for **Python 3.13** (the latest version published by the Python Software Foundation), and click **Get**.
2. Close and reopen PowerShell, then verify: `python --version` (should print 3.13.x).
3. Verify pip works: `python -m pip --version`.

If typing `python` opens the Microsoft Store instead of printing a version, Python is not installed yet; complete step 1. Always run pip as `python -m pip ...` so packages go to the same Python you run scripts with.

If the Store is blocked on your machine, ask IT or install the latest Python from python.org, checking **Add python.exe to PATH**.

## What each module needs

| Module | Prerequisites | Packages (installed by BOOTSTRAP) | Secrets |
|---|---|---|---|
| `obsidian-memory` | None beyond the table above | None | None |
| `fireflies` | Python 3.11+, `obsidian-memory` | `requests`, `keyring` (see `modules/fireflies/requirements.txt`) | `fireflies_api_key`, which you store yourself |

Maintainers only: `pip install -r tools/requirements.txt` (`pyyaml`) to run `tools/validate_manifests.py`.

## Fireflies API key

Sign in at app.fireflies.ai, open **Settings**, then **MCP & API**, and copy your API key. Store it in your own terminal with the command Claude gives you during setup. **Never paste it into Claude.** See `SECURITY.md`.

## Accounts and policy

- A Claude plan that includes Claude Code.
- A Fireflies account whose meetings you are allowed to process. Transcripts can contain client-confidential or regulated data; check your organization's policy first.
