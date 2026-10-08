# Concepts: the layers of a harness

A short guide to the pieces the modules install. You do not need this to use them, but it helps when you start customizing.

## Skills

A skill is a folder with a `SKILL.md` file under `~/.claude/skills/<name>/`. The file has a short description (when to use it) and instructions (what to do). Claude reads the descriptions at session start and loads a skill's full instructions when your request matches.

Use a skill for a **repeatable task with a specific method**: filing a note, reviewing a meeting, building a report.

## CLAUDE.md

A markdown file Claude reads at the start of every session. `~/.claude/CLAUDE.md` applies to all your sessions; a `CLAUDE.md` inside a project folder applies there.

Use it for **standing rules and facts**: where your vault is, how you like answers, which tools to prefer. Keep it short; long files get skimmed.

Rule of thumb: *always true* goes in CLAUDE.md, *how to do a specific task* goes in a skill.

## Memory

Claude does not remember earlier sessions by default. Memory is anywhere you tell it to write things down and look them up again. In this repo that is an Obsidian vault of plain markdown files with consistent frontmatter and tags, so Claude can find notes by metadata instead of guessing.

## Scripts and schedules

Code that runs outside the chat: for example fetching transcripts from an API. Scripts store secrets in your OS credential store, not in files. Schedules (such as a Windows scheduled task) run scripts on a timer and are always opt-in.

## State folder and `~/.claude-harness/`

`~/.claude-harness/` holds *your* settings (one `<module>.toml` per module) and an `installed.json` record. A module's **state folder** is where its scripts and downloaded data live. Nothing personal is ever written into this repo.

## Placeholders

Module files contain `{{NAME}}` markers. During install Claude fills them from your answers and defaults, so the skill and CLAUDE.md block that land on your machine are specific to you. Tailoring a module later re-fills them.
