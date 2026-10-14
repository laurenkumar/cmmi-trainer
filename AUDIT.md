# CMMI Academy: Pedagogical, UX and Exam-Readiness Audit — 14 October 2026

## Scope and method

Review of repository content `index.html`, `app.js`, `app.css` and `data.json`, including all 31 PAs, foundation modules and training questions. Browser-level smoke tests covered FR→EN language switching, representative foundation/PA lessons, interactive chapter switching, flashcard/glossary reveal, 120-question exam initialization and mobile overflow checks. Vercel deployment metadata was checked for `READY`; protected website HTML could not be independently fetched via the Vercel account connector, therefore tests were performed on the same GitHub source locally, not asserted as a live browser test.

### Referenced official materials

- CMMI Model Quick Reference Guide v4.0, August 2026 (summary only).
- CMMI Credentialing Guide for Practitioners, August 2026 (exam framework, 30 official sample questions, prerequisites and exam rules).
- CMMI Appraisal Method (distinct organizational appraisal process).

## Findings

| Priority | Finding | Why it matters | Status in this release |
|---|---|---|---|
| Critical | PA reading modules repeated generalized explanations and did not fully enumerate normative practices | High risk of overestimating exam mastery | **Open**: unique scenarios and practical flows exist, but full-model coverage is not possible from the quick reference |
| Critical | Entire trainer and questions were French | The intended exam language is English | **Improved**: 40 English learning modules, 206 English questions, UI toggle, 102-item vocabulary lab |
| High | Mock exam capped at 40 questions with unrealistic time limit | Does not train four-hour pacing or weighted content areas | **Fixed**: 120/240 option and weighted domain selection |
| High | Many answer options were obviously nonsensical; answer index was predictable | Leads to inflated scores | **Improved**: EN alternatives use plausible PA interventions and randomized correct-answer positions; further editorial item calibration needed |
| High | Successful completion of one trivial activity marked a lesson as mastered | Overstates demonstrated understanding | **Open**: the last activity still gates validation, but should be followed by retrieval after 24h and multi-question mastery checks |
| High | Practitioner 2026 exam framework was not a dedicated learning module | Exam conditions and high-weight sections overlooked | **Fixed**: F09 explains the current exam format, prerequisite, content weighting and restrictions |
| Medium | UI uses a mixture of French and English after switching | Increases cognitive friction | **Partly improved**: navigation, learning flow and quiz UI translated; some ancillary labels remain French |
| Medium | Evidence exercises are short and fictional rather than complete artifacts and interviews | Insufficient for real appraisal preparation | **Open**: needs multi-document cases, interview simulations and independent justification evaluation |
| Medium | Mobile and desktop navigation should be validated after every change | Interaction bugs can block learning | **Smoke tested**: no JS exceptions in selected flows; broader regression testing needed |
| Important | No systematic diagnostic using calibrated scoring and interval review | Learner cannot reliably identify readiness | **Open**: retrieval practice and dashboard exist; readiness still does not match official passing criteria |

## Accuracy boundaries

The published August 2026 Practitioner exam has 120 questions over 4 hours. Listed content weights are Core/Virtual 50%, Development 15%, Services 15%, Security/Safety 5%, Suppliers 5%, Data 5%, People 5%. The official guide contains 30 **sample** questions, not released past examination papers. The mandatory **Building Organizational Capability** course cannot be bypassed through this trainer. The current passing percentage is not published by CMMI Institute.

## Next required improvements before calling this certification-ready

1. Licensed model access and human-reviewed mappings to every applicable practice and group level (with links to the **user-owned** licensed material, not republishing it).
2. Editor-reviewed question discrimination and a true five-option/three-option mix where appropriate, with realistic wrong answers, difficulty stratification, spaced retesting, distractor rationales and confidence ratings.
3. Substantially deeper teaching and memory practice for category/CA/PA relationships, high-maturity quantitative concepts, organizational appraisal roles and process evidence scenarios.
4. Simulated multi-document case packs: requirements, work products, logs, interviews, contradictory evidence and a reasoned appraisal finding exercise.
5. Complete interface translation, keyboard accessibility pass, screen-reader quality and regression coverage for every learning route.
6. Final verification against any policy or content-outline changes during 2027.

**Conclusion:** a better independent bilingual foundation, **not** an official certification course and **not yet sufficient alone** to assure exam readiness or a recognized organizational maturity result.