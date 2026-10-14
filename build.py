#!/usr/bin/env python3
"""Rebuild the self-contained index.html from editable source files."""
from pathlib import Path
import json

root = Path(__file__).resolve().parent
css = (root / "app.css").read_text(encoding="utf-8")
js = (root / "app.js").read_text(encoding="utf-8")
data = json.loads((root / "data.json").read_text(encoding="utf-8"))
assert len(data["areas"]) == 31 and len(data["foundations"]) == 8
assert len(data["questions"]) >= 260
payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
assert "</script" not in js.lower() and "</script" not in payload.lower()
html = (
    '<!doctype html><html lang="fr"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    '<meta name="theme-color" content="#142a43">'
    '<meta name="description" content="CMMI Academy · cours interactifs et préparation d’appraisal">'
    '<title>CMMI Academy 2027 — édition approfondie</title><style>'
    + css + '</style></head><body><div id="root"></div><script>window.CMMI_DATA='
    + payload + ';\n' + js + '</script></body></html>'
)
(root / "index.html").write_text(html, encoding="utf-8")
print("Built index.html:", len(html.encode("utf-8")), "bytes")
