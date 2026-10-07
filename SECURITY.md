# Security

## The rule

**Never paste an API key, token, or password into Claude.** Anything you type in a Claude Code session can be stored in conversation transcripts and sent to the model.

## How keys are handled here

1. You get the key from the service's website.
2. You run the module's key-setup script **in your own terminal** (not through Claude). It prompts with hidden input and stores the key in your operating system's credential store (Windows Credential Manager, macOS Keychain, or Linux Secret Service) via the `keyring` library.
3. Scripts read the key from the credential store at run time. As a fallback they read an environment variable named in the module's `MODULE.md`.
4. Keys are never written to this repo, to config files, or to CLAUDE.md.

If you pasted a key into a chat or file by mistake, rotate it at the provider immediately.

## Guardrails this repo can add (with your consent)

During setup Claude may offer to add Claude Code permission deny rules so it cannot read common secret files (`.env`, `*.key`, and the harness secrets paths). These are always an explicit opt-in.

## Data sensitivity

Modules that handle meeting transcripts or notes may touch client-confidential or regulated data (including PHI/PII). Check your organization's policy before pointing any pipeline at such data, and keep outputs in locations you are approved to use.

## Reporting a problem

If you find a secret or personal value committed to this repo, tell the maintainer and rotate it.
