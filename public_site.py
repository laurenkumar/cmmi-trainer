"""Render crawlable bilingual lessons from the same teaching sources as the app.
No JS needed, no alternate bot content, and no invented credential claims.
"""
from pathlib import Path
from html import escape as e
import json, re, shutil
from xml.etree.ElementTree import Element, SubElement, tostring
from content.guides import GUIDES
BASE='https://cmmi-trainer.vercel.app'
DATE='2026-10-17'
LABELS={
 'fr':{'home':'Cours et guides','app':'Ouvrir mon espace','lessons':'Les 40 leçons','guides':'Guides pratiques','sources':'Sources et méthode','glossary':'Glossaire','read':'Lire la leçon','workshop':'Faire l’atelier','study':'Étudier et suivre mes acquis','next':'Leçon suivante','previous':'Leçon précédente','lang':'Read in English','note':'Ressource pédagogique indépendante. CMMI® est une marque du CMMI Institute. Aucune affiliation ou certification officielle revendiquée.'},
 'en':{'home':'Lessons and guides','app':'Open my study space','lessons':'The 40 lessons','guides':'Practical guides','sources':'Sources and method','glossary':'Glossary','read':'Read lesson','workshop':'Open workshop','study':'Study and track progress','next':'Next lesson','previous':'Previous lesson','lang':'Lire en français','note':'Independent educational resource. CMMI® is a trademark of CMMI Institute. No affiliation or official certification claimed.'}}
def text(fr,en,lang):return en if lang=='en' else fr
def para(s):
    # Markdown emphasis from the existing original teaching copy, escaped first.
    return '<p>'+re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',e(str(s)))+'</p>'
def ul(items):return '<ul>'+''.join('<li>'+e(str(x))+'</li>' for x in items)+'</ul>'
def lesson_path(l,lang):return f'/{lang}/lessons/{l["id"].lower()}/'
def name(l,lang):return l.get('en',{}).get('title',l['title']) if lang=='en' else l['title']
def summary(l,lang):return l.get('en',{}).get('summary',l.get('goal',l.get('summary',''))) if lang=='en' else l.get('summary',l.get('goal',''))
def app_url(lang,**args):return '/?lang='+lang+''.join('&'+e(k)+'='+e(v) for k,v in args.items())
def link(path,label,cls=''):return f'<a class="{cls}" href="{e(path,quote=True)}">{e(label)}</a>'
def sources_html(D,lang,indices=None,extra=()):
    rows=[]
    for i in indices if indices is not None else range(len(D['sourceRegister'])):
        s=D['sourceRegister'][i]
        rows.append('<li>'+link(s['url'],s['title'])+' · '+e(s.get('date','2026'))+'</li>')
    rows += ['<li>'+link(url,title)+'</li>' for url,title in extra]
    return '<section class="source-note"><h2>'+e(LABELS[lang]['sources'])+'</h2><ul>'+''.join(rows)+'</ul><p>'+text('Références contrôlées le 17 octobre 2026. Synthèse pédagogique originale ; consulter la source pour ses règles et son périmètre exacts.','References checked on 17 October 2026. Original educational synthesis; consult each source for its exact rules and scope.',lang)+'</p></section>'
