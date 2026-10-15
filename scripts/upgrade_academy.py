#!/usr/bin/env python3
"""Original bilingual teaching cases. No licensed normative practice statements.

Public source mapping stays in data.json; cases, numbers and options below are fictional.
Run after expand_public_groups.py. Deterministic; also invalidates obsolete mastery keys.
"""
import json, hashlib, collections
from pathlib import Path
P=Path(__file__).resolve().parent.parent
D=json.loads((P/'data.json').read_text())

# Each record is an independently authored problem: competing explanations,
# an observation that separates them, and an operational intervention.
# Fields are French/English pairs; none are normative requirements.
CASES={
'CAR':[
('Trois incidents ont la même signature après déploiement. D01 attribue les erreurs à la vigilance. D02 retrouve un validateur contourné dans les trois exécutions. D03 montre que la formation a déjà été suivie.','Three post-release incidents share a signature. D01 blames inattention. D02 shows the same bypassed validator in all three executions. D03 shows that training was already completed.'),
('Le nombre de récidives baisse après une modification du pipeline, mais le volume de déploiements baisse aussi et deux autres contrôles changent simultanément.','Recurrence counts fall after a pipeline change, but deployment volume also falls and two other controls change at the same time.'),
('Reconstituer les exécutions et tester le rôle du validateur avant de choisir une action préventive.','Reconstruct the executions and test the validator hypothesis before selecting a preventive action.'),
('Comparer les journaux avec et sans contrôle, à exposition comparable, et rechercher des causes concurrentes.','Compare logs with and without the control at comparable exposure and investigate competing causes.'),
('Former à nouveau les trois auteurs avant de vérifier le mécanisme.','Retrain the three authors before checking the mechanism.'),
('Attribuer la cause au dernier changement car il précède les incidents.','Assign causation to the latest change because it preceded the incidents.'),
('Clore l’analyse puisque les tickets ont été corrigés individuellement.','Close the analysis because each incident ticket has been fixed.')],
'CM':[
('D01 approuve la baseline B17. D02 associe le paquet livré au commit B18. D03 confirme que le correctif urgent était autorisé, sans identifier le binaire finalement déployé.','D01 approves baseline B17. D02 links the delivered package to commit B18. D03 confirms authorization of an emergency fix without identifying the deployed binary.'),
('Le dépôt contient tous les commits, mais le manifeste de livraison et l’artefact client n’ont pas la même empreinte. La sauvegarde restaure le dépôt, pas l’environnement client.','The repository contains every commit, but the release manifest and customer artifact have different hashes. The backup restores the repository, not the customer environment.'),
('Identifier l’artefact réellement installé puis réconcilier autorisation, baseline et contenu livré.','Identify the installed artifact and reconcile authorization, baseline and delivered content.'),
('Recouper empreinte du binaire client, manifeste signé et approbation du changement correspondant.','Corroborate the customer binary hash, signed manifest and approval for the corresponding change.'),
('Ajouter un tag sur B18 pour faire correspondre la documentation a posteriori.','Tag B18 to make the documentation agree retrospectively.'),
('Restaurer B17 immédiatement sans examiner l’impact du retour arrière.','Restore B17 immediately without assessing rollback impact.'),
('Accepter l’historique Git comme preuve suffisante du contenu installé.','Accept Git history as sufficient proof of the installed content.')],
'CONT':[
('D01 fixe un objectif de reprise de 2 heures pour le support. D02 montre une restauration technique en 70 minutes. D03 indique que les agents restent sans accès client pendant 3 heures supplémentaires.','D01 sets a two-hour support recovery objective. D02 shows a technical restore in 70 minutes. D03 says agents still lack customer access for another three hours.'),
('Un exercice annoncé comme réussi restaure les serveurs, mais il exclut le fournisseur d’identité et les communications de crise dont dépend le service critique.','A reportedly successful exercise restores servers but excludes the identity provider and crisis communications on which the critical service depends.'),
('Évaluer la reprise du service complet, y compris accès et dépendances, puis traiter l’écart à l’objectif.','Assess recovery of the complete service, including access and dependencies, then address the objective gap.'),
('Demander la chronologie jusqu’à une transaction métier utilisable, avec dépendances et conditions d’exercice.','Request the timeline through a usable business transaction, including dependencies and exercise conditions.'),
('Valider la continuité sur les seules 70 minutes de restauration du serveur.','Accept continuity based solely on the 70-minute server restore.'),
('Allonger immédiatement l’objectif de reprise pour aligner le plan sur l’exercice.','Immediately extend the recovery objective to fit the exercise.'),
('Acheter un serveur de secours avant d’identifier la dépendance bloquante.','Buy a spare server before identifying the blocking dependency.')],
'DM':[
('D01 décrit une architecture commune des données clients. D02 donne deux propriétaires différents à la même donnée. D03 montre une suppression dans le CRM qui n’est pas propagée au lac de données.','D01 describes a common customer-data architecture. D02 assigns two different owners to the same data. D03 shows a CRM deletion that never reaches the data lake.'),
('Un catalogue est complet sur les tables centrales, mais il exclut les exports manuels. Une équipe utilise ces exports pour prendre des décisions et personne n’en contrôle la conservation.','A catalog covers central tables but excludes manual exports. A team uses those exports for decisions and nobody controls their retention.'),
('Clarifier responsabilités et cycle de vie, puis vérifier la propagation des règles entre systèmes.','Clarify ownership and lifecycle, then verify rule propagation across systems.'),
('Suivre une donnée du CRM aux copies, avec métadonnées, propriétaire, accès et événement de suppression.','Trace a data item from CRM through copies, with metadata, owner, access and deletion event.'),
('Nettoyer les doublons sans résoudre les responsabilités contradictoires.','Clean duplicates without resolving conflicting ownership.'),
('Remplacer le catalogue par un schéma technique plus détaillé.','Replace the catalog with a more detailed technical schema.'),
('Limiter le périmètre aux bases centrales pour rendre le catalogue complet.','Restrict scope to central databases so the catalog becomes complete.')],
'DQ':[
('D01 annonce 99 % de données valides. D02 calcule ce taux après exclusion des lignes rejetées. D03 révèle que ces lignes alimentent encore la facturation.','D01 reports 99% valid data. D02 computes that rate after excluding rejected rows. D03 shows those rows still feed billing.'),
('Une opération de nettoyage réduit les erreurs observées sur un extrait. La règle d’entrée n’a pas changé et le prochain import réintroduit les mêmes formats invalides.','Cleansing reduces observed errors in an extract. The entry rule is unchanged and the next import reintroduces the same invalid formats.'),
('Redéfinir le périmètre et les critères de qualité, mesurer les rejets métier et agir à la source.','Clarify quality scope and criteria, measure business-relevant rejects and address the source.'),
('Comparer l’entrée brute, les rejets et la sortie de facturation avec la même définition de validité.','Compare raw input, rejected rows and billing output using the same validity definition.'),
('Publier le taux de 99 % car il est exact sur les seules lignes retenues.','Publish 99% because it is accurate for retained rows alone.'),
('Répéter le nettoyage sans examiner les critères ni les entrées.','Repeat cleansing without examining criteria or input.'),
('Moyenner les pourcentages des deux systèmes sans examiner les volumes.','Average both systems’ percentages without examining their volumes.')],
'DAR':[
('D01 fixe une pondération coût 40, fiabilité 60. D02 classe X premier. D03 révèle que la fiabilité de X utilise une promesse commerciale alors que celle de Y utilise des mesures réelles.','D01 sets cost weight 40 and reliability 60. D02 ranks X first. D03 reveals that X reliability uses a sales promise whereas Y reliability uses measured results.'),
('Une matrice multicritère est signée après le choix du fournisseur. Une simulation change les poids et inverse le classement ; aucun décideur n’a documenté ce compromis.','A decision matrix is signed after supplier selection. A sensitivity test changes the weights and reverses the ranking; no decision maker documented this tradeoff.'),
('Rendre les données comparables et examiner la sensibilité du choix avant de confirmer la décision.','Make evidence comparable and examine ranking sensitivity before confirming the decision.'),
('Retrouver critères approuvés avant décision, méthode de notation et données comparables pour chaque option.','Retrieve pre-decision criteria, scoring method and comparable data for each alternative.'),
('Retenir X puisque sa note calculée est la plus haute.','Select X because its calculated score is highest.'),
('Augmenter le poids de fiabilité jusqu’à confirmer le fournisseur préféré.','Raise the reliability weight until the preferred supplier wins.'),
('Choisir Y parce que ses chiffres semblent plus prudents.','Choose Y because its numbers look more conservative.')],
'ESAF':[
('D01 accepte un danger résiduel si un arrêt de sécurité fonctionne. D02 teste cet arrêt à température ambiante. D03 situe l’usage réel en chambre froide, où le capteur n’a pas été évalué.','D01 accepts residual hazard if a safety stop works. D02 tests the stop at room temperature. D03 places actual use in cold storage, where the sensor has not been evaluated.'),
('La formation à la sécurité est attestée, mais un changement de cadence modifie l’exposition au danger. L’analyse et les essais couvrent encore l’ancienne cadence.','Safety training is documented, but a production-rate change alters hazard exposure. Analysis and tests still cover the previous rate.'),
('Réexaminer le danger et l’efficacité du contrôle dans les conditions d’utilisation prévues avant acceptation.','Reassess the hazard and control effectiveness in intended operating conditions before acceptance.'),
('Relier conditions réelles, analyse de danger, critères de tolérance et essais du contrôle de sécurité.','Link actual conditions, hazard analysis, tolerance criteria and safety-control tests.'),
('Accepter le risque car le composant possède un certificat fournisseur.','Accept the risk because the component has a supplier certificate.'),
('Conserver l’acceptation car aucun accident n’a encore été observé.','Keep the acceptance because no accident has occurred yet.'),
('Ajouter une signature de formation sans réévaluer le contrôle.','Add a training signature without reassessing the control.')],
'ESEC':[
('D01 exige un accès administrateur nominatif. D02 montre une authentification forte. D03 relève un compte partagé de secours utilisé chaque nuit sans attribution.','D01 calls for named administrator access. D02 shows strong authentication. D03 identifies a shared emergency account used nightly without attribution.'),
('Une architecture de sécurité couvre l’application, mais le service d’assistance peut réinitialiser les accès sans contrôle d’identité comparable. La revue ne teste que la connexion principale.','A security architecture covers the application, but support can reset access without comparable identity checks. The review tests only the primary login.'),
('Traiter le chemin de contournement dans l’approche de sécurité et vérifier son utilisation réelle.','Address the bypass path within the security approach and verify actual use.'),
('Croiser les événements de connexion, les réinitialisations et les autorisations sur les chemins alternatifs.','Correlate login events, resets and authorizations across alternative paths.'),
('Déclarer la sécurité maîtrisée puisque l’accès principal utilise la MFA.','Declare security controlled because the primary login uses MFA.'),
('Désactiver tous les accès de secours sans étudier la continuité.','Disable all emergency access without considering continuity.'),
('Mettre à jour la politique sans vérifier les comptes existants.','Update the policy without checking existing accounts.')],
'EVW':[
('D01 impose une réponse en deux heures. D02 trace les décisions à Paris. D03 montre que Bangalore reçoit les demandes après sa journée et ne dispose d’aucun délégataire.','D01 sets a two-hour response expectation. D02 logs decisions in Paris. D03 shows Bangalore receives requests after its working day with no delegate.'),
('L’équipe distante dispose des outils et des accès. Les blocages persistent car les décisions sont prises en réunion locale et les comptes rendus arrivent après la fenêtre de validation.','The remote team has tools and access. Blockages persist because decisions happen in local meetings and notes arrive after the approval window.'),
('Adapter fenêtres de décision, délégations et traces asynchrones aux contraintes réelles des sites.','Adapt decision windows, delegation and asynchronous records to actual site constraints.'),
('Reconstituer une demande entre fuseaux, avec heures locales, décision, relais et accès à la trace.','Trace a request across time zones, including local times, decision, handover and access to the record.'),
('Installer un nouvel outil de visioconférence pour réduire les délais.','Install a new video-conferencing tool to reduce delay.'),
('Imposer une présence permanente au site distant pour respecter les deux heures.','Require permanent attendance at the remote site to meet the two-hour target.'),
('Mesurer uniquement le nombre de messages échangés entre les sites.','Measure only the number of messages exchanged between sites.')],
'EST':[
('D01 estime une refonte à 40 jours à partir de cinq écrans. D02 révèle deux interfaces non incluses. D03 utilise l’historique d’un projet sans migration alors que celle-ci est nécessaire ici.','D01 estimates a redesign at 40 days from five screens. D02 reveals two excluded interfaces. D03 uses history from a project without migration although migration is needed here.'),
('Le devis respecte la date imposée, mais confond effort et durée. Trois spécialistes sont supposés disponibles à temps plein alors qu’ils sont engagés à mi-temps sur un autre projet.','The quote meets the imposed date but confuses effort and duration. Three specialists are assumed full-time although half their capacity is committed elsewhere.'),
('Réestimer le périmètre et les hypothèses avec un historique comparable et une incertitude explicite.','Re-estimate scope and assumptions using comparable history and explicit uncertainty.'),
('Rechercher la décomposition, les interfaces, l’historique normalisé et les hypothèses d’effort et disponibilité.','Request decomposition, interfaces, normalized history and effort/availability assumptions.'),
('Ajouter une marge de 10 % sans revoir le périmètre ni les hypothèses.','Add a 10% buffer without revisiting scope or assumptions.'),
('Diviser l’effort par trois pour obtenir directement la durée.','Divide effort by three to obtain elapsed duration directly.'),
('Conserver le chiffre initial afin de ne pas modifier l’engagement commercial.','Keep the initial number to avoid changing the sales commitment.')],
'GOV':[
('D01 fixe un objectif de baisse des retards. D02 attribue un responsable. D03 montre que le comité refuse les deux arbitrages de capacité nécessaires sans changer l’objectif.','D01 sets a delay-reduction objective. D02 assigns an owner. D03 shows the committee denies both required capacity decisions without changing the objective.'),
('La direction reçoit un tableau vert. Le budget d’amélioration a été retiré et les risques de non-atteinte sont exclus de l’ordre du jour, malgré une demande du responsable.','Leadership receives a green dashboard. Improvement funding was withdrawn and objective risks are excluded from the agenda despite the owner’s request.'),
('Faire arbitrer explicitement objectifs, moyens et risques, puis suivre l’effet de la décision.','Obtain an explicit tradeoff among objectives, resources and risks, then track its effect.'),
('Relier comptes rendus d’arbitrage, ressources réellement allouées et évolution de la performance visée.','Link decision minutes, actually allocated resources and movement in target performance.'),
('Créer un nouvel indicateur sans porter la contradiction au comité.','Create another indicator without escalating the contradiction.'),
('Remplacer le responsable avant de vérifier les ressources disponibles.','Replace the owner before checking available resources.'),
('Diffuser à nouveau l’objectif en supposant que la communication suffit.','Communicate the objective again assuming communication is sufficient.')],
'II':[
('D01 publie une méthode commune. D02 forme les équipes. D03 montre qu’un outil indispensable n’est accessible qu’aux chefs de projet ; les opérateurs créent une procédure parallèle.','D01 publishes a common method. D02 trains teams. D03 shows a necessary tool is accessible only to project leads; operators create a parallel process.'),
('Les équipes connaissent le processus mais l’adaptation aux projets courts n’est pas disponible. Les contrôles suivent les signatures de lecture et ignorent l’usage réel.','Teams know the process but tailoring for short projects is unavailable. Monitoring tracks reading signatures and ignores actual use.'),
('Lever l’obstacle d’accès et vérifier l’appropriation du processus dans le travail réel.','Remove the access barrier and verify adoption in actual work.'),
('Observer un opérateur réaliser la tâche avec les ressources, compétences et adaptations disponibles.','Observe an operator perform the task with available resources, skills and tailoring.'),
('Faire signer de nouveau le manuel pour prouver son déploiement.','Have staff sign the manual again to prove deployment.'),
('Sanctionner la procédure parallèle avant d’étudier l’obstacle opérationnel.','Penalize the parallel process before investigating the operational barrier.'),
('Acheter une formation supplémentaire sans tester les accès.','Purchase more training without testing access.')],
'IRP':[
('D01 clôt un incident dès redémarrage de l’API. D02 montre la récidive trois nuits de suite. D03 indique que les clients ne reçoivent aucun statut pendant le redémarrage.','D01 closes an incident when the API restarts. D02 shows recurrence on three consecutive nights. D03 says customers receive no status during restart.'),
('Le délai moyen de clôture baisse parce que les incidents sont transférés vers une file de problèmes. Le service reste perturbé et les clients ouvrent de nouveaux tickets.','Mean closure time falls because incidents move to a problem queue. The service remains disrupted and customers open new tickets.'),
('Distinguer rétablissement, communication et prévention de récidive, puis vérifier chaque résultat.','Separate restoration, communication and recurrence prevention, and verify each outcome.'),
('Relier chronologie du service, échanges clients, tickets rouverts et analyse des incidents récurrents.','Link service timeline, customer communication, reopened tickets and recurring-incident analysis.'),
('Clore à chaque redémarrage car le traitement technique a été effectué.','Close after each restart because a technical treatment was performed.'),
('Optimiser le nombre de tickets fermés sans vérifier le service rendu.','Optimize closed-ticket counts without checking delivered service.'),
('Fusionner toutes les récidives en un ticket pour améliorer le taux.','Merge all recurrences into one ticket to improve the rate.')],
'MPM':[
('D01 compare le délai moyen de deux sites. D02 inclut les jours d’attente à Lyon. D03 les exclut à Lille ; le comité classe pourtant Lille comme référence de performance.','D01 compares average lead time at two sites. D02 includes waiting days in Lyon. D03 excludes them in Lille, yet the committee treats Lille as the performance reference.'),
('Une courbe montre une baisse après amélioration. Le mode de calcul, le mix des demandes et la date d’extraction ont changé en même temps ; les séries sont fusionnées.','A chart falls after an improvement. Calculation, request mix and extraction date changed simultaneously; the series were merged.'),
('Stabiliser les définitions et la qualité des données avant de comparer ou d’attribuer un effet.','Stabilize definitions and data quality before comparing performance or attributing an effect.'),
('Retracer définitions opérationnelles, populations, dates et données brutes de chaque série.','Trace operational definitions, populations, dates and raw data for each series.'),
('Choisir le site avec la moyenne la plus faible comme standard commun.','Choose the site with the lowest mean as the common standard.'),
('Fixer des limites statistiques sur la série fusionnée sans vérifier sa comparabilité.','Set statistical limits on the merged series without checking comparability.'),
('Conclure à une causalité parce que la courbe baisse après la décision.','Infer causation because the chart falls after the decision.')],
'MST':[
('D01 classe les vulnérabilités par score technique. D02 place une faille d’un serveur isolé en tête. D03 révèle une faille moins notée sur une passerelle exposée avec accès aux paiements.','D01 ranks vulnerabilities by technical score. D02 prioritizes an isolated server. D03 reveals a lower-scored flaw on an exposed gateway with payment access.'),
('Le bulletin de sécurité est distribué et le correctif installé sur les serveurs inventoriés. Une passerelle récemment ajoutée est absente de l’inventaire et reste exposée.','The security bulletin is distributed and inventoried servers are patched. A newly added gateway is missing from inventory and remains exposed.'),
('Réévaluer la priorité selon exposition et impact métier puis vérifier la couverture du traitement.','Reassess priority using exposure and business impact, then verify treatment coverage.'),
('Recouper inventaire réel, exposition, exploitabilité, impact et preuve de remédiation.','Correlate actual inventory, exposure, exploitability, impact and remediation evidence.'),
('Traiter uniquement le score technique le plus élevé sans contexte.','Treat only the highest technical score without context.'),
('Clore le risque quand le bulletin a été transmis à tous.','Close the risk once the bulletin has been forwarded to everyone.'),
('Déclarer le parc protégé sur la base des seuls serveurs connus.','Declare the estate protected based only on known servers.')],
'MC':[
('D01 affiche 60 % du budget consommé et 80 % des tâches closes. D02 montre que ces tâches représentent seulement 35 % de l’effort prévu. D03 reporte une dépendance critique.','D01 shows 60% budget spent and 80% of tasks closed. D02 shows those tasks represent only 35% of planned effort. D03 postpones a critical dependency.'),
('Le statut reste vert car la date finale n’a pas changé. Une action corrective est décidée mais son responsable n’a aucune capacité et aucun effet n’est suivi.','Status stays green because the final date is unchanged. A corrective action is agreed but its owner has no capacity and no effect is tracked.'),
('Analyser l’avancement pondéré et la dépendance, décider une correction réalisable et suivre son effet.','Analyze weighted progress and the dependency, agree a feasible correction and track its effect.'),
('Comparer réalisations, effort restant, engagements critiques et suivi de l’action corrective.','Compare actual progress, remaining effort, critical commitments and corrective-action follow-up.'),
('Garder le vert puisque 80 % des tâches sont terminées.','Keep green status because 80% of tasks are closed.'),
('Changer la date du plan pour supprimer l’écart sans revoir les engagements.','Change the planned date to erase the variance without revisiting commitments.'),
('Ouvrir davantage de petites tâches pour améliorer le pourcentage terminé.','Create more small tasks to improve the completion percentage.')],
'OT':[
('D01 atteste 100 % de présence à une formation. D02 montre que seuls 4 agents sur 10 réussissent la tâche cible. D03 signale que le cours utilisait une ancienne version de l’outil.','D01 records 100% training attendance. D02 shows only four of ten agents perform the target task. D03 says the course used an old tool version.'),
('La satisfaction de formation est élevée, mais les nouveaux arrivants n’ont pas pratiqué le scénario d’incident utilisé sur le terrain. Leur superviseur effectue les tâches à leur place.','Training satisfaction is high, but new hires never practiced the incident scenario used in the field. Their supervisor performs the tasks for them.'),
('Réexaminer les besoins et le transfert en situation, puis adapter et réévaluer la formation.','Revisit needs and on-the-job transfer, then adapt and reassess training.'),
('Observer une tâche représentative après formation et comparer aux compétences attendues pour le rôle.','Observe a representative post-training task against skills expected for the role.'),
('Valider la compétence puisque tous ont signé la feuille de présence.','Confirm competence because everyone signed the attendance sheet.'),
('Répéter le même cours sans vérifier l’écart entre version enseignée et utilisée.','Repeat the same course without checking taught versus deployed versions.'),
('Utiliser la satisfaction comme seule mesure d’efficacité de la formation.','Use satisfaction as the only training-effectiveness measure.')],
'PR':[
('D01 enregistre une revue avant livraison. D02 liste six défauts majeurs. D03 montre une approbation alors que quatre défauts restent sans décision ni vérification de correction.','D01 records a pre-release peer review. D02 lists six major defects. D03 shows approval while four defects lack a disposition or correction check.'),
('Le nombre de revues augmente, mais elles portent sur des documents préliminaires. Les interfaces modifiées après revue génèrent les défauts de recette et ne sont pas revues.','Review counts increase, but reviews cover preliminary documents. Interfaces changed after review cause acceptance defects and are not reviewed.'),
('Relier les défauts à leur traitement et contrôler la couverture de la version effectivement livrée.','Link defects to their disposition and check review coverage of the actual delivered version.'),
('Demander version examinée, critères, liste des défauts, décisions et vérifications de correction.','Request reviewed version, criteria, defects, dispositions and correction checks.'),
('Approuver car une réunion de revue a eu lieu avant la livraison.','Approve because a review meeting occurred before delivery.'),
('Mesurer l’efficacité par le nombre de participants et de réunions.','Measure effectiveness by participant and meeting counts.'),
('Exiger zéro défaut dans les comptes rendus pour accélérer l’approbation.','Require zero recorded defects to accelerate approval.')],
'PLAN':[
('D01 affecte deux spécialistes à plein temps. D02 leur attribue simultanément un autre projet. D03 confirme les dates sans accord des responsables de ressources.','D01 assigns two specialists full-time. D02 assigns them to another project simultaneously. D03 confirms dates without resource-owner agreement.'),
('Le planning contient toutes les tâches, mais une validation fournisseur est placée après l’intégration qui en dépend. La réserve de capacité ne couvre que les développeurs internes.','The schedule lists every task but places supplier approval after the integration that depends on it. Capacity reserve covers only internal developers.'),
('Réconcilier capacité, dépendances et engagements avant de confirmer un planning exécutable.','Reconcile capacity, dependencies and commitments before confirming an executable plan.'),
('Recouper affectations réelles, dépendances et accords des parties qui fournissent les ressources.','Corroborate actual allocations, dependencies and agreements from resource-providing parties.'),
('Figer le Gantt car toutes les activités y sont présentes.','Freeze the Gantt chart because every activity appears in it.'),
('Réduire uniformément les durées pour conserver la date cible.','Reduce all durations uniformly to preserve the target date.'),
('Ajouter une marge globale sans résoudre la dépendance impossible.','Add a global buffer without resolving the impossible dependency.')],
'PAD':[
('D01 présente une bibliothèque versionnée. D02 montre que trois équipes téléchargent des copies différentes. D03 indique que les retours de terrain ne sont rattachés à aucun propriétaire de modèle.','D01 shows a versioned library. D02 shows three teams downloading different copies. D03 says field feedback has no assigned template owner.'),
('La bibliothèque est à jour sur le serveur central, mais les liens des nouveaux projets pointent vers une archive. Le nombre d’actifs augmente sans mesure d’utilité.','The central library is current, but new-project links point to an archive. Asset counts grow without any check of usefulness.'),
('Rendre les actifs de référence accessibles et maintenus, puis vérifier leur usage et traiter les retours.','Make reference assets accessible and maintained, then check use and handle feedback.'),
('Suivre un nouvel utilisateur vers l’actif courant et retrouver la décision sur son retour d’expérience.','Trace a new user to the current asset and retrieve the disposition of their feedback.'),
('Ajouter des modèles pour augmenter la richesse de la bibliothèque.','Add templates to increase library richness.'),
('Conserver toutes les copies sans règle de référence pour favoriser l’autonomie.','Keep every copy without a reference rule to encourage autonomy.'),
('Déclarer l’adoption sur le seul nombre de téléchargements.','Declare adoption based only on download counts.')],
'PCM':[
('D01 choisit une amélioration pour réduire les reprises. D02 déploie la nouvelle procédure partout. D03 ne mesure que le nombre de personnes informées, pas les reprises.','D01 selects an improvement to reduce rework. D02 deploys the new process everywhere. D03 measures only people notified, not rework.'),
('Un pilote réduit les délais dans une équipe experte, mais les autres équipes ont des contraintes différentes. Le comité généralise sans analyser ces conditions de réussite.','A pilot reduces delays in an expert team, but other teams have different constraints. The committee scales it without analyzing success conditions.'),
('Relier l’amélioration à l’objectif métier, évaluer son effet et préparer un déploiement adapté.','Link improvement to the business objective, evaluate its effect and plan suitable rollout.'),
('Comparer résultats du pilote, conditions d’application, coûts et mesure de l’objectif avant généralisation.','Compare pilot outcomes, conditions, costs and objective measures before scaling.'),
('Conclure au succès parce que la procédure a été diffusée partout.','Conclude success because the procedure was distributed everywhere.'),
('Revenir à l’ancien processus sans examiner les résultats du pilote.','Return to the old process without examining pilot results.'),
('Étendre le pilote à l’identique en supposant toutes les équipes comparables.','Scale the pilot unchanged assuming all teams are comparable.')],
'PQA':[
('D01 approuve le plan qualité. D02 trouve un écart sur une livraison. D03 indique que le responsable évalué clôt lui-même l’écart sans preuve de correction ni contrôle indépendant.','D01 approves the quality plan. D02 finds a release deviation. D03 shows the assessed owner closing it without correction evidence or an independent check.'),
('Le tableau qualité affiche zéro écart ouvert. Les tickets ont été fermés après changement de libellé, mais les échantillons opérationnels montrent toujours le comportement non conforme.','The quality dashboard shows zero open deviations. Tickets were closed after relabeling, but operational samples still show the nonconforming behavior.'),
('Vérifier objectivement l’application et la correction de l’écart puis porter les problèmes non résolus au bon niveau.','Objectively check implementation and correction, then escalate unresolved issues appropriately.'),
('Relier constat, critère examiné, communication, correction observée et décision objective de clôture.','Link finding, evaluated criterion, communication, observed correction and objective closure decision.'),
('Accepter la clôture parce que le responsable du processus l’a signée.','Accept closure because the process owner signed it.'),
('Réécrire le libellé de l’écart pour rendre le tableau conforme.','Relabel the deviation to make the dashboard compliant.'),
('Réaliser un contrôle documentaire supplémentaire sans examiner la pratique réelle.','Perform another document review without examining actual work.')],
'PI':[
('D01 valide les composants séparément. D02 révèle deux schémas d’interface incompatibles. D03 assemble une version différente de celle livrée au client.','D01 passes components separately. D02 reveals two incompatible interface schemas. D03 assembles a version different from the customer delivery.'),
('L’intégration réussit sur un environnement de test simplifié. La configuration cible utilise une autre version de protocole et la séquence d’assemblage dépend d’un fournisseur absent du test.','Integration passes in a simplified environment. The target uses a different protocol version and the assembly sequence depends on a supplier absent from the test.'),
('Réconcilier interfaces, versions et environnement puis vérifier l’assemblage de la solution cible.','Reconcile interfaces, versions and environment, then verify assembly of the target solution.'),
('Retrouver contrats d’interface, séquence d’assemblage, configuration cible et résultats d’intégration correspondants.','Retrieve interface contracts, assembly sequence, target configuration and corresponding integration results.'),
('Accepter l’intégration puisque chaque composant passe ses tests unitaires.','Accept integration because each component passes unit tests.'),
('Figer le protocole le plus récent sans consulter les contraintes des composants.','Freeze the newest protocol without consulting component constraints.'),
('Livrer l’assemblage de test en supposant les configurations équivalentes.','Deliver the test assembly assuming configurations are equivalent.')],
'RDM':[
('D01 approuve une modification d’exigence. D02 actualise la conception. D03 montre des tests liés à l’ancienne version et une attente client non arbitrée.','D01 approves a requirement change. D02 updates design. D03 shows tests linked to the old version and an unresolved customer expectation.'),
('La matrice relie chaque exigence à un test, mais plusieurs tests ont été retirés. Une nouvelle exigence d’interface n’est reliée à aucun composant et le plan reste inchangé.','The matrix links each requirement to a test, but several tests were retired. A new interface requirement links to no component and the plan is unchanged.'),
('Analyser l’impact et réconcilier exigences, engagements, conception et tests dans les deux sens.','Analyze impact and reconcile requirements, commitments, design and tests bidirectionally.'),
('Suivre une exigence modifiée jusqu’au composant et au test actif, puis remonter d’un test à son besoin.','Trace a changed requirement to its component and active test, then trace a test back to its need.'),
('Accepter la traçabilité parce que chaque ligne de matrice contient un identifiant.','Accept traceability because every matrix row contains an identifier.'),
('Modifier les tests seulement après livraison pour préserver le planning.','Change tests only after release to preserve the schedule.'),
('Considérer la signature client comme preuve suffisante de cohérence des livrables.','Treat customer signature as sufficient proof of work-product consistency.')],
'RSK':[
('D01 classe le risque fournisseur faible. D02 constate la disparition de l’unique remplaçant. D03 garde la même probabilité et une réponse sans responsable disponible.','D01 rates supplier risk low. D02 records the loss of the only replacement. D03 keeps the probability unchanged and a response with no available owner.'),
('Le registre est à jour en date, mais les déclencheurs ne sont pas suivis. Une opportunité d’automatisation est rejetée sans comparaison du gain et de son risque d’intégration.','The register has a current date but triggers are not monitored. An automation opportunity is rejected without comparing benefit and integration risk.'),
('Réévaluer exposition et déclencheurs, attribuer une réponse réalisable et en suivre l’effet.','Reassess exposure and triggers, assign a feasible response and track its effect.'),
('Relier hypothèses de probabilité et d’impact, événements récents, déclencheur et capacité du responsable.','Link likelihood/impact assumptions, recent events, trigger and owner capacity.'),
('Conserver le score car la dernière revue est signée cette semaine.','Keep the score because the latest review was signed this week.'),
('Ajouter tous les événements possibles sans les prioriser.','Add every possible event without prioritizing them.'),
('Choisir la réponse au coût le plus faible sans examiner le risque résiduel.','Choose the cheapest response without examining residual risk.')],
'SDM':[
('D01 promet une réponse sous quatre heures ouvrées. D02 mesure le délai jusqu’à l’accusé automatique. D03 montre que le client attend deux jours avant une prise en charge utile.','D01 promises a response within four business hours. D02 measures time to automatic acknowledgment. D03 shows the customer waits two days for useful handling.'),
('Le taux de respect SLA est élevé, mais les demandes réouvertes sont comptées comme nouvelles et leur attente initiale disparaît. La capacité de l’équipe n’est pas ajustée aux pics.','SLA attainment is high, but reopened requests count as new and their initial wait disappears. Team capacity is not adjusted for demand peaks.'),
('Réconcilier l’engagement de service avec la mesure et adapter l’organisation de livraison aux écarts.','Reconcile service commitment with measurement and adapt delivery to the gaps.'),
('Retracer la demande client, les heures ouvrées, les réouvertures et le résultat de service accepté.','Trace the customer request, business-hour clock, reopenings and accepted service result.'),
('Valider le SLA puisque l’accusé automatique est envoyé immédiatement.','Accept SLA attainment because automatic acknowledgment is immediate.'),
('Exclure les demandes réouvertes pour ne compter que le travail nouveau.','Exclude reopened requests to count only new work.'),
('Ajouter du personnel avant d’étudier la définition et la distribution des délais.','Add staff before examining delay definitions and distribution.')],
'STSM':[
('D01 propose un nouveau service premium. D02 prévoit une forte demande à partir des clients existants. D03 ne teste ni disposition à payer ni capacité de support spécialisée.','D01 proposes a premium service. D02 predicts demand from existing customers. D03 tests neither willingness to pay nor specialist support capacity.'),
('Le portefeuille conserve un service peu demandé parce qu’il a été rentable l’an dernier. De nouveaux besoins sont observés, mais aucune revue ne relie marché, offre et moyens.','The portfolio retains a low-demand service because it was profitable last year. New needs are observed but no review connects market, offering and capability.'),
('Évaluer besoins, valeur et capacité de l’offre avant de décider son évolution dans le portefeuille.','Evaluate needs, value and offering capability before deciding portfolio evolution.'),
('Comparer besoins de segments, usage, disposition à payer, coûts et capacités nécessaires à l’offre.','Compare segment needs, usage, willingness to pay, cost and capabilities needed for the offering.'),
('Lancer le premium car les clients actuels sont satisfaits du service standard.','Launch premium because current customers like the standard service.'),
('Conserver le portefeuille sur la base de la seule rentabilité passée.','Keep the portfolio based solely on past profitability.'),
('Transférer la décision au support sans revoir la stratégie de service.','Delegate the decision to support without reviewing service strategy.')],
'SAM':[
('D01 accepte un livrable fournisseur sur un test de démonstration. D02 contient un critère contractuel non testé. D03 facture une modification sans accord sur son prix ni son périmètre.','D01 accepts a supplier delivery after a demo. D02 contains an untested contractual criterion. D03 invoices a change with no agreement on price or scope.'),
('Le fournisseur livre à l’heure mais remplace un composant par un équivalent non évalué. Le tableau de performance ne suit que les dates, et l’acceptation ne vérifie pas l’interface modifiée.','The supplier delivers on time but substitutes an unevaluated component. Performance tracking covers only dates and acceptance never checks the changed interface.'),
('Réconcilier accord, modification et critères d’acceptation avant d’accepter et de suivre la livraison.','Reconcile agreement, change and acceptance criteria before accepting and tracking delivery.'),
('Recouper accord courant, approbations de changement, essais d’acceptation et performance du fournisseur.','Corroborate current agreement, change approvals, acceptance tests and supplier performance.'),
('Accepter car le fournisseur a respecté la date de livraison.','Accept because the supplier met the delivery date.'),
('Payer la modification puis négocier son périmètre à la revue suivante.','Pay for the change and negotiate scope at the next review.'),
('Refuser tous les livrables sans distinguer critères satisfaits et points ouverts.','Reject all deliverables without distinguishing satisfied criteria from open issues.')],
'TS':[
('D01 choisit une architecture pour sa performance. D02 mesure cette performance sur données en mémoire. D03 exige en production un stockage chiffré et une latence non testée.','D01 selects an architecture for performance. D02 measures it using in-memory data. D03 requires encrypted production storage and an untested latency target.'),
('L’équipe choisit de construire un composant pour éviter les frais de licence. Le calcul omet maintenance, intégration et migration ; une option de réutilisation n’a pas été comparée.','The team chooses to build a component to avoid license fees. The analysis omits maintenance, integration and migration; reuse was never compared.'),
('Comparer les solutions sur les contraintes et le coût de cycle de vie, puis vérifier le choix technique.','Compare solutions against constraints and lifecycle cost, then verify the technical selection.'),
('Demander alternatives, critères de conception, hypothèses de coût et essais dans les contraintes cibles.','Request alternatives, design criteria, cost assumptions and tests under target constraints.'),
('Choisir la solution la plus rapide dans le seul banc d’essai disponible.','Select the fastest solution in the only available benchmark.'),
('Construire car l’absence de licence implique un coût total inférieur.','Build because having no license fee implies lower total cost.'),
('Acheter systématiquement pour transférer tous les risques techniques au fournisseur.','Always buy to transfer all technical risks to the supplier.')],
'VV':[
('D01 montre tous les tests techniques réussis. D02 couvre les exigences spécifiées. D03 rapporte que les utilisateurs ne terminent pas la tâche dans leur environnement réel.','D01 shows passing technical tests. D02 covers specified requirements. D03 says users cannot complete their task in the actual environment.'),
('Un client approuve une démonstration métier. Les tests de conformité de l’interface n’ont pas été rejoués après modification et la démonstration utilise un simulateur de connexion.','A customer approves a business demo. Interface conformance tests were not rerun after a change and the demo uses a connection simulator.'),
('Distinguer conformité aux exigences et usage prévu, puis examiner la lacune dans son environnement.','Distinguish requirement conformance from intended use, then investigate the gap in its environment.'),
('Relier exigences, critères, configuration testée et scénarios d’usage dans l’environnement cible.','Link requirements, criteria, tested configuration and usage scenarios in the target environment.'),
('Accepter l’usage prévu parce que les tests techniques réussissent.','Accept intended use because technical tests pass.'),
('Utiliser la démonstration métier pour remplacer tous les tests de conformité.','Use the business demo to replace all conformance tests.'),
('Attribuer l’échec aux utilisateurs sans examiner les conditions d’usage.','Blame users without examining usage conditions.')],
'WE':[
('D01 affecte une mission à une équipe autonome. D02 lui confie la responsabilité du délai. D03 réserve toutes les décisions d’outillage à un comité mensuel qui bloque le travail.','D01 assigns a mission to an autonomous team. D02 makes it accountable for timing. D03 reserves every tooling decision to a monthly committee that blocks work.'),
('Le transfert d’un expert est réalisé sans relais de compétence. Les nouvelles responsabilités sont annoncées mais les mécanismes de coordination et de reconnaissance restent liés aux anciens rôles.','An expert transfers with no skill handover. New responsibilities are announced but coordination and recognition mechanisms remain tied to old roles.'),
('Aligner responsabilités, compétences, transitions et pouvoirs de décision sur la mission confiée.','Align responsibilities, skills, transitions and decision authority with the assigned mission.'),
('Retracer une affectation réelle, les compétences, le relais, les décisions autorisées et la coordination.','Trace an actual assignment, skills, handover, authorized decisions and coordination.'),
('Augmenter la responsabilité du délai sans modifier les droits de décision.','Increase schedule accountability without changing decision rights.'),
('Déclarer l’autonomie puisque l’organigramme emploie ce mot.','Declare autonomy because the organization chart uses that word.'),
('Supprimer toute coordination pour que chaque équipe puisse décider seule.','Remove all coordination so every team can decide alone.')]
}

def t(pair,lang): return pair[lang=='en']
def rotate(options,seed):
 n=seed%len(options);return options[n:]+options[:n],(-n)%len(options)

def exam_question(a,form,domain,index,lens,lang):
 c=CASES[a['id']];en=lang=='en';b=form=='B';intro=t(c[b],lang)
 # Independent forms use different evidence mechanisms and different datasets;
 # within a form, linked case questions explicitly share a dossier ID.
 caseid=f'{form}-{domain}-{a["id"]}'
 base=(f'Dossier {caseid} (fictional). ' if en else f'Dossier {caseid} (fictif). ')+intro
 action=t(c[2],lang);trace=t(c[3],lang);bad=[t(x,lang) for x in c[4:7]]
 before=(18,120) if b else (12,80);after=(9,45) if b else (8,40)
 numeric=(f' D04 counts {before[0]} adverse outcomes in {before[1]} comparable operations before the intervention, then {after[0]} in {after[1]} afterwards. The definition is unchanged; case mix has not been checked.' if en else f' D04 compte {before[0]} résultats indésirables sur {before[1]} opérations comparables avant intervention, puis {after[0]} sur {after[1]} après. La définition est inchangée ; le mix des cas n’a pas été vérifié.')
 prompts=[
 ('Quelle décision est la mieux étayée par D01–D03 ?', 'Which decision is best supported by D01–D03?'),
 ('Quelle investigation distinguerait le mieux un succès apparent d’une application effective ?', 'Which investigation best separates apparent success from actual implementation?'),
 ('Une seule action peut être engagée cette semaine. Laquelle réduit le mieux l’incertitude décisive ?', 'Only one action can start this week. Which best reduces the decisive uncertainty?'),
 ('Que peut-on conclure des données D04 avant toute attribution causale ?', 'What can be concluded from D04 before any causal attribution?'),
 ('Le responsable propose de clôturer sur le seul indicateur de volume. Quelle réponse conserve le bon objet de contrôle ?', 'The owner proposes closure using only a volume indicator. Which response preserves the right object of control?'),
 ('Un autre site déclare avoir réussi. Quelle condition rendrait sa preuve transférable au cas présent ?', 'Another site reports success. What condition would make its evidence transferable to this case?'),
 ('Un comité veut décider sur les seuls documents approuvés. Quelle vérification doit peser davantage dans ce dossier ?', 'A committee wants to decide using approved documents alone. Which check should carry more weight in this dossier?'),
 ('Après une action, le volume d’anomalies baisse. Quelle suite permet de distinguer correction, couverture et effet ?', 'After an action, adverse counts fall. Which next step separates correction, coverage and effect?'),
 ('Le prochain test est limité à un échantillon. Comment concevoir une vérification utile à la décision ?', 'The next test is limited to a sample. How should it be designed to support the decision?')]
 prompt=t(prompts[lens],lang)
 if lens==3:
  base+=numeric
  right=('The count falls, but the adverse rate rises from 15% to 20%; causation and case-mix effects remain unresolved.' if en else 'Le nombre baisse, mais le taux indésirable passe de 15 % à 20 % ; causalité et effet du mix restent à examiner.')
  options=[right,('The rate improves because the adverse count falls.' if en else 'Le taux s’améliore puisque le nombre d’événements baisse.'),('The rate is unchanged because both periods use the same definition.' if en else 'Le taux est inchangé car les deux périodes utilisent la même définition.'),('The action caused deterioration; the two rates establish causation.' if en else 'L’action a causé la dégradation ; les deux taux établissent la causalité.')]
  why=('D04 requires dividing events by exposure: 0.15 then 0.20, a five percentage-point increase. A count reduction is not a rate improvement. These observations alone do not isolate a causal effect.' if en else 'D04 impose de diviser les événements par l’exposition : 0,15 puis 0,20, soit +5 points. Une baisse de volume n’est pas une amélioration de taux. Ces observations n’isolent pas un effet causal.')
 elif lens in (1,6,8):
  right=trace;options=[right]+bad
  why=(f'The missing link is operational corroboration: {trace} The alternatives {"shift attention to a proxy or commit before resolving the discrepancy" if en else ""}.' if en else f'Le chaînon manquant est un recoupement opérationnel : {trace} Les alternatives privilégient un proxy, une décision prématurée ou une preuve qui ne répond pas à la contradiction.')
 elif lens==5:
  right=(f'Check comparable scope, version and operating conditions, then {trace[0].lower()+trace[1:]}' if en else f'Vérifier périmètre, version et conditions comparables, puis {trace[0].lower()+trace[1:]}')
  options=[right,('Use its aggregate success score without checking conditions.' if en else 'Reprendre son score global sans vérifier les conditions.'),('Require identical document names; content and use can differ.' if en else 'Exiger les mêmes noms de documents ; contenu et usage peuvent différer.'),('Replace local observations with the other site’s signed declaration.' if en else 'Remplacer les observations locales par la déclaration signée de l’autre site.')]
  why=('Transfer requires comparable mechanisms and operating conditions. A title, aggregate score or distant claim cannot resolve this local discrepancy.' if en else 'Le transfert suppose des mécanismes et conditions comparables. Un titre, un score agrégé ou une affirmation distante ne résout pas cette contradiction locale.')
 elif lens==7:
  base+=numeric;right=(f'Normalize outcomes and inspect coverage, then {trace[0].lower()+trace[1:]}' if en else f'Normaliser les résultats et examiner la couverture, puis {trace[0].lower()+trace[1:]}'); options=[right]+bad
  why=('Fewer events can reflect lower exposure. Check what changed, which population was covered and whether the operational mechanism works; separate that from causal attribution.' if en else 'Moins d’événements peut refléter moins d’exposition. Vérifier le changement, la population couverte et le mécanisme opérationnel ; distinguer cela de l’attribution causale.')
 else:
  right=action;options=[right]+bad
  why=(f'D01–D03 disagree about what actually worked. {action} {trace} The other actions either preserve an untested assumption, optimize a proxy, or commit without resolving the material gap.' if en else f'D01–D03 se contredisent sur ce qui fonctionne réellement. {action} {trace} Les autres actions conservent une hypothèse non vérifiée, optimisent un proxy ou engagent une décision avant de résoudre la lacune déterminante.')
 options,answer=rotate(options,index+(1 if b else 0))
 return {'id':f'MOCK-{form}-{domain}-{index:02d}-{lang}','form':form,'examDomain':domain,'area':a['id'],'kind':'evidence-analysis','difficulty':3,'q':base+'\n\n'+prompt,'options':options,'answer':answer,'explanation':why,'caseId':caseid,'reasoningSkill':['decision','corroboration','priority','rate-vs-count','proxy','transfer','traceability','causation','sampling'][lens],'source':a['source'],'sourcePage':a['page'],'provenance':'original-fictional-assessment'}

# Keep official content-area proportions, with 31 PA coverage in each form.
# Development and services retain the same PA allocation as the original forms.
for form in ('A','B'):
 template=D['mockExamForms'][form]['fr']
 for lang in ('fr','en'):
  seen=collections.Counter();new=[]
  for i,q in enumerate(template):
   a=next(a for a in D['areas'] if a['id']==q['area']);lens=seen[a['id']];seen[a['id']]+=1
   new.append(exam_question(a,form,q['examDomain'],i+1,lens,lang))
  D['mockExamForms'][form][lang]=new

# Teaching case C is distinct from both hold-out form families. Existing
# walkthroughs are rewritten to explain mechanisms rather than repeat PA names.
for ai,a in enumerate(D['areas']):
 c=CASES[a['id']]
 for lang in ('fr','en'):
  en=lang=='en';lab=a['caseLab'][lang]
  lab['context']=(f'Training dossier C-{a["id"]}. A pilot and a newly onboarded team use different operating arrangements. The scope contains both; determine what the evidence establishes before selecting a follow-up.' if en else f'Dossier d’apprentissage C-{a["id"]}. Un pilote et une équipe nouvellement intégrée travaillent selon des dispositions différentes. Le périmètre comprend les deux ; déterminer ce qui est établi avant de décider la suite.')
  lab['artifacts'][0]['body']=(f'D01 is the approved intent: {a["en"].get("goal",a["en"].get("summary",a["goal"]))}. Its publication date precedes onboarding of the second team; no tailoring decision for that team is attached.' if en else f'D01 décrit l’intention approuvée : {a["goal"]} Sa publication précède l’intégration de la seconde équipe ; aucune décision d’adaptation pour cette équipe n’est jointe.')
  lab['artifacts'][1]['body']=(f'D02 is a dated pilot sample: {a["en"].get("evidence","")}. Its author can demonstrate use on the pilot. Records for the second team have not been sampled.' if en else f'D02 est un échantillon daté du pilote : {a["deep"]["evidenceContrast"][0]} Son auteur peut montrer l’usage sur le pilote. Les traces de la seconde équipe n’ont pas encore été échantillonnées.')
  lab['artifacts'][2]['body']=(f'D03 records a missing link: {t(c[3],lang)} This check has not been performed on the second team. The manager says their work differs from the pilot; that explanation has not been tested.' if en else f'D03 identifie un chaînon à examiner : {t(c[3],lang)} Cette vérification n’a pas été réalisée sur la seconde équipe. Le responsable indique un travail différent du pilote ; cette explication n’est pas encore vérifiée.')
  lab['artifacts'][3]['body']=('D04: the pilot reports 6 adverse events in 60 operations. The new team reports 4 in 20. Their combined count is 10 in 80. No before/after series exists; an organization-wide causal improvement is not established.' if en else 'D04 : le pilote compte 6 événements indésirables sur 60 opérations. La nouvelle équipe en compte 4 sur 20. Le total est 10 sur 80. Aucune série avant/après n’est disponible ; une amélioration causale organisationnelle n’est pas établie.')
  lab['coach']=(f'D02 supports local use; D03 identifies a coverage and comparability question. D04 gives 10% and 20%, with a combined rate of 12.5%, not the unweighted mean of 15%. Investigate the difference with comparable definitions and scope. Domain follow-up: {t(c[3],lang)}' if en else f'D02 étaye un usage local ; D03 pose une question de couverture et de comparabilité. D04 donne 10 % et 20 %, avec un taux global de 12,5 %, et non la moyenne non pondérée de 15 %. Examiner la différence avec définitions et périmètre comparables. Suite propre au domaine : {t(c[3],lang)}')
  lab['interviews']=[{'role':('Pilot lead' if en else 'Responsable du pilote'),'quote':('I can reproduce the pilot record; I have not observed the new team.' if en else 'Je peux reproduire la trace du pilote ; je n’ai pas observé la nouvelle équipe.')},{'role':('New-team lead' if en else 'Responsable de la nouvelle équipe'),'quote':('We use a different workflow. Before concluding it is equivalent, examine an actual case with us.' if en else 'Notre flux de travail diffère. Avant de le juger équivalent, examinons ensemble un cas réel.')}]
  walkthrough=a['practiceWalkthrough'][lang]
  for i,w in enumerate(walkthrough):
   step=(a['en'] if en else a['deep'])['steps'][i]
   w['body']=(f'This step connects a decision to an observable mechanism: {step[1]} In training dossier C-{a["id"]}, distinguish the pilot’s demonstrated use from the new team’s untested equivalence. An approved intention does not settle whether the mechanism works.' if en else f'Cette étape relie une décision à un mécanisme observable : {step[1]} Dans le dossier C-{a["id"]}, distinguer l’usage démontré sur le pilote et l’équivalence non testée de la nouvelle équipe. L’intention approuvée ne résout pas la question du fonctionnement.')
   w['evidence']=t(c[3],lang)
  # Five reasoning questions using the training dossier, held out from mocks.
  sets=[
   (('What does the disagreement between the two leads establish?' if en else 'Que permet d’établir le désaccord entre les responsables ?'),[('The pilot is supported locally; equivalence and coverage on the new team need corroboration.' if en else 'Le pilote est étayé localement ; équivalence et couverture sur la nouvelle équipe restent à recouper.'),('The new team necessarily fails because it works differently.' if en else 'La nouvelle équipe est nécessairement en échec car elle travaille différemment.'),('The approved process proves both teams operate identically.' if en else 'Le processus approuvé prouve que les deux équipes fonctionnent à l’identique.'),('The two interviews cancel each other out, so D02 has no value.' if en else 'Les deux entretiens s’annulent, donc D02 n’a aucune valeur.')],lab['coach']),
   (('Which domain-specific check best resolves D03?' if en else 'Quelle vérification propre au domaine résout le mieux D03 ?'),[t(c[3],lang)]+[t(x,lang) for x in c[4:7]],('Check the mechanism at issue, not a signature, proxy or premature decision. ' if en else 'Vérifier le mécanisme en cause, sans le remplacer par une signature, un proxy ou une décision prématurée. ')+t(c[2],lang)),
   (('Using D04, what is the combined adverse-event rate?' if en else 'Avec D04, quel est le taux global d’événements indésirables ?'),[('12.5%, using 10 events divided by 80 operations.' if en else '12,5 %, soit 10 événements divisés par 80 opérations.'),('15%, the arithmetic mean of both team rates.' if en else '15 %, moyenne arithmétique des deux taux.'),('10%, because the pilot has more observations.' if en else '10 %, car le pilote a davantage d’observations.'),('20%, because the newer team determines organizational performance.' if en else '20 %, car la nouvelle équipe détermine la performance organisationnelle.')],('Combine counts and exposure: (6+4)/(60+20)=12.5%. Equal weighting of unequal populations gives a different, inappropriate aggregate.' if en else 'Combiner événements et exposition : (6+4)/(60+20)=12,5 %. Pondérer également des populations différentes donne un agrégat inadapté.')),
   (('Which next decision preserves the purpose of this PA?' if en else 'Quelle décision suivante préserve l’intention de cette PA ?'),[t(c[2],lang)]+[t(x,lang) for x in c[4:7]],('Resolve the material uncertainty and check its operational consequence. ' if en else 'Résoudre l’incertitude déterminante et en vérifier la conséquence opérationnelle. ')+t(c[3],lang)),
   (('Can D04 establish that rollout caused an improvement?' if en else 'D04 établit-il que le déploiement a causé une amélioration ?'),[('No: these are different teams without a comparable before/after series; investigate mix and operating differences.' if en else 'Non : ce sont deux équipes sans série avant/après comparable ; examiner mix et conditions de travail.'),('Yes: the combined rate is below the newer team rate.' if en else 'Oui : le taux global est inférieur à celui de la nouvelle équipe.'),('Yes: the pilot has fewer adverse events per operation.' if en else 'Oui : le pilote a moins d’événements par opération.'),('No inference of any kind is possible, including calculating the two rates.' if en else 'Aucune inférence n’est possible, même le calcul des deux taux.')],('The rates are descriptive evidence, not a causal design. Neither blanket success nor rejection of all observations follows. The difference should guide investigation.' if en else 'Les taux sont descriptifs, sans dispositif causal. Ni succès généralisé ni rejet de toute observation ne s’ensuit. La différence doit orienter l’enquête.'))]
  a['masteryQuestions'][lang]=[]
  for i,(q,opts,why) in enumerate(sets):
   options,answer=rotate(opts,ai+i)
   a['masteryQuestions'][lang].append({'id':f'{a["id"]}-R8-{i+1}','q':f'C-{a["id"]} · '+q,'options':options,'answer':answer,'why':why})
  # Mission now uses the same visible packet and a domain-specific decision.
  dest=a['en'] if en else a['deep']
  dest['question']=(f'C-{a["id"]}: which follow-up resolves the material gap in the records?' if en else f'C-{a["id"]} : quelle suite résout la lacune déterminante des pièces ?')
  choices,correct=rotate([t(c[2],lang)]+[t(x,lang) for x in c[4:7]],ai)
  dest['choices']=choices;dest['correct']=correct;dest['why']=t(c[3],lang)
  # PG cards teach the published summary and require transfer to a case rather
  # than picking between "check evidence" and "declare official maturity".
  for entry in a.get('publicGroupCourse',{}).get('entries',[]):
   v=entry[lang];n=entry['groupLevel']
   v['question']=(f'C-{a["id"]}, PG{n}: {v["concept"]} Which follow-up addresses the documented uncertainty without converting one sample into an organization-wide claim?' if en else f'C-{a["id"]}, PG{n} : {v["concept"]} Quelle suite traite l’incertitude documentée sans transformer un exemple en affirmation organisationnelle ?')
   opts=[t(c[3],lang)]+[t(x,lang) for x in c[4:7]]
   v['options'],entry['answer']=rotate(opts,ai+n)
   v['why']=(f'The public summary defines the learning focus, while C-{a["id"]} requires corroborating actual operation. {t(c[3],lang)} None of these checks alone establishes a formal PG or maturity rating.' if en else f'Le résumé public définit l’objet d’étude ; C-{a["id"]} exige de recouper le fonctionnement réel. {t(c[3],lang)} Aucun de ces contrôles ne délivre à lui seul un niveau PG ou de maturité officiel.')
   v['workedExample']=lab['artifacts'][2]['body']+' '+lab['artifacts'][3]['body']

D['contentRevision']='2026-10-15-r8'
D['assessmentRevision']='r8-evidence'
D['examContentPolicy']['reasoningScope']='Original case-based analysis exercises exceed the remember/understand emphasis described in the 2024 public adoption guide; no official exam equivalence or pass prediction.'
D['sourceRegister']=[{'title':'CMMI Model Quick Reference Guide v4.0','date':'2026-08-25','url':'https://www.isaca.org/resources/reference-guide/cmmi-model-quick-reference-guide','scope':'31 PA public summaries and six excerpted PQA practices; not the full licensed model'},{'title':'Adoption Guide for CMMI Credentials','date':'2024-09-13','pages':'25–26','scope':'Historical public content-area weights; 2027 rules must be rechecked'},{'title':'CMMI Practitioner Policy','url':'https://cmmiinstitute.com/getattachment/4c4e2b29-ac18-430e-bc24-683aec85d8b9/POLICY-CMMI-Certification-Certified-CMMI-Practitioner-Policy.pdf','scope':'120 questions, four hours; passing score not public'}]
(P/'data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
print('Upgraded 31 training case files, 310 bilingual mastery items, 99 PG checks and 480 bilingual hold-out exam items.')
