# CMMI Academy V4 — teaching, UX, localization & exam-readiness audit
Date: 2026-10-14. Scope: local V4 production build generated from `app.js`, `app.css`, `data.json`; reviewed against the two user-supplied CMMI reference PDFs and publicly listed August 2026 official Practitioner credentialing materials. This is an independent audit of a training simulator, not an official CMMI appraisal.

## Measured coverage and changes

| Item | Verified V4 state |
|---|---|
| Curriculum | 40 lessons (9 foundations, 31 Practice Areas) in French and English |
| Practice Group summaries | 102 bilingual group-level teaching summaries, covering levels displayed in user-provided quick reference |
| Practice *counts* in quick guide | 276 listed, but the full *normative wording of these practices is not included* |
| Expanded instruction | 4 guided, evidence-oriented walkthroughs per lesson, FR and EN; original applied examples and common pitfalls |
| Contradictory case material | 4 documents and 2 fictional conflicting interviews per lesson in each language (320 documents and 160 interviews) |
| Assessment | 5 independent mastery items per lesson/language = 400 items, score displayed after submission, threshold 4/5 (80%) before lesson marked mastered; earlier V3 achievements do not bypass V4 gate |
| Separate quiz banks | 275 French + 206 English = 481 practice questions, plus the above mastery checks |
| Exam simulation | 120 questions / 240 min / domain proportions following the August 2026 Practitioner overview; simulator scores are **not** an official passing prediction |
| Media | 6-scene animated explainer per lesson × two languages = 80 interactive explainers; subtitles and browser TTS with play/pause/speed controls. Source generator outputs 80 Hyperframes-compatible HTML compositions |
| Glossary | 102 EN terms with 102 distinct French definitions; previously missing 62 FR labels have been completed |
| Mobile | 390 px overflow regression fixed (document scrollWidth equals 390 px), UI interaction regression passing |

## Actual test evidence
- `python audit_content.py` → PASS for all 40 bilingual lessons, source levels, 400 mastery questions, 80 scenes, contradictions, and 102 definitions.
- `python test_ui_fast.py` → PASS at 1440 and 390 px; tested CAR case, five-question graded assessment, persistence of completion, language change, video presentation; no JavaScript page errors or horizontal overflow.
- `python audit_translation.py` → English screens and five lesson stages surveyed for residual French text. The bilingual glossary deliberately retains French equivalences. These are programmatic inspections, **not** certified human translation proofreading of every paragraph.

## Final readiness conclusion (important)
**The platform is not yet sufficient as a sole, guaranteed study source for an official exam or company appraisal.** It offers comprehensive practice-area *overviews* and much stronger application exercises. However, the user's quick reference explicitly says it cannot replace the full licensed CMMI Model. The detailed normative wording, detailed examples and context-specific information for **all 276 individual practices** are missing. No responsible educational review can guarantee passing based only on simulated question scores. The official training and credential eligibility requirements still apply. The 2026 credentialing guide is the latest reference verified here; re-check 2027 policies.

### Remaining prioritized improvements
1. **P0 — Licensed model:** Acquire lawful access to CMMI v4.0 Model Viewer for the applicable view, then write original practice-level explanations with precise identifiers, citations and verified educational examples (without reproducing licensed text in violation of terms). Link each practice to evidence tasks.
2. **P0 — Human subject-matter review:** Have a qualified CMMI instructor/Lead Appraiser validate scenarios, practice group descriptions, answer keys, and domain mapping. Current practice tests are **original**, not validated official exam items.
3. **P1 — True MP4s:** Hyperframes compositions are generated, but an external CLI render and 80 locally sourced French/English audio tracks have **not** been produced or uploaded. Browser speech synthesis depends on voice availability and varies by OS/locale.
4. **P1 — Human bilingual proofreading:** Native FR/EN authoring covers all 40 lessons and new media/evaluations; static UI localization checks pass on tested flows. A certified bilingual proofreader should review terminology and tone in all edge-case settings and dialogs.
5. **P2 — Longitudinal learning validity:** Measure delayed recall after 7/30 days and require diversified case families before predicting a learner is ready.

## Official reference links
- CMMI Institute [Quick Reference Guide (Aug 2026)](https://cmmiinstitute.com/resource-files/public/cmmi-model-quick-reference-guide).
- CMMI Institute [Credentialing Guide for Practitioners (Aug 2026)](https://cmmiinstitute.com/resource-files/public/cmmi-model-materials/cmmi-credentialing-guide-for-practitioners).
- CMMI Institute [Model Viewer](https://www.cmmiinstitute.com/products/cmmi/cmmi-model-viewer).
- HeyGen [Hyperframes source](https://github.com/heygen-com/hyperframes), Apache-2.0.

**Legal boundaries:** no copyrighted official exam questions or non-public licensed model text has been copied into the app. Case documents, scripts and mastery tests are original fictional educational content.

## 2026-10-14 additional audit and rendering correction
- Licensing independently checked against ISACA's current [IP sharing policy](https://cmmiinstitute.com/getattachment/da36326f-d5ad-4478-ad59-74ae042c688e/CMMI-MDDAP-IP-Policy-Update-Use-Cases_Feb2025_PDF.pdf). The public summary's **276 count** cannot be represented as verified instructional coverage of 276 detailed normative practice statements. No unlicensed copies scraped from GitHub can be incorporated.
- Official [Model Viewer](https://cmmiinstitute.com/products/cmmi/cmmi-model-viewer) costs US$150/year (as listed in October 2026) and includes full practice statements and supplemental information. A course review by an authorized expert remains needed.
- Previous claim of 80 HyperFrames videos was too strong: the prior project included only compositions. The updated generator creates source scenes with local French/English audio WAV and timed subtitle VTT; the new GitHub Actions workflow renders and tests all 80 MP4 files remotely. Its successful completion must be verified before claiming publication.
- The app continues to offer its browser-based narrator as a fallback, independent of the external MP4 assets.