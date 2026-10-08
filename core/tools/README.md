# core/tools

Small helpers BOOTSTRAP runs for you. You normally never call these yourself.

| Script | What it does |
|---|---|
| `build_toml.py` | Builds a module's `~/.claude-harness/<module>.toml` from its `defaults.toml` plus `--set` (settings) and `--ph` (placeholder) overrides. `--base <existing.toml>` keeps the user's earlier values (for tailoring and updates), and `--ph-from <other.toml>:NAME` copies a placeholder from another module. Writes valid TOML so paths never need hand escaping. |
| `fill_placeholders.py` | Replaces `{{NAME}}` markers in a template using the `[placeholders]` table of a toml file. Exits non-zero and writes nothing if any marker has no value. |
| `replace_block.py` | Replaces (or appends) a module's marked block in a CLAUDE.md file, so updates never duplicate a block. |

All need Python 3.11+ (they use `tomllib`). Run `build_toml.py --help`, or the others with no arguments, for usage.
