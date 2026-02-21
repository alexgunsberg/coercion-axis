# Coercion Axis (Pakkoakseli)

Open-source political self-assessment based on one explicit dimension:
**acceptance of state-initiated coercion**.

This repository is now **English-first** for transparency and international auditability.
The original Finnish source materials are preserved.

## Project Naming
- English name: **Coercion Axis**
- Finnish name: **Pakkoakseli**

Note: "corrosion axis" would describe material decay; the intended term here is **coercion**.

## What this measures
- Single axis only (no hidden multidimensional weighting)
- Score options per question: `[-4, -2, 0, +2, +4]`
- Negative values: more liberty / less coercion
- Positive values: more statism / more coercion

## Current language status
- App chrome/UI: English-first
- Question bank in app: currently Finnish source wording
- Finnish full question source: `QUESTIONS.fi.md`
- English canonical question file: `QUESTIONS.md` (work-in-progress)

## Run locally
Open `index.html` in a browser. No backend is required.

## Simulation
Run:

```bash
python3 simulator/simulate.py
```

## Open-source intent
This project exists so the model, math, and scoring logic are inspectable and forkable.

## License
MIT (`LICENSE`)

## Sync from site quiz source

To keep this open-source repo aligned with the live site question bank, run:

```bash
/Users/alexgunsberg/.openclaw/workspace/projects/pakkoakseli/scripts/sync-from-pohjolanihme.sh
```

This sync updates:
- `const allQuestions = [...]`
- `const shortIndices = [...]`

Source file used by default:
- `/Users/alexgunsberg/Library/CloudStorage/ProtonDrive-alex.gunsberg@proton.me-folder/pohjolanihme_website_v01/layouts/tool/quiz.html`
