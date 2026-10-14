# CMMI Academy 2027 — FR/EN

[Open the app](https://cmmi-trainer.vercel.app/) · Independent learning resource, not ISACA certification.

## Curriculum

- 40 interactive lessons (9 foundations, 31 Practice Areas) with French and English explanatory texts, diagrams, original cases and graded quizzes.
- 102 public, practice-group level summaries. 276 is the *count of normative practices* in the public reference guide, **not** the number of normative practice statements licensed and reproduced on this website.
- 320 fictional evidence records, 160 conflicting interviews, 400 lesson mastery items and 481 additional quizzes.
- 102 bilingual glossary entries and Practitioner-like exam sessions (120 items/240 minutes). The simulated score is **not** an official prediction of success.
- In-browser animated explainers with free OS browser speech synthesis.
- Actual narrated FR/EN video publishing workflow under `.github/workflows/render-videos.yml`. The encoded MP4 player is displayed only if a rendered asset exists. See `VIDEO_GUIDE.md`.

## Development

Python 3. Run `python3 audit_content.py && python3 build.py` and open `index.html`. Edit `app.js`, `app.css`, and `data.json`; `build.py` embeds all three into the standalone HTML. Vercel automatically deploys the repository root.

HyperFrames authoring:

```bash
python3 generate_hyperframes.py --with-audio
npm install -g hyperframes
hyperframes render --composition video_compositions/CAR-en.html --fps 12 --quality draft --output videos/CAR-en.mp4
```

On GitHub Actions, the workflow automatically renders eight parallel batches of ten, checks audio tracks and subtitle files, then commits the 80 completed videos when all are successful. Do **not** infer that this is complete just from an Actions workflow existing.

## Official coverage and rights

The copyrighted CMMI v4.0 detailed practice statements and additional normative implementation guidance are **not** included. The CMMI Institute [Quick Reference Guide](https://cmmiinstitute.com/resource-files/public/cmmi-model-quick-reference-guide) itself says it cannot replace the model for training or appraisals. The licensed [Model Viewer](https://cmmiinstitute.com/products/cmmi/cmmi-model-viewer) gives access to the full model; its [IP sharing restrictions](https://cmmiinstitute.com/getattachment/da36326f-d5ad-4478-ad59-74ae042c688e/CMMI-MDDAP-IP-Policy-Update-Use-Cases_Feb2025_PDF.pdf) prohibit distributing detailed licensed portions to unlicensed users. We cannot circumvent that by copying leaked GitHub versions.

The authorized Building Organizational Capability course and other requirements remain prerequisites to the Practitioner certification, and organizational maturity ratings require an actual appraisal. Official content and policies may change in 2027. Get review of practice-level training and question keys by a qualified CMMI instructor before making pass-readiness claims.

CMMI® is a trademark of CMMI Institute / ISACA. HyperFrames is by HeyGen (open source; check its license). Narration uses free eSpeak voices locally (basic, robotic quality) or browser voices.