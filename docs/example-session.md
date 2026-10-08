# Example session: first-time setup of both modules

> **Provenance.** This is the transcript of a sandboxed run of `BOOTSTRAP.md` (repo commit `3e1a743`) by a fresh Claude Code session with no other context, answering as a scripted user. Python was simulated as "not installed" until the scripted user "installed" it, Git was already present, and the Fireflies key step was simulated (no real key was stored or used and no API call was made). Tool output is summarized in italics and real paths are replaced with `<you>`. After this run, the maintainers fixed a few small things, so today's wording differs slightly (for example, Claude now asks you to choose modules before it stops for Python, and the sample meeting is previewed as a client meeting so every section shows).
>
> Scenario: a Windows user on Claude Desktop (Code tab), signed in, without Python, who installs both `obsidian-memory` and `fireflies`. Git is installed first (see `REQUIREMENTS.md`, "Installing Git"), because the Code tab needs it before a session can start.

**Legend:** **You** = the user. **Claude** = Claude Code. *Italics* = what happens behind the scenes.

---

**You:** Follow BOOTSTRAP.md.

**Claude:** I'll check what's on this machine first. I won't install or change anything yet.

*(reads BOOTSTRAP.md, REQUIREMENTS.md, README.md; runs `git --version`: 2.x; runs `python --version`: not found; checks `~/.claude`: not present)*

- OS: Windows 11
- Git: installed
- Python: **not installed** (typing `python` just points at the Microsoft Store)
- `~/.claude` and `~/.claude/skills`: don't exist yet. I'll create them after you approve a plan.

Fireflies needs Python 3.11 or newer, and I can't install it for you. Here's what to do:

1. Open the **Microsoft Store**, search for **Python 3.13** (published by the Python Software Foundation), and click **Get**.
2. Close and reopen PowerShell, then run `python --version`. It should print 3.13.x.
3. Run `python -m pip --version` to confirm pip works.

If the Store is blocked, ask IT, or install the latest Python from python.org and tick **Add python.exe to PATH**. Tell me when it's done and I'll re-check.

*You install Python from the Microsoft Store.*

**You:** Python's installed.

**Claude:** *(re-runs detection: Python 3.13.x, interpreter path recorded, pip works)* Python 3.13 is there, and I'll use it from here on. Which of these do you want?

- `obsidian-memory`: an Obsidian vault Claude writes to, tags, files, and searches the same way every time.
- `fireflies`: pulls your Fireflies transcripts and turns them into standard meeting notes. It needs `obsidian-memory`.

**You:** both

**Claude:** Good. Fireflies files into the vault, so both are in. Python is fine. After you approve I'll install two small packages (`requests`, `keyring`). Two quick questions, and I'll use sensible defaults for everything else:

1. Where should your Obsidian vault live? If you have one, give me the path. Otherwise I'd suggest `~/Documents/Vault`.
2. What email is your Fireflies account under? I use it to keep only meetings you organized or attended.

**You:** Vault's at `C:/Users/<you>/Documents/Vault`. Email is jordan.lee@example.com

**Claude:** Here's the plan. Nothing has been written yet.

*obsidian-memory*
- Creates the 10 vault folders (Inbox, Clients, Internal, Projects, Reference, Meetings, People, Daily Notes, Templates, Archive) in your vault.
- Copies 7 note templates into `80 - Templates`.
- Copies the `obsidian-note-router` skill to `~/.claude/skills`.
- Appends an "Obsidian Vault" block to `~/.claude/CLAUDE.md`. That's the file for all your sessions, and I can use a different one if you prefer.
- Writes `~/.claude-harness/obsidian-memory.toml`.
- No secrets.

*fireflies*
- Creates the state folder `~/.claude-harness/fireflies`. That's where Claude keeps the scripts and downloaded transcripts.
- Copies `poll.py` and the key helper into it.
- Installs `requests` and `keyring` with the Python above.
- Copies the `meeting-review` skill to `~/.claude/skills`.
- Appends a "Fireflies Meetings" block to the same CLAUDE.md.
- Writes `fireflies.toml`.
- Needs one secret, `fireflies_api_key`. You'll store it yourself in your own terminal; it never comes through this chat.

*Default meeting notes:* a 3-sentence summary, decisions, action items, risks for client meetings, and a parking lot. You can reshape this after setup.

*Opt-in extras, off unless you say yes:* scheduled hourly polling (a Windows scheduled task) and any Claude settings changes. Okay to go ahead, and do you want scheduled polling?

