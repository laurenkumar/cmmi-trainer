# CMMI Academy 2027 — independent public-source learning

Live site: <https://cmmi-trainer.vercel.app/> · Release R10 · French / English.
Public reading: [/fr/](https://cmmi-trainer.vercel.app/fr/) and [/en/](https://cmmi-trainer.vercel.app/en/).

## Learning pathway

- 40 bilingual lessons: nine foundations and 31 Practice Areas.
- Existing applied examples, 99 public Practice Group cards and six individually published PQA practice excerpts.
- **31 new applied workshops**, with four sequences per area: understand the mechanism, examine three fictional records, make two decisions, produce and self-review a deliverable.
- **62 new decision questions per language**, with plausible competing actions and feedback only after both answers are submitted. Wrong attempts, retries and best scores are retained.
- Analysis drafts, deliverables, rubric checks and workshop progress persist separately for French and English and are included in progress export/import.
- Written work uses an explicit **self-review rubric** and an example response. Neither checkbox completion nor text length is presented as expert grading or certified proficiency.
- Two independent 120-question mock forms, A and B, per language remain unchanged. They follow the public 2026 blueprint but are not psychometrically validated replicas of the official exam.
- 80 existing silent HyperFrames revision videos, 35 seconds each, with captions. This release does not re-render or replace their bytes.
- Existing lesson progress is preserved; new workshop progress has its own 31-workshop counter. Official examination eligibility and certification remain outside this application.

## Public discovery and reading

The build creates **94 crawlable bilingual HTML pages**: 80 lesson pages, eight practical guide pages, two catalogues, two glossaries and two sources/method pages. Their substantive content, links and navigation work without JavaScript.

Each page has a unique title/description, canonical URL, reciprocal `hreflang`, Open Graph metadata, visible source attribution and matching JSON-LD. The release also publishes `robots.txt`, a sitemap with language alternates and `/release.json`. Public lessons hand off to the matching interactive lesson or workshop, preserving local progress.

See [SEO_GEO.md](SEO_GEO.md) for scope and measurement. Technical crawlability does not prove search-engine indexing, ranking, or citation in an AI answer.

## Build and verification

Editable sources: `data.json`, `app.js`, `app.css`, `content/`, `public_site.py`, `reading.css`.
`build.py` generates the standalone root `index.html` and the deployable `dist/` tree.
Vercel builds `dist/`; source scripts, tests and node modules are not in that deployment output.

```sh
npm ci --ignore-scripts
python3 build.py
node --check app.js
python3 audit_release.py
python3 test_public_site.py
python3 validate_release.py --git-ref HEAD
npx playwright install --with-deps chrome
CHROMIUM_CHANNEL=chrome npm test
CHROMIUM_CHANNEL=chrome npm run test:workshops
```

Python 3, Node.js 22+, FFmpeg/ffprobe and Google Chrome (including H.264 codecs) are used for verification.
`QA_SCREEN=desktop` / `mobile` select the screen profile; `BASE_URL` runs the browser flows against a published release. GitHub Actions runs both profiles in separate jobs and uploads both old and new browser-test reports.

A restricted local runtime can set `CHROMIUM_PATH` and `CHROMIUM_ARGS` for an available browser. `SKIP_MEDIA_PLAYBACK=1` is an explicit local-only fallback for Chromium builds without H.264 support; it is **not set in CI**, and such a run is not evidence of browser video playback. FFmpeg decoding, production hashes and compatible-browser playback are separate evidence.

To compare every published video and subtitle with the local manifest:

```sh
python3 validate_release.py --base-url https://cmmi-trainer.vercel.app
```

See [VIDEO_GUIDE.md](VIDEO_GUIDE.md) for rendering/publication and [AUDIT_R10.md](AUDIT_R10.md) for this release's verification evidence and limitations.

## Source scope

The public 2026 Quick Reference Guide summarizes PA/PG topics and six PQA practice excerpts. It does not replace the licensed full model. The **276 individual normative statements are not reproduced or reconstructed**. Workshop cases, numbers, decisions, example responses and rubrics are original teaching material, not official requirements.

- [CMMI Model Quick Reference Guide v4.0](https://www.isaca.org/resources/reference-guide/cmmi-model-quick-reference-guide), 25 August 2026.
- [CMMI Credentialing Guide for Practitioners](https://cmmiinstitute.com/getattachment/8051d124-5dd9-44fd-9bf0-4842c6d58b16/CMMI-Credentialing-Guide-for-Practitioners.pdf), 31 August 2026.
- [Practitioner Policy](https://cmmiinstitute.com/getattachment/dfa7876d-b91e-4fd6-84f6-b6283f099a13/POLICY-CMMI-Certification-Certified-CMMI-Practitioner-Policy.pdf), 14 July 2026.

Public exam references describe BOC training, 120 questions and four hours. Some current policy text still references v3.0 while the quick guide is v4.0; verify the version and rules applicable to the actual session. This project's 2027 name is not a prediction of 2027 rules. The learning threshold of 80% is not the official passing threshold. Translations, exam equivalence and human learning effectiveness have not been independently certified.
