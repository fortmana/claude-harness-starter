# fireflies — interview

The goal is a meeting note that contains what **this** user actually needs. Do not skip this interview and do not fill answers in for the user. Ask in one or two batches, offer the examples, and then generate the placeholder text below from their answers.

Save answers to `~/.claude-harness/fireflies.toml` (config values) and keep the generated text for the skill.

## Part 1: Setup values

1. **Your email address** — used to keep only meetings you organized or attended. Strongly recommended: the API can return transcripts from other people's meetings. -> `my_email` in the toml.
2. **How far back on the first run?** Default 7 days. -> `lookback_days`.
3. **Meetings to skip entirely?** Words in titles to ignore (for example "lunch", "interview", "personal"). -> `skip_title_patterns` in the toml and `{{SKIP_RULES}}` (a sentence naming the same rules, plus any content-based rules such as "skip meetings with no business content").
4. **Where should state live?** Default `~/.claude-harness/fireflies`. -> `state_dir` in the toml and `{{STATE_DIR}}` (use the resolved path).

## Part 2: What matters to you

5. **What kinds of meetings do you have?** (for example client working sessions, internal status, 1:1s, sales calls, interviews, steering committees). For each, one line on its purpose. -> `{{MEETING_TYPES}}` as a bulleted list: `- **<Type>** — <purpose>; <how to recognize it>`.
6. **What do you need out of a meeting?** Offer these and let them add their own; ask which apply to which meeting type:
   - Short summary
   - Decisions made (labelled)
   - Action items with owner and due date
   - Risks or concerns raised
   - Open questions
   - Client or stakeholder commitments
   - Attendance and participation (who spoke, who stayed quiet)
   - Parking lot (topics deferred)
   - Key quotes
   - Draft follow-up email
   - Anything specific to their work (for example billing implications, scope changes, system or data issues)

   -> `{{OUTPUT_SECTIONS}}` as a numbered list. For each section give its heading, exactly what to include, the format (for example `- [Owner] — [Action] — [Due]`), and what to write when empty (for example "No action items recorded."). Note which sections apply only to certain meeting types.
7. **Dates.** Do people say "EOW", "next week", "by Thursday"? Should those be converted to calendar dates anchored to the meeting date, and in what format? -> `{{DATE_RULES}}`. Default: convert relative phrases to `YYYY-MM-DD` anchored to the meeting date and keep the speaker's exact phrase in quotes; if a date is unclear, write "date unclear — confirm".
8. **People.** Fireflies often labels speakers "Speaker 1". How should unknown speakers be handled (label as "Unidentified speaker", infer from context and mark "(inferred)")? Are there names or nicknames Claude should know? -> `{{PEOPLE_RULES}}`.
9. **Style.** Length and tone (terse bullets, short paragraphs), anything to avoid. -> `{{STYLE_RULES}}`.

## Part 3: Where it goes

10. **Destination folder** for meeting notes (relative to the vault from the obsidian-memory module, for example `50 - Meetings`). Split by client or by type? -> `{{NOTES_FOLDER}}` (for example `50 - Meetings/<Client or Internal>`).
11. **Keep the full raw transcript?** If yes, where (for example `50 - Meetings/Transcripts`). -> `{{RAW_TRANSCRIPT_RULE}}` ("Save the full transcript as a note in <folder>, linked from the meeting note." or "Do not keep raw transcripts.").
12. **Tags.** Which `client/...` and `tool/...` tags should apply when recognized? -> `{{TAG_RULES}}`. Default: use the obsidian-memory tag taxonomy.
13. **Sensitivity.** What in a transcript should trigger a flag (client-confidential, personal, regulated data)? -> `{{SENSITIVITY_RULES}}`.

## Part 4: How it runs

14. **How should new transcripts be fetched?** Manually ("run the poll"), on a schedule (opt-in; see `MODULE.md`), or both. Only register a scheduled task if they say yes.
15. **How should processing run?** In a Claude Code session ("process my meetings"), or headless on a schedule (see `MODULE.md`, opt-in).

## After the interview

1. Generate the placeholder text from the answers and show the user the resulting "What to produce" section for a quick sanity check.
2. Fill the skill, copy it, and run `verify.md`, which tests the skill on a sample transcript. Offer to adjust sections immediately after seeing real output.
