---
name: meeting-review
description: >
  Use when the user wants to process Fireflies meeting transcripts, summarize or document a meeting, or pull
  action items, decisions, or follow-ups from a transcript. Triggers: "process my meetings", "process pending
  transcripts", "review this meeting", "summarize this call", "write up the notes from our meeting", or any
  pasted transcript. Reads pending transcript packages, produces a standardized meeting note shaped by the
  user's preferences, files it, and archives the package. Writes without asking approval.
---

# Meeting Review

Turns a transcript into a standardized meeting note that contains what matters to this user. The structure
below was generated from the user's setup interview; edit it any time the notes stop being useful.

## Inputs

**Pending packages:** JSON files in `{{STATE_DIR}}/pending/`. Each has: `id`, `title`, `date`, `duration_seconds`,
`organizer`, `attendees`, `transcript_text`, `ai_summary` (Fireflies' own gist/overview/action items), `source`.

**Pasted or uploaded transcripts:** treat the same way. The meeting date is required to resolve relative dates;
if it cannot be determined, ask once before analyzing.

## Meeting types

{{MEETING_TYPES}}

Classify each meeting into one of these types from its title, attendees, and content. If none fits, use
"General" and say so.

## What to produce

For every meeting, write a note with these sections, in this order:

{{OUTPUT_SECTIONS}}

## Rules

**Dates.** {{DATE_RULES}}

**People.** {{PEOPLE_RULES}}

**Style.** {{STYLE_RULES}}

**Skip rules.** {{SKIP_RULES}} When a meeting is skipped, archive its package to `processed/` and add one line
to the report; do not write a note.

**Never invent** names, owners, dates, decisions, or commitments. Mark inferences with "(inferred)". Use the
Fireflies `ai_summary` only as a cross-check, never as the sole source.

## Where notes go

- Meeting notes: `{{NOTES_FOLDER}}` as `YYYY-MM-DD <Meeting title>.md`.
- Raw transcript: {{RAW_TRANSCRIPT_RULE}}
- Tags: {{TAG_RULES}}
- Frontmatter on every note:

```yaml
---
date: YYYY-MM-DD
type: meeting
meeting_type: <one of the types above>
client: <client shortname or internal>
project: <project or blank>
meeting_title: <title>
organizer: <organizer>
duration: <Xh Ym>
participants: <comma-separated names>
source: fireflies
transcript_id: <id>
tags: [type/meeting, source/meeting-transcript, client/<shortname or internal>, status/active]
---
```

Follow the `obsidian-note-router` skill's conventions for naming and tags when it is installed. Where the frontmatter above and the router's differ, the frontmatter above wins; it is a superset, so client and project queries still find these notes.

## Workflow

1. List `{{STATE_DIR}}/pending/*.json`. If empty, say so and stop.
2. For each package: classify, apply skip rules, write the note and (if configured) the raw transcript.
3. Move the processed package to `{{STATE_DIR}}/processed/`. If writing the note fails, leave the package in
   `pending/` and report the error.
4. Report once at the end: one line per meeting with the note path, meeting type, and count of action items
   and decisions; list skipped meetings; flag anything that looked sensitive ({{SENSITIVITY_RULES}}).

Write autonomously; do not ask for approval to create notes. Confirm only before overwriting an existing note.
