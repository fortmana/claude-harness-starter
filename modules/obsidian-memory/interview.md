# obsidian-memory — base questions

Ask only this. Everything else comes from `defaults.toml`. Clients, tools, topics, and projects start empty and are added by the router skill as they come up; folder changes and tag taxonomy are handled by the optional tailoring step (`tailor.md`).

1. **Vault location.** Ask: "Where should your Obsidian vault live? If you already have one, give me its path. Otherwise I'd suggest `~/Documents/Vault` (a local folder outside OneDrive or other sync folders works best)." Resolve to an absolute path with forward slashes. -> `{{VAULT_PATH}}`.
   - If the folder already exists and contains notes, do not restructure it. Create only missing folders and the templates, and say so in the plan.

## Computed, not asked

- Which CLAUDE.md receives the block: default `~/.claude/CLAUDE.md`; mention it in the plan so the user can change it.

## Placeholder formats (used by `defaults.toml` and when tailoring)

| Placeholder | Format | Example |
|---|---|---|
| `VAULT_PATH` | Absolute path, forward slashes | `C:/Users/<you>/Documents/Vault` |
| `CLIENT_FOLDERS` | Comma-separated folder names (or the default sentence) | `Acme Health, Northwind Clinics` |
| `CLIENT_TAGS` | Space-separated backticked tags, lowercase (may be empty) | `` `client/acme` `client/northwind` `` |
| `TOOL_TAGS` | Space-separated backticked tags | `` `tool/python` `tool/excel` `` |
| `REFERENCE_TOPICS` | Comma-separated (or the default sentence) | `Denials, Excel tips, Python` |
| `SENSITIVITY_RULES` | One sentence ending with a period | `Anything with patient information or client financials.` |

`[settings]` for this module has no required keys. Client folders use the full name (`Acme Health`); `client:` frontmatter and `client/...` tags use the lowercase shortname (`acme`).
