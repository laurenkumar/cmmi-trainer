#!/usr/bin/env python3
"""Original applications of public PA summaries. No invented practice IDs.

Each example, calculation and teaching recommendation is fictional. The public
source anchors the topic, not the made-up numbers or the proposed record format.
"""
from pathlib import Path
import json, runpy
P=Path(__file__).resolve().parent.parent
D=json.loads((P/'data.json').read_text())
# Why the distinction matters, then a fully worked transfer example (FR / EN).
LESSONS={
'CAR':(
"Une corrélation indique où chercher, pas quelle cause retenir. Reconstituer la chaîne événement → mécanisme → résultat permet de proposer une action qui modifie réellement le mécanisme. Les causes d'un succès peuvent aussi être analysées pour le reproduire.",
"Correlation indicates where to investigate, not which cause to accept. Reconstructing event → mechanism → outcome makes it possible to select an action that changes the mechanism. Successful outcomes can also be analyzed to support repetition.",
"Le pilote passe de 12 incidents pour 120 livraisons à 6 pour 40 : le taux augmente de 10 % à 15 %, malgré une baisse du nombre. Les six incidents ont-ils emprunté le contrôle contourné ? Comparer les journaux et les types de livraison avant d'attribuer un effet à la correction.",
"A pilot moves from 12 incidents in 120 releases to 6 in 40: the rate increases from 10% to 15% despite a lower count. Did the six incidents pass through the bypassed control? Compare execution logs and release mix before attributing an effect to the fix."),
'CM':(
"L'historique de versions répond à « qu'est-ce qui a changé ? ». L'intégrité d'une référence ajoute « quel ensemble exact était autorisé et livré ? ». Un dépôt complet ne prouve donc pas l'identité du binaire installé. Un audit de configuration rapproche les éléments identifiés et leur état réel.",
"Version history answers what changed. Baseline integrity also asks which exact set was authorized and delivered. A complete repository therefore does not prove the identity of the installed binary. A configuration audit reconciles identified items with actual status.",
"B17 référence le code C17, la configuration K4 et la bibliothèque L8. Le serveur contient C17/K5/L8. Le code est correct mais l'ensemble diffère. Retrouver l'autorisation de K5, son impact et le paquet réellement déployé avant de corriger le manifeste ou d'envisager un retour arrière.",
"B17 references code C17, configuration K4 and library L8. The server contains C17/K5/L8. The code matches but the set differs. Trace K5 authorization, impact and the deployed package before correcting the manifest or considering rollback."),
'CONT':(
"Continuer une activité critique exige davantage qu'une sauvegarde. La chaîne inclut personnes, accès, dépendances, communication et ordre de reprise. Un exercice vérifie la procédure et teste si le service utile reprend dans les conditions envisagées ; ces deux questions peuvent avoir des résultats différents.",
"Continuing a critical activity requires more than backups. The chain includes people, access, dependencies, communication and recovery order. An exercise checks the procedure and tests whether a usable service resumes under intended conditions; these questions can have different answers.",
"La base est restaurée en 40 minutes mais l'identité reste indisponible 3 heures. Les clients ne peuvent pas commander : mesurer seulement la restauration de la base masque l'échec métier. Rejouer la reprise de bout en bout et modifier la dépendance bloquante dans le plan.",
"The database restores in 40 minutes but identity remains unavailable for 3 hours. Customers cannot order: timing only database restoration hides business failure. Rehearse end-to-end recovery and address the blocking dependency in the plan."),
'DM':(
"Gérer les données consiste à rendre leur sens, leur circulation et leur responsabilité explicables. Les métadonnées permettent de savoir ce qu'un champ signifie ; l'architecture explique où il est transformé. La qualité des valeurs relève d'une question voisine, DQ, sans remplacer cette organisation.",
"Data management makes meaning, movement and responsibility explainable. Metadata describes what a field means; architecture explains where it is transformed. Value quality is the neighboring DQ concern and does not replace this management structure.",
"Le champ « revenu » désigne du brut dans CRM et du net dans Finance. Les deux bases sont exactes selon leur définition mais une jointure produit une comparaison trompeuse. Identifier définition, propriétaire, transformation et consommateur, puis vérifier une transaction traversant les deux systèmes.",
"Revenue means gross in CRM and net in Finance. Both databases can be accurate under their definitions while a join yields a misleading comparison. Identify definition, owner, transformation and consumer, then trace one transaction through both systems."),
'DQ':(
"La qualité dépend de l'usage : validité de format, complétude et exactitude ne sont pas interchangeables. Nettoyer un extrait traite des valeurs présentes. Définir des critères et revoir le mécanisme d'entrée aide à comprendre pourquoi les mêmes défauts reviennent et si l'activité est efficace.",
"Quality depends on use: format validity, completeness and accuracy are not interchangeable. Cleansing an extract addresses current values. Defining criteria and examining the intake mechanism helps explain recurring defects and whether quality activities work.",
"990 lignes valides sur 1 000 conservées donnent 99 %. Si 100 lignes invalides ont été exclues à l'import, le taux sur les 1 100 reçues est 90 %. Préciser le dénominateur et tracer les rejets avant de communiquer une amélioration ; le choix du périmètre change la décision.",
"990 valid rows among 1,000 retained rows gives 99%. If intake excluded 100 invalid rows, validity among 1,100 received rows is 90%. State the denominator and trace rejected rows before reporting improvement; scope changes the decision."),
'DAR':(
"Une matrice de notes rend une décision visible, mais ne garantit ni la comparabilité des données ni la qualité des critères. Séparer besoin, contraintes éliminatoires, critères de préférence et méthode d'évaluation évite d'habiller après coup un choix déjà fait.",
"A scoring matrix makes a decision visible but guarantees neither comparable evidence nor sound criteria. Separating needs, exclusion constraints, preference criteria and evaluation method avoids retrofitting a justification to a choice already made.",
"A coûte 80 et obtient 6/10 en fiabilité ; B coûte 100 et obtient 9/10. Avec un poids coût de 80 %, A gagne ; avec 30 %, B peut gagner. Examiner la sensibilité et les hypothèses métier. Aucun poids universel n'est imposé par cet exemple pédagogique.",
"A costs 80 and scores 6/10 for reliability; B costs 100 and scores 9/10. A can win at 80% cost weight and B at 30%. Examine sensitivity and business assumptions. This teaching example imposes no universal weighting rule."),
'ESAF':(
"Un danger, une exposition et un dommage sont liés sans être identiques. La présence d'un contrôle ne démontre pas que le risque résiduel est tolérable. Examiner le contexte d'usage et les limites de fonctionnement du contrôle permet d'éviter une acceptation basée sur un essai sans rapport avec le terrain.",
"Hazard, exposure and harm are related but distinct. A control's presence does not establish tolerable residual risk. Examining use context and control operating limits prevents acceptance based on a test unrelated to field conditions.",
"L'arrêt automatique fonctionne à 20 °C ; la machine sera utilisée à −10 °C. Le certificat du composant ne comble pas cette lacune. Examiner la tolérance applicable et l'essai dans l'environnement prévu, puis documenter la décision de traitement du danger et ses limites.",
"An automatic stop works at 20°C; the machine will operate at −10°C. A component certificate does not fill that gap. Examine applicable tolerance and testing in the intended environment, then record the hazard-handling decision and its limits."),
'ESEC':(
"Une approche de sécurité relie besoins et objectifs aux chemins d'accès, aux rôles et aux opérations. Un contrôle fort sur l'écran principal peut être contourné par l'assistance ou un compte de secours. ESEC organise cette capacité ; MST approfondit l'analyse des menaces et vulnérabilités.",
"A security approach links needs and objectives to access paths, roles and operations. A strong main-login control can be bypassed through support or emergency accounts. ESEC organizes capability; MST focuses more closely on threats and vulnerabilities.",
"Tous les utilisateurs passent la MFA, sauf le compte de secours partagé utilisé chaque nuit. Le taux de connexions MFA masque ce chemin. Rapprocher autorisations, usages et réinitialisations, puis examiner une solution qui préserve aussi la continuité d'exploitation.",
"All users pass MFA except a shared emergency account used nightly. MFA adoption rates hide this path. Reconcile authorizations, actual use and resets, then examine a response that also preserves operating continuity."),
'EVW':(
"Installer un outil de visioconférence ne constitue pas à lui seul une méthode de travail virtuel. Les contraintes de fuseau, d'accès, de transmission et de coordination déterminent si le travail peut réellement avancer. Revoir l'efficacité suppose de regarder les résultats et les blocages, pas seulement les connexions.",
"Installing video-conferencing software alone does not establish a virtual-work approach. Time zones, access, handoffs and coordination determine whether work can proceed. Reviewing effectiveness means examining outcomes and blockers rather than connection counts alone.",
"Paris transmet une demande à 18 h ; l'équipe distante ne la voit qu'après une journée d'attente. Les réunions sont suivies mais les décisions manquent dans le dossier partagé. Tester une transmission asynchrone avec contexte, décision et responsable avant de multiplier les réunions.",
"Paris hands over a request at 18:00; the remote team sees it after a day's delay. Meetings are attended but decisions are absent from the shared record. Test an asynchronous handoff with context, decision and owner before adding more meetings."),
'EST':(
"Une estimation exprime une prévision et ses hypothèses ; un engagement est une décision prise à partir de cette prévision et des contraintes. Taille, effort, durée et coût ne se déduisent pas mécaniquement l'un de l'autre. Des données historiques ne sont pertinentes que si leur contexte est comparable.",
"An estimate is a forecast with assumptions; a commitment is a decision made using that forecast and constraints. Size, effort, duration and cost do not mechanically determine one another. Historical data is useful only when context is sufficiently comparable.",
"100 composants à 2 heures donnent 200 heures de réalisation. Ajouter 40 heures d'intégration mène à 240 heures. Deux personnes disponibles 20 heures par semaine chacune suggèrent 6 semaines de charge, avant dépendances et aléas ; ce calcul n'est pas une promesse de date.",
"100 components at 2 hours each imply 200 build hours. Adding 40 integration hours gives 240. Two people available 20 hours weekly each suggest 6 weeks of workload, before dependencies and uncertainty; this is not a promised date."),
'GOV':(
"La gouvernance relie les objectifs métier aux arbitrages et à la responsabilité de la direction. Une politique signée ne fournit pas les ressources nécessaires et un tableau de bord ne décide pas à la place du sponsor. Chercher comment l'information reçue modifie priorités, moyens ou suivi.",
"Governance connects business objectives to senior-management decisions and accountability. A signed policy does not provide resources, and a dashboard does not make sponsor decisions. Trace how received information changes priorities, resources or oversight.",
"La direction vise un délai de 5 jours, mais les dossiers attendent 8 jours faute de capacité. Le reporting hebdomadaire existe depuis trois mois sans arbitrage. Une décision étayée examine capacité et priorités, attribue une action puis vérifie son effet au lieu d'exiger un indicateur vert.",
"Management targets a 5-day lead time but cases wait 8 days because capacity is insufficient. Weekly reporting has run for three months without a decision. An informed decision examines capacity and priorities, assigns action and checks its effect rather than demanding a green indicator."),
'II':(
"L'infrastructure d'implémentation rend l'usage durable : moyens, compétences, processus utilisables et retours du travail réel. Elle complète GOV : la direction soutient et arbitre, tandis que les équipes doivent disposer des conditions pour appliquer les processus et signaler ce qui ne fonctionne pas.",
"Implementation infrastructure sustains use through resources, skills, usable processes and operational feedback. It complements GOV: management sponsors and decides, while teams need practical conditions to apply processes and report what fails.",
"Une procédure impose une revue mais les outils n'autorisent aucun relecteur externe à l'équipe. Les écarts ne sont donc pas seulement un manque de volonté. Examiner l'accès, la charge et les compétences, puis vérifier une revue réalisée après correction des conditions de travail.",
"A procedure calls for review but tools grant no access to reviewers outside the team. Deviations therefore need not indicate unwillingness. Examine access, workload and skills, then inspect an actual review after working conditions are corrected."),
'IRP':(
"Rétablir le service traite l'incident présent. Prévenir une nouvelle perturbation demande d'analyser des incidents sélectionnés et leurs résolutions. Une clôture administrative n'est pas équivalente à un rétablissement vérifié, ni un redémarrage à une action de prévention durable.",
"Restoring service handles the current incident. Preventing future disruption requires analysis of selected incidents and resolutions. Administrative closure is not verified restoration, and a restart is not necessarily lasting prevention.",
"Le même service redémarre cinq fois dans la semaine ; chaque ticket respecte le délai de clôture. Le client subit pourtant cinq interruptions. Relier les tickets, vérifier le rétablissement et analyser les données de résolution pour choisir une action de prévention suivie dans le temps.",
"The same service restarts five times in a week and every ticket meets its closure target. Customers still experience five disruptions. Link tickets, verify restoration and analyze resolution data to choose a prevention action tracked over time."),
'MPM':(
"Une mesure utile a un objectif et une définition opérationnelle : unité, période, population et traitement des exclusions. Sans cela, un chiffre stable peut masquer un changement de méthode. Une référence statistique décrit un comportement observé ; elle n'est pas une limite contractuelle ni une cible métier.",
"A useful measure has an objective and an operational definition: unit, period, population and exclusions. Otherwise a stable figure may hide a changed method. A statistical baseline describes observed behavior; it is neither a contractual limit nor a business target.",
"L'équipe A compte le délai depuis la demande ; B depuis l'acceptation. Leurs moyennes de 8 et 5 jours ne sont pas comparables. Recalculer une période commune, vérifier exclusions et variation, puis choisir l'analyse appropriée avant de déclarer B plus performante.",
"Team A measures lead time from request; B from acceptance. Means of 8 and 5 days are not comparable. Recalculate using a common starting point, check exclusions and variation, then choose suitable analysis before declaring B better."),
'MST':(
"Une vulnérabilité est une faiblesse ; une menace peut l'exploiter dans un contexte donné. Le score technique seul ne fixe pas l'ordre de traitement. Exposition, actifs concernés et efficacité des réponses changent la décision. L'analyse quantitative soutient le choix sans convertir une probabilité incertaine en certitude.",
"A vulnerability is a weakness; a threat may exploit it in a particular context. Technical score alone does not determine handling order. Exposure, affected assets and response effectiveness change the decision. Quantitative analysis supports choices without turning uncertain likelihood into certainty.",
"Une faille notée 9 touche un poste isolé ; une faille notée 7 permet d'atteindre une passerelle exposée critique. Examiner exposition et conséquences avant de prioriser. Après correction, vérifier le chemin d'exploitation : fermer le ticket ne démontre pas l'efficacité du contrôle.",
"A score-9 flaw affects an isolated workstation; a score-7 flaw reaches a critical exposed gateway. Examine exposure and consequences before prioritizing. After remediation, verify the exploit path: closing a ticket does not establish control effectiveness."),
'MC':(
"Le suivi compare le réel à une référence explicite puis conduit à des actions lorsque l'écart le justifie. Changer la référence pour rendre l'indicateur vert ne résout pas la cause du retard. Une replanification peut être légitime si les effets, engagements et décisions restent compréhensibles.",
"Monitoring compares actuals with an explicit reference and leads to action when deviations warrant it. Changing the reference to turn an indicator green does not resolve delay. Replanning can be legitimate when effects, commitments and decisions remain traceable.",
"Le plan prévoyait 40 tâches et 200 heures ; 30 tâches consomment déjà 210 heures. « 75 % terminé » masque la dérive d'effort et la taille des tâches restantes. Examiner estimation à terminaison, dépendances et actions avec les parties concernées avant de reconfirmer la date.",
"The plan allows 40 tasks and 200 hours; 30 tasks have already consumed 210 hours. '75% complete' hides effort variance and remaining task size. Examine completion forecast, dependencies and corrective action with affected stakeholders before reconfirming the date."),
'OT':(
"Une formation dispensée, une connaissance acquise et une compétence appliquée sont trois observations différentes. La formation organisationnelle relie besoins des rôles, offre de formation et efficacité. La participation peut être nécessaire à suivre sans constituer une preuve suffisante de progrès dans le travail.",
"Training delivered, knowledge acquired and skill applied are different observations. Organizational training connects role needs, training provision and effectiveness. Attendance can be worth tracking without sufficiently demonstrating improvement in actual work.",
"Les 20 analystes suivent le cours et réussissent le quiz. Deux semaines plus tard, 8 dossiers sur 10 omettent encore l'analyse demandée. Observer une tâche réelle, vérifier les obstacles et ajuster formation ou conditions de travail plutôt que rééditer les attestations.",
"All 20 analysts attend and pass the quiz. Two weeks later, 8 of 10 work records still omit the intended analysis. Observe a real task, investigate barriers and adjust training or working conditions rather than reissuing certificates."),
'PR':(
"Une revue par les pairs recherche des problèmes dans un produit de travail avec une préparation adaptée. Une approbation de diffusion et une revue technique ne répondent pas toujours à la même question. Les résultats deviennent utiles lorsqu'on relie les défauts repérés à leur traitement et, ensuite, à des enseignements.",
"A peer review looks for work-product issues using suitable preparation. Release approval and technical review do not always answer the same question. Findings become useful when identified defects are connected to resolution and then to learning.",
"Une conception reçoit deux signatures mais le registre ne décrit aucun point examiné. Un calcul critique reste faux dans la version livrée. Reprendre le produit, les critères de revue, les compétences des relecteurs et la résolution des observations ; ajouter une signature ne corrige pas le calcul.",
"A design receives two signatures but the log describes no examined issues. A critical calculation remains wrong in the delivered version. Inspect the product, review criteria, reviewer expertise and issue resolution; adding a signature does not fix the calculation."),
'PLAN':(
"Le plan transforme une prévision en organisation du travail : ressources, compétences, dépendances et engagements doivent être cohérents. L'estimation relève de EST ; PLAN utilise cette base et réconcilie le travail avec la capacité disponible. L'accord des acteurs compte lorsqu'une dépendance menace la réalisation.",
"A plan turns a forecast into organized work: resources, skills, dependencies and commitments must be coherent. EST supplies estimates; PLAN uses them and reconciles work with available capacity. Stakeholder agreement matters when a dependency threatens delivery.",
"Le projet demande 240 heures sur quatre semaines. Deux personnes n'offrent que 20 heures par semaine chacune, soit 160 heures. Le déficit de 80 heures doit être arbitré par périmètre, capacité ou calendrier. Une signature du planning ne fait pas disparaître ce déficit.",
"A project requires 240 hours over four weeks. Two people each offer 20 hours weekly, totaling 160 hours. The 80-hour gap requires a scope, capacity or schedule decision. A signed schedule does not remove it."),
'PAD':(
"Un actif de processus est utile s'il aide à refaire un travail de façon comprise et reproductible. Sa publication ne garantit pas sa pertinence ou son accessibilité. Une bibliothèque commune doit permettre de trouver la bonne version et de comprendre comment l'adapter sans perdre le but recherché.",
"A process asset is useful when it supports understandable, repeatable work. Publication does not guarantee relevance or accessibility. A shared library should let users find the right version and understand how to adapt it while preserving its purpose.",
"Le modèle de revue v3 est publié mais les nouveaux arrivants téléchargent v1 depuis un ancien favori. Le compteur de fichiers publiés augmente alors que le travail utilise l'ancienne version. Tester la recherche et les accès d'un utilisateur, puis corriger le chemin de diffusion et l'obsolescence.",
"Review template v3 is published but new starters download v1 through an old bookmark. Published-file counts rise while work uses the old version. Test discovery and access as a user, then correct distribution and obsolete entry points."),
'PCM':(
"L'amélioration de processus commence par un problème de performance et un objectif, pas par le déploiement d'un outil choisi à l'avance. L'adoption et l'effet sont deux résultats différents. Un pilote aide à examiner la proposition ; la pérennité suppose ensuite un déploiement et un suivi adaptés.",
"Process improvement starts from a performance problem and objective rather than a tool selected in advance. Adoption and effect are different outcomes. A pilot helps examine the proposal; sustained improvement then needs suitable deployment and follow-up.",
"Un nouveau formulaire est utilisé dans 95 % des dossiers. Le taux de reprise reste à 18 %. Cela étaye l'adoption, pas l'effet espéré sur les reprises. Examiner quels défauts le changement devait prévenir, puis comparer les résultats pertinents avec leurs conditions avant de généraliser une conclusion.",
"A new form appears in 95% of cases while rework remains 18%. This supports adoption, not the intended rework benefit. Examine which defects the change was meant to prevent, then compare relevant outcomes and conditions before generalizing a conclusion."),
'PQA':(
"L'assurance qualité examine des processus et produits de travail contre des références enregistrées. L'objectivité vient de critères explicites et d'un examen traçable ; l'exemple ne déduit aucune obligation d'auditeur externe. Une opportunité d'amélioration peut exister même si aucun écart n'est établi.",
"Quality assurance evaluates processes and work products against recorded references. Objectivity relies on explicit criteria and traceable evaluation; this example infers no requirement for an external auditor. An improvement opportunity can exist without an established deviation.",
"Le responsable signe la clôture d'un écart puis l'échantillon suivant retrouve la même absence de test. La signature prouve une décision, pas la correction. Relier constat, critère, communication, action et contrôle du résultat ; rouvrir le suivi de la lacune non résolue selon les dispositions applicables.",
"The owner signs closure of a finding, then the next sample still lacks the same test. The signature establishes a decision, not correction. Link finding, criterion, communication, action and result check; resume follow-up of the unresolved gap under applicable arrangements."),
'PI':(
"Deux composants corrects séparément peuvent échouer ensemble. L'intégration relie stratégie, environnement, identification des composants et compatibilité des interfaces. Un test unitaire de chacun ne prouve pas leur comportement combiné. Les descriptions de connexion doivent évoluer avec la solution.",
"Two components that work separately can fail together. Integration connects strategy, environment, component identity and interface compatibility. Unit tests for each do not establish combined behavior. Connection descriptions need to evolve with the solution.",
"A envoie une date UTC ; B la lit comme une date locale. Chaque composant passe ses tests mais les commandes changent de jour à l'intégration. Comparer contrat d'interface, versions et test combiné dans l'environnement prévu avant de conclure que l'un des composants est seul responsable.",
"A sends UTC timestamps; B reads them as local time. Both pass unit tests but orders shift days during integration. Compare the interface contract, versions and combined testing in the intended environment before blaming one component alone."),
'RDM':(
"Développer des exigences cherche une compréhension partagée du besoin ; les gérer maintient la cohérence après changement. Une matrice de traçabilité prouve des liens seulement s'ils restent valides. Le lien doit aider à retrouver l'effet d'une modification sur les produits, activités et plans, dans les deux directions.",
"Requirements development seeks shared understanding of needs; management preserves consistency through change. A trace matrix supports links only while they remain valid. Links should help trace a change's effects on products, activities and plans in both directions.",
"R12 v2 réduit un délai à 2 secondes. La conception change, mais T12 vérifie encore le seuil de 5 secondes de v1. La case « test lié » est vraie sans démontrer v2. Suivre le changement jusqu'au critère du test, au résultat et à l'engagement des acteurs concernés.",
"R12 v2 reduces response time to 2 seconds. Design changes but T12 still checks v1's 5-second limit. 'Test linked' is true without demonstrating v2. Trace the change to the test criterion, result and commitments of affected stakeholders."),
'RSK':(
"Un risque est une possibilité défavorable, un problème est déjà observé et une opportunité peut produire un effet favorable. Les identifier ne suffit pas : l'analyse oriente une réponse et la surveillance vérifie son actualité. Une matrice probabilité-impact est une aide possible, pas une formule universelle imposée ici.",
"A risk is a possible adverse event, an issue is already observed and an opportunity can have a favorable effect. Identification alone is insufficient: analysis guides handling and monitoring keeps it current. A likelihood-impact matrix is one possible aid, not a universal formula imposed here.",
"Un fournisseur pourrait livrer dix jours trop tard. Le registre nomme un propriétaire mais personne ne suit le jalon qui déclenche la solution de secours. Clarifier le signal, la réponse et la décision de déclenchement. Pour une automatisation, comparer aussi le bénéfice potentiel et le risque d'intégration.",
"A supplier may deliver ten days late. The register names an owner but nobody monitors the milestone that triggers the fallback. Clarify the signal, response and activation decision. For automation, also compare potential benefit with integration risk."),
'SDM':(
"La gestion de service relie ce qui est convenu, les demandes reçues et le système capable de les traiter. Un délai contractuel ne s'applique correctement qu'avec des définitions cohérentes. L'état de préparation du service compte avant d'accepter une nouvelle charge ou une modification.",
"Service management connects agreements, incoming requests and a system capable of handling them. A contractual time target requires consistent definitions. Service readiness matters before accepting new load or a change.",
"L'accord annonce une réponse en 4 heures ; le tableau de bord mesure une première réponse automatique en 2 minutes alors que le traitement démarre après 9 heures. Clarifier la définition convenue, suivre la demande et vérifier capacité et disponibilité du système avant de déclarer l'engagement tenu.",
"The agreement promises a response within 4 hours; the dashboard times a 2-minute automatic acknowledgment while handling starts after 9 hours. Clarify the agreed definition, trace the request and check system capacity and readiness before declaring the commitment met."),
'STSM':(
"La stratégie de services choisit ce que l'organisation veut offrir au regard des besoins métier et des capacités. Le catalogue n'est pas seulement une liste commerciale. Il relie descriptions, niveaux de service et décisions sur les offres nouvelles ou modifiées. SDM organise ensuite la livraison du service convenu.",
"Service strategy chooses what the organization offers in light of business needs and capabilities. A catalog is more than a sales list. It connects descriptions, service levels and decisions about new or changed offerings. SDM then manages delivery of agreed services.",
"Les commerciaux proposent du 24/7 alors que l'organisation ne dispose que d'une équipe de jour. Les demandes clients montrent un besoin de nuit limité à deux comptes. Comparer options, capacité et besoins stratégiques avant de standardiser l'offre, puis aligner description et niveau annoncé.",
"Sales offers 24/7 support while the organization has only a daytime team. Customer evidence shows night demand concentrated in two accounts. Compare options, capacity and strategic needs before standardizing the offer, then align description and advertised level."),
'SAM':(
"La relation fournisseur suit une chaîne de décisions : sélection, accord, pilotage, acceptation et paiement. Une facture réglée ne prouve pas la conformité du livrable. Des critères connus à l'avance permettent de distinguer ce qui était convenu, ce qui a été livré et les écarts à résoudre.",
"Supplier management follows a chain: selection, agreement, oversight, acceptance and payment. A paid invoice does not establish deliverable conformance. Predefined criteria distinguish what was agreed, delivered and still unresolved.",
"Le contrat prévoit une capacité de 500 requêtes par seconde. Le fournisseur livre un rapport à 200, puis la facture est payée. Retrouver les conditions d'acceptation et l'essai comparable avant d'accepter le livrable ; le paiement et une démonstration commerciale ne remplacent pas cette vérification.",
"The agreement specifies 500 requests per second. The supplier provides a report at 200 and the invoice is paid. Trace acceptance conditions and comparable testing before accepting the deliverable; payment and a sales demonstration do not replace that check."),
'TS':(
"Une solution technique traduit les exigences en choix de conception et réalisation. Construire, acheter ou réutiliser sont des options à évaluer dans leur contexte. Une comparaison utile intègre contraintes d'usage, coût sur la durée, interfaces et informations nécessaires à la mise en œuvre.",
"A technical solution translates requirements into design and implementation choices. Build, buy and reuse are options to evaluate in context. A useful comparison includes operating constraints, lifecycle cost, interfaces and information needed for implementation.",
"Construire coûte 20 au départ et 12 par an ; acheter coûte 35 puis 4 par an. Sur trois ans, les totaux simplifiés sont 56 et 47. Examiner aussi migration, intégration et contraintes avant de choisir : l'absence de licence ne garantit pas le coût total le plus faible.",
"Building costs 20 upfront and 12 annually; buying costs 35 then 4 annually. Simplified three-year totals are 56 and 47. Also examine migration, integration and constraints: no license fee does not guarantee lowest total cost."),
'VV':(
"La vérification demande si la solution respecte ses exigences ; la validation demande si elle répond à l'usage prévu dans son environnement cible. Un même essai peut fournir des éléments utiles aux deux questions, mais réussir l'une n'implique pas automatiquement réussir l'autre.",
"Verification asks whether a solution meets its requirements; validation asks whether it serves intended use in its target environment. One test can provide evidence for both questions, but success on one does not automatically establish the other.",
"L'écran respecte le contraste chiffré de la spécification en laboratoire. Les utilisateurs portant des gants ne peuvent pas sélectionner les commandes dans l'atelier. La vérification du contraste ne valide pas cet usage. Revoir critères, utilisateurs représentatifs et environnement, puis analyser et communiquer les résultats.",
"A screen meets its specified laboratory contrast value. Users wearing gloves cannot select controls in the workshop. Contrast verification does not validate that use. Revisit criteria, representative users and environment, then analyze and communicate results."),
'WE':(
"Donner une responsabilité sans autorité, compétence ou moyens peut produire une autonomie seulement déclarée. L'empowerment relie objectifs métier, compétences et capacité de décision des individus et groupes. Les résultats aident à examiner les obstacles ; une charte signée ne montre pas à elle seule que l'équipe peut agir.",
"Responsibility without authority, skills or resources can produce autonomy in name only. Empowerment connects business objectives, competencies and decision capability of people and groups. Outcomes help reveal obstacles; a signed charter alone does not show that a team can act.",
"Une équipe est dite autonome sur la résolution des demandes, mais tout geste exige l'approbation d'un directeur absent. Les erreurs augmentent sous la pression des délais. Examiner droits de décision, compétences, charge et retours avant de conclure à un manque de motivation.",
"A team is declared autonomous in request resolution, but every action needs approval from an absent director. Errors rise under deadline pressure. Examine decision rights, skills, workload and feedback before concluding motivation is lacking.")}
# Load original case records without executing the prior migrations.
import ast
module=ast.parse((P/'scripts/upgrade_academy.py').read_text())
CASES=ast.literal_eval(next(n.value for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CASES' for t in n.targets)))
for ai,a in enumerate(D['areas']):
    notes=LESSONS[a['id']];case=CASES[a['id']]
    a['appliedLesson']={}
    for li,lang in enumerate(('fr','en')):
        a['appliedLesson'][lang]={'reasoning':notes[li], 'example':notes[li+2],
          'sourceScope':('Exemple fictif et méthode pédagogique originale ; le guide public définit le sujet, pas ces nombres ni ce format de preuve.' if lang=='fr' else 'Fictional example and original teaching method; the public guide defines the topic, not these numbers or this evidence format.')}
        # Level-specific reading instructions clarify what the public topic adds.
        for entry in a.get('publicGroupCourse',{}).get('entries',[]):
            v=entry[lang];n=entry['groupLevel']
            scenario=case[0 if n==1 else 1][li]
            # A different task at each level: intervention, corroboration, transfer,
            # validity of quantitative inference, organizational optimization.
            if n==1:
                prompt=('Quelle première décision traite le mécanisme décrit ?' if li==0 else 'Which initial decision addresses the mechanism described?')
                good=case[2][li]
            elif n==2:
                prompt=('Quel examen permet de trancher l’incertitude avant de confirmer la réponse ?' if li==0 else 'Which investigation resolves the uncertainty before confirming the response?')
                good=case[3][li]
            elif n==3:
                prompt=('Le pilote sert maintenant de référence à une autre équipe. Quelle suite évite une généralisation non étayée ?' if li==0 else 'Another team is now adopting this pilot as its reference. Which follow-up avoids unsupported generalization?')
                good=(f'Examiner les conditions de transfert et un cas de la nouvelle équipe ; {case[3][li][0].lower()+case[3][li][1:]}' if li==0 else f'Examine transfer conditions and a case from the new team; {case[3][li][0].lower()+case[3][li][1:]}')
            elif n==4:
                prompt=('D04 : les résultats défavorables passent de 12/120 à 6/40, avec un contexte modifié. Quelle conclusion quantitative est défendable ?' if li==0 else 'D04: adverse outcomes change from 12/120 to 6/40 while context changes. Which quantitative conclusion is defensible?')
                good=('Le taux passe de 10 % à 15 % ; examiner exposition, définition et contexte avant d’attribuer un effet à l’action.' if li==0 else 'The rate moves from 10% to 15%; examine exposure, definition and context before attributing an effect to the action.')
            else:
                prompt=('Deux solutions réduisent le problème local, mais l’une augmente les délais du processus suivant. Comment éclairer l’optimisation organisationnelle ?' if li==0 else 'Two solutions reduce the local issue, but one increases downstream delays. How should organizational optimization be informed?')
                good=('Comparer les effets prévus et observés sur les objectifs métier et les processus concernés, avec leurs hypothèses et incertitudes.' if li==0 else 'Compare predicted and observed effects on business objectives and affected processes, including assumptions and uncertainty.')
            wrong=[x[li] for x in case[4:7]]
            if n==4:
                wrong=[('Le nombre a baissé de moitié : l’action a donc amélioré la performance.' if li==0 else 'Counts halved, so the action improved performance.'),('Le taux a augmenté : l’action est donc nécessairement la cause de la dégradation.' if li==0 else 'The rate increased, so the action necessarily caused deterioration.'),('La définition est constante : les différences de contexte peuvent être ignorées.' if li==0 else 'The definition is unchanged, so contextual differences can be ignored.')]
            if n==5:
                wrong=[('Choisir la plus forte baisse locale et traiter le délai aval dans un autre projet.' if li==0 else 'Choose the largest local reduction and handle downstream delay in a separate project.'),('Déployer les deux solutions simultanément pour additionner leurs gains annoncés.' if li==0 else 'Deploy both together to add their advertised gains.'),('Conserver seulement le coût de mise en œuvre comme critère d’optimisation.' if li==0 else 'Use implementation cost alone as the optimization criterion.')]
            base=[good]+wrong;shift=(ai+n)%4;v['options']=base[shift:]+base[:shift];entry['answer']=(-shift)%4
            v['question']=f'C-{a["id"]}-PG{n} · '+scenario+'\n\n'+prompt
            v['workedExample']=notes[li+2]
            v['why']=(f'Le point public étudié est : {v["concept"]} La décision retenue traite la lacune du cas : {good} Les autres réponses ferment trop tôt, changent un indicateur ou imposent une décision sans résoudre la contradiction. Ce cas ne délivre aucun niveau officiel.' if li==0 else f'The public learning focus is: {v["concept"]} The selected decision addresses the case gap: {good} Alternatives close too early, change a proxy or commit without resolving the discrepancy. This case awards no official rating.')
            v.setdefault('sourceExplanation',v['explanation'])
            v['explanation']=notes[li]+' '+v['sourceExplanation']
# The exam reports expose exact original case scope rather than claiming
# statistical independence: several items can deliberately share a case file.
D['examContentPolicy']['caseReuseWithinForm']='Items within one form may share a dossier. Forms A/B have separate fictional situations; no shared case IDs or question stems with each other or training.'
D['contentRevision']='2026-10-15-r9';D['assessmentRevision']='r9-applied-public'
D['sourceRegister'][1]={'title':'CMMI Credentialing Guide for Practitioners','date':'2026-08-31','url':'https://cmmiinstitute.com/getattachment/8051d124-5dd9-44fd-9bf0-4842c6d58b16/CMMI-Credentialing-Guide-for-Practitioners.pdf','pages':'27, 30–31','verifiedOn':'2026-10-15','scope':'Public exam content weights, 120 questions, four hours; not a prediction of 2027 changes'}
D['sourceRegister'][2].update({'url':'https://cmmiinstitute.com/getattachment/dfa7876d-b91e-4fd6-84f6-b6283f099a13/POLICY-CMMI-Certification-Certified-CMMI-Practitioner-Policy.pdf','date':'2026-07-14','verifiedOn':'2026-10-15'})
(P/'data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
print('Added 31 original bilingual applied lessons; replaced 99 recognition checks with applied decisions.')
# Vary quantitative decisions: reduced counts can accompany better, worse or
# unchanged rates, and growing counts can accompany a lower rate.
import re
examples=[(12,120,6,40),(8,80,12,200),(6,100,9,150),(20,100,12,100),(18,90,8,80),(7,140,6,60),(15,150,12,300)]
for form in ('A','B'):
    for lang in ('fr','en'):
        qs=[q for q in D['mockExamForms'][form][lang] if q['reasoningSkill']=='rate-vs-count']
        for i,q in enumerate(qs):
            a,b,c,d=examples[(i+(3 if form=='B' else 0))%len(examples)]
            r1=100*a/b;r2=100*c/d
            fmt=lambda x:f'{x:g}'
            record=(f'D04 : {a} résultats défavorables sur {b} opérations avant, puis {c} sur {d} après. La définition est inchangée ; le contexte et la composition des opérations restent à examiner.' if lang=='fr' else f'D04 records {a} adverse outcomes in {b} operations before, then {c} in {d} afterwards. The definition is unchanged; operating context and case mix remain unexamined.')
            q['q']=re.sub(r'D04.*?(?= D02\s*:|\n\n)',lambda _:record,q['q'],flags=re.S)
            # A stems put D04 at the end; keep the question's final instruction.
            direction=('baisse' if r2<r1 else 'augmente' if r2>r1 else 'reste identique') if lang=='fr' else ('falls' if r2<r1 else 'rises' if r2>r1 else 'is unchanged')
            correct=(f'Le taux {direction} : {fmt(r1)} % puis {fmt(r2)} % ; ces observations seules ne démontrent pas un effet causal.' if lang=='fr' else f'The rate {direction}: {fmt(r1)}% then {fmt(r2)}%; these observations alone do not establish a causal effect.')
            options=[correct,
              (f'Le taux passe de {fmt(r2)} % à {fmt(r1)} % ; l’ordre des périodes est sans effet sur la conclusion.' if lang=='fr' else f'The rate changes from {fmt(r2)}% to {fmt(r1)}%; period order does not affect the conclusion.') if r1!=r2 else ('Le nombre a changé, donc le taux a nécessairement changé.' if lang=='fr' else 'Counts changed, so the rate necessarily changed.'),
              ('La comparaison des nombres suffit ; les volumes d’opérations ne modifient pas l’interprétation.' if lang=='fr' else 'Comparing counts is sufficient; operation volumes do not affect interpretation.'),
              ('Une définition inchangée permet d’attribuer tout changement à l’intervention seule.' if lang=='fr' else 'An unchanged definition attributes any change to the intervention alone.')]
            pos=q['answer'];q['options']=options[-pos:]+options[:-pos] if pos else options
            q['explanation']=(f'Calcul : {a}/{b} × 100 = {fmt(r1)} % ; {c}/{d} × 100 = {fmt(r2)} %. Le dénominateur représente l’exposition. Il faut ensuite examiner le contexte, les autres changements et les incertitudes avant d’attribuer une cause.' if lang=='fr' else f'Calculation: {a}/{b} × 100 = {fmt(r1)}%; {c}/{d} × 100 = {fmt(r2)}%. The denominator represents exposure. Context, other changes and uncertainty still need examination before causal attribution.')
(P/'data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