**You:** Looks good, go ahead. No scheduled polling.

**Claude:** Installing now.

*(creates the folders; writes both toml files; fills the two skills and two CLAUDE.md blocks; creates the vault folders and templates; copies `poll.py`, `harness_secrets.py` and `requirements.txt`; pip installs the packages; writes `installed.json`)*

File checks:
- State folder has `poll.py` and `harness_secrets.py`, and the `requests` and `keyring` imports work: pass
- `fireflies.toml` has your email: pass
- Both skills and CLAUDE.md have no leftover `{{...}}`: pass
- Vault folders and 7 templates exist: pass

Now the key. Do this in your own terminal, not here. First get the key: sign in at app.fireflies.ai, then **Settings**, then **MCP & API**, and copy your API key. Then run this in PowerShell:

```powershell
cd $HOME\.claude-harness\fireflies; & "<your Python path>" harness_secrets.py set fireflies_api_key
```

Paste the key at the hidden prompt. If it ever lands in a chat or file, rotate it in Fireflies. Reply "Stored" when done.

*You run the command in your own terminal.*

**You:** Stored.

**Claude:** Thanks. *(runs `harness_secrets.py check fireflies_api_key`, then `poll.py --dry-run`, which lists meetings and saves nothing; these were not run in the sandbox because no real key existed)*

I've recorded the install. To finish, start a **new Claude Code session**, because skills and CLAUDE.md only load at session start. Then say "Process my pending meetings."

Want help tailoring your meeting summaries? I'll show you what the default looks like and you tell me what to change, or you can use it as is. How about your vault? Same offer for how it's organized.

**You:** Yes for the meeting summaries. No thanks to the vault, as is.

**Claude:** Sounds good. I've left the vault as is, and you can say "tailor my vault" any time. You have no real meetings yet, so I ran the meeting-review skill on a built-in sample meeting. This is only a preview and nothing is filed:

---

**Project Falcon weekly status**, 2026-03-10, 30m, Dana Reyes (organizer), Sam Ortiz, Priya Nair

**Summary**
The team reviewed the data migration: staging is loaded, but the production cutover is blocked until the vendor confirms a schema change. They agreed to keep the current reporting tool for phase one and to park the training budget until next month's planning meeting.

**Decisions**
- Decision: Keep the current reporting tool for phase one; revisit in phase two.

**Action items**
- Priya Nair — Chase the vendor for schema-change confirmation and update the thread — 2026-03-13 ("by Friday")
- Sam Ortiz — Draft the production cutover checklist — 2026-03-18 ("next Wednesday")

**Parking lot**
- Training budget (not yet approved); revisit at next month's planning meeting.

---

That's a short summary, decisions, who owes what and by when, and anything deferred. Risks only show for client meetings. What would you change?

**You:** hmm, it's okay

**Claude:** A few things people often change:
- add something, like a "follow-ups for just me" list, open questions, or a draft follow-up email
- cut something you won't use
- make the summary shorter or more bullet-like

Does any of that sound right?

**You:** drop the risks section completely, add a 'follow-ups for me' section at the top with just my action items, and shorten the summary to two sentences

**Claude:** Here's the same meeting with those changes. The sample has no one named Jordan, so your section is empty here:

---

**Project Falcon weekly status**, 2026-03-10

**Follow-ups for me**
Nothing for you.

**Summary**
Staging is loaded, but the production cutover is blocked until the vendor confirms a schema change. The team kept the current reporting tool for phase one and parked the training budget.

**Decisions**
- Decision: Keep the current reporting tool for phase one; revisit in phase two.

**Action items**
- Priya Nair — Chase the vendor for schema-change confirmation and update the thread — 2026-03-13 ("by Friday")
- Sam Ortiz — Draft the production cutover checklist — 2026-03-18 ("next Wednesday")

**Parking lot**
- Training budget (not yet approved); revisit at next month's planning meeting.

---

**You:** perfect

**Claude:** Saving that. *(updates the summary-structure and style settings in `fireflies.toml`; re-fills and replaces the installed skill; reads it back to confirm; no leftover placeholders)*

Your summaries now have a "Follow-ups for me" section at the top, a two-sentence summary, and no risks section. It applies from your next new session.

You're set up. Start a new Claude Code session and say "Process my pending meetings" once Fireflies has meetings for you. You can say "tailor my meeting summaries" or "tailor my vault" any time. To remove either module, see "How to remove it" in its `MODULE.md`.
