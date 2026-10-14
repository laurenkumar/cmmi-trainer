#!/usr/bin/env python3
"""Render-ready, silent Cartesian motion stories for all 40 lessons, FR+EN.

Source: original project learning text and public PG summary interpretations.
Follows heygen-com/hyperframes composition timing, no synthetic narration or audio assets.
"""
import argparse, html, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'data.json').read_text(encoding='utf-8'))
COURSES=DATA['foundations']+DATA['areas']
ES=html.escape

def concise(s,n=105):
 s=re.sub(r'\s+',' ',re.sub(r'\*\*','',str(s or ''))).strip().strip(' .')
 if len(s)<=n:return s
 sub=s[:n].rsplit(' ',1)[0]
 return sub+'…'

def line_item(code,text):
 return '<div class="entry"><span class="entry-no">'+ES(code)+'</span><span>'+ES(concise(text,81))+'</span></div>'

def root_css():
 return '''
:root{--paper:#f7f3e9;--paper2:#ece7db;--ink:#282822;--stone:#a59a89;--muted:#6d695e;--pine:#526458;--terracotta:#b47761;--line:#cfc7b9}
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:var(--paper);color:var(--ink);font-family:Arial,Helvetica,sans-serif}
#stage{height:100%;width:100%;position:relative;overflow:hidden;background:var(--paper)}
#stage:before{content:'';position:absolute;inset:0;opacity:.36;pointer-events:none;background-image:linear-gradient(to right,transparent 119px,var(--line) 120px,transparent 121px),linear-gradient(to bottom,transparent 119px,var(--line) 120px,transparent 121px);background-size:120px 120px}
#stage:after{content:'';position:absolute;left:38px;top:35px;bottom:34px;width:1px;background:var(--line)}
.clip{position:absolute;inset:0;overflow:hidden;padding:42px 70px 55px;display:flex;flex-direction:column}
.kicker{font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:2.5px;color:var(--pine)}
.hairline{height:1px;background:var(--line);width:100%;margin:19px 0}
.mainTitle{font-family:Georgia,'Times New Roman',serif;font-size:54px;line-height:1.05;letter-spacing:-1.6px;font-weight:400;max-width:800px;margin:18px 0 12px}
.mainTitle.small{font-size:45px}.deck{font-size:21px;line-height:1.4;color:var(--muted);max-width:770px;margin:6px 0}
.label{font-size:12px;color:var(--muted);font-weight:700;letter-spacing:1.4px;text-transform:uppercase}
.footer{position:absolute;bottom:22px;left:69px;right:60px;font-size:11px;letter-spacing:2px;display:flex;justify-content:space-between;color:var(--muted);text-transform:uppercase}
.chart{display:flex;align-items:flex-end;gap:13px;border-left:1px solid var(--ink);border-bottom:1px solid var(--ink);height:160px;width:300px;padding:0 22px;position:relative}
.chart:before{content:'';position:absolute;inset:20px 0 30px;border-top:1px dashed var(--line)}
.bar{width:35px;background:var(--stone);border-top:3px solid var(--pine);position:relative}
.bar:nth-child(2){background:#b9a994}.bar:nth-child(3){background:#b3c0b6}.bar:nth-child(4){background:#8eaa9a}
.chartLabel{font-size:10px;position:absolute;bottom:-23px;left:0;width:100%;text-align:center}
.split{display:grid;grid-template-columns:1fr 1fr;gap:25px;align-items:stretch;margin-top:22px;max-height:390px}
.card{border:1px solid var(--line);padding:24px;background:#faf8f2;min-height:212px}
.card.bad{background:#f0eae1}.card.good{background:#eaf0ea}
.card .cap{font-size:11px;font-weight:800;letter-spacing:2px;color:var(--muted);text-transform:uppercase;display:block;margin-bottom:14px}
.card .big{font-family:Georgia,'Times New Roman',serif;font-size:26px;line-height:1.22;margin:0}
.card .tiny{font-size:15px;line-height:1.38;color:var(--muted);margin:14px 0 0}
.rowpath{display:flex;gap:0;width:100%;align-items:center;margin-top:28px}
.node{background:#f6f1e7;border:1px solid #c6bbad;min-height:150px;flex:1;display:flex;flex-direction:column;justify-content:space-between;padding:17px 15px}
.node:nth-of-type(3){background:#eceee7}.node:nth-of-type(5){background:#e4eade}.node:nth-of-type(7){background:#dce6db}
.node strong{font-size:22px;line-height:1.24;font-family:Georgia,'Times New Roman',serif;font-weight:400}
.node small{font-size:11px;font-weight:800;letter-spacing:1px;color:var(--pine)}
.arrow{font-size:22px;color:var(--stone);padding:0 7px}
.ladder{display:flex;gap:11px;align-items:flex-end;height:210px;margin-top:36px}
.level{display:flex;align-items:center;justify-content:center;flex-direction:column;width:132px;background:var(--paper2);border:1px solid var(--line);text-align:center;position:relative}
.level b{font-size:40px;font-family:Georgia,serif;font-weight:400}.level small{font-size:11px;letter-spacing:1px;color:var(--muted)}
.level:nth-child(2){background:#ecece2}.level:nth-child(3){background:#dbe6d9}.level:nth-child(4){background:#c6d9c9}.level:nth-child(5){background:#a5c3ad}
.question{font-family:Georgia,serif;font-size:32px;line-height:1.22;margin:19px 0;color:var(--ink)}
.rule-note{display:flex;gap:15px;align-items:flex-start;padding:16px;border-top:1px solid var(--line);font-size:17px;color:var(--muted)}
.rule-note b{font-family:Georgia,serif;font-size:31px;color:var(--pine);font-weight:400}
.aside-tag{position:absolute;top:44px;right:60px;border:1px solid var(--line);padding:9px 14px;font-size:12px;letter-spacing:1px;color:var(--muted);font-weight:700}
.axis{position:absolute;right:55px;bottom:95px;width:190px;height:140px;border-left:1px solid var(--stone);border-bottom:1px solid var(--stone)}
.axis:before{content:'';position:absolute;inset:20px;border-bottom:1px dashed #c7b9aa;transform:rotate(-25deg)}
.axis i{position:absolute;display:block;width:10px;height:10px;background:var(--pine);border-radius:50%;top:28px;right:35px}
.progress{position:absolute;left:0;bottom:0;background:var(--pine);height:5px}
.compact{font-size:42px}
'''

