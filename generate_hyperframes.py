#!/usr/bin/env python3
"""Build audio-synchronized native HyperFrames compositions for every lesson in FR/EN.

All speech is original project curriculum text. Offline synthesis uses espeak + ffmpeg
(no external API, commercial voice or subscription). Run `python generate_hyperframes.py`.
"""
import argparse, html, json, re, shutil, subprocess, wave
from pathlib import Path

P=Path(__file__).resolve().parent
D=json.loads((P/'data.json').read_text(encoding='utf-8'))
LESSONS=D['foundations']+D['areas']
CSS='''
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;background:#091b2b;color:#fff;font-family:Arial,Helvetica,sans-serif;overflow:hidden}
#composition{position:relative;width:960px;height:540px;overflow:hidden;background:radial-gradient(circle at 28% 18%,#1c6072 0%,#0d334a 44%,#091b2b 85%)}
.clip{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:42px 70px}
.tag{font-size:17px;letter-spacing:3px;color:#67e7da;font-weight:800}
.title{font-size:44px;line-height:1.10;font-weight:800;margin:25px 0 20px;max-width:820px}
.caption{font-size:25px;line-height:1.36;color:#dceff8;max-width:800px}
.sceneNumber{position:absolute;bottom:35px;font-size:17px;color:#8ddbd8}
.watermark{position:absolute;bottom:12px;right:20px;color:#95aebf;font-size:12px}
.bgOrb{position:absolute;left:-100px;bottom:-80px;width:430px;height:430px;border:2px solid #61e9d336;border-radius:50%}
#composition:after{content:'';position:absolute;right:-95px;top:-95px;width:330px;height:330px;border:1px solid #ffffff20;border-radius:50%;pointer-events:none}
'''

def run(args):
    proc=subprocess.run(args, capture_output=True, text=True)
    if proc.returncode: raise RuntimeError(f'{args[0]} failed: {proc.stderr[-1200:]}')


def duration_wav(path):
    with wave.open(str(path),'rb') as w:return w.getnframes()/w.getframerate()


def vtt_time(seconds):
    n=round(seconds*1000);ms=n%1000;n//=1000;sec=n%60;n//=60;minute=n%60;hour=n//60
    return f'{hour:02d}:{minute:02d}:{sec:02d}.{ms:03d}'


def generate(selected=None, with_audio=False, outdir=None):
    outdir=outdir or P/'video_compositions';outdir.mkdir(parents=True,exist_ok=True)
    if with_audio and not shutil.which('espeak'):raise RuntimeError('espeak is required for offline speech')
    vids=0
    for a in LESSONS:
        for lang in ('fr','en'):
            name=f'{a["id"]}-{lang}'
            if selected is not None and name not in selected:continue
            scenes=a['videoScenes'][lang]
            clips=[];audio=[];subtitles=['WEBVTT',''];t=0
            for i,sc in enumerate(scenes):
                audiofile=outdir/'audio'/f'{name}-{i+1:02d}.wav'
                if with_audio:
                    audiofile.parent.mkdir(parents=True,exist_ok=True)
                    text=' '.join(sc['speech'].split())
                    # eSpeak is 100% local, deterministic and does not require internet.
                    run(['espeak','-v',lang,'-s','165','-a','150','-w',str(audiofile),text])
                    audio_duration=duration_wav(audiofile)
                else:
                    audio_duration=max(7.0,len(sc['speech'].split())/2.8)
                n=round(max(7.5,audio_duration+1.0),2)
                clips.append(f'<section id="slide-{i+1}" class="clip" data-start="{t:.2f}" data-duration="{n:.2f}" data-track-index="1"><span class="tag">CMMI ACADEMY · {html.escape(a["id"])} · {lang.upper()}</span><div class="title">{html.escape(sc["heading"])}</div><div class="caption">{html.escape(sc["caption"])}</div><div class="sceneNumber">{i+1} / {len(scenes)}</div></section>')
                if with_audio:
                    audio.append(f'<audio id="voice-{i+1}" src="audio/{audiofile.name}" data-start="{t:.2f}" data-duration="{audio_duration:.2f}" data-track-index="2" preload="auto"></audio>')
                subtitles+= [str(i+1),f'{vtt_time(t)} --> {vtt_time(t+n)}',sc['speech'].strip(),'']
                t+=n
            # data-no-timeline is supported for pure timed-clip projects. Never create a fake JS timeline.
            markup=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}</style></head><body><main id="composition" data-composition-id="{name}" data-no-timeline data-start="0" data-duration="{t:.2f}" data-width="960" data-height="540"><div class="bgOrb"></div>{''.join(clips)}{''.join(audio)}<div class="watermark">Independent educational content · not an official CMMI exam</div></main></body></html>'''
            (outdir/f'{name}.html').write_text(markup,encoding='utf-8')
            subtitles_file=outdir/f'{name}.vtt'
            subtitles_file.write_text('\n'.join(subtitles),encoding='utf-8')
            vids+=1
    print(f'Generated {vids} HyperFrames compositions (audio={with_audio}) in {outdir}')
    return vids

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--with-audio',action='store_true')
    parser.add_argument('--shard',type=int,default=None,help='0..7, each shard is ten lesson-language compositions')
    parser.add_argument('--count-shards',type=int,default=8)
    parser.add_argument('--outdir',type=Path,default=None)
    args=parser.parse_args()
    names=[f'{a["id"]}-{lang}' for a in LESSONS for lang in ('fr','en')]
    selected=None if args.shard is None else {n for i,n in enumerate(names) if i%args.count_shards==args.shard}
    generate(selected=selected,with_audio=args.with_audio,outdir=args.outdir)