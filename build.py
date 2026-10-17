#!/usr/bin/env python3
"""Build the standalone app and a deployable, crawlable bilingual static site."""
from pathlib import Path
import json
from content.workshops import W
from public_site import build_site
root=Path(__file__).resolve().parent
data=json.loads((root/'data.json').read_text(encoding='utf-8'))
assert len(data['areas'])==31 and len(data['foundations'])>=9
assert len(data['questions'])>=275 and len(data['enQuestions'])>=206
assert set(W)=={a['id'] for a in data['areas']}
data['workshops']=W
data['contentRevision']='2026-10-17-r10'
style=(root/'app.css').read_text(encoding='utf-8')
script=(root/'app.js').read_text(encoding='utf-8')
payload=json.dumps(data,ensure_ascii=False,separators=(',',':'))
assert '</script' not in payload.lower() and '</script' not in script.lower()
fallback='<main><h1>CMMI Academy : apprendre, pratiquer et préparer sa certification</h1><p>40 leçons bilingues, 31 ateliers originaux et deux examens blancs indépendants. Préparation complémentaire fondée sur les sources publiques.</p><p><a href="/fr/">Cours et guides en français</a> · <a href="/en/">English lessons and guides</a></p><p>Les exercices interactifs nécessitent JavaScript. Les pages de lecture restent accessibles sans JavaScript.</p></main>'
html=(
    '<!doctype html><html lang="fr"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    '<meta name="theme-color" content="#142a43">'
    '<meta name="description" content="CMMI Academy : 40 leçons, 31 ateliers et deux examens blancs bilingues. Préparation indépendante fondée sur les sources publiques.">'
    '<link rel="canonical" href="https://cmmi-trainer.vercel.app/">'
    '<title>CMMI Academy 2027 — Apprendre, pratiquer, évaluer</title><style>'+style+'</style>'
    '</head><body><div id="root">'+fallback+'</div><script>window.CMMI_DATA='+payload+';\n'+script+'</script></body></html>'
)
(root/'index.html').write_text(html,encoding='utf-8')
pages=build_site(root,data)
print(f'Built app ({len(html.encode("utf-8")):,} bytes), {len(pages)} public pages, 31 bilingual workshops and unchanged 80 MP4 / 80 VTT files.')
