# CMMI Academy 2027 — bilingual trainer

Interactive **French/English** study platform for CMMI v4.0 concepts and preparation for personal Practitioner certification and organizational appraisal participation. [Open the live app](https://cmmi-trainer.vercel.app/).

## Features
- 40 lessons: nine foundations and 31 Practice Areas, with original reading, diagrams, fictional cases and workshops in FR/EN.
- 481 original practice questions: 275 French and 206 English.
- 120-question, 240-minute English mock-exam option, with 2026 Practitioner content-area weights (Core/Virtual 50%, Development 15%, Services 15%, Security/Safety 5%, Suppliers 5%, Data 5%, People 5%).
- 102 bilingual technical vocabulary cards with recall challenges.
- 20 fictional appraisal cases, flashcards, evidence checklist and local progress.

## Files
- `index.html`: complete standalone application, deployed as a static site.
- `app.js`: editable behavior; `app.css`: editable styles; `data.json`: curriculum, glossary, questions.
- `build.py`: re-create `index.html` after editing sources; `test_content.py`: content validation.
- `AUDIT.md`: findings and limitations.

Run `python build.py && python test_content.py`. Commit generated `index.html` along with edited sources to trigger Vercel from `main`.

## Boundaries and sources
This is independent educational material, not official exam questions, licensed CMMI model content or recognized appraisal. The **Quick Reference Guide v4.0** is a summary, not the full normative model. The **Building Organizational Capability** course remains a prerequisite to the Practitioner. No practice test can guarantee certification.

Official references: [CMMI Quick Reference Guide](https://cmmiinstitute.com/resource-files/public/cmmi-model-quick-reference-guide), [2026 Practitioner Credentialing Guide](https://www.cmmiinstitute.com/getattachment/8051d124-5dd9-44fd-9bf0-4842c6d58b16/CMMI-Credentialing-Guide-for-Practitioners.pdf). Check 2027 policies when registering.
