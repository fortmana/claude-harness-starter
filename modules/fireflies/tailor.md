# fireflies — tailoring the meeting summary (optional)

This is a conversation, not a form. **Show the user a real result first, then ask what they would change.** Do not read out a list of questions.

## When

Offer this after the install works (BOOTSTRAP step 9). Ask once: "Want help tailoring your meeting summaries? I'll show you what the default looks like and you tell me what to change. Or you can use it as is and change it any time by asking."

If they decline, stop. The default skill is already installed and working. Mention they can say "tailor my meeting summaries" at any time to come back to this.

## 1. Show the default

1. Pick the input, in this order: a real meeting waiting in `<state_dir>/pending/`, otherwise (if the key is stored and they agree) run `poll.py` and use the most recent meeting, otherwise `samples/sample_transcript.json`.
2. Following the installed `meeting-review` skill, write the note **inline in chat only** (do not file it or move the package).
3. Say, in one or two sentences, what you did and what the note is made of. Then ask: **"What would you change?"** Leave it open.

## 2. Iterate

Listen to what they say and make the change. If they are not sure what to ask for, offer two or three suggestions that fit what you saw, for example:

- a section they would not use, or one that is missing (open questions, client commitments, a follow-up email draft, key quotes, attendance and participation, anything specific to their work)
- a different length or style (shorter summary, bullets only, more detail on decisions)
- how people or dates were handled (unknown speakers, "next Wednesday" turned into a date)
- different treatment for client versus internal meetings or 1:1s
- where notes and transcripts go, or how they are named and tagged
- meetings that should be skipped (by title words)

Regenerate the same note after each change so they see the effect. Stop when they are happy. Never push through the whole list.

## 3. Apply it

When they approve:

1. Update the matching values in `[placeholders]` (and `skip_title_patterns` in `[settings]` if skip words changed) in `~/.claude-harness/fireflies.toml`.
2. Re-fill the skill from `skills/meeting-review/SKILL.md` with `core/tools/fill_placeholders.py` and replace the installed copy. Read it back to confirm the change is present.
3. If they added a new meeting type or section, make sure `MEETING_TYPES` and `OUTPUT_SECTIONS` stay consistent with each other.
4. Tell them what changed in one or two lines and that it applies from the next new session.

## Notes

- Never invent content for sections the transcript does not support. Keep "(inferred)" markers.
- Keep user answers out of the repo; only `~/.claude-harness/` and `~/.claude/skills/` change.
