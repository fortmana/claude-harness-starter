# obsidian-memory — interview

Ask these in one batch. Save the answers to `~/.claude-harness/obsidian-memory.toml`, then use them to fill the `{{PLACEHOLDERS}}` in the skill and CLAUDE.md block.

1. **Vault path.** Where is your Obsidian vault (or where should it be created)? Prefer a local folder outside cloud-sync folders. If it must be in OneDrive or a similar sync folder, note it. -> `{{VAULT_PATH}}`
2. **Clients or contexts.** What clients, customers, or contexts do you work with? Give short names. If none, say "internal only". -> `{{CLIENT_FOLDERS}}`, `{{CLIENT_TAGS}}` (as `client/<shortname>`, lowercase, no spaces)
3. **Projects.** Any active projects to seed folders for? (Optional.)
4. **Tools and technologies.** Which tools or technologies will your notes mention often? -> `{{TOOL_TAGS}}` (as `tool/<name>`)
5. **Reference topics.** What subjects will you want reusable how-to notes about? -> `{{REFERENCE_TOPICS}}`
6. **Sensitivity.** What counts as sensitive in your work (client-confidential data, personal data, regulated data such as health or financial information)? -> `{{SENSITIVITY_RULES}}`
7. **Folder changes.** The default folder set is below. Want to rename, add, or drop any? (`00 - Inbox` and `80 - Templates` are required.)

   `00 - Inbox`, `10 - Clients`, `20 - Internal`, `30 - Projects`, `40 - Reference`, `50 - Meetings`, `60 - People`, `70 - Daily Notes`, `80 - Templates`, `99 - Archive`
8. **Existing vault?** If a vault with notes already exists, do not restructure it. Create only missing folders and the templates, and offer to adapt the routing rules to the existing layout.

Defaults when the user has no preference: tags `client/internal`, no seeded projects, no tool tags, sensitivity "client-confidential or personal data".