def breadcrumb(items):
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">'+ ' / '.join(link(p,t) for p,t in items)+'</nav>'
def render_page(lang,path,title,description,body,kind='WebPage',lesson=False):
    L=LABELS[lang];other='en' if lang=='fr' else 'fr';alternate='/'+other+path[3:]
    url=BASE+path
    graph=[{'@type':'Organization','@id':BASE+'/#publisher','name':'CMMI Academy','url':BASE+'/'},
           {'@type':'WebSite','@id':BASE+'/#website','name':'CMMI Academy','url':BASE+'/'},
           {'@type':kind,'@id':url+'#page','url':url,'name':title,'description':description,'inLanguage':lang,'dateModified':DATE,
            'author':{'@id':BASE+'/#publisher'},'publisher':{'@id':BASE+'/#publisher'},'isPartOf':{'@id':BASE+'/#website'}}]
    if lesson:graph[-1].update({'learningResourceType':'Lesson','educationalUse':'Independent study'})
    graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':L['home'],'item':BASE+'/'+lang+'/'},{'@type':'ListItem','position':2,'name':title,'item':url}]})
    schema=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<','\\u003c')
    return ('<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="theme-color" content="#142a43"><title>'+e(title)+' | CMMI Academy</title>'
        '<meta name="description" content="'+e(description,quote=True)+'"><meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">'
        '<link rel="canonical" href="'+url+'">'+''.join('<link rel="alternate" hreflang="'+a+'" href="'+BASE+('/'+a+path[3:])+'">' for a in ['fr','en'])+
        '<link rel="alternate" hreflang="x-default" href="'+BASE+'/en/'+path[4:]+'">'
        '<meta property="og:type" content="'+('article' if kind in ['Article','LearningResource'] else 'website')+'"><meta property="og:title" content="'+e(title,quote=True)+'">'
        '<meta property="og:description" content="'+e(description,quote=True)+'"><meta property="og:url" content="'+url+'"><meta property="og:locale" content="'+('fr_FR' if lang=='fr' else 'en_US')+'">'
        '<meta name="twitter:card" content="summary"><link rel="stylesheet" href="/reading.css"><script type="application/ld+json">'+schema+'</script></head><body>'
        '<a class="skip" href="#main">'+text('Aller au contenu','Skip to content',lang)+'</a><header class="masthead"><a class="brand" href="/'+lang+'/">C<span>CMMI Academy<small>2027 · '+text('apprendre et pratiquer','learn and practice',lang)+'</small></span></a><nav aria-label="'+text('Navigation principale','Main navigation',lang)+'">'+link('/'+lang+'/',L['home'])+link('/'+lang+'/glossary/',L['glossary'])+link('/'+lang+'/sources/',L['sources'])+link(alternate,L['lang'])+'</nav></header>'
        '<main id="main" class="reading">'+body+'</main><footer class="site-footer">'+e(L['note'])+'<p>'+link(app_url(lang),L['app'])+' · '+link('/'+lang+'/sources/',L['sources'])+'</p></footer></body></html>')

def lesson_body(D,l,lang,lessons):
    L=LABELS[lang];ispa=l['id'].startswith('PA-');code=l['id'][3:] if ispa else l['id'];deep=l['en'] if lang=='en' else l['deep']
    title=name(l,lang);path=lesson_path(l,lang)
    body=breadcrumb([('/'+lang+'/',L['home']),(path,code)])+'<article><div class="eyebrow">'+e(code)+' · '+text('LEÇON ET CAS PRATIQUE','LESSON AND APPLIED CASE',lang)+'</div><h1>'+e(title)+'</h1><p class="lead">'+e(summary(l,lang))+'</p>'
    body+='<p class="byline">CMMI Academy · '+text('Rédaction pédagogique indépendante · mise à jour','Independent educational content · updated',lang)+' '+DATE+'</p><div class="actions">'+link(app_url(lang,lesson=l['id']),L['study'],'button')+(link(app_url(lang,workshop=code),L['workshop'],'button outline') if ispa else '')+'</div>'
    body+='<section><h2>'+text('Comprendre le sujet','Understand the topic',lang)+'</h2>'+''.join(para(p) for p in deep['paragraphs'])+'</section>'
    body+='<section><h2>'+text('Raisonner étape par étape','Reason step by step',lang)+'</h2><ol>'+''.join('<li><strong>'+e(step[0])+'</strong> — '+e(step[1])+'</li>' for step in deep['steps'])+'</ol></section>'
    if ispa:
        applied=l['appliedLesson'][lang]
        body+='<section><h2>'+text('Exemple commenté','Worked example',lang)+'</h2>'+para(applied['reasoning'])+para(applied['example'])+'</section>'
        w=D['workshops'][code]
        body+='<section id="workshop"><div class="eyebrow">'+text('ATELIER ORIGINAL · 4 SÉQUENCES','ORIGINAL WORKSHOP · 4 SEQUENCES',lang)+'</div><h2>'+text('1. Comprendre le mécanisme','1. Understand the mechanism',lang)+'</h2>'+para(w['concept'][lang])+'<h2>'+text('2. Examiner les trois pièces','2. Examine the three records',lang)+'</h2><p class="notice">'+text('Les faits, chiffres et seuils de ce cas sont fictifs. Ils ne constituent pas des exigences CMMI.','Facts, figures and thresholds in this case are fictional. They are not CMMI requirements.',lang)+'</p>'+''.join('<div class="record">'+para(r[lang])+'</div>' for r in w['records'])
        body+='<h2>'+text('3. Prendre deux décisions','3. Make two decisions',lang)+'</h2>'+''.join('<h3>'+e(q['prompt'][lang])+'</h3>'+ul(o[lang] for o in q['options']) for q in w['questions'])+link(app_url(lang,workshop=code),text('Répondre et obtenir la correction après tentative','Answer and get feedback after submission',lang),'button')
        body+='<h2>'+text('4. Produire et se relire','4. Produce and self-review',lang)+'</h2>'+para(w['task'][lang])+ul(r[lang] for r in w['rubric'])+'<p class="notice">'+text("Cette grille permet une autoévaluation. La qualité du livrable n'est pas corrigée automatiquement.","This rubric supports self-review. Deliverable quality is not automatically graded.",lang)+'</p></section>'
        body+='<section><h2>'+text('Périmètre public de cette leçon','This lesson’s public-source scope',lang)+'</h2><p>'+text('Le thème est relié au guide rapide v4.0, page ','The topic is linked to the v4.0 quick guide, page ',lang)+str(l['page'])+'. '+text("Les exercices et exemples sont originaux. Ils ne reconstituent pas les énoncés normatifs individuels du modèle sous licence.","Exercises and examples are original. They do not reconstruct individual normative statements from the licensed model.",lang)+'</p></section>'
    else:body+='<section><h2>'+text('Situation de transfert','Transfer scenario',lang)+'</h2>'+para(deep['story'])+'<p>'+e(deep['lesson'])+'</p></section>'
    body+=sources_html(D,lang,[0] if ispa else [0,1,2])+'</article>'
    idx=lessons.index(l)
    body+='<nav class="lesson-pagination" aria-label="'+text('Autres leçons','Other lessons',lang)+'">'+(link(lesson_path(lessons[idx-1],lang),L['previous']+' : '+name(lessons[idx-1],lang)) if idx else '')+(link(lesson_path(lessons[idx+1],lang),L['next']+' : '+name(lessons[idx+1],lang)) if idx+1<len(lessons) else '')+'</nav>'
    return body

