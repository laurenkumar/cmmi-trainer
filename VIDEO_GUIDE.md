# 80 CMMI lessons — actual HyperFrames MP4 and offline speech

The app contains 40 lessons × 2 languages. Each has a six-scene interactive HTML explainer, and will display a native MP4 with accessible subtitles **only when successfully rendered and published**.

## Video rendering

- `generate_hyperframes.py` generates 80 HyperFrames compositions from the teaching content. It uses the framework's timed `.clip` / `data-no-timeline` contract, not an invented JS timeline.
- `python3 generate_hyperframes.py --with-audio` generates 480 WAV narration segments with **eSpeak**, entirely locally and free of charge, plus bilingual `.vtt` captions. French and English are synthesized natively, not translated by the TTS engine.
- Real MP4 files are rendered using the official [HyperFrames CLI](https://github.com/heygen-com/hyperframes) via `hyperframes render` and checked with `ffprobe` to ensure an audio stream is present.
- `.github/workflows/render-videos.yml` splits generation into eight parallel jobs, verifies all 80 rendered MP4/VTT pairs, then commits `videos/` on main. Vercel's existing GitHub integration should deploy the new assets.

## Workflow status

The source compositions alone **are not MP4 files**. Run the GitHub Actions workflow `Render 80 bilingual HyperFrames lessons`, or let its trigger run when the generator or lesson data is updated. Do **not** claim videos are available until the workflow succeeds and `videos/*.mp4` exist on GitHub and Vercel.

Local rendering requires Node.js 22, official `hyperframes` npm CLI, Chrome/Chromium, FFmpeg and eSpeak. The current ChatGPT container cannot download the npm package due to unavailable DNS; the CI workflow installs it on GitHub-hosted runners. A rendered track is free software-generated speech; quality is intentionally basic compared to paid neural voices.

To reproduce one file:

```bash
python3 generate_hyperframes.py --with-audio
npm install -g hyperframes
hyperframes render --composition video_compositions/CAR-en.html --fps 12 --quality draft --output videos/CAR-en.mp4
ffprobe -v error -show_entries format=duration videos/CAR-en.mp4
```

No copyrighted full normative CMMI model content is packaged. Narration follows original educational scenarios and public summaries.