# Example session: first-time setup of both modules

> **Provenance.** This is the transcript of a sandboxed run of `BOOTSTRAP.md` (repo commit `25dd9b4`) by a fresh Claude Code session with no other context, answering as a scripted user. In the run, Python was simulated as "not installed" until the scripted user "installed" it, Git was already present, and the Fireflies key step and live API calls were simulated (no real key was stored or used). Tool output is summarized in italics, and real paths are replaced with `<you>`. After this run, the maintainers merged the two interviews into one de-duplicated round, added a "which CLAUDE.md?" question, and made a few smaller fixes, so today's wording differs slightly.
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

I need Python 3.11 or newer for what you're likely to want (the Fireflies module). I can't install it for you. Here's what to do (from `REQUIREMENTS.md`, "Installing Python"):

1. Open the **Microsoft Store**, search for **Python 3.13** (published by the Python Software Foundation), and click **Get**.
2. Close and reopen PowerShell, then run `python --version`. It should print 3.13.x.
3. Run `python -m pip --version` to confirm pip works.

If the Store is blocked on your machine, ask IT, or install the latest Python from python.org and tick **Add python.exe to PATH**. If typing `python` opens the Store, it isn't installed yet. Tell me when it's done and I'll re-check.

*You install Python from the Microsoft Store.*

**You:** Python's installed.

**Claude:** *(re-runs detection: Python 3.13.x, interpreter path recorded, pip works)* Python 3.13 is installed. I'll use it as your Python from here on; setup and the key step will both use the same one.

Which of these do you want?

| Module | What you get |
|---|---|
| `obsidian-memory` | An Obsidian vault that Claude writes to, tags, files, and searches the same way every time |
| `fireflies` | Pulls your Fireflies transcripts and turns them into notes shaped around what you care about (needs `obsidian-memory`) |

**You:** Both.

**Claude:** Good. Fireflies files into the vault, so both are in. Prerequisites: Python is fine. I'll need two small packages (`requests`, `keyring`) once you approve. Nothing else.

I'll ask everything in one round. Casual answers are fine. Nothing gets written until you approve a plan.

**Vault**
1. Where is (or should be) your Obsidian vault? A local folder outside OneDrive is best.
2. What clients or contexts do you work with? Short names are fine.
3. Any active projects to make folders for?
4. Which tools do your notes mention a lot?
5. What subjects would you want reusable how-to notes on?
6. What counts as sensitive in your work?
7. Default folders are `00 - Inbox`, `10 - Clients`, `20 - Internal`, `30 - Projects`, `40 - Reference`, `50 - Meetings`, `60 - People`, `70 - Daily Notes`, `80 - Templates`, `99 - Archive`. Want to rename, add, or drop any?
8. Do you already have notes in the vault?

**Meetings**
9. Your email (so I keep only meetings you organized or attended)?
10. How far back should the first fetch go? (Default 7 days.)
11. Any meetings to skip, by words in the title?
12. What kinds of meetings do you have, and what is each for? What should I do with meetings that fit none of them?
13. What do you want out of a meeting? Options: short summary, decisions, action items with owner and due date, risks, open questions, client commitments, attendance and participation, parking lot, key quotes, draft follow-up email, or something specific to your work. Say which apply to which meeting types.
14. When people say "EOW" or "next Wednesday", should I turn that into a real date?
15. How should I handle unknown speakers like "Speaker 1"? Any names or nicknames I should know?
16. Preferred style (terse bullets, short paragraphs)? Anything to avoid?
17. Where should meeting notes go, split by client or not? Keep the full raw transcript, and where?
18. Which client or tool tags should apply?
19. Do transcripts add anything to the sensitivity rules above?
20. Fetch transcripts manually or on a schedule? Process them in Claude sessions?
21. Which CLAUDE.md should get the instructions: `~/.claude/CLAUDE.md` (all sessions) or a project one?

**You:** I'm Jordan Lee, jordan.lee@example.com, healthcare finance consultant. Vault's at `C:/Users/<you>/Documents/Vault`, it's new. Clients are Acme Health and Northwind Clinics. One project, Denial Analytics for Acme. I use Python, Excel, Power BI. Reference topics: Denials, Excel tips, Python. Sensitive is anything with patient info or client financials. Default folders are fine, no existing notes. Meetings are client working sessions, internal team status, and 1:1s with my manager. Skip anything with "lunch" or "interview" in the title. I want a 3-sentence summary, decisions clearly labelled, action items with owner and due date, risks only for client working sessions, and a parking lot. Turn "EOW", "next Wednesday" etc. into real dates but keep what they said in quotes. Unknown speakers "Unidentified speaker", guesses marked "(inferred)". Terse bullets. Notes in 50 - Meetings/<Client or Internal>, raw transcripts in 50 - Meetings/Transcripts. Tags like client/acme. I'll fetch manually and process in Claude Code. Nothing extra for sensitivity. Put the CLAUDE.md block in the one for all sessions.

