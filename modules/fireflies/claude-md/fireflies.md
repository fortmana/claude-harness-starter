<!-- claude-harness:fireflies:start -->
## Fireflies Meetings

- New Fireflies transcripts are fetched by `{{STATE_DIR}}/poll.py` into `{{STATE_DIR}}/pending/`.
- When asked to process meetings or a transcript, use the `meeting-review` skill; it writes the note and archives the package.
- Never ask the user for the Fireflies API key and never print it. It lives in the OS credential store (secret name `fireflies_api_key`); if it is missing, tell the user to run `python harness_secrets.py set fireflies_api_key` in their own terminal.
- Transcripts can contain client-confidential or regulated data. Follow the sensitivity rules in the `meeting-review` skill.
<!-- claude-harness:fireflies:end -->
