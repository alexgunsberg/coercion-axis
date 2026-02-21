# Coercion Axis Question Bank (English Canonical)

This file is the canonical English question set for the open-source repository.

Current status:
- Scoring model is stable and implemented.
- Finnish source wording exists in `QUESTIONS.fi.md`.
- Full line-by-line English translation is in progress.

## Scoring Model (applies to every question)
Each question must use exactly five options and this score scale:
- `-4`: Maximum liberty / minimum coercion
- `-2`: Leans liberty
- `0`: Neutral / status-quo
- `+2`: Leans coercion / statism
- `+4`: Maximum state control

## Translation and neutrality rules
- Preserve semantic meaning; avoid rhetorical drift.
- Do not change score polarity between languages.
- Keep option intensity monotonic from `-4` to `+4`.
- Changes must be reviewed as content changes, not just copy edits.

## Temporary source of truth for active app content
Until full translation is completed in `index.html`, the runtime question bank still uses Finnish wording.

Contributors who want to help can submit PRs that:
1. Translate one section at a time.
2. Include a side-by-side mapping to `QUESTIONS.fi.md`.
3. Confirm scoring parity for each option.
