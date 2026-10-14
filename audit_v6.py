#!/usr/bin/env python3
"""Read-only content checks for the publicly documented PQA micro-course and held-out mocks."""
import json, re, collections
from pathlib import Path
p=Path(__file__).parent
d=json.loads((p/'data.json').read_text(encoding='utf-8'))
assert len(d['areas'])==31 and len(d['foundations'])==9
pqa=next(a for a in d['areas'] if a['id']=='PQA')['publicPracticeLesson']
assert [v['code'] for v in pqa['entries']]==['PQA 1.1','PQA 2.1','PQA 2.2','PQA 2.3','PQA 2.4','PQA 3.1']
assert [v['level'] for v in pqa['entries']]==[1,2,2,2,2,3]
assert len(pqa['diagnostics'])==6
for item in pqa['entries']:
 for lang in ('fr','en'):
  assert all(len(item[lang][key])>=25 for key in ('explanation','workedExample','evidence','pitfall'))
for a in d['areas']:
 assert set(a['levelsEn'])==set(a['deep']['levelFr']),a['id']
assert len(d['questions'])>=275 and len(d['enQuestions'])>=206
expected={'CORE':60,'DEV':18,'SVC':18,'SEC':6,'SPM':6,'DATA':6,'PPL':6}
for lang in ('fr','en'):
 all_exams=[]
 for form in ('A','B'):
  qs=d['mockExamForms'][form][lang]
  assert len(qs)==120
  assert collections.Counter(q['examDomain'] for q in qs)==expected
  assert all(len(q['options'])==4 and 0<=q['answer']<4 and len(set(q['options']))==4 for q in qs)
  assert all(q['q'].strip() and len(q['explanation'])>30 for q in qs)
  assert all(q['options'][q['answer']].strip('. ').lower() not in q['q'].lower() for q in qs),'Answer already present in stem'
  all_exams+=qs
 def norm(x):return re.sub(r'\s+',' ',x.casefold().strip())
 practice={norm(q['q']) for q in d['questions' if lang=='fr' else 'enQuestions']}
 stems=[norm(q['q']) for q in all_exams]
 ids=[q['id'] for q in all_exams]
 assert len(set(stems))==len(stems)==240 and len(set(ids))==240
 assert not (set(stems)&practice)
 assert all(q['id'].startswith('MOCK-') for q in all_exams)
 print(f'{lang}: 2 x 120 held-out mock questions, no exact overlaps; domain quota OK')
print('PASS: PQA 6 practices, 31 bilingual PG summaries, original A/B exam forms and disjoint training bank')