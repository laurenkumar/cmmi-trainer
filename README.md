# CMMI Academy 2027 — PQA public practice deep dive + two blind mock exams

Live site: <https://cmmi-trainer.vercel.app/>. Single-file static app, French/English.

## What's new in this update

- **PQA (Process Quality Assurance):** a step-by-step module covering each of the six practice identifiers openly published in the 2026 CMMI Model Quick Reference Guide (pp. 22, 32–33): PQA 1.1; PQA 2.1–2.4; and PQA 3.1. Each contains a new explanation, one worked example, evidence to collect, a common pitfall, an interview prompt, and a bilingual micro-quiz. The practice IDs and levels derive from the public guide; teaching content is independently authored, not copied from the licensed full model.
- **31 Practice Areas:** corrected the English level descriptions, replacing repeated generic blurbs with domain-specific explanations based on public practice-group summaries. The French PQA level-3 summary was corrected to reflect recording improvement opportunities.
- **Separate examination banks:** two 120-question bilingual mock-exam forms, A and B. No question in either form is also used in the lesson/quiz banks; A and B have no identical stems. Questions only reveal explanations at the end, with analysis of results across the seven official content-area groupings. An exam from A followed by B presents unseen questions; a third session explicitly labels itself a *retake*.
- **Responsive:** tested in Chromium desktop and 390px mobile, including bilingual PQA navigation and the A → B transitions.

## How to study

1. Open **Parcours pédagogique / Learning pathway** → **PQA** → **Comprendre / Understand**.
2. Use the anchor **Explorer les six pratiques PQA** to go directly to the detailed learning cards. Expand each practice to see the explanation, real-life-inspired example, evidence, and formative question.
3. Use the **Mastery check** at the end of the lesson. This is a learning check, not a professional credential.
4. Open **Quiz et examen blanc / Mock exam** → **Exam**. Form A and form B have different questions. After finishing both, the app will label subsequent exams as retakes.

## Building & tests

Static deploy: `index.html`. Editable sources: `data.json`, `app.js`, `app.css`. Regenerate with `python build.py`, then `python audit_v6.py`. No external runtime API required.

The other features (video lesson players, bilingual narration, simulated audit files and 80 generated MP4 files in `videos/`) are unchanged.

## Source and scope limits

- Official source: **CMMI Model Quick Reference Guide v4.0** (CMMI Institute, 25 August 2026), particularly pp. 22, 32–33 for PQA: <https://www.isaca.org/resources/reference-guide/cmmi-model-quick-reference-guide>.
- Practitioner exam reference: **CMMI Credentialing Guide for Practitioners** (August 2026): <https://www.cmmiinstitute.com/resource-files/public/cmmi-model-materials/cmmi-credentialing-guide-for-practitioners>.
- Only the **six publicly excerpted PQA practices** have been individually expanded and verified against the supplied document. The 31 Practice Areas have public-level summaries but **not** all 276 individually detailed licensed normative practice statements. Other practice-group summaries in the site are learning paraphrases, not certification criteria.
- The two exam forms contain **independently generated educational questions**; their subject matter is tied to public PA goals, but their difficulty, distractors, psychometrics, translations and official-exam equivalence have not been independently certified. No success guarantee. Official qualification prerequisites and 2027 policies still apply.