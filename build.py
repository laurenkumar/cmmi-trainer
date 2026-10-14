#!/usr/bin/env python3
"""Build the standalone, deployable index.html from the editable source files."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
data=json.loads((root/'data.json').read_text(encoding='utf-8'))
assert len(data['areas'])==31 and len(data['foundations'])>=9
assert len(data['questions'])>=275 and len(data['enQuestions'])>=206
style=(root/'app.css').read_text(encoding='utf-8')
script=(root/'app.js').read_text(encoding='utf-8')
payload=json.dumps(data,ensure_ascii=False,separators=(',',':'))
assert '</script' not in payload.lower() and '</script' not in script.lower()
html=(
    '<!doctype html><html lang="fr"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    '<meta name="theme-color" content="#142a43">'
    '<meta name="description" content="CMMI Academy · 40 cours bilingues, quiz, glossaire et préparation CMMI Practitioner 2027">'
    '<title>CMMI Academy 2027 — bilingual study</title><style>'+style+'</style>'
    '</head><body><div id="root"></div><script>window.CMMI_DATA='+payload+';\n'+script+'</script></body></html>'
)
(root/'index.html').write_text(html,encoding='utf-8')
print(f'Built index.html ({len(html.encode("utf-8")):,} bytes; {len(data["foundations"])+len(data["areas"])} lessons; {len(data["questions"])+len(data["enQuestions"])} practice questions).')