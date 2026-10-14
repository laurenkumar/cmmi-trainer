#!/usr/bin/env python3
from pathlib import Path
import json
p=Path(__file__).resolve().parent
d=json.loads((p/'data.json').read_text(encoding='utf-8'))
assert len(d['areas'])==31 and len(d['foundations'])>=9
assert len(d['questions'])>=275 and len(d['enQuestions'])>=206
css=(p/'app.css').read_text(encoding='utf-8')
js=(p/'app.js').read_text(encoding='utf-8')
payload=json.dumps(d,ensure_ascii=False,separators=(',',':'))
assert '</script' not in js.lower() and '</script' not in payload.lower()
html='<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#142a43"><title>CMMI Academy 2027 — bilingual study</title><style>'+css+'</style></head><body><div id="root"></div><script>window.CMMI_DATA='+payload+';\n'+js+'</script></body></html>'
(p/'index.html').write_text(html,encoding='utf-8')
print('Built',len(html),'characters')
