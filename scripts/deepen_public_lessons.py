#!/usr/bin/env python3
"""Original explanations of publicly listed PG topics, reviewed against guide pp.6–31.
This does not assign new individual practice identifiers or formal appraisal criteria.
"""
from pathlib import Path
import json
P=Path(__file__).resolve().parent.parent;D=json.loads((P/'data.json').read_text())
# One decision per publicly reported PG, in increasing PG order. These are
# original teaching paraphrases, deliberately separate from normative statements.
TOPICS={
'CAR':[
('Choisir un résultat qui mérite une analyse et agir sur ses causes ; ne pas limiter la recherche aux résultats négatifs.','Choose an outcome worth examining and address its causes; useful analysis can also explain a positive outcome.'),
('Sélectionner les résultats à analyser puis engager des actions reliées aux causes identifiées, plutôt que corriger seulement les symptômes.','Select outcomes for analysis and connect actions to identified causes rather than treating symptoms alone.'),
('Relier l’analyse à une démarche organisationnelle, enregistrer les données de résolution et faire remonter des propositions d’amélioration réutilisables.','Connect analysis to organizational processes, retain resolution data and submit reusable improvement proposals.'),
('Examiner les causes et l’effet des actions avec des techniques statistiques pertinentes ; une comparaison brute avant/après ne suffit pas à isoler un effet.','Use suitable statistical techniques to investigate causes and action effects; a raw before/after comparison does not isolate an effect.'),
('Comparer quantitativement des solutions et des processus pour optimiser la performance au-delà du seul problème local.','Quantitatively compare solutions and processes to optimize performance beyond a single local issue.')],
'CM':[
('Identifier quelle version d’un produit de travail est conservée et pouvoir retrouver son historique élémentaire.','Identify which work-product version is retained and recover its basic history.'),
('Choisir les éléments contrôlés, gérer les références et changements dans un système cohérent, décrire les versions et vérifier leur intégrité par des audits de configuration.','Select controlled items, manage baselines and changes coherently, describe versions and examine integrity through configuration audits.')],
'CONT':[
('Préparer une réponse de secours à une perturbation importante, en partant de l’opération qui doit pouvoir continuer.','Prepare a contingency response to a major disruption, starting from the operation that must continue.'),
('Hiérarchiser fonctions et ressources essentielles, puis préparer et utiliser les plans qui permettent la reprise des opérations.','Prioritize essential functions and resources, then prepare and use plans that restore operations.'),
('Relier formation à la continuité, vérification et validation des plans, analyse des exercices et corrections dans une démarche organisationnelle.','Connect continuity training, plan verification and validation, exercise analysis and corrections through an organizational approach.')],
'DM':[
('Relier les objectifs de gestion des données aux métadonnées nécessaires pour comprendre les données effectivement utilisées.','Connect data-management objectives to metadata needed to understand the data actually used.'),
('Décrire l’architecture de gestion des données et appliquer une méthode cohérente à leur cycle de vie.','Describe the data-management architecture and apply a coherent approach across the lifecycle.'),
('Installer une capacité organisationnelle de gestion des données, la déployer puis revoir son fonctionnement et traiter les constats.','Establish and deploy an organizational data-management capability, review its operation and address findings.')],
'DQ':[
('Identifier les dimensions de qualité utiles et nettoyer les données ; une valeur propre ne démontre pas encore une prévention durable.','Identify relevant quality dimensions and cleanse data; a clean value alone does not demonstrate lasting prevention.'),
('Définir les critères de nettoyage et mettre en œuvre une démarche de qualité qui reste actualisée et utilisée.','Define cleansing criteria and implement a data-quality approach that remains current and in use.'),
('Évaluer la qualité des données à l’échelle organisationnelle, revoir l’efficacité des activités et agir sur ce qui reste défaillant.','Assess organizational data quality, review activity effectiveness and act on remaining weaknesses.')],
'DAR':[
('Faire apparaître plusieurs options et conserver la décision, au lieu de traiter une préférence comme l’unique possibilité.','Make alternatives visible and retain the decision instead of treating a preference as the only possibility.'),
('Définir règles, critères et méthode d’évaluation ; comparer des alternatives avec ces repères avant de choisir une solution.','Define decision rules, criteria and evaluation methods; compare alternatives against them before selecting a solution.'),
('Clarifier dans une démarche organisationnelle quels rôles prennent les décisions ; une matrice de scores ne remplace pas cette responsabilité.','Clarify decision-making roles through an organizational approach; a scoring matrix does not replace accountability.')],
'ESAF':[
('Identifier les besoins et dangers de sûreté, les prioriser et engager des réponses adaptées.','Identify safety needs and hazards, prioritize them and initiate suitable responses.'),
('Définir objectifs et contraintes critiques de sûreté et les moyens de traiter sécurité de l’environnement de travail et sécurité fonctionnelle.','Define critical safety objectives and constraints, covering both workplace and functional safety.'),
('Déployer une capacité organisationnelle de sûreté, évaluer son fonctionnement et appliquer des stratégies de contrôle en traitant les résultats.','Deploy an organizational safety capability, evaluate its operation and follow control strategies while addressing results.')],
'ESEC':[
('Reconnaître, prioriser et traiter les besoins et problèmes de sécurité qui menacent l’activité.','Recognize, prioritize and address security needs and issues affecting operations.'),
('Construire objectifs et approche de sécurité pour les dimensions pertinentes : physique, mission, personnes, processus et cybersécurité.','Build security objectives and an approach across relevant physical, mission, personnel, process and cyber dimensions.'),
('Relier opérations de sécurité, stratégie et architecture organisationnelles ; réaliser des revues et évaluations puis donner suite aux constats.','Connect security operations with organizational strategy and architecture; perform reviews and evaluations and act on findings.')],
'EVW':[
('Identifier les contraintes du travail virtuel et permettre la réalisation effective du travail à distance.','Identify virtual-work constraints and enable actual remote work.'),
('Rendre l’approche de travail virtuel reproductible, la gérer et corriger les écarts qui gênent la réalisation.','Make virtual work reproducible, manage the approach and correct deviations that impede delivery.'),
('Déployer stratégie et capacité organisationnelles de travail virtuel ; revoir périodiquement leur efficacité et adapter les dispositions.','Deploy organizational virtual-work strategy and capability; periodically review effectiveness and adapt arrangements.')],
'EST':[
('Produire des estimations permettant de commencer à apprécier le travail nécessaire.','Produce estimates that provide an initial view of the work needed.'),
('Rendre explicites le périmètre, la taille puis l’effort, la durée et le coût associés, avec les raisons qui soutiennent ces chiffres.','Make scope and size explicit, then related effort, duration and cost, with the reasoning supporting those numbers.'),
('Utiliser des méthodes organisationnelles et les actifs de processus et mesures historiques pour établir les estimations.','Use organizational methods, process assets and historical measurement resources to establish estimates.')],
'GOV':[
('La direction identifie les priorités et une approche pour atteindre les objectifs métier.','Leadership identifies priorities and an approach for achieving business objectives.'),
('La direction communique les objectifs, fournit fonction, ressources et formation, suit les résultats et impose une responsabilité effective sur les processus.','Leadership communicates objectives, supplies function, resources and training, monitors results and holds process responsibilities accountable.'),
('Vérifier que compétences, mesures et processus permettent de servir les objectifs métier, et traiter les problèmes de performance qui les compromettent.','Check that capabilities, measures and processes support business objectives, and address performance issues that threaten them.'),
('Utiliser l’analyse statistique et quantitative pertinente pour éclairer les arbitrages de gouvernance relatifs aux objectifs.','Use relevant statistical and quantitative analysis to inform governance tradeoffs concerning objectives.')],
'II':[
('Exécuter les pratiques du périmètre plutôt que se limiter à en approuver l’intention.','Perform in-scope practices rather than merely approve their intent.'),
('Donner les ressources et compétences nécessaires, tenir les processus à jour et vérifier leur application dans le travail.','Provide needed resources and skills, keep processes current and check their use in work.'),
('Utiliser les actifs organisationnels, adapter les processus selon les dispositions communes et alimenter les améliorations par le retour du terrain.','Use organizational assets, tailor processes through shared arrangements and feed operational experience into improvements.'),
('Rendre possible l’usage des techniques quantitatives par les personnes, ressources et processus qui les mettent effectivement en œuvre.','Enable practical use of quantitative techniques through the people, resources and processes that apply them.')],
'IRP':[
('Enregistrer les incidents et engager leur traitement pour rétablir l’opération.','Record incidents and initiate handling to restore operations.'),
('Préparer et suivre une réponse cohérente aux incidents, avec suivi jusqu’à résolution et communication aux personnes concernées.','Prepare and follow a coherent incident response, with tracking through resolution and communication to affected parties.'),
('Relier la prévention des récidives et la gestion des incidents à une démarche organisationnelle et aux résultats observés.','Connect recurrence prevention and incident management to an organizational approach and observed results.')],
'MPM':[
('Recueillir des mesures utiles et traiter les problèmes de performance constatés.','Collect useful measures and address observed performance problems.'),
('Définir objectifs de mesure et définitions opérationnelles, recueillir, analyser et conserver les données pour utiliser les résultats.','Define measurement objectives and operational definitions, collect, analyze and retain data, and use the results.'),
('Relier les mesures aux objectifs métier, organiser une capacité commune et préserver la qualité d’un référentiel de mesures utilisable.','Connect measures to business objectives, organize shared capability and preserve a usable measurement repository.'),
('Choisir objectifs et méthodes quantitatives adaptés ; construire des références et modèles de performance pour analyser ou prédire l’atteinte des objectifs.','Choose suitable objectives and quantitative methods; build performance baselines and models to assess or predict goal achievement.'),
('Analyser la capacité à atteindre les objectifs métier et sélectionner les améliorations selon leur effet potentiel sur la performance.','Analyze the ability to achieve business objectives and select improvements by their potential performance impact.')],
'MST':[
('Enregistrer menaces et vulnérabilités et prendre des mesures pour les traiter.','Record threats and vulnerabilities and take action to address them.'),
('Maintenir méthode et critères d’évaluation, hiérarchiser et suivre les menaces critiques, puis apprécier l’efficacité des réponses.','Maintain an approach and evaluation criteria, prioritize and track critical threats, and assess response effectiveness.'),
('Relier gestion et vérification des menaces à une stratégie et architecture organisationnelles, et analyser les résultats de sécurité.','Connect threat management and verification to organizational strategy and architecture, and analyze security results.'),
('Combiner renseignement sur les menaces et analyse statistique ou quantitative pour choisir des solutions de sécurité adaptées.','Combine threat intelligence with statistical or quantitative analysis to select suitable security solutions.')],
'MC':[
('Tracer le travail terminé et résoudre les problèmes identifiés.','Record completed work and resolve identified issues.'),
('Comparer réalisations et estimations, ressources et engagements, y compris transition vers l’exploitation ; suivre les corrections jusqu’à résolution.','Compare actual work with estimates, resources and commitments, including transition to operations; track corrections through resolution.'),
('Gérer le projet dans son processus et son plan, surveiller dépendances critiques et environnement de travail, et résoudre les écarts avec les parties concernées.','Manage work against its process and plan, monitor critical dependencies and work environment, and resolve issues with affected stakeholders.')],
'OT':[
('Former les personnes pour soutenir la réalisation du travail.','Train people to support work performance.'),
('Identifier les besoins, réaliser les formations utiles et en conserver les enregistrements.','Identify needs, provide relevant training and retain training records.'),
('Coordonner les besoins des projets et de l’organisation, tenir des plans stratégiques et à court terme et évaluer l’efficacité du dispositif.','Coordinate project and organizational needs, maintain strategic and short-term plans and evaluate training effectiveness.')],
'PR':[
('Faire examiner les produits de travail par des pairs et enregistrer les problèmes repérés.','Have peers review work products and record identified issues.'),
('Sélectionner les produits à revoir, utiliser des procédures et supports préparés et suivre le traitement des défauts identifiés.','Select products for review, use prepared procedures and materials, and track the handling of identified defects.'),
('Analyser les données et résultats des revues selon une démarche organisationnelle pour comprendre leur apport.','Analyze review data and outcomes through an organizational approach to understand their contribution.')],
'PLAN':[
('Lister le travail et attribuer les personnes qui doivent le réaliser.','List the work and assign the people who will perform it.'),
('Réconcilier estimations et capacité, compétences, budget et calendrier ; prévoir participation et transition, puis obtenir des engagements sur un plan cohérent.','Reconcile estimates with capacity, skills, budget and schedule; plan involvement and transition, then obtain commitments to a coherent plan.'),
('Adapter les processus communs et utiliser actifs et mesures historiques ; négocier les dépendances critiques et préparer l’environnement du projet.','Tailor shared processes and use assets and measurement history; negotiate critical dependencies and plan the project environment.'),
('Employer des techniques statistiques et quantitatives pour élaborer et actualiser des processus de projet qui soutiennent les objectifs de performance.','Use statistical and quantitative techniques to develop and update project processes supporting performance objectives.')],
'PAD':[
('Développer les actifs de processus nécessaires à l’exécution du travail.','Develop process assets needed to perform the work.'),
('Identifier les actifs utiles, les créer, acquérir ou réutiliser, puis les rendre accessibles.','Identify useful assets, create, acquire or reuse them, and make them accessible.'),
('Maintenir architecture et bibliothèque de processus, règles d’adaptation, standards d’environnement et de mesure, dans une stratégie organisationnelle d’actifs.','Maintain process architecture and library, tailoring guidance, work-environment and measurement standards within an organizational asset strategy.')],
'PCM':[
('Apporter du support aux processus, examiner forces et faiblesses et traiter les problèmes ou opportunités d’amélioration.','Provide process support, examine strengths and weaknesses, and address problems or improvement opportunities.'),
('Choisir des améliorations de processus ou d’actifs puis préparer et suivre leur mise en œuvre.','Select process or asset improvements, then plan and follow their implementation.'),
('Aligner objectifs d’amélioration et objectifs métier, explorer les méthodes utiles, soutenir déploiement et maintien et évaluer les résultats.','Align improvement and business objectives, explore useful methods, support deployment and maintenance, and evaluate results.'),
('Vérifier les améliorations sélectionnées avec une analyse statistique et quantitative de la performance attendue.','Evaluate selected improvements using statistical and quantitative analysis against expected performance.')],
'PI':[
('Assembler la solution et la fournir au client.','Assemble the solution and deliver it to the customer.'),
('Préparer stratégie, environnement, procédures et critères d’intégration ; identifier les composants, vérifier leur aptitude puis évaluer l’assemblage avant livraison.','Prepare integration strategy, environment, procedures and criteria; identify components, check readiness and evaluate the assembly before delivery.'),
('Tenir à jour les descriptions d’interface, vérifier leur respect et examiner la compatibilité des composants intégrés.','Keep interface descriptions current, check adherence and examine integrated-component compatibility.')],
'RDM':[
('Enregistrer les exigences afin de disposer d’une représentation identifiable du besoin.','Record requirements to create an identifiable representation of the need.'),
('Recueillir besoins, contraintes et interfaces, confirmer la compréhension et les engagements, prioriser et maintenir liens bidirectionnels et cohérence des plans et livrables.','Gather needs, constraints and interfaces, confirm understanding and commitments, prioritize, and maintain bidirectional links and consistency of plans and outputs.'),
('Développer exigences de solution et composants, scénarios d’usage et interfaces ; équilibrer les contraintes et valider les exigences dans l’environnement prévu.','Develop solution and component requirements, usage scenarios and interfaces; balance constraints and validate requirements for the intended environment.')],
'RSK':[
('Identifier et actualiser les risques et les opportunités, y compris leurs effets positifs possibles.','Identify and update risks and opportunities, including possible positive effects.'),
('Analyser les éléments identifiés, suivre leur état et communiquer les évolutions aux personnes concernées.','Analyze identified items, monitor their status and communicate changes to affected people.'),
('Définir catégories et paramètres, stratégie et plans selon une démarche organisationnelle, puis réaliser les activités de traitement prévues.','Define categories and parameters, strategy and plans through an organizational approach, then perform planned handling activities.')],
'SDM':[
('Utiliser le système de service pour fournir et gérer les services.','Use the service system to provide and manage services.'),
('Tenir et suivre les accords, traiter les demandes, analyser les données pour faire évoluer les engagements et vérifier la préparation du système de service.','Maintain and follow agreements, handle requests, analyze data for agreement changes and check service-system readiness.'),
('Créer, actualiser et utiliser des systèmes et accords de service standards à l’échelle de l’organisation.','Create, update and actively use organizational standard service systems and agreements.')],
'STSM':[
('Dresser l’inventaire des services actuellement proposés.','Inventory the services currently offered.'),
('Décrire les services, analyser besoins stratégiques et capacités, puis suivre une approche de création ou modification de l’offre.','Describe services, analyze strategic needs and capability, then follow an approach for creating or modifying offerings.'),
('Maintenir et utiliser les descriptions et niveaux des services standards organisationnels.','Maintain and use organizational standard-service descriptions and service levels.')],
'SAM':[
('Identifier et choisir les fournisseurs, consigner l’accord puis accepter ou refuser leurs livrables et traiter les factures.','Identify and select suppliers, record the agreement, accept or reject deliverables and handle invoices.'),
('Évaluer selon des critères, solliciter et comparer les réponses ; gérer les engagements et changements puis vérifier l’accord avant acceptation et paiement.','Evaluate against criteria, solicit and compare responses; manage commitments and changes, then check agreement fulfillment before acceptance and payment.'),
('Effectuer des revues techniques des livrables et piloter performance et processus fournisseur selon les critères de l’accord.','Perform technical reviews of deliverables and manage supplier performance and processes against agreement criteria.'),
('Choisir mesures et méthodes d’analyse pour piloter quantitativement l’atteinte des objectifs de performance fournisseur.','Choose measures and analysis methods to quantitatively manage supplier performance against targets.')],
'TS':[
('Construire une solution qui satisfait les exigences spécifiées.','Develop a solution that satisfies specified requirements.'),
('Concevoir et réaliser la solution, examiner le design pour traiter ses problèmes et donner les indications nécessaires à son utilisation.','Design and build the solution, evaluate the design for issues and provide guidance for its use.'),
('Comparer des alternatives selon des critères de conception, arbitrer construire, acheter ou réutiliser, maintenir les informations de réalisation et concevoir les interfaces.','Compare alternatives against design criteria, assess build/buy/reuse choices, maintain implementation information and design interfaces.')],
'VV':[
('Vérifier la conformité aux exigences et valider l’usage prévu dans l’environnement cible, puis conserver et communiquer les résultats.','Verify requirement conformance and validate intended use in the target environment, retaining and communicating results.'),
('Sélectionner composants et méthodes, préparer et maintenir l’environnement et suivre des procédures de vérification et validation actualisées.','Select components and methods, prepare and maintain the environment and follow current verification and validation procedures.'),
('Maintenir des critères cohérents de vérification et validation, les appliquer puis analyser et communiquer les résultats.','Maintain consistent verification and validation criteria, apply them, and analyze and communicate results.')],
'WE':[
('Identifier les engagements et les attribuer aux groupes de travail concernés.','Identify commitments and assign them to the relevant workgroups.'),
('Affecter le travail selon les compétences, gérer entrées et sorties de rôles et maintenir la coordination dans et entre les groupes.','Assign work according to skills, manage transitions into and out of roles and maintain coordination within and across groups.'),
('Développer les compétences organisationnelles et une structure qui donne pouvoir d’agir aux groupes, avec stratégies et mécanismes de rémunération actualisés.','Develop organizational competencies and a structure that empowers workgroups, with current compensation strategies and mechanisms.')]
}
for a in D['areas']:
 if a['id']=='PQA':continue
 levels=sorted(a['deep']['levelFr'],key=int);topics=TOPICS[a['id']];assert len(levels)==len(topics),(a['id'],levels)
 a['deep']['levelFr']={lv:topics[i][0] for i,lv in enumerate(levels)};a['levelsEn']={lv:topics[i][1] for i,lv in enumerate(levels)}
 for i,entry in enumerate(a['publicGroupCourse']['entries']):
  lv=entry['groupLevel'];expected=topics[i]
  for lang in ('fr','en'):
   en=lang=='en';v=entry[lang];focus=expected[en];previous=topics[i-1][en] if i else None
   v['title']=f'PG {lv} · '+('Decision and implementation' if en else 'Décision et mise en œuvre')
   v['concept']=focus
   v['explanation']=((f'What changes from the preceding public group: {previous} The additional focus here is: {focus} Treat this as a progression of attention, not as an independent maturity rating.' if en else f'Progression depuis le groupe public précédent : {previous} L’attention supplémentaire porte ici sur : {focus} Cette progression ne constitue pas un niveau de maturité attribué indépendamment.') if previous else (f'The starting focus is practical execution: {focus} A formal document is useful only insofar as it helps explain the performed work.' if en else f'Le point de départ est une exécution observable : {focus} Un document formel est utile dans la mesure où il explique le travail effectivement réalisé.'))
   v['workedExample']=(f'Original application: ask the team to demonstrate this activity: {focus} In dossier C-{a["id"]}, D02 covers the pilot while D03 leaves the new team unexamined. Choose a relevant sample, explain the differences, and distinguish local execution from any claim about the full scope.' if en else f'Application originale : demander à l’équipe de montrer concrètement cette activité : {focus} Dans C-{a["id"]}, D02 couvre le pilote tandis que D03 laisse la nouvelle équipe non examinée. Choisir un échantillon pertinent, expliquer les différences et distinguer exécution locale et affirmation sur tout le périmètre.')
   # Different same-PA activities are plausible distractors, not silly claims
   # about a certificate or a missing document title.
   options=[focus]+[x[en] for j,x in enumerate(topics) if j!=i]
   decoys=[('Normalize outcomes across comparable populations before attributing a causal effect.' if en else 'Normaliser les résultats entre populations comparables avant d’attribuer un effet causal.'),('Analyze the cost of changing the approach before selecting a rollout schedule.' if en else 'Analyser le coût du changement de méthode avant de fixer un calendrier de déploiement.'),('Compare staff allocation with planned commitments before revising the budget.' if en else 'Comparer les affectations et engagements prévus avant de revoir le budget.')]
   options=(options+decoys)[:4];n=(i+len(a['id']))%4;options=options[n:]+options[:n];entry['answer']=(-n)%4
   v['options']=options
   v['question']=(f'The team is preparing work corresponding specifically to the public PG{lv} summary for {a["id"]}. All proposals may be useful, but which directly addresses this group’s distinctive focus?' if en else f'L’équipe prépare un travail correspondant spécifiquement au résumé public PG{lv} de {a["id"]}. Les propositions peuvent être utiles ; laquelle vise directement l’objet distinctif de ce groupe ?')
   v['why']=(f'The public PG{lv} focus is: {focus} The other activities address a different group or a separate management question. A useful activity is not automatically evidence of this particular focus.' if en else f'Le résumé public PG{lv} porte sur : {focus} Les autres activités répondent à un autre groupe ou à une question de gestion distincte. Une activité utile n’étaye pas automatiquement ce point précis.')
 # Replace generic original repeated PA paragraphs with explanatory mechanism.
 for lang in ('fr','en'):
  dest=a['en'] if lang=='en' else a['deep'];en=lang=='en'
  dest['paragraphs']=[(f'{a["en"]["title"]} starts with an operational question: {a["en"].get("scenario","")} Identify the decision that changes how the work is performed and the records that could disprove an attractive but incomplete account.' if en else f'{a["title"]} part d’une question opérationnelle : {a["scenario"]} Identifier la décision qui change la façon de travailler et les traces susceptibles de réfuter une explication séduisante mais incomplète.'),topics[0][en],('Progression through the public summaries: ' if en else 'Progression dans les résumés publics : ')+' '.join(f'PG{lv}: {topics[i][en]}' for i,lv in enumerate(levels[1:],1)),('The case files below are invented teaching material. To reason well, state what each record establishes, what remains uncertain and what new observation could change the decision. The public guide does not expose all underlying individual practice statements.' if en else 'Les dossiers ci-dessous sont des situations pédagogiques inventées. Pour raisonner, préciser ce qu’établit chaque pièce, ce qui reste incertain et quelle observation modifierait la décision. Le guide public n’expose pas tous les énoncés individuels sous-jacents.')]
(P/'data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
print('Reviewed and expanded 99 bilingual PG explanations, source-specific distinctions and same-PA checks.')
