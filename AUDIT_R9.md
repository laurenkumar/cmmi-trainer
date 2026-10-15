# CMMI Academy 2027 — release R9, 15 October 2026

## Confirmed initial defects

The successful Actions run 38728958911 generated 80 MP4 files, downloaded them into tracked `videos/`, then ran `git reset --hard origin/main`. The reset replaced the new files with the committed old videos. Its subsequent `Already published` message was false evidence of publication. Earlier runs also failed during rendering or branch publication. The production page still served the old release.

The unpublished working tree contained restored public cards and original evidence-based cases, but public-group checks mostly asked the learner to recognize a statement copied from the lesson. A successful build alone did not establish pedagogical depth.

## Changes

- Preserve incoming media in a separate directory. Fast-forward the branch before installation; refuse incomplete batches and source changes during rendering.
- Decode every frame of all 80 MP4 files; check H.264/yuv420p, 960×540, 35 seconds, silence, captions and SHA-256 hashes. Compare working files with committed and served bytes.
- Pin HyperFrames to 0.8.161. Recovery requires a successful render run with a verified source commit.
- Add 31 original applied lessons in French and English, with worked examples covering causation, configuration identity, recovery dependencies, data denominators, capacity, lifecycle costs, interfaces and other PA-specific decisions.
- Replace 99 public-group recognition checks with scenario decisions. Preserve the six explicitly published PQA practice identifiers and separate them from public group summaries.
- Keep A and B at 120 original questions per language, with separate case IDs and question stems. Several questions within a form intentionally share a dossier; the forms are not psychometrically validated. Quantitative questions cover increased, decreased and unchanged rates and distinguish counts, exposure and causation.
- Preserve notes and history when assessment content changes; invalidate obsolete mastery. Reject malformed progress imports before changing saved state, and recheck assessment revision on import.
- Replace the repeated aggregate-rate mastery item with 31 PA-specific transfer questions per language and 31 additional bilingual D05 case documents.
- Add GitHub quality gates for content, reproducible build, media integrity and browser interactions.

## Public-source scope

The 2026 public Quick Reference Guide supplies 31 PA summaries, 102 PG summaries in total, and six individually excerpted PQA practices. The interface has 99 PG cards for the other 30 PAs plus the six PQA practice cards. The 276 individual normative practice statements are not reproduced or reconstructed. The public guide explicitly does not replace the full model for training or appraisal.

Current exam facts were checked against the official 14 July 2026 Practitioner Policy and 31 August 2026 Credentialing Guide: 120 questions, four hours, and content weights 50/15/15/5/5/5/5. These are current references, not guaranteed 2027 rules. The application's 80% mastery target is a learning threshold; the official passing score is not public. Questions, companies, examples, numbers and evidence formats are original educational material.

## Verification

Local desktop and mobile suites and the full public mobile suite passed on the final teaching content. Each suite traversed all 40 lessons in French and English, all lesson tabs, incorrect/correct missions, 0/5 failure, 5/5 success, public checks and completion gates. Each completed both 120-question forms in both languages, expecting 120/120 on A and 84/120 on B.

Additional checks passed: all navigation routes without horizontal overflow, video search recovery, playback, seeking and speed changes, audit-note persistence across grading/navigation, flashcard state, 31-row CSV contents, glossary search, keyboard lesson activation, progress export/import, rejected malformed imports, obsolete-assessment invalidation while retaining notes, reload persistence and four-hour exam expiry scoring unanswered questions as incorrect. No uncaught page errors occurred in the full suites.

In production, both French and English caption tracks loaded all five cues and displayed an active cue at 8 seconds. Range requests returned HTTP 206 and the requested 1,024 bytes; VTT used the correct MIME type. The final 80 MP4 and 80 VTT bytes matched the published manifest, after full MP4 decoding. The public HTML matched the generated source bytes.

Detailed Vercel API log access returned 403/404 through the connector; deployment evidence uses successful Vercel commit statuses, the READY project state, GitHub build gates and direct public-byte/browser verification. Automated use of answer keys checks application scoring and persistence, not learner proficiency, expert approval, or exam equivalence. Mobile checks use Chromium at a 390×844 touch viewport; physical iOS/Safari behavior is outside this test.

## Final evidence and delivery

| Check | Result | Evidence |
|---|---|---|
| GitHub render and publication | PASS, all eight shards and publication | [Run 38769429621](https://github.com/laurenkumar/cmmi-trainer/actions/runs/38769429621) |
| GitHub release gates | PASS, desktop and mobile jobs | [Run 38769889024](https://github.com/laurenkumar/cmmi-trainer/actions/runs/38769889024) |
| Reproducible source build | PASS, no generated HTML diff | CI job logs |
| Full local browser suite | PASS, 160 lesson/language/screen traversals and 960 exam answers | Desktop 1440×1000 and mobile 390×844, FR and EN |
| Full public mobile suite | PASS, 80 lesson/language traversals and 480 exam answers | [Production](https://cmmi-trainer.vercel.app/) |
| Public desktop focused checks | PASS | Keyboard activation, obsolete-import migration, retained notes, CSV rows, search and reload |
| All published media bytes | PASS, 80 MP4 plus 80 VTT | [Published manifest](https://cmmi-trainer.vercel.app/videos/manifest.json), render source 9225226a0f0d64dd5a591aeb7b36a0e2b0208dea |
| Production deployment | READY, Vercel status success | Deployment dpl_C1odbUK4mmGkWsqTxx1LpYBdQ4M4; media publication commit d5071d117360372a4e24b5fe28540750c967c3ec |

Final generated/public HTML SHA-256: `8c44ad631ff55f359c3fcf141dfad35dbf7373945da3301478faa6c855b1585c`.

No reproducible functional failure remained in the tested flows. The recovery workflow was reviewed but not dispatched separately; the primary generation/publication workflow was executed successfully twice. Physical iOS/Safari playback and browser-specific pronunciation voices were not tested. Educational difficulty and official-exam equivalence require independent human review; the full licensed model and future 2027 rules are outside this public-source release.
