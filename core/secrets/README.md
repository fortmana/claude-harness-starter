# core/secrets

`harness_secrets.py` stores and reads API keys using the OS credential store (`keyring`), so keys never appear in files, config, or Claude sessions.

- Requires `pip install keyring`.
- BOOTSTRAP copies this file next to a module's scripts when that module declares `secrets` in its manifest.
- The user runs `python harness_secrets.py set <name>` **in their own terminal**. Claude must never ask for or receive the value.
- Service name in the credential store: `claude-harness`.
