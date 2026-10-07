---
name: obsidian-note-router
description: >
  Use whenever the user wants to capture, log, file, or save a note to their Obsidian vault, or pastes
  raw notes or meeting content and wants it organized. Triggers: "add a note", "log this", "capture this",
  "file this", "save this to Obsidian", "process my inbox", "clean this up", "make it a note". Classifies
  the input, adds frontmatter and tags, files it in the right folder, and writes it without asking approval.
---

# Obsidian Note Router

Vault path: `{{VAULT_PATH}}`

Write and edit notes directly with Read / Write / Edit. Search with Grep / Glob scoped to a specific
subfolder, never the whole drive.

## Folders

| Folder | Purpose |
|---|---|
| `00 - Inbox` | Unprocessed captures; default when routing is ambiguous |
| `10 - Clients/{Client}` | Client-specific work, findings, decisions. Known clients: {{CLIENT_FOLDERS}} |
| `20 - Internal/{Area}` | Internal team or company work |
| `30 - Projects/{Project}` | Active project notes; link back to the client |
| `40 - Reference/{Topic}` | Evergreen learnings. Topics: {{REFERENCE_TOPICS}} |
| `50 - Meetings` | One note per meeting |
| `60 - People` | One note per key contact |
| `70 - Daily Notes` | One note per day |
| `80 - Templates` | Note templates (see below) |
| `99 - Archive` | Completed or inactive notes |

## Naming

- Most notes: `{Folder}/YYYY-MM-DD Title.md`
- Daily notes: `70 - Daily Notes/YYYY-MM-DD.md`
- People: `60 - People/Full Name.md`

## Routing (first match wins)

1. Meeting -> `50 - Meetings`
2. About a specific person -> `60 - People`
3. Quick, time-sensitive capture with no clear home -> `70 - Daily Notes`
4. Reusable technical lesson or pattern -> `40 - Reference/{Topic}`
5. Tied to a client engagement -> `10 - Clients/{Client}` or `30 - Projects/{Project}`
6. Internal work -> `20 - Internal/{Area}`
7. Ambiguous or incomplete -> `00 - Inbox`, with a line explaining why

## Frontmatter (every note)

```yaml
---
date: YYYY-MM-DD
type: meeting | decision | reference | action-item | person | daily | note
client: <client shortname or internal>
project: <project or blank>
tags: [type/..., client/..., status/active]
---
```

## Tag taxonomy

- **Type** (pick one): `type/meeting` `type/decision` `type/reference` `type/action-item` `type/person` `type/daily` `type/note`
- **Client** (pick one): {{CLIENT_TAGS}} `client/internal` `client/personal`
- **Status** (pick one): `status/active` `status/on-hold` `status/complete` `status/archived`
- **Tool** (optional): {{TOOL_TAGS}}
- **Source** (if generated from something): `source/meeting-transcript` `source/manual`

Only use tags from this list. If a new client, tool, or topic appears, add it to this skill and use it.

## Required fields

Date, client or context, note type, and (for client notes) project. Infer them from the conversation and the
content first. If one cannot be inferred, do not block: file to `00 - Inbox`, say why in the note, and ask
in the report.

## Templates

Use the matching template in `80 - Templates` for the note type: `meeting`, `decision`, `reference`,
`person`, `daily`, `action-item`, `note`.

## Workflow

1. Parse the input; infer date, context, type, project, and next actions.
2. Pick the folder with the routing rules; apply frontmatter, tags, and the matching template.
3. Write the note. Never ask permission to create or append to a note.
4. Report: full path, folder, type, tags. Offer to move or retag if routing was a judgment call. Offer a
   standalone action-item note if tasks were found.

## Behavior

- Confirm only before overwriting or deleting an existing note.
- Sensitivity rules: {{SENSITIVITY_RULES}} If content matches, flag it before writing and confirm the user
  wants it stored.
- Default status is `active`.
- Match the naming of existing notes for the same client or project.
- If a note contains a reusable technical lesson, also suggest a trimmed copy in `40 - Reference`.
- Moving or renaming notes by file operations does not update `[[links]]`; mention this if the user uses links.
