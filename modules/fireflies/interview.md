# fireflies — base questions

Ask only this. Everything else comes from `defaults.toml`; do not ask about meeting types, sections, dates, style, folders, tags, or schedule during install. Those are handled by the optional tailoring step (`tailor.md`) after the install works.

1. **Your email address.** Ask: "What email is your Fireflies account under? I use it to keep only meetings you organized or attended, because the API can return transcripts from other people's meetings." -> `my_email` in `[settings]`.

## Computed, not asked

- `{{STATE_DIR}}` and `state_dir`: `~/.claude-harness/fireflies` resolved to an absolute path with forward slashes. Tell the user where it is; do not ask.
- `python` in `[settings]`: the interpreter recorded in BOOTSTRAP step 1.
- `{{SENSITIVITY_RULES}}`: use the default. Only if `obsidian-memory` was installed earlier with a customized value, copy that value into this module's `[placeholders]` instead.

## Placeholder formats (used by `defaults.toml` and when tailoring)

| Placeholder | Format |
|---|---|
| `STATE_DIR` | Absolute path, forward slashes (same as `state_dir` in `[settings]`) |
| `MEETING_TYPES` | Markdown bullet list |
| `OUTPUT_SECTIONS` | Markdown numbered list, one item per section: heading, what to include, format, empty-case text, which meeting types it applies to |
| `DATE_RULES`, `PEOPLE_RULES`, `STYLE_RULES`, `SKIP_RULES` | One short paragraph each, full sentences ending with a period |
| `NOTES_FOLDER` | Vault-relative path, forward slashes, may include `<Client or Internal>` |
| `RAW_TRANSCRIPT_RULE`, `TAG_RULES`, `SENSITIVITY_RULES` | One sentence ending with a period |

Required `[settings]` keys: `my_email`, `lookback_days`, `skip_title_patterns`, `state_dir`, `python` (forward-slash path to the interpreter). Folder names use the client's full name (for example `Acme Health`); the `client:` frontmatter value and tags use the lowercase shortname (for example `acme`).
