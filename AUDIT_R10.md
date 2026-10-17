# R10 delivery audit — 17 October 2026

## Scope and current result

Two requested workstreams: deepen the public-source learning pathway and implement SEO/GEO foundations. Application changes, teaching copy and generated public content are in the repository; the production release is checked by actual HTTP responses and file hashes, not by commits alone.

- Application: <https://cmmi-trainer.vercel.app/>
- Public French catalogue: <https://cmmi-trainer.vercel.app/fr/>
- Public English catalogue: <https://cmmi-trainer.vercel.app/en/>
- Release manifest: <https://cmmi-trainer.vercel.app/release.json>
- Code commit: `a6e84a67176f38dbb3a0d3847bbc57924300a741`.
- Release workflow: <https://github.com/laurenkumar/cmmi-trainer/actions/runs/39038082956>.

## Initial findings

The inspected repository and served application were R9. The later conversational claim of 31 additional applied workshops was not reflected in the current default branch or the live release. Existing 40 lessons, PA examples, 99 public group cards, six PQA excerpts, both mock forms and 80 captioned videos were preserved.

R9 rendered its learning interface from JavaScript into an otherwise empty root element. It had no independent HTML lesson pages, bilingual public catalogue, public guide series or sitemap.

## Pedagogical work delivered

| Component | R10 addition |
| --- | --- |
| Applied workshops | 31 original bilingual workshops, one per PA. |
| Sequences | Four per PA: understand a mechanism, examine records, make decisions, produce/self-review. 124 bilingual sequence designs. |
| Evidence | Three domain-specific fictional records per workshop: 93 bilingual records. |
| Decisions | Two per workshop: 62 original questions per language, with four plausible competing decisions, delayed correction and explanatory reasoning. |
| Written application | One deliverable prompt, four self-review criteria and a possible response per PA. |
| Persistence | Analysis drafts, written deliverables, question attempts, best scores and rubric checks saved by PA and language; included in export/import. |
| Honest assessment | Multiple-choice decisions are scored. Written quality is explicitly self-reviewed; checkbox completion is not expert marking. |
| Study pathway | A public guide connects foundations, workshops, form A, revision and form B, with official-preparation boundaries. |
| Original copy | Approximately 16,676 words across French and English, including records, questions, alternatives, feedback, prompts, rubrics and example responses. This is added teaching copy, not a claim of normative coverage. |

Examples include a configuration rollback that fails to restore parameters/data, recovery objectives defeated by inaccessible keys, mismatched data identities, price scoring that masks a hard decision constraint, capacity reduced by support work, unpropagated requirement changes and field validation with gloves on a tablet.

Editorial review replaced irrelevant distractors with plausible competing actions. It also reconciled the measurement case's excluded-population calculation (15/16 = 93.75%, versus 15/20 = 75% of original commitments) and clarified first response versus incident resolution in the service-delivery case.

The 276 individual normative practices are not reproduced or reconstructed. New cases, numbers, thresholds, decisions, grids and responses are original fictional teaching material based on public PA topics. Existing A/B mock banks remain unchanged and separate from workshop questions. No official requirement, future 2027 exam rule, pass threshold, certification equivalence or human pass-rate claim was invented.

## SEO/GEO work delivered

94 public pages, plus the existing application:

- 80 lesson pages: 40 French and 40 English.
- Eight guide pages: CMMI explained, Practitioner preparation, CMMI/Scrum/SAFe, study plan, in both languages.
- Two catalogues, two glossaries and two sources/method pages.

They contain substantive readable HTML without JavaScript, real internal links, unique titles/descriptions, self-canonical URLs, reciprocal French/English `hreflang`, Open Graph metadata and appropriate JSON-LD. Source scope, dated references and editorial responsibility are visible. Public lessons hand off to the correct interactive lesson/workshop and language.

`robots.txt`, an XML sitemap with all 95 canonical URLs and language alternates, a release manifest and a genuine missing-page 404 are published. Only the generated `dist/` tree is deployed; source scripts and test files are excluded from the deployment output. Google AI search foundations are addressed through clear text, useful answers, sources and crawlability, without claiming a special AI file or schema guarantees inclusion.

