"""Independent automated gate: localization, source trace, accessibility hooks, mastery rigor."""
from pathlib import Path
import json,collections,re
P=Path(__file__).resolve().parent; D=json.loads((P/'data.json').read_text());allL=D['foundations']+D['areas']
assert len(D['areas'])==31 and len(D['foundations'])==9
assert len(D['glossary'])==102
assert all(w['fr'].strip() and w['fr']!='Terme métier' and len(w['definitionFr'])>25 for w in D['glossary'])
assert sum(len(a['deep']['levelFr']) for a in D['areas'])==102
assert sum(a['officialPracticeCount'] for a in D['areas'])==276
for a in allL:
 assert len(a['practiceWalkthrough']['fr'])==len(a['practiceWalkthrough']['en'])==4,a['id']
 for lang in ('fr','en'):
  assert len(a['videoScenes'][lang])==6,a['id']
  assert len(a['caseLab'][lang]['artifacts'])==(5 if a in D['areas'] else 4) and len(a['caseLab'][lang]['interviews'])==2
  q=a['masteryQuestions'][lang];assert len(q)==5,a['id']
  assert len({x['q'] for x in q})==5
  for x in q:
   assert len(x['options'])==4 and len(set(x['options']))==4,(a['id'],lang,x['id'])
   assert 0<=x['answer']<4 and len(x['why'])>60,(a['id'],x['id'])
  for video in a['videoScenes'][lang]:
   assert all(video.get(k) for k in ['heading','caption','speech'])
 assert a['en'].get('title') and a['deep'].get('paragraphs')
 if a in D['areas']:
  assert set(a['levelsEn'])==set(a['deep']['levelFr'])
  assert 0 < len(a['practiceGroupsCovered']) <= 5
for lang in ('fr','en'):
 q=[qq for a in allL for qq in a['masteryQuestions'][lang]]
 assert len(q)==200 and len({qq['q'] for qq in q})>=95
print('PASS: 40 bilingual lessons, 102 PG summaries, 276 quick-guide practice counts, 80 videos, 382 bilingual fictional documents, 160 interviews, 400 mastery questions, 102 full French glossary definitions.')
print('Coverage warning: normative full CMMI model practices are NOT present; current license-backed model not supplied.')
print('Vocab note: English pronunciation depends on installed browser TTS voices.')