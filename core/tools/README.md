# core/tools

Small helpers BOOTSTRAP runs for you. You normally never call these yourself.

| Script | What it does |
|---|---|
| `build_toml.py` | Builds a module's `~/.claude-harness/<module>.toml` from its `defaults.toml` plus `--set` (settings) and `--ph` (placeholder) overrides. Writes valid TOML so paths never need hand escaping. |
| `fill_placeholders.py` | Replaces `{{NAME}}` markers in a template using the `[placeholders]` table of a toml file. Exits non-zero and writes nothing if any marker has no value. |

Both need Python 3.11+ (they use `tomllib`). Run either with no arguments (or open the file) for usage.