**Claude:** Thanks, Jordan. Here is the plan. Nothing has been changed yet.

**Module: obsidian-memory**
- Packages: none.
- Vault folders: the 10 default folders, plus `10 - Clients/Acme Health`, `10 - Clients/Northwind Clinics`, `30 - Projects/Denial Analytics`, `40 - Reference/{Denials, Excel tips, Python}`.
- 7 templates copied to `80 - Templates`: meeting, decision, reference, person, daily, action-item, note.
- Skill: `~/.claude/skills/obsidian-note-router/`, with your answers filled in.
- CLAUDE.md: an `## Obsidian Vault` block appended to `~/.claude/CLAUDE.md`.
- Config: `~/.claude-harness/obsidian-memory.toml`. Tags: `client/acme`, `client/northwind`, `tool/python`, `tool/excel`, `tool/powerbi`. Sensitivity rule: "Anything with patient information or client financials."
- Secrets: none.

**Module: fireflies**
- Packages: `requests`, `keyring`, installed with your Python.
- State folder (where Claude keeps the scripts and downloaded transcripts): `~/.claude-harness/fireflies/`, containing `poll.py`, `harness_secrets.py`, `requirements.txt`, `pending/`, `processed/`.
- Meeting-note folders: `50 - Meetings/{Acme Health, Northwind Clinics, Internal, Transcripts}`.
- Skill: `~/.claude/skills/meeting-review/`.
- CLAUDE.md: a `## Fireflies Meetings` block in the same file.
- Config: `~/.claude-harness/fireflies.toml` (your email, a 7-day first fetch, skip words "lunch" and "interview"). `~/.claude-harness/installed.json` records both modules.
- Secret needed (name only): `fireflies_api_key`. You store it yourself in your own terminal. I never see it.
- Meetings that match none of your three types are filed under Internal and labelled "General". Say so if you'd rather something else.

**What each meeting note will contain (please correct this):**

Meeting types:
- Client working session: a client name in the title or client attendees.
- Internal team status: internal attendees only, "status" or "standup" in the title.
- 1:1 with manager: two attendees, "1:1" in the title.
- General: anything else.

Sections, in this order:
1. **Summary:** exactly 3 sentences.
2. **Decisions:** each bullet starts with `Decision:`. Empty case: "No decisions recorded."
3. **Action items:** `- [Owner] — [Action] — [Due]`. Empty case: "No action items recorded."
4. **Risks:** client working sessions only, otherwise omitted. Empty case: "No risks raised."
5. **Parking lot:** deferred topics. Empty case: "Nothing parked."

Rules:
- **Dates:** relative phrases become `YYYY-MM-DD` anchored to the meeting date, with your phrase kept in quotes, for example 2026-03-13 ("EOW"). "EOW" or "by Friday" means that week's Friday. "next Wednesday" means that weekday in the following Monday-to-Sunday week. If a date is unclear, I write "date unclear — confirm".
- **People:** unknown speakers are "Unidentified speaker"; guesses are marked "(inferred)".
- **Style:** terse bullets, no filler.
- **Skip:** titles containing "lunch" or "interview".
- **Tags:** `client/acme` or `client/northwind` when recognised, otherwise `client/internal`, plus any `tool/` tags that apply.

**Separate opt-ins (not included unless you say yes):**
- Scheduled polling (a Windows scheduled task). Do you want it?
- Claude Code settings edits or secret-file deny rules.

Without scheduling, you run the poll by hand and then ask me to "process my meetings". Approve this plan?

**You:** Looks good. No to scheduled polling. Go ahead.

**Claude:** Installing now, nothing scheduled.

*(creates `~/.claude/skills` and `~/.claude-harness`; writes both toml files; fills each skill and CLAUDE.md block with `fill_placeholders.py`, all succeeded; creates the vault folders; copies the templates, `poll.py`, `harness_secrets.py` and `requirements.txt`; appends both blocks to `~/.claude/CLAUDE.md`; pip installs `requests` and `keyring`; writes `installed.json`)*

