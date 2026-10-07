"""Shared secret helpers for claude-harness-starter modules.

Store a secret (run in YOUR terminal, never through Claude):
    python harness_secrets.py set <secret_name>

Check that a secret exists without printing it:
    python harness_secrets.py check <secret_name>

Remove a secret:
    python harness_secrets.py delete <secret_name>

Scripts read secrets with get_secret(name, env_var=...). Lookup order:
OS credential store (via keyring), then the named environment variable.
Secret values are never printed or logged.
"""
from __future__ import annotations

import getpass
import os
import sys

SERVICE = "claude-harness"


def get_secret(name: str, env_var: str | None = None) -> str | None:
    try:
        import keyring

        value = keyring.get_password(SERVICE, name)
        if value:
            return value
    except Exception:  # noqa: BLE001 - keyring backend may be missing
        pass
    if env_var:
        value = os.environ.get(env_var, "").strip()
        if value:
            return value
    return None


def require_secret(name: str, env_var: str | None = None) -> str:
    value = get_secret(name, env_var)
    if not value:
        sys.exit(
            f"Secret '{name}' not found. Run: python harness_secrets.py set {name}"
            + (f"  (or set the {env_var} environment variable)" if env_var else "")
        )
    return value


def _set(name: str) -> int:
    import keyring

    value = getpass.getpass(f"Enter value for '{name}' (input hidden): ").strip()
    if not value:
        print("No value entered; nothing stored.")
        return 1
    keyring.set_password(SERVICE, name, value)
    print(f"Stored '{name}' in the OS credential store.")
    return 0


def _check(name: str) -> int:
    ok = get_secret(name) is not None
    print(f"'{name}': {'found' if ok else 'NOT found'}")
    return 0 if ok else 1


def _delete(name: str) -> int:
    import keyring

    try:
        keyring.delete_password(SERVICE, name)
        print(f"Deleted '{name}'.")
        return 0
    except keyring.errors.PasswordDeleteError:
        print(f"'{name}' was not stored.")
        return 1


def main(argv: list[str]) -> int:
    if len(argv) != 3 or argv[1] not in {"set", "check", "delete"}:
        print(__doc__)
        return 2
    return {"set": _set, "check": _check, "delete": _delete}[argv[1]](argv[2])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
