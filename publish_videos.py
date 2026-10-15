#!/usr/bin/env python3
"""Install one complete render batch after updating the branch, never before.

The incoming directory is outside tracked videos, so a branch update cannot
silently overwrite the rendered bytes. Partial batches fail before installation.
"""
import argparse, json, shutil, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def install(incoming):
    data = json.loads((ROOT / 'data.json').read_text())
    expected = {f'{x["id"]}-{lang}.{ext}'
                for x in data['foundations'] + data['areas']
                for lang in ('fr', 'en') for ext in ('mp4', 'vtt')}
    actual = {p.name for p in incoming.iterdir() if p.suffix in ('.mp4', '.vtt')}
    if actual != expected:
        raise ValueError(f'Incomplete render batch: missing={sorted(expected-actual)}, unexpected={sorted(actual-expected)}')
    for name in sorted(expected):
        shutil.copy2(incoming / name, ROOT / 'videos' / name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('incoming', type=Path)
    parser.add_argument('--source-commit', required=True)
    args = parser.parse_args()
    subprocess.run(['git', 'fetch', 'origin', 'main'], cwd=ROOT, check=True)
    subprocess.run(['git', 'merge', '--ff-only', 'origin/main'], cwd=ROOT, check=True)
    # Never publish media against lessons that changed during rendering.
    subprocess.run(['git', 'diff', '--exit-code', args.source_commit, 'HEAD', '--',
                    'generate_hyperframes.py', 'data.json'], cwd=ROOT, check=True)
    install(args.incoming.resolve())