File checks:
- obsidian-memory: all 4 passed. The vault folders exist, all 7 templates are present, and the skill and CLAUDE.md block have no unfilled placeholders and contain the vault path.
- fireflies: checks 1-4 passed. `poll.py` and `harness_secrets.py` are in the state folder, `requests` and `keyring` import, `my_email` is set, and the skill and block are clean.
- fireflies check 5 needs your key, so I'm stopping here.

**Storing your Fireflies key (do this yourself; never paste it into this chat):**
1. Sign in at app.fireflies.ai, go to **Settings**, then **MCP & API**, and copy your API key.
2. Open **PowerShell** yourself and run this, which uses the same Python I recorded:
   ```powershell
   cd $HOME\.claude-harness\fireflies; & "<your Python path>" harness_secrets.py set fireflies_api_key
   ```
3. Paste the key at the hidden prompt and press Enter. Nothing shows as you paste.
4. If you pasted the key anywhere else (a chat or a file), generate a new one in Fireflies and store that instead.

Tell me when it's stored.

*You run the command in your own terminal.*

**You:** Stored.

**Claude:** Thanks. *(runs `harness_secrets.py check fireflies_api_key`, then `poll.py --dry-run`, which lists meetings and saves nothing; in this sandbox run the key checks were not run because no key existed)*

Setup is done. Recorded in `installed.json`: obsidian-memory 0.1.0 and fireflies 0.1.0.

**Next steps:**
1. Start a **new Claude Code session**. Skills and CLAUDE.md only load at session start.
2. Try these:
   - "Log this: met with Acme today, agreed to move go-live to March. Send the contract by Friday."
   - Paste messy notes and say "clean this up and file it".
   - "Save this: check vendor pricing next week." (It should land in the Inbox with a question.)
   - "What did we decide about the go-live date?"
   - Ask me to "overwrite that note with ..." and check that I ask first.
   - For Fireflies: run `python poll.py` from the state folder, then say "process my meetings".
3. Open the vault in Obsidian and reload with Ctrl+R.
4. Back the vault up with the Obsidian Git plugin or a Git repo in the vault folder, since Claude can edit many files at once.
5. Don't scan OneDrive or a sync folder recursively. Keep any search inside one vault subfolder.

**To remove things:**
- obsidian-memory: delete `~/.claude/skills/obsidian-note-router/`, remove the `## Obsidian Vault` block from `~/.claude/CLAUDE.md`, and delete `obsidian-memory.toml` and its entry in `installed.json`. Your vault is left untouched.
- fireflies: run `harness_secrets.py delete fireflies_api_key`, delete `~/.claude/skills/meeting-review/`, remove the `## Fireflies Meetings` block, and delete the state folder, `fireflies.toml`, and its entry in `installed.json`.

---

## In the new session (behavior check on the sample transcript)

**You:** Process my pending meetings.

*(A sample transcript is waiting in `pending/`.)*

**Claude:** Processed 1 meeting. One decision, two action items, one parked item. Written to `50 - Meetings/Internal/2026-03-10 Project Falcon weekly status.md`; raw transcript saved to `50 - Meetings/Transcripts/`; package archived to `processed/`. Is there anything you'd add, cut, or reformat in the note?

The note it wrote (internal status meeting, so no Risks section):

```markdown
---
date: 2026-03-10
type: meeting
meeting_type: Internal team status
client: internal
project:
meeting_title: Project Falcon weekly status
organizer: organizer@example.com
duration: 0h 30m
participants: Dana Reyes, Sam Ortiz, Priya Nair
source: fireflies
transcript_id: sample-0001
tags: [type/meeting, source/meeting-transcript, client/internal, status/active]
---

# Project Falcon weekly status — 2026-03-10

Transcript: [[2026-03-10 Project Falcon weekly status - Transcript]]

## Summary
The team reviewed the data migration: the staging load is finished, but the production cutover is blocked until the vendor confirms the schema change. Priya will chase the vendor, and the group agreed to keep the current reporting tool for phase one. Training budget approval is parked, and Sam will draft the cutover checklist.

## Decisions
- Decision: keep the current reporting tool for phase one; revisit in phase two.

## Action items
- Priya Nair — Chase vendor for schema-change confirmation (email today, update thread) — 2026-03-13 ("end of week", "by Friday")
- Sam Ortiz — Draft cutover checklist — 2026-03-18 ("next Wednesday")

## Parking lot
- Training budget (not yet approved) — revisit at next month's planning meeting; date unclear — confirm
```
