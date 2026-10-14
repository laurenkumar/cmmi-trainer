# CMMI Academy 2027

Application d'apprentissage interactive en français pour préparer les concepts CMMI v4.0 et le raisonnement d'une évaluation d'entreprise (*appraisal*).

## Fonctionnalités

- 39 leçons (8 fondations et 31 Practice Areas), avec cours détaillés, schémas cliquables, cas d'entreprise et ateliers interactifs.
- 269 questions d'entraînement originales et examens blancs chronométrés.
- Simulateur d'audit (20 dossiers), flashcards, grille de préparation et suivi des progrès enregistré localement.
- Interface responsive, sans compte, API ni serveur.

## Démarrage

Ouvrir `index.html` dans un navigateur, ou servir ce fichier avec un serveur statique. Pour un déploiement Vercel, sélectionner le preset **Other** et publier la racine du dépôt (aucune commande de build nécessaire).

## Sources du projet

- `index.html` : application complète autonome, version prête à publier.
- `app.css` : feuilles de style modifiables.
- `app.js` : logique interactive modifiable.
- `data.json` : contenu pédagogique et questions.
- `build.py` : reconstruit `index.html` à partir des trois fichiers ci-dessus.

Après modification des sources, exécuter : `python build.py`, puis committer aussi le nouvel `index.html`.

## Périmètre pédagogique

Le contenu a été conçu à partir du *CMMI Model Quick Reference Guide v4.0* (2026) et du *CMMI Adoption Guide for CMMI Credentials* (2024) fournis pour le projet. Le guide rapide n'est **pas** le modèle normatif complet et ne suffit pas, à lui seul, pour une évaluation officielle. Les scénarios, réponses et scores sont pédagogiques et ne sont pas des examens ni des appraisals officiels.

Projet indépendant ; CMMI® est une marque du CMMI Institute. Les progrès restent dans le stockage local du navigateur ; les fonctions d'export/import de l'application permettent de les transférer.
