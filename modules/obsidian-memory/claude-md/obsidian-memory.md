## Obsidian Vault

Vault: {{VAULT_PATH}}
Access: read and write the vault directly with Read / Write / Edit / Grep / Glob. No MCP server is used.

### Capturing
- For any request to capture, log, file, or save information, use the `obsidian-note-router` skill. Do not write ad hoc notes.
- Write autonomously, then report the path, folder, and tags. Confirm only before overwriting or deleting an existing note.
- If client or project is unclear, file to `00 - Inbox` and say why.

### Retrieving
Before answering a question about past work, decisions, people, or projects:
1. Search by metadata first: Grep for tags or frontmatter (for example `type: decision` or a `client/...` tag) inside the most likely folder.
2. Then by location: list the folder the routing rules say it would live in.
3. Then by full text, scoped to a specific folder.
4. Read the matching notes before answering and cite their paths. If nothing is found, say so rather than guessing.

### Safety
- Never run recursive searches from the drive root, a cloud-sync root, or the Documents folder. Always scope to a specific vault subfolder.
- Flag sensitive content (see the router skill) before storing it.
