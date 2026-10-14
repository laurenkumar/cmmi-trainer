# CMMI Academy — Content & assessment audit (14 October 2026)

## Method

Checked the *CMMI Model Quick Reference Guide v4.0 (2026)* supplied by the project owner, focusing on pp. 22, 32–33 for the six publicly reproduced PQA practice statements. Compared 31 PG-level bilingual summaries with the quick guide's PA structure and fixed overly generic English summaries. Exam questions are newly written/assembled from the public PA summaries and concrete examples; they are not authorized ISACA past questions.

## Coverage

| Requirement | Finding |
|---|---|
| All 31 PA present | Yes |
| All 276 licensed practice statements reproduced | **No**; unavailable for public redistribution |
| One practice-by-practice public-source course | **PQA: six distinct identifiers, levels and examples** |
| Bilingual PQA explanations and exercises | Yes |
| English PG descriptions specific to each PA | Yes; 31 PA checked for level-key consistency |
| Private assessment pools | Distinct from quiz banks in UI; content still inspectable in public client-source code |
| 120-question weighting | 60 CORE/VRT, 18 DEV, 18 SVC, 6 SEC/SAF, 6 SPM, 6 DATA, 6 PPL per form |
| Two fresh mock exams per language | Yes: A and B, 240 distinct questions per language |
| After A+B | Retake labelled; questions necessarily recur after both forms |
| Official score predictive validity | **Not established**; no representative pass-rate data |
| Certified human translation / subject-matter review | **Not performed** |

## Functional tests

`python audit_v6.py`: JSON and language schema, six PQA entries, 31 PG keys, two 120-question forms, domain quotas, unique stems, no overlap between exam and practice banks, no literal answer leakage in prompt.

`test_fast.py`: Chromium click through PQA micro-check, bilingual switch, start 120-question form A, submit answers and render diagnosis, start unseen form B, third launch labelled retake. Mobile 390px viewport no overflow; no runtime JS errors.

## Limitations & next content sprint

1. **Model access**: the public quick guide explicitly says it is not a substitute for the licensed model. The detailed statements, additional required information and explanatory guidance for remaining practices require authorized access. Do not invent them.
2. **Real mastery quality**: the mock forms are independent of practice quizzes and of each other but many items still depend on identifying the appropriate PA/response from short scenarios. Human review is needed to flag implausible distractors, assess discrimination, ambiguity and reading level. The 80% threshold used in course practice is not an official passing score.
3. **Translation**: bilingual PQA content and the 31 English PG summaries were rewritten for meaning; a native-speaking certified instructor should audit all case studies and QCM explanations before describing the translation as perfect.
4. **Video**: the original 80 MP4 (40 lessons in FR and EN) are unchanged. This PQA expansion is longer than its existing video, so the video does not narrate all six new practice-level mini-lessons.
5. **Exam security**: all correct answers are present in the downloadable web app. For a genuinely secure exam, put the held-out bank and marking behind authenticated server endpoints.