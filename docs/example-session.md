# Example session: first-time setup of both modules

> **Illustrative.** This walkthrough is written from the current `BOOTSTRAP.md`, `REQUIREMENTS.md`, and module files to show what the conversation looks like. It is not a captured log, so exact wording, tool output, and version numbers will differ. Scenario: a Windows user on Claude Desktop (Code tab) with Claude signed in, but without Git or Python installed, who installs both `obsidian-memory` and `fireflies`.

**Legend:** **You** = the user. **Claude** = Claude Code. *Italic notes* = what is happening behind the scenes.

---

## Before the session: Git

You open Claude Desktop, switch to the **Code** tab, and choose the repo folder. Claude Desktop tells you Git for Windows is required. You follow `REQUIREMENTS.md` > *Installing Git*:

1. Right-click the Endpoint Central icon in the system tray, choose **Self Service Portal**, and install **Git**.
2. Fully quit and reopen Claude Desktop.
3. Reopen the Code tab on the repo folder.

---

## The session

**You:** Follow BOOTSTRAP.md.

**Claude:** I'll check what's on this machine first. I won't install or change anything yet.

*Claude runs `git --version` and `python --version`.*

**Claude:**
- Git: 2.x installed
- Python: **not installed** (running `python` opens the Microsoft Store)
- `~/.claude/skills`: not present yet (I'll create it later)

The `fireflies` module needs Python 3.11 or newer, so I need you to install it before I go on. I can't do that for you. Here's what to do (from `REQUIREMENTS.md`):

1. Open the **Microsoft Store**, search for **Python 3.13**, and click **Get**.
2. Close and reopen PowerShell, then run `python --version`. It should print 3.13.x.
3. Run `python -m pip --version` to confirm pip works.

Tell me when that's done and I'll re-check.

*You install Python from the Store.*

**You:** Python's installed.

**Claude:** *(re-runs detection)* Python 3.13.x at `C:/Users/<you>/AppData/Local/Microsoft/WindowsApps/...`. pip works. Ready.

Which modules do you want?

| Module | What you get |
|---|---|
| `obsidian-memory` | An Obsidian vault Claude writes to, tags, files, and retrieves from consistently |
| `fireflies` | Pull Fireflies transcripts and turn them into notes that match what matters to you (needs `obsidian-memory`) |

**You:** Both.

**Claude:** Good. `fireflies` depends on `obsidian-memory`, so both are in. Prerequisites check: Python 3.13 is fine. I'll need to install two small packages (`requests`, `keyring`) after you approve the plan. Nothing else is required.

Now I'll ask everything in one round. Answer casually; partial answers are fine.

**About your vault**
1. Where is (or should be) your Obsidian vault? A local folder outside OneDrive is best.
2. What clients or contexts do you work with? Short names are fine.
3. Any active projects to create folders for?
4. Tools you mention a lot?
5. Subjects you'd want reusable how-to notes about?
6. What counts as sensitive in your work?
7. The default folders are `00 - Inbox`, `10 - Clients`, `20 - Internal`, `30 - Projects`, `40 - Reference`, `50 - Meetings`, `60 - People`, `70 - Daily Notes`, `80 - Templates`, `99 - Archive`. Any changes?

**About your meetings**
8. Your email address (used so only meetings you organized or attended are kept)?
9. What kinds of meetings do you have, and what is each for?
10. What do you want out of a meeting? Options: short summary, decisions, action items with owner and due date, risks, open questions, client commitments, attendance and participation, parking lot, key quotes, follow-up email draft, or something specific to your work. Tell me which apply to which meeting types.
11. People say "EOW" or "next Wednesday": should I convert those to real dates?
12. Unknown speakers ("Speaker 1"): how should I handle them?
13. Preferred style (terse bullets, short paragraphs)?
14. Where should meeting notes go, and do you want raw transcripts kept?
15. Any meetings to skip (title words)?
16. Anything transcripts add to the sensitivity rules?
17. Fetch manually or on a schedule? Process inside Claude sessions?

**You:**
1. `C:\Users\<you>\Documents\Vault`, it's new
2. Acme Health and Northwind Clinics
3. A Denial Analytics project for Acme
4. Python, Excel, Power BI
5. Denials, Excel tips, Python
6. Anything with patient info or client financials
7. Defaults are fine
8. jordan.lee@example.com
9. Client working sessions (Acme, Northwind), internal team status, and 1:1s with my manager
10. A 3-sentence summary, decisions clearly labelled, action items with owner and due date, risks only for client sessions, and a parking lot
11. Yes, real dates, but keep the phrase they said
12. Call them "Unidentified speaker" and mark guesses "(inferred)"
13. Terse bullets
14. `50 - Meetings/<client or Internal>`, and keep transcripts in `50 - Meetings/Transcripts`
15. Skip anything with "lunch" or "interview" in the title
16. No additions
17. Manual for now, process in Claude

**Claude:** Thanks. Here's the plan. I haven't changed anything yet.

**obsidian-memory**
- Create the vault folders (defaults plus `10 - Clients/Acme Health`, `10 - Clients/Northwind Clinics`, `30 - Projects/Denial Analytics`, `40 - Reference/{Denials, Excel tips, Python}`, `50 - Meetings/{Acme Health, Northwind Clinics, Internal, Transcripts}`).
- Copy 7 note templates into `80 - Templates`.
- Install the `obsidian-note-router` skill to `~/.claude/skills/`.
- Append an `## Obsidian Vault` block to `~/.claude/CLAUDE.md` (applies to all your sessions).
- Write `~/.claude-harness/obsidian-memory.toml`.

**fireflies**
- Install `requests` and `keyring` with `python -m pip`.
- Create the state folder `~/.claude-harness/fireflies/` (where I keep the scripts and downloaded transcripts) with `poll.py` and `harness_secrets.py`.
- Install the `meeting-review` skill to `~/.claude/skills/` and append a `## Fireflies Meetings` block to `~/.claude/CLAUDE.md`.
- Write `~/.claude-harness/fireflies.toml` (your email, skip words, state folder, Python path).
- A secret named `fireflies_api_key`. **You** store it in your own terminal; I never see it.

**What your meeting notes will contain** (generated from your answers; tell me what to change):
1. Summary: 3 sentences.
2. Decisions: each labelled, only confirmed ones.
3. Action items: `- [Owner] — [Action] — [Due]`. Relative dates become real dates with the original phrase in quotes.
4. Risks: client working sessions only.
5. Parking lot: topics deferred.
Unknown speakers are "Unidentified speaker"; guesses are marked "(inferred)". Style: terse bullets.

**Opt-ins, separate from the above:** a scheduled task to poll Fireflies automatically. You said manual, so I'll skip it.

Approve this plan?

**You:** Looks good. Go ahead.

*Claude creates the folders, fills every placeholder from your answers, copies files, and installs the packages. A skill with unfilled placeholders is never copied.*

**Claude:** Done. File checks:

- Vault folders and 7 templates: pass
- `obsidian-note-router` and `meeting-review` skills: installed, no unfilled placeholders
- `~/.claude/CLAUDE.md` blocks: added
- `requests` and `keyring` import under Python 3.13: pass
- `fireflies.toml`: your email is set

**One step is yours.** I never handle your Fireflies API key.

1. Go to app.fireflies.ai, open **Settings**, then **MCP & API**, and copy your API key.
2. Open a **new PowerShell window** (not this chat) and run:

   ```powershell
   cd $HOME\.claude-harness\fireflies
   python harness_secrets.py set fireflies_api_key
   ```
3. Paste the key at the hidden prompt and press Enter. You'll see `Stored 'fireflies_api_key' in the OS credential store.`

Don't paste the key here. Tell me when it's stored.

*You run the command in your own terminal.*

**You:** Stored.

**Claude:** *(runs `python harness_secrets.py check fireflies_api_key`)* `'fireflies_api_key': found`.

*(runs `python poll.py --dry-run`, which lists meetings and saves nothing)* It found 6 meetings in the last 7 days that you organized or attended; 2 were skipped by your title rules. Nothing was saved. The key works.

I've recorded both modules in `~/.claude-harness/installed.json`.

**Last step:** the skills load only in a new session. Please close this session and start a new one in any folder. Then try these:

- *"Log this: met with Acme today, agreed to move go-live to March. Send the contract by Friday."* I should file it under Acme with tags, report the path, and not ask for approval.
- *"Process my pending meetings."* (First run `python poll.py` in your terminal to fetch transcripts, or ask me to run it.)

To uninstall either module, see "How to remove it" in its `MODULE.md`.

---

## In the new session

**You:** Log this: met with Acme today, agreed to move go-live to March. Send the contract by Friday.

**Claude:** Filed.
- `50 - Meetings/Acme Health/2026-10-08 Acme go-live timing.md`
- Type: meeting · Client: `client/acme` · Tags: `type/meeting`, `client/acme`, `status/active`
- Action: Send the contract to Acme — 2026-10-09 ("by Friday")

**You:** Process my pending meetings.

**Claude:** Processed 3 meetings (1 skipped: title contained "interview"):
- `50 - Meetings/Acme Health/2026-10-06 Denial Analytics working session.md`: client working session; 4 actions, 2 decisions, 1 risk
- `50 - Meetings/Internal/2026-10-07 Team status.md`: internal status; 3 actions, 1 decision
- `50 - Meetings/Internal/2026-10-07 1-1 with manager.md`: 1:1; 2 actions
- Raw transcripts saved to `50 - Meetings/Transcripts/`. Packages archived to `processed/`.

Flagged: the 10-06 session mentioned an account number; it looks like patient information, so I left it out of the note. Want me to include it?

**You:** Leave it out. Can you add a "Follow-ups for me" section at the top?

**Claude:** Added to the `meeting-review` skill (top section: your action items only). Existing notes are unchanged; say the word and I'll regenerate them.
