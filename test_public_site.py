#!/usr/bin/env python3
"""Audit generated content, reciprocal language links and real internal targets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json,collections,xml.etree.ElementTree as ET
from content.workshops import W
BASE='https://cmmi-trainer.vercel.app'
ROOT=Path(__file__).parent/'dist'
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.links=[];self.lang=None;self.h1=0;self.ids=set();self.canonical=[];self.alternates={};self.desc=[];self.schemas=[];self.schema=False;self.title='';self.in_title=False;self.text=[];self.skip=0;self.feed(s)
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='html':self.lang=a.get('lang')
  if t=='h1':self.h1+=1
  if t in ('script','style'):self.skip+=1
  if t=='title':self.in_title=True
  if a.get('id'):self.ids.add(a['id'])
  if t in ['a','link'] and a.get('href'):self.links.append(a['href'])
  if t=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if t=='link' and a.get('hreflang'):self.alternates[a['hreflang']]=a['href']
  if t=='meta' and a.get('name')=='description':self.desc.append(a['content'])
  if t=='script' and a.get('type')=='application/ld+json':self.schema=True
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip-=1
  if t=='script':self.schema=False
  if t=='title':self.in_title=False
 def handle_data(self,s):
  if self.schema:self.schemas.append(json.loads(s))
  if self.in_title:self.title+=s
  if self.skip==0:self.text.append(s)
pages={}
for file in ROOT.rglob('index.html'):
 path='/'+str(file.relative_to(ROOT).parent).replace('.','').strip('/')+'/'
 if path=='//':path='/'
 pages[path]=Page(file.read_text())
assert len(pages)==95,len(pages)
titles=[];descs=[]
for path,p in pages.items():
 assert p.h1==1,(path,'h1',p.h1)
 assert p.canonical==[BASE+path],(path,p.canonical)
 assert len(p.desc)==1 and len(p.desc[0])>=30,path
 if path!='/':
  assert p.lang==path[1:3],path
  assert set(p.alternates)=={'fr','en','x-default'},path
  assert len(' '.join(p.text).split())>90,path
  assert len(p.schemas)==1 and p.schemas[0]['@context']=='https://schema.org',path
  for lang in ['fr','en']:
   other='/'+lang+path[3:]
   assert p.alternates[lang]==BASE+other,path
   assert pages[other].alternates[p.lang]==BASE+path,(path,other)
  assert p.alternates['x-default']==BASE+'/en'+path[3:],path
 titles.append(p.title);descs.extend(p.desc)
 for href in p.links:
  u=urlsplit(href)
  if u.netloc and u.netloc!='cmmi-trainer.vercel.app':continue
  target=unquote(u.path) or path
  dest=ROOT/target.lstrip('/')
  assert (dest/'index.html').exists() if target.endswith('/') else dest.is_file(),(path,href,'broken link')
  if u.fragment and target in pages:assert u.fragment in pages[target].ids,(path,href,'missing anchor')
assert len(set(titles))==len(titles),'duplicate titles'
assert len(set(descs))==len(descs),'duplicate descriptions'
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
listed={el.text.removeprefix(BASE) for el in ET.parse(ROOT/'sitemap.xml').findall('.//s:loc',ns)}
assert listed==set(pages),(len(listed),len(pages))
assert 'Allow: /' in (ROOT/'robots.txt').read_text()
assert not any((ROOT/p).exists() for p in ['data.json','app.js','build.py','content','node_modules'])
cfg=json.loads(Path('vercel.json').read_text())
assert cfg.get('outputDirectory')=='dist' and cfg.get('buildCommand')=='python3 build.py','Deploy must build and serve the audited static output'
D=json.loads(Path('data.json').read_text())
for code,w in W.items():
 assert len(w['records'])==3 and len(w['rubric'])==4
 for lang in ['fr','en']:
  assert len(w['concept'][lang].split())>=10,code
  assert len(w['sample'][lang].split())>=25,code
  assert all(len(r[lang].split())>=5 for r in w['records']),code
  for q in w['questions']:
   assert len(q['options'])==4 and 0<=q['answer']<4
   assert len({v[lang] for v in q['options']})==4
   assert q['options'][q['answer']][lang] not in q['prompt'][lang]
   assert q['prompt'][lang] not in {v['q'] for f in D['mockExamForms'].values() for v in f[lang]}
assert len({w['concept']['fr'] for w in W.values()})==31
assert len({w['sample']['en'] for w in W.values()})==31
print('PASS: 94 bilingual public pages + app; unique titles/descriptions; real links/anchors; reciprocal hreflang; JSON-LD; sitemap; deploy output; 31 original bilingual workshops / 62 decisions per language.')
