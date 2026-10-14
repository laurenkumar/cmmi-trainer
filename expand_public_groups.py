#!/usr/bin/env python3
"""Attach original study material to the PUBLIC CMMI v4 PG summaries.

PG-level descriptions are interpretations, never alleged individual normative practices.
Each group includes a falsifiable sample, a limit of evidence, a bilingual micro-check.
"""
import json
from pathlib import Path
P=Path(__file__).parent
D=json.loads((P/'data.json').read_text(encoding='utf-8'))
# Hand-authored FR explanations in source-document PG order. No invented practice identifiers.
FR={
'CAR':['Sélectionner un résultat et commencer à traiter sa cause.','Choisir les résultats à analyser et conduire des actions sur leurs causes.','Utiliser une méthode organisationnelle de recherche de causes, suivre les actions et capitaliser les améliorations.','Employer des analyses statistiques pour examiner les causes et les effets des corrections.','Comparer les solutions et optimiser la performance à l’échelle de l’organisation.'],
'CM':['Assurer un premier contrôle des versions.','Identifier les éléments sous configuration, gérer les références, les changements et les audits d’intégrité.'],
'CONT':['Préparer une réponse aux interruptions majeures.','Prioriser les activités vitales, affecter les ressources et suivre un plan de reprise.','Déployer la formation et tester puis améliorer les plans de continuité.'],
'DM':['Fixer les objectifs de gestion des données et définir les métadonnées utiles.','Construire l’architecture de gestion des données et appliquer la méthode définie.','Déployer une capacité commune de gestion des données et contrôler son efficacité.'],
'DQ':['Définir des critères élémentaires de qualité et corriger les données défectueuses.','Définir les règles de nettoyage et suivre un processus de qualité des données.','Évaluer la qualité à l’échelle organisationnelle et améliorer le dispositif.'],
'DAR':['Identifier des options avant une décision.','Comparer les options selon des critères explicites et enregistrer la justification du choix.','Appliquer une méthode de décision et des responsabilités communes à l’organisation.'],
'ESAF':['Identifier et prioriser les dangers.','Établir des objectifs et contrôles couvrant la sécurité des personnes et la sécurité fonctionnelle.','Déployer des évaluations et contrôles de sûreté communs et agir sur les résultats.'],
'ESEC':['Identifier, prioriser et traiter les besoins de sécurité.','Définir des objectifs et une méthode cohérente pour protéger les opérations et solutions.','Déployer les opérations et revues de sécurité selon une stratégie organisationnelle.'],
'EVW':['Identifier les besoins du travail à distance et permettre son exécution.','Gérer une méthode de travail virtuel reproductible et corriger ses écarts.','Déployer une capacité de travail virtuel et réexaminer son efficacité.'],
'EST':['Produire une estimation de départ.','Estimer le périmètre, la taille, l’effort, la durée et le coût avec les hypothèses.','Employer les méthodes et mesures historiques partagées par l’organisation.'],
'GOV':['La direction fixe les objectifs importants.','La direction communique les objectifs, fournit les moyens et contrôle la responsabilité.','Vérifier que compétences, mesures et processus servent les objectifs métier.','Prendre des décisions fondées sur l’analyse quantitative des performances.'],
'II':['Appliquer les pratiques fondamentales du périmètre.','Assurer ressources, formation, actualisation et suivi des processus.','Utiliser, adapter et enrichir les actifs communs de processus.','Développer la capacité à employer des techniques quantitatives dans le travail.'],
'IRP':['Recenser les incidents et perturbations.','Suivre une méthode documentée de résolution et de communication des incidents.','Prévenir leur répétition et améliorer le dispositif à l’échelle de l’organisation.'],
'MPM':['Recueillir des mesures et traiter les problèmes de performance.','Définir les objectifs et définitions des mesures, collecter, analyser et conserver les résultats.','Aligner les mesures sur les objectifs métier et maintenir un référentiel de données de qualité.','Employer des méthodes quantitatives pour comprendre et piloter la performance.','Optimiser les processus en s’appuyant sur les résultats de performance mesurés.'],
'MST':['Identifier les menaces et vulnérabilités.','Classer, suivre et traiter les menaces selon des critères partagés.','Déployer une méthode organisationnelle et des revues régulières des menaces.','Mesurer et améliorer quantitativement la maîtrise des menaces.'],
'MC':['Enregistrer le travail accompli et résoudre les problèmes.','Comparer réalisations et prévisions, surveiller engagements et ressources, puis corriger les écarts.','Suivre les dépendances critiques et gérer les écarts selon les processus communs.'],
'OT':['Identifier les besoins de formation.','Former les personnes aux compétences nécessaires à leurs responsabilités.','Élaborer une stratégie organisationnelle de compétences et mesurer les effets des formations.'],
'PR':['Réaliser des revues entre pairs.','Planifier les revues, relever les défauts et vérifier leur correction.','Mesurer l’efficacité des revues et améliorer les pratiques communes.'],
'PLAN':['Répertorier les activités et leurs responsables.','Construire un plan réaliste intégrant estimations, capacités, budget, échéances et engagements.','Utiliser les processus organisationnels et gérer les dépendances du plan.','Améliorer la planification grâce aux approches quantitatives pertinentes.'],
'PAD':['Repérer les actifs de processus réutilisables.','Développer et mettre à disposition les modèles et guides utiles.','Maintenir et améliorer une bibliothèque organisationnelle de processus.'],
'PCM':['Aider à l’application des processus et repérer les possibilités d’amélioration.','Choisir puis déployer les améliorations de processus suivant un plan.','Relier les objectifs d’amélioration aux objectifs métier et aux processus clés.','Évaluer quantitativement les résultats des améliorations sélectionnées.'],
'PI':['Assembler et fournir une solution.','Préparer l’environnement, intégrer les composants et contrôler la solution obtenue.','Gérer les interfaces et la compatibilité des composants au niveau organisationnel.'],
'RDM':['Consigner les besoins et exigences.','Confirmer les besoins, prioriser les exigences et maintenir une traçabilité bidirectionnelle.','Développer les exigences des composants, scénarios et interfaces en contrôlant leur cohérence.'],
'RSK':['Identifier risques et opportunités.','Analyser, prioriser et suivre les réponses aux risques et opportunités.','Mettre en œuvre une méthode organisationnelle commune et l’améliorer.'],
'SDM':['Fournir les services demandés.','Planifier et contrôler la livraison selon les accords et engagements de service.','Déployer des méthodes et actifs organisationnels pour gérer les services.'],
'STSM':['Identifier les besoins et opportunités de nouveaux services.','Établir une stratégie de service cohérente avec les besoins et moyens métier.','Faire vivre la gestion stratégique des services dans l’organisation.'],
'SAM':['Identifier les fournisseurs, conclure les accords et accepter ou refuser les livrables.','Choisir selon des critères, piloter les engagements et vérifier les livraisons.','Mener des revues techniques et gérer la performance fournisseur.','Utiliser des analyses quantitatives pour améliorer la performance des fournisseurs.'],
'TS':['Créer une solution qui répond aux exigences.','Concevoir, réaliser et évaluer la solution ; documenter son utilisation.','Comparer des options techniques, arbitrer construire/acheter/réutiliser et contrôler les interfaces.'],
'VV':['Vérifier la conformité aux exigences et valider l’usage dans l’environnement cible.','Choisir les méthodes, environnements et procédures de vérification et de validation.','Définir des critères communs et analyser systématiquement les résultats.'],
'WE':['Identifier les responsabilités à affecter aux groupes de travail.','Attribuer les missions selon compétences, gérer les transitions et coordonner les équipes.','Développer compétences, structures et mécanismes durables d’autonomisation.'],
}
# Concrete situations: decision, trace with stronger probative value, weak conflicting trace.
SCENARIOS={
'CAR':('Incidents identiques après trois mises en production','analyse datée des causes et mesure des récidives','liste des tickets fermés sans cause commune'),
'CM':('Deux versions concurrentes d’une livraison en production','baseline horodatée, approbation du changement, audit de configuration','dépôt Git seul, sans règle de release'),
'CONT':('Coupure électrique d’un centre de support','plan testé avec RTO et journal d’exercice','plan signé mais jamais exercé'),
'DM':('Données clients redondantes dans plusieurs outils','catalogue, propriétaire et règle d’accès vérifiables','schéma technique sans responsabilité sur les données'),
'DQ':('Codes postaux incohérents dans 18 % des dossiers','règle de validation, échantillon après correction et suivi du taux','nettoyage ponctuel sans critères communs'),
'DAR':('Choisir entre deux hébergeurs critiques','matrice de critères pondérés et décision motivée','choix du directeur sans comparaison'),
'ESAF':('Fonction de sécurité non testée sur un automate','analyse de dangers, mesures de maîtrise et résultat de tests','promesse que le fournisseur est certifié'),
'ESEC':('Réutilisation de comptes d’administration partagés','registre des accès, actions de remédiation et revue effective','politique de mots de passe non appliquée'),
'EVW':('Équipe répartie sur trois fuseaux horaires','protocole d’astreinte, retour d’expérience et suivi de disponibilité','déclaration « le télétravail marche »'),
'EST':('Chiffrage d’une refonte applicative','hypothèses d’effort, références historiques et écarts mesurés','date imposée sans périmètre estimé'),
'GOV':('La direction annonce « zéro retard »','revue de résultats et décision d’allocation budgétaire','slogan diffusé à tous mais sans moyens'),
'II':('Une procédure commune reste inutilisée','formation, échantillon d’usage et ajustement des moyens','manuel validé sans vérification de terrain'),
'IRP':('Panne récurrente de l’API de paiement','chronologie d’incident, résolution et contrôle de non-récidive','message « incident clos » sans analyse'),
'MPM':('Délais clients en hausse malgré le volume livré','définitions stables, séries temporelles et décision corrective','dashboard comportant des chiffres incomparables'),
'MST':('Serveurs exposés à une vulnérabilité majeure','inventaire d’exposition, priorisation et preuve de correction','bulletin CVE simplement transféré par email'),
'MC':('Budget consommé plus vite que le travail','écarts réels/prévus, décision de révision et effet constaté','statut vert malgré un dépassement documenté'),
'OT':('Techniciens non formés à un nouvel outil','matrice des besoins, formation puis vérification en situation','feuille d’émargement comme unique preuve de compétence'),
'PR':('Défauts d’architecture découverts en recette','compte rendu de revue, défauts et preuve de leur correction','commentaires informels non suivis'),
'PLAN':('Planning accepté malgré un manque de ressources','capacité, dépendances, jalons et engagements réconciliés','diagramme de Gantt sans accord des intervenants'),
'PAD':('Cinq projets recréent le même modèle qualité','bibliothèque versionnée et mesure des usages','dossier partagé obsolète et introuvable'),
'PCM':('Processus de déploiement génère des retouches','priorisation des améliorations, expérimentation et résultats','réorganisation décidée sans mesure d’effet'),
'PI':('Trois modules fonctionnent seuls mais pas ensemble','contrats d’interface, résultat d’intégration et anomalies corrigées','tests unitaires seuls'),
'RDM':('Modification d’exigence non propagée aux tests','traçabilité bidirectionnelle et analyse d’impact signée','tableau d’exigences sans liens aux livrables'),
'RSK':('Dépendance à un fournisseur unique','registre de probabilité/impact, mesures et suivi de réponse','liste des risques jamais réévaluée'),
'SDM':('Demandes client traitées hors délai','engagements SLA, tickets horodatés et actions sur les écarts','score de satisfaction sans délai réel'),
'STSM':('Service populaire mais déficitaire','analyse de portefeuille, besoins, capacité et décision stratégique','nouveau service lancé sans analyse de valeur'),
'SAM':('Livrables d’un sous-traitant incomplets','accord signé, critères d’acceptation et revue de performance','facture réglée comme preuve de conformité'),
'TS':('Deux architectures répondent aux mêmes besoins','arbitrage documenté, contraintes et tests de conception','architecture préférée du développeur senior'),
'VV':('Solution conforme au cahier des charges mais inutilisable','tests de conformité ET essai utilisateur en environnement cible','100 % de tests unitaires comme preuve d’usage réel'),
'WE':('Départs fréquents et surcharge dans une équipe','affectations, compétences, transferts et mesures d’engagement','organigramme sans vérification des rôles'),
}
# Specific qualitative questions test how evidence progresses, not identification alone.
LADDER={1:('initial observation','première observation'),2:('managed and repeatable','gérée et reproductible'),3:('organization-wide','étendue à l’organisation'),4:('quantitatively informed','étayée quantitativement'),5:('statistically optimized','optimisée statistiquement')}
for area in D['areas']:
 if area['id']=='PQA':continue
 ident=area['id']; levels=area['levelsEn']; translations=FR[ident]
 assert len(translations)==len(levels),(ident,translations,levels)
 scene,strong,weak=SCENARIOS[ident]; en_scene=area['en']['scenario']; en_strong=area['en']['evidence']; en_weak=area['en']['pitfall']; entries=[]
 for i,(lv,en) in enumerate(levels.items()):
  n=int(lv);fr=translations[i]
  maturity_en,maturity_fr=LADDER[n]
  true_en=f'At this stage: {en}'
  true_fr=f'À ce stade : {fr}'
  # The worked example is explicitly an illustration, not a claimed normative practice.
  if n==1:
   worked_fr=f'Une équipe constate : « {scene} ». Elle documente un premier cas vérifiable et une action de départ, sans prétendre que tous les projets fonctionnent déjà ainsi.'
   worked_en=f'A team observes: “{en_scene}.” It records one verifiable instance and initial action without claiming organization-wide adoption.'
   evidence_fr=f'Départ utile : {strong}. La trace seule ne démontre pas la généralisation.'
   evidence_en=f'Useful initial record: {en_strong}. One case does not establish broad adoption.'
  elif n==2:
   worked_fr=f'Deux projets comparables rencontrent « {scene} ». Ils suivent une méthode gérée, conservent leurs décisions et expliquent les écarts avec les engagements.'
   worked_en=f'Two comparable projects encounter “{en_scene}.” They follow a managed approach, retain decisions, and explain deviations from commitments.'
   evidence_fr=f'À vérifier : {strong}, responsable désigné et suivi daté sur les projets pertinents.'
   evidence_en=f'Check: {en_strong}, identified owner, and dated follow-up in relevant project samples.'
  elif n==3:
   worked_fr=f'L’organisation publie un cadre commun applicable au cas « {scene} » ; deux équipes démontrent comment elles l’ont adapté et remontent leurs résultats à un référentiel partagé.'
   worked_en=f'The organization deploys common guidance for “{en_scene}”; two teams demonstrate tailoring and feed their findings into shared organizational assets.'
   evidence_fr=f'À vérifier : {strong}, référentiel partagé, adaptations approuvées et revues de mise en œuvre.'
   evidence_en=f'Check: {en_strong}, shared assets, authorized tailoring and implementation reviews.'
  elif n==4:
   worked_fr=f'L’organisation mesure les résultats relatifs à « {scene} » avec des définitions cohérentes et des méthodes quantitatives appropriées ; elle documente les décisions fondées sur ces résultats.'
   worked_en=f'The organization measures outcomes for “{en_scene}” using consistent definitions and appropriate quantitative techniques, documenting decisions informed by those results.'
   evidence_fr=f'À vérifier : {strong}, cohérence des données, séries temporelles et justification statistique.'
   evidence_en=f'Check: {en_strong}, data comparability, time series and justified statistical methods.'
  else:
   worked_fr=f'L’organisation compare plusieurs interventions sur « {scene} », mesure l’effet des améliorations, puis choisit une optimisation fondée sur des résultats robustes.'
   worked_en=f'The organization compares interventions for “{en_scene},” evaluates the effect of improvements and selects an optimization supported by robust performance evidence.'
   evidence_fr=f'À vérifier : {strong}, comparaison avant/après, incertitude et pérennité des gains.'
   evidence_en=f'Check: {en_strong}, before/after comparison, uncertainty and sustained improvement.'
  bad_fr=f'Contre-exemple : {weak}. Ne pas confondre cette affirmation avec une démonstration.'
  bad_en=f'Counterexample: {en_weak}. Do not mistake this statement for proof of consistent implementation.'
  opts_fr=[f'Examiner {strong} au regard du niveau {n} et des projets concernés.',f'Accepter {weak} sans autre vérification.',f'Conclure automatiquement que l’organisation a atteint le niveau de maturité {n}.']
  opts_en=[f'Examine {en_strong} against level {n} and the sampled work.',f'Accept {en_weak} without further checking.',f'Automatically declare organizational maturity level {n}.']
  rotation=(len(ident)+n)%3
  opts_fr=opts_fr[rotation:]+opts_fr[:rotation]
  opts_en=opts_en[rotation:]+opts_en[:rotation]
  answer=(3-rotation)%3
  entries.append({'groupLevel':n,'provenance':'public-pg-summary','sourcePage':area['page'],'en':{'title':f'Practice Group {n} — {maturity_en.title()}','concept':true_en,'workedExample':worked_en,'evidence':evidence_en,'pitfall':bad_en,'question':f'What would best support the level {n} claim for this case?','options':opts_en,'why':f'Use the publicly summarized PG{n} intent, then check records and corroboration. A project example alone never establishes an official maturity rating.'},'fr':{'title':f'Practice Group {n} — {maturity_fr.capitalize()}','concept':true_fr,'workedExample':worked_fr,'evidence':evidence_fr,'pitfall':bad_fr,'question':f'Quel examen de preuve défend le mieux une affirmation de niveau {n} dans ce cas ?','options':opts_fr,'why':f'Il faut raisonner à partir du résumé public PG{n}, recouper les traces et préserver les limites de l’échantillon. Une simulation ne produit pas de niveau officiel.'},'answer':answer})
 area['publicGroupCourse']={'status':'interpretation-from-public-summary','source':'CMMI Model Quick Reference Guide v4.0 (2026)','sourceUrl':'https://www.isaca.org/resources/reference-guide/cmmi-model-quick-reference-guide','sourcePage':area['page'],'disclaimer':{'fr':f'{area["officialPracticeCount"]} pratiques officielles existent dans cette PA. Les cartes ci-dessous expliquent les {len(entries)} résumés publics des Practice Groups ; ce ne sont PAS les énoncés individuels complets du modèle sous licence. Exemples et exercices créés pour apprendre.','en':f'This PA contains {area["officialPracticeCount"]} official practices. The {len(entries)} cards below interpret public Practice Group summaries, NOT the complete licensed individual practice statements. Examples and questions are original teaching materials.'},'entries':entries}
D['v7PublicCoverage']={'publicGroupAreas':30,'officialDetailedPracticeAreas':1,'officialIndividualPracticeExcerpts':'PQA only (6)','publicGroupCards':sum(len(a.get('publicGroupCourse',{}).get('entries',[])) for a in D['areas']),'officialIndividualStatementsTotalAccordingToGuide':sum(a['officialPracticeCount'] for a in D['areas']),'warning':'PG summaries do not describe each underlying individual normative practice. Content is original instructional interpretation of the publicly available guide.'}
(P/'data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print(D['v7PublicCoverage'])