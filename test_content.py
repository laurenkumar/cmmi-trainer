from pathlib import Path
import json
d=json.loads((Path(__file__).parent/'data.json').read_text(encoding='utf-8'))
assert len(d['areas'])==31 and len(d['foundations'])>=9
assert len(d['cases'])==20 and len(d['glossary'])>=100
assert len(d['questions'])>=275 and len(d['enQuestions'])>=206
lessons=d['areas']+d['foundations']
assert all(x.get('deep') and x.get('en') for x in lessons)
qs=d['questions']+d['enQuestions']
assert len({x['id'] for x in qs})==len(qs)
assert all(0<=x['answer']<len(x['options']) and len(x['options'])==len(set(x['options'])) for x in qs)
assert d['examBlueprint']['total']==120 and d['examBlueprint']['minutes']==240
print('PASS:',len(lessons),'lessons',len(qs),'questions')
