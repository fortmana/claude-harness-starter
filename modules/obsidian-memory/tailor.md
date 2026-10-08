# obsidian-memory — tailoring the vault (optional)

This is a conversation, not a form. **Show the user the default, then ask what they would change.**

## When

Offer this after the install works (BOOTSTRAP step 9). Ask once: "Want help tailoring how your vault is organized? I'll show you the defaults and you tell me what to change, or you can use it as is. The router also learns clients, tools, and topics as they come up."

If they decline, stop. Mention they can say "tailor my vault" at any time.

## 1. Show the default

Show three things, briefly:

1. The folder tree (the ten default folders and what each is for, in one line each).
2. One example capture: take something they said in this session, or a made-up one, and show the note the router would write: path, frontmatter, tags.
3. How retrieval works in one sentence (Claude searches by tags and frontmatter, then by folder, then by text).

Then ask: **"What would you change?"** Leave it open.

## 2. Iterate

Make the change they ask for and show the result. If they are unsure, offer two or three suggestions that fit what you know about them:

- their clients and projects (create folders, add `client/...` tags)
- tools and technologies they mention often (add `tool/...` tags)
- renaming, adding, or dropping folders (for example no `60 - People`)
- what counts as sensitive in their work
- adding their own note types or templates

Stop when they are happy. Do not walk through the whole list.

## 3. Apply it

1. Update `[placeholders]` in `~/.claude-harness/obsidian-memory.toml`.
2. Re-fill the skill and CLAUDE.md block with `core/tools/fill_placeholders.py` and replace the installed copies. If folders changed, edit the skill's folder table, routing rules, and the CLAUDE.md block so they all agree, and create the new folders. Read the files back to confirm.
3. If the `fireflies` module is installed and a folder it uses changed, update its `NOTES_FOLDER` and `RAW_TRANSCRIPT_RULE` to match.
4. Tell them what changed in one or two lines and that it applies from the next new session.
