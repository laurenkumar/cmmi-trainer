#!/usr/bin/env python3
"""Verify real media bytes, captions, content, and optionally committed/served bytes."""
from pathlib import Path
import argparse,json,subprocess,hashlib,concurrent.futures,urllib.request,os
P=Path(__file__).parent
def sha(b):return hashlib.sha256(b).hexdigest()
def validate(path):
 b=path.read_bytes();info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_type,codec_name,width,height,pix_fmt','-of','json',str(path)]))
 assert [x['codec_type'] for x in info['streams']]==['video'],path
 v=info['streams'][0];assert v['codec_name']=='h264' and v['width']==960 and v['height']==540 and v['pix_fmt']=='yuv420p',path
 assert abs(float(info['format']['duration'])-35)<.15,path
 # Decode every frame; a valid header does not establish playable content.
 subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(path),'-f','null','-'],check=True,capture_output=True)
 cap=path.with_suffix('.vtt').read_text();assert cap.startswith('WEBVTT') and cap.count('-->')==5,path
 return path.stem,{'sha256':sha(b),'captionSha256':sha(path.with_suffix('.vtt').read_bytes()),'bytes':len(b),'duration':float(info['format']['duration']),'width':960,'height':540,'audio':False,'codec':'h264','captions':5}
def main():
 p=argparse.ArgumentParser();p.add_argument('--write-manifest',action='store_true');p.add_argument('--git-ref');p.add_argument('--base-url');p.add_argument('--render-run',default=os.getenv('GITHUB_RUN_ID'));p.add_argument('--render-commit',default=os.getenv('RENDER_SHA'));args=p.parse_args()
 d=json.loads((P/'data.json').read_text());expected={f'{x["id"]}-{lang}' for x in d['areas']+d['foundations'] for lang in ('fr','en')}
 paths=sorted((P/'videos').glob('*.mp4'));assert {p.stem for p in paths}==expected
 assert {p.stem for p in (P/'videos').glob('*.vtt')}==expected
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:manifest=dict(e.map(validate,paths))
 if args.write_manifest:
  d['videoManifest']=manifest;(P/'data.json').write_text(json.dumps(d,ensure_ascii=False,separators=(',',':')))
  (P/'videos'/'manifest.json').write_text(json.dumps({'release':d['contentRevision'],'renderSourceRun':args.render_run,'renderSourceCommit':args.render_commit,'videos':manifest},indent=2))
 else:assert d.get('videoManifest')==manifest,'Manifest mismatch; media changed after validation'
 if args.git_ref:
  for stem,m in manifest.items():
   for ext,key in [('mp4','sha256'),('vtt','captionSha256')]:
    b=subprocess.check_output(['git','show',f'{args.git_ref}:videos/{stem}.{ext}'],cwd=P);assert sha(b)==m[key],stem
 if args.base_url:
  def check(item):
   stem,m=item
   for ext,key in [('mp4','sha256'),('vtt','captionSha256')]:
    req=urllib.request.Request(args.base_url.rstrip('/')+f'/videos/{stem}.{ext}?verify={m[key][:12]}')
    with urllib.request.urlopen(req,timeout=45) as r:
     assert r.status==200 and sha(r.read())==m[key],stem
   return stem
  with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:assert len(list(e.map(check,manifest.items())))==80
 print(f'PASS: 80 decoded silent H264 MP4 + 80 five-cue VTT; hashes '+('match production' if args.base_url else 'verified'))
if __name__=='__main__':main()
