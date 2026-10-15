#!/usr/bin/env python3
"""Release gates for complete coverage, bilingual consistency and honest source scope."""
import json,collections,re,subprocess
from pathlib import Path
P=Path(__file__).parent;D=json.loads((P/'data.json').read_text());lessons=D['areas']+D['foundations']
for script in ['test_content.py','audit_content.py','audit_v6.py']:
 subprocess.run(['python3',str(P/script)],check=True)
assert len(D['areas'])==31
assert sum(len(a.get('publicGroupCourse',{}).get('entries',[])) for a in D['areas'])==99
assert all(a['source'] and str(a['page']) in a['source'] for a in D['areas'])
for a in D['areas']:
 assert a['page'] in range(6,32)
 for lang in ('fr','en'):
  assert 'D05' in a['caseLab'][lang]['artifacts'][-1]['body']
  assert 'D05' in a['masteryQuestions'][lang][2]['q']
  assert 'combined adverse-event rate' not in a['masteryQuestions'][lang][2]['q']
 for x in a.get('publicGroupCourse',{}).get('entries',[]):
  assert x['sourcePage']==a['page']
  for lang in ('fr','en'):
   v=x[lang];assert len(v['options'])==4 and len(set(v['options']))==4
   assert v['options'][x['answer']] not in v['question'],(a['id'],lang,x['groupLevel'])
   assert len(v['question'].split())>=25
   assert 'PG'+str(x['groupLevel']) in v['question']
   assert 'distinctive focus' not in v['question']
  assert all(len(a['appliedLesson'][lang]['example'].split())>=30 for lang in ('fr','en'))
for lang in ['fr','en']:
 teaching={q['q'] for l in lessons for q in l['masteryQuestions'][lang]}
 practice={q['q'] for q in D['questions' if lang=='fr' else 'enQuestions']}
 forms=[D['mockExamForms'][f][lang] for f in ['A','B']]
 assert not ({q['caseId'] for q in forms[0]} & {q['caseId'] for q in forms[1]})
 for form,qs in zip(['A','B'],forms):
  assert len(qs)==120 and len({q['id'] for q in qs})==120
  assert not ({q['q'] for q in qs} & (teaching|practice))
  assert len({q['area'] for q in qs})==31
  assert all(all(record in q['q'] for record in ['D01','D02','D03']) for q in qs)
  positions=collections.Counter(q['answer'] for q in qs);assert max(positions.values())-min(positions.values())<=4,positions
  skills=collections.Counter(q['reasoningSkill'] for q in qs);assert len(skills)==9
  print(lang,form,dict(skills),'answer positions',dict(positions))
for l in lessons:
 for lang in ['fr','en']:
  for q in l['masteryQuestions'][lang]:
   assert len(q['options'])==4 and 0<=q['answer']<4
print('PASS: release coverage, 99 public PG cards, six PQA excerpts, 31 PA per mock, 9 reasoning skills, balanced keys and disjoint forms.')