def make(lesson,lang):
 ispa='domain' in lesson
 title=(lesson.get('en',{}).get('title') if lang=='en' else lesson.get('title')) or lesson.get('title')
 code=lesson['id']; ident=ES(code); length=35
 en=lang=='en'
 label=('PUBLIC PRACTICE GROUP SUMMARY' if en else 'SYNTHÈSE PUBLIQUE DES NIVEAUX')
 steps=(lesson['en'].get('steps') if en else lesson['deep'].get('steps')) or lesson['deep'].get('steps') or []
 steps=[(str(i+1).zfill(2),s[1] if isinstance(s,(list,tuple)) and len(s)>1 else str(s)) for i,s in enumerate(steps[:4])]
 while len(steps)<4:steps.append((str(len(steps)+1).zfill(2),'Review and document outcomes' if en else 'Examiner les résultats'))
 course=lesson.get('publicGroupCourse',{});
 pgs=course.get('entries',[])
 groups=[(x['groupLevel'],x[lang]['concept'].split(': ',1)[-1]) for x in pgs]
 if not groups and ispa: groups=[(int(k),s) for k,s in lesson.get('levelsEn',{}).items()]
 if not groups:groups=[(1,'Identify'),(2,'Manage'),(3,'Improve')]
 contrast=lesson['deep'].get('evidenceContrast') or []
 good=(contrast[0] if contrast and len(contrast[0])<94 else lesson.get('evidence','')) if not en else lesson.get('en',{}).get('evidence','')
 bad=(contrast[1] if len(contrast)>1 else lesson.get('pitfall','')) if not en else lesson.get('en',{}).get('pitfall','')
 scenario=lesson['en'].get('scenario') if en else lesson.get('scenario')
 scenario=scenario or lesson['deep'].get('story')
 title=concise(title,62)
 cards=[]
 # 01: conceptual problem map
 cards.append(f'''<section class="clip" data-start="0" data-duration="7" data-track-index="1"><div class="kicker">CMMI ACADEMY / {ident} / {lang.upper()}</div><div class="hairline"></div><h1 class="mainTitle">{ES(title)}</h1><p class="deck">{ES(concise(scenario,110))}</p><div class="axis"><i></i></div><div class="footer"><span>{ES('Understand → Apply → Verify' if en else 'Comprendre → Appliquer → Vérifier')}</span><span>01 / 05</span></div><div class="progress" style="width:20%"></div></section>''')
 # 02: process is NOT generic narration; graphical causal path from the module's steps
 step_html=''.join(f'<div class="node"><small>{ES(k)}</small><strong>{ES(concise(text,52))}</strong></div>'+('<div class="arrow">→</div>' if i<3 else '') for i,(k,text) in enumerate(steps))
 cards.append(f'''<section class="clip" data-start="7" data-duration="7" data-track-index="1"><div class="kicker">{ES('01 / METHOD IN ACTION' if en else '01 / MÉTHODE APPLIQUÉE')}</div><div class="hairline"></div><h2 class="mainTitle small">{ES('From problem to action' if en else 'Du problème à l’action')}</h2><div class="rowpath">{step_html}</div><p class="deck" style="font-size:17px;margin-top:20px">{ES('Follow the full chain; a document alone is not proof.' if en else 'Suivre la chaîne complète : un document seul ne suffit pas.')}</p><div class="footer"><span>CMMI / {ident}</span><span>02 / 05</span></div><div class="progress" style="width:40%"></div></section>''')
 # 03: evidence comparison directly relates to real learning content
 cards.append(f'''<section class="clip" data-start="14" data-duration="7" data-track-index="1"><div class="kicker">{ES('02 / EVIDENCE TRIANGULATION' if en else '02 / CROISEMENT DES PREUVES')}</div><div class="hairline"></div><h2 class="mainTitle small">{ES('Claim versus evidence' if en else 'Affirmation ou preuve ?')}</h2><div class="split"><div class="card bad"><span class="cap">{ES('WEAK SIGNAL' if en else 'INDICE FAIBLE')}</span><p class="big">{ES(concise(bad,98))}</p></div><div class="card good"><span class="cap">{ES('BETTER SUPPORT' if en else 'TRACE PLUS SOLIDE')}</span><p class="big">{ES(concise(good,112))}</p></div></div><div class="footer"><span>{ES('Corroboration before conclusion' if en else 'Recouper avant de conclure')}</span><span>03 / 05</span></div><div class="progress" style="width:60%"></div></section>''')
 # 04: true PG ladder, not invented individual practice ids
 levels=''.join(f'<div class="level" style="height:{78+j*28}px"><small>PG</small><b>{lv}</b></div>' for j,(lv,txt) in enumerate(groups))
 highlight=groups[-1][1] if groups else ''
 cards.append(f'''<section class="clip" data-start="21" data-duration="7" data-track-index="1"><div class="kicker">{ES(label)}</div><div class="hairline"></div><h2 class="mainTitle small">{ES('Progressive practice groups' if en else 'Progression des Practice Groups')}</h2><div class="ladder">{levels}</div><p class="deck" style="font-size:16px;margin-top:17px">PG{groups[-1][0]} — {ES(concise(highlight,111))}</p><div class="footer"><span>{ES('Public PG summaries ≠ licensed individual practices' if en else 'Résumé public ≠ pratiques normatives complètes')}</span><span>04 / 05</span></div><div class="progress" style="width:80%"></div></section>''')
 # 05: unique specific review question
 what=lesson['en'].get('evidence') if en else lesson.get('evidence')
 prompt=('What independent record would prove this was performed?' if en else 'Quelle trace indépendante permettrait de vérifier l’exécution ?')
 cards.append(f'''<section class="clip" data-start="28" data-duration="7" data-track-index="1"><div class="kicker">{ES('03 / ACTIVE RECALL' if en else '03 / MÉMORISATION ACTIVE')}</div><div class="hairline"></div><h2 class="mainTitle small">{ES('Your next audit question' if en else 'Ta prochaine question d’audit')}</h2><p class="question">{ES(prompt)}</p><div class="rule-note"><b>↗</b><span>{ES(concise(what,143))}</span></div><div class="aside-tag">{ES('Pause to answer' if en else 'Pause et réponds')}</div><div class="footer"><span>{ES('Study the practice group cards in the app' if en else 'Approfondis avec les cartes de niveaux')}</span><span>05 / 05</span></div><div class="progress" style="width:100%"></div></section>''')
 section='\n'.join(cards)
 css=root_css()
 doc=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{ES(title)}</title><style>{css}</style></head><body><div id="stage" data-composition-id="cmmi-{ident}-{lang}" data-start="0" data-duration="{length}" data-width="960" data-height="540">{section}</div><script src="https://cdn.jsdelivr.net/npm/gsap@3.12.7/dist/gsap.min.js"></script><script>window.__timelines=window.__timelines||{{}};const tl=window.gsap?gsap.timeline({{paused:true}}):null;if(tl){{document.querySelectorAll('.clip').forEach((scene)=>{{const s=Number(scene.dataset.start);tl.fromTo(scene.querySelector('.mainTitle'),{{opacity:0,y:18}},{{opacity:1,y:0,duration:.6,ease:'power2.out'}},s+.18);}});window.__timelines['cmmi-{ident}-{lang}']=tl;}}</script></body></html>'''
 vtt=['WEBVTT','']
 for i,t in enumerate([0,7,14,21,28]):
  label_text=['Concept','Workflow','Evidence','Practice groups','Apply'][i] if en else ['Notion','Processus','Preuves','Niveaux','Application'][i]
  vtt.extend([str(i+1),f'00:00:{t:02d}.000 --> 00:00:{t+7:02d}.000',f'{title} — {label_text}',''])
 return doc,'\n'.join(vtt)

def generate(shard=None,output=None,selected=None):
 out=Path(output) if output else ROOT/'video_compositions';out.mkdir(parents=True,exist_ok=True)
 made=[]
 for i,lesson in enumerate(COURSES):
  for lang in ('fr','en'):
   filename=f'{lesson["id"]}-{lang}'
   if selected and filename not in selected:continue
   if shard is not None and (i*2+(0 if lang=='fr' else 1))//10!=shard:continue
   html_text,vtt=make(lesson,lang)
   (out/f'{filename}.html').write_text(html_text,encoding='utf-8')
   (out/f'{filename}.vtt').write_text(vtt,encoding='utf-8')
   made.append(filename)
 print(f'Cartesian silent video compositions: {len(made)} / 80 ({", ".join(made[:4])})')
 return made

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--shard',type=int);p.add_argument('--output');p.add_argument('--selected',action='append');p.add_argument('--with-audio',action='store_true',help='Deprecated: always silent')
 a=p.parse_args();generate(a.shard,a.output,set(a.selected) if a.selected else None)