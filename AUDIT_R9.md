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

Results and final URLs are appended after execution. Automated use of answer keys checks application scoring and persistence, not learner proficiency, expert approval, or exam equivalence. Mobile checks use Chromium at a 390×844 touch viewport; physical iOS/Safari behavior is outside this test.