def build_site(root,D):
    out=root/'dist'
    if out.exists():shutil.rmtree(out)
    out.mkdir()
    shutil.copy2(root/'index.html',out/'index.html')
    shutil.copytree(root/'videos',out/'videos')
    shutil.copy2(root/'reading.css',out/'reading.css')
    pages=[]
    def write(lang,path,title,desc,body,kind='WebPage',lesson=False):
        dest=out/path.lstrip('/')/'index.html';dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(render_page(lang,path,title,desc,body,kind,lesson),encoding='utf-8');pages.append(path)
    lessons=D['foundations']+[dict(a,id='PA-'+a['id']) for a in D['areas']]
    for lang in ['fr','en']:
        L=LABELS[lang]
        title=text('Apprendre le CMMI : cours, cas pratiques et préparation Practitioner','Learn CMMI: lessons, practical cases and Practitioner preparation',lang)
        desc=text('40 leçons, 31 ateliers et deux examens blancs bilingues. Un parcours indépendant fondé sur les sources publiques CMMI.','40 lessons, 31 workshops and two bilingual mock exams. An independent pathway based on public CMMI sources.',lang)
        body='<section class="hero"><div class="eyebrow">CMMI ACADEMY · '+text('ÉDITION 2027','2027 EDITION',lang)+'</div><h1>'+e(title)+'</h1><p class="lead">'+e(desc)+'</p><div class="actions">'+link(app_url(lang),L['app'],'button')+link('/'+lang+'/guides/study-plan/',text('Choisir mon parcours','Choose my pathway',lang),'button outline')+'</div><div class="metrics"><span><b>40</b> '+text('leçons','lessons',lang)+'</span><span><b>31</b> '+text('ateliers originaux','original workshops',lang)+'</span><span><b>2 × 120</b> '+text('questions d’examen','mock exam questions',lang)+'</span></div></section>'
        body+='<p class="notice">'+text("Préparation indépendante complémentaire. La formation officielle requise, le modèle complet sous licence et l'examen restent distincts de cette plateforme.","Independent supplementary preparation. Required official training, the licensed full model and the certification exam remain separate from this platform.",lang)+'</p>'
        body+='<section id="guides"><h2>'+L['guides']+'</h2><div class="cards">'+''.join('<article class="reading-card"><h3>'+link('/'+lang+'/guides/'+slug+'/',g['title'][lang])+'</h3><p>'+e(g['description'][lang])+'</p></article>' for slug,g in GUIDES.items())+'</div></section>'
        body+='<section id="lessons"><h2>'+L['lessons']+'</h2><div class="cards">'+''.join('<article class="reading-card"><div class="eyebrow">'+e(l['id'].replace('PA-',''))+'</div><h3>'+link(lesson_path(l,lang),name(l,lang))+'</h3><p>'+e(summary(l,lang))+'</p>'+link(lesson_path(l,lang),L['read'])+'</article>' for l in lessons)+'</div></section>'
        body+=sources_html(D,lang)
        write(lang,'/'+lang+'/',title,desc,body)
        for l in lessons:
            desc=summary(l,lang)
            # A concise, unique summary, not a fragment with a mechanically cut word.
            write(lang,lesson_path(l,lang,),'%s · %s'%(l['id'].replace('PA-',''),name(l,lang)),desc,lesson_body(D,l,lang,lessons),'LearningResource',True)
        for slug,g in GUIDES.items():
            body=breadcrumb([('/'+lang+'/',L['home']),('/'+lang+'/guides/'+slug+'/',g['title'][lang])])+'<article><div class="eyebrow">'+L['guides']+'</div><h1>'+e(g['title'][lang])+'</h1><p class="byline">CMMI Academy · '+DATE+'</p><p class="answer">'+e(g['answer'][lang])+'</p>'
            if slug=='cmmi-scrum-safe':
                rows=[('CMMI',text('Capacités et amélioration de la performance organisationnelle','Organizational capabilities and performance improvement',lang)),('Scrum',text('Cadre de travail pour générer de la valeur face à des problèmes complexes','Framework for generating value through adaptive solutions to complex problems',lang)),('SAFe',text('Agilité à plus grande échelle et articulation de plusieurs équipes','Agility at scale and coordination across teams',lang))]
                body+='<table><caption>'+text('Comparaison des finalités publiques','Comparison of public purposes',lang)+'</caption><thead><tr><th>'+text('Approche','Approach',lang)+'</th><th>'+text('Angle principal','Primary focus',lang)+'</th></tr></thead><tbody>'+''.join('<tr><th>'+e(a)+'</th><td>'+e(b)+'</td></tr>' for a,b in rows)+'</tbody></table>'
            body+=''.join('<section><h2>'+e(h[lang])+'</h2>'+para(p[lang])+'</section>' for h,p in g['sections'])
            body+=sources_html(D,lang,g['sources'],g.get('extraSources',[]))+'</article><div class="actions">'+link('/'+lang+'/#lessons',L['lessons'],'button')+link(app_url(lang,route='train'),text('Ouvrir les entraînements','Open practice exams',lang),'button outline')+'</div>'
            write(lang,'/'+lang+'/guides/'+slug+'/',g['title'][lang],g['description'][lang],body,'Article')
        body='<h1>'+L['glossary']+' CMMI · EN / FR</h1><p class="lead">'+text('Définitions pédagogiques originales, pour relier les termes anglais aux notions étudiées.','Original learning definitions connecting English terms with the concepts studied.',lang)+'</p><dl class="glossary">'+''.join('<div id="term-'+str(i)+'"><dt>'+e(g['term'])+' · '+e(g.get('fr',''))+'</dt><dd>'+e(g.get('definitionFr',g['definition']) if lang=='fr' else g['definition'])+'</dd></div>' for i,g in enumerate(D['glossary']))+'</dl>'+sources_html(D,lang,[0])
        write(lang,'/'+lang+'/glossary/',L['glossary']+' CMMI : '+str(len(D['glossary']))+text(' notions anglais-français',' English-French concepts',lang),text('Comprendre les termes du CMMI en anglais et en français avec des définitions pédagogiques.','Understand CMMI terms in English and French through learning definitions.',lang),body)
        body='<h1>'+L['sources']+'</h1><p class="lead">'+text('Qui publie, sur quelles bases et avec quelles limites ?','Who publishes, on what basis and with what limitations?',lang)+'</p>'
        sections=[(text('Responsabilité éditoriale','Editorial responsibility',lang),text("Publication : projet CMMI Academy, maintenu par Dorian Laurenceau. Les cas et grilles sont des créations pédagogiques originales. Aucun statut de formateur agréé, de partenaire officiel ou de validation indépendante par un expert n'est revendiqué.","Publisher: the CMMI Academy project, maintained by Dorian Laurenceau. Cases and rubrics are original educational creations. No accredited-instructor status, official partnership or independent expert validation is claimed.",lang)),
            (text('Périmètre des sources','Source scope',lang),text("Le guide rapide public v4.0 résume 31 Practice Areas et des groupes de pratiques ; il publie aussi six extraits individuels PQA. Il ne remplace pas le modèle complet sous licence. Les ateliers n'inventent pas les exigences manquantes et ne reconstituent pas les 276 énoncés individuels.","The public v4.0 quick guide summarizes 31 Practice Areas and practice groups; it also publishes six individual PQA excerpts. It does not replace the licensed full model. Workshops do not invent missing requirements or reconstruct the 276 individual statements.",lang)),
            (text('Méthode pédagogique','Teaching method',lang),text("Une leçon relie thème, mécanisme, exemples et contrôle. Chaque atelier ajoute trois pièces fictives, deux décisions et un livrable. La correction des QCM est automatique ; la grille du livrable est une autoévaluation. Les tests logiciels valident navigation et calcul des scores, sans démontrer l'efficacité d'apprentissage chez des personnes.","Each lesson connects topic, mechanism, examples and checks. Each workshop adds three fictional records, two decisions and a deliverable. Multiple-choice marking is automatic; the deliverable rubric is self-review. Software tests validate navigation and score calculation without demonstrating learning effectiveness in people.",lang)),
            (text('Versions et certification','Versions and certification',lang),text("L'édition 2027 est le nom du parcours. Les informations d'examen sont tirées de documents publics datés de 2026. Certaines politiques conservent des mentions v3.0 alors que le guide rapide est v4.0 : vérifier la référence applicable à sa session. Aucun seuil de réussite officiel ni taux de réussite utilisateur n'est inventé.","The 2027 edition is the pathway's name. Exam information comes from public documents dated 2026. Some policies retain v3.0 references while the quick guide is v4.0: verify the reference applicable to your session. No official pass threshold or learner pass rate is invented.",lang)),
            (text('Données personnelles et correction','Personal data and corrections',lang),text("Les brouillons, scores et progrès sont conservés dans le navigateur ; l'export permet une sauvegarde personnelle. Aucun outil d'analyse de trafic n'est ajouté. Pour proposer une correction, utiliser le dépôt public du projet en indiquant l'URL, le passage concerné et une source publique vérifiable.","Drafts, scores and progress are stored in the browser; export supports a personal backup. No traffic analytics tool is added. To propose a correction, use the public project repository with the URL, affected passage and a verifiable public source.",lang))]
        body+=''.join('<section><h2>'+e(h)+'</h2>'+para(p)+'</section>' for h,p in sections)+sources_html(D,lang)+'<p>'+link('https://github.com/laurenkumar/cmmi-trainer','GitHub · CMMI Academy')+'</p>'
        write(lang,'/'+lang+'/sources/',L['sources']+' · CMMI Academy',text('Sources officielles publiques, méthode des ateliers, responsabilité éditoriale et limites de préparation.','Official public sources, workshop method, editorial responsibility and preparation limitations.',lang),body)
    # Explicit bot policy: discovery/search allowed. This does not promise inclusion.
    (out/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+BASE+'/sitemap.xml\n')
    ns='http://www.sitemaps.org/schemas/sitemap/0.9';xns='http://www.w3.org/1999/xhtml'
    import xml.etree.ElementTree as ET
    ET.register_namespace('',ns);ET.register_namespace('xhtml',xns)
    tree=Element('{'+ns+'}urlset')
    for path in ['/']+pages:
        item=SubElement(tree,'{'+ns+'}url');SubElement(item,'{'+ns+'}loc').text=BASE+path
        SubElement(item,'{'+ns+'}lastmod').text=DATE
        if path!='/':
            for lang in ['fr','en']:
                SubElement(item,'{'+xns+'}link',{'rel':'alternate','hreflang':lang,'href':BASE+'/'+lang+path[3:]})
    (out/'sitemap.xml').write_bytes(tostring(tree,encoding='utf-8',xml_declaration=True))
    (out/'release.json').write_text(json.dumps({'revision':D['contentRevision'],'date':DATE,'lessons':40,'workshops':len(D['workshops']),'publicPages':len(pages),'mockForms':2,'questionsPerMock':120},indent=2)+'\n')
    (out/'404.html').write_text('<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="robots" content="noindex"><title>Page introuvable · CMMI Academy</title><h1>Page introuvable / Page not found</h1><a href="/fr/">Cours en français</a> · <a href="/en/">English lessons</a></html>')
    return pages