See [SEO_GEO.md](SEO_GEO.md) for implementation and measurement boundaries.

## Defects found and corrected during verification

1. **First publication omitted the changed `vercel.json`.** The application updated while new public routes returned 404. The missing configuration was committed, project build/output settings were aligned, and a regression assertion now requires building and serving `dist/`. Actual public routes and their bytes were then checked again.
2. **Language/route reload mismatch.** A deep-link language could override a later language switch on reload. The application now updates a validated permalink with current language and study route. Language, workshop, lesson and navigation reload behavior were retested locally and in live Chrome.
3. **Workshop import validation.** Imported numeric/boolean score and state fields are validated, and rendered scores are escaped. A malformed score import is rejected without changing existing progress.
4. **Browser-test environment.** The available local headless Chromium lacks H.264 codecs. Local full-app checks explicitly skipped video playback while every MP4 was decoded with FFmpeg. CI uses branded Google Chrome with codecs and does not set the skip flag. Live Chrome playback was separately observed.

## Verification evidence

| Check | Scope / result |
| --- | --- |
| Syntax and build | Python compilation, JavaScript syntax, reproducible `index.html` and generated static output passed. |
| Legacy content audits | Existing content/media release gates passed, including 99 public group cards, six PQA excerpts, 31 PA coverage per mock, disjoint mock forms and balanced answer positions. |
| Public-page audit | 94 public pages + application: valid targets/anchors, unique metadata, reciprocal languages, JSON-LD, sitemap and deployment configuration passed. |
| No-JavaScript browser reading | All 95 HTML routes opened successfully and displayed substantive content. |
| Existing lesson interactions | 40 lessons × two languages × two screen profiles: every tab, 0/5 failure, 5/5 success, required public-summary checks and completion gates passed locally. |
| Existing mocks | Eight full runs: A scored 120/120; deliberately mixed B scored 84/120, per language and screen profile. Corrections hidden until completion; domain totals, timeout denominator, history and progress export/import checked. |
| New workshops | 31 workshops × two languages × two profiles: 0/2 and 2/2 attempts, delayed explanations, analysis/draft reload, four rubric checks, example response, independent language progress, export/import and invalid import checked. |
| Permalinks | Changing language, opening another lesson and selecting another route survive reload; stale workshop parameters are removed. |
| Production HTTP | 95 HTML pages and five supporting resources compared byte-for-byte with local SHA-256; an unknown route returns HTTP 404. |
| Media | All 80 silent H.264 MP4 files decoded, 35-second metadata and five subtitle cues checked. Published hashes for all 80 MP4 + 80 VTT matched the expected manifest. Video bytes were not changed by this release. |
| Live browser sample | Public catalogue → CAR lesson → matching workshop, French 2/2, English 0/2, delayed explanations and reload/language separation observed in production. A production video loaded to readyState 4, duration 35 s, and advanced after Play. |
| GitHub Actions | PASS — workflow 39038082956 completed successfully. Both desktop and mobile jobs passed all content, media, build, legacy browser and new-workshop steps; Chrome playback was not skipped. |
| Production deployment | READY — production deployment `dpl_F4dMVN6AtWea9FbafvkLqGpM8pco` for code `a6e84a6`. All 100 checked served resources matched the final local build. |

Local browser profiles are desktop 1440×1000 and mobile-emulated 390×844, not a physical-device/Safari test. Answer-key-driven test runs validate application behavior and scoring, not learner proficiency or psychometric validity.

The current production header checks also found no `noindex` header on the sampled public pages. Source paths `/data.json` and `/app.js` returned 404. Vercel build-log access through the connector returned 404; no claim is made that those logs were inspected. Build execution was verified through GitHub Actions and actual deployed output.

## Remaining limits

- No independently reviewed mapping to every individual licensed practice or validation of official-exam equivalence.
- No measured learner outcome or defensible probability of certification success. Required official training and authorized full-model study remain separate.
- No Search Console property connected, indexing confirmed, rankings measured or AI-answer citations established. The site is technically prepared for discovery; acquisition results remain to be measured.
- No Google Analytics or other tracker installed, no paid domain purchased and no certification or accreditation status claimed.
