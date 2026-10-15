# Videos: silent bilingual HyperFrames capsules

40 lessons × French/English = 80 silent, 35-second MP4 capsules with five caption cues each. These are revision summaries; the detailed teaching lives in the lessons and case files.

## Render and publish

The render workflow uses eight shards and HyperFrames 0.8.161. Each shard uploads ten MP4 and ten VTT files. The publish job downloads to `rendered/`, fast-forwards `main` while the assets are still separate, rejects source drift and partial batches, then installs and validates the new files. It never resets tracked assets after downloading.

`validate_release.py --write-manifest` fully decodes media and records hashes. `--git-ref HEAD` verifies committed bytes; `--base-url https://cmmi-trainer.vercel.app` compares all 160 public media resources with those hashes. `videos/manifest.json` records source run and commit. The player uses hashes in asset URLs.

The recovery workflow accepts only a successful render run from this repository. Recovery refuses lessons changed since that render; run a fresh render in that case.

A green run or a commit alone is insufficient: inspect publication, deployment, public hashes, range serving and browser playback.
