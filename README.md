# Révisions

Site personnel de révision : cours rédigés, quiz auto-corrigés, TD corrigés, labo Python, protégé par un code PIN.

## Lancer en local

```bash
npm install
cp .env.example .env.local   # puis renseigner APP_PIN et SESSION_SECRET
npm run dev                  # http://localhost:3000
```

## Accès

- Le PIN est lu dans la variable d'environnement `APP_PIN` (jamais dans le code).
- Après le PIN, un jeton signé (HS256, `SESSION_SECRET`) est posé en cookie `HttpOnly` pour **1 heure** ; à l'expiration, le PIN est redemandé.
- Anti-bruteforce : 5 échecs → 15 min de blocage pour le client ; 30 échecs en 1 h (tous clients) → 1 h de blocage.
- Toutes les pages passent par `src/proxy.ts` **et** sont revérifiées côté serveur (`requireSession`). Le contenu des cours n'est jamais dans les fichiers JavaScript publics (vérifié par un test E2E).

## Ajouter un cours

1. Déclarer le cours dans `content/courses.yaml` (slug, matière, titre, description, tags, couleur).
2. Créer `content/<slug>/NN-nom.md` pour chaque partie, avec un frontmatter :
   ```yaml
   ---
   title: "Ch1 — Titre (entre guillemets s'il contient « : »)"
   summary: Une phrase.
   kind: chapter   # chapter | sheet | td | project | exam
   tags: [mot-clé]
   minutes: 45
   ---
   ```
3. Rédiger en Markdown avec maths `$…$` / `$$…$$` et les encadrés :
   `:::definition[Titre]`, `:::theorem`, `:::property`, `:::method`, `:::warning`, `:::key`, `:::note`,
   `:::example`, `:::intuition`, `:::pattern` (motif de preuve), `:::exercise[Titre]`, `:::exam[Titre]`,
   et les blocs repliés `:::hint[Indice 1]`, `:::correction`, `:::solution`, `:::skeleton`.
4. Quiz auto-corrigés dans `NN-nom.items.yaml` (types `qcm`, `truefalse`, `numeric`), insérés avec `::item{id="…"}`.
   Chaque réponse calculable reçoit un champ `verify` (table de vérité, identité ensembliste, dénombrement,
   expression Python…) recalculé par `npm run verify:py`.

Le build échoue si : une directive est inconnue, un quiz n'a pas de bonne réponse ou d'explication, un quiz
n'est jamais affiché, une formule LaTeX est invalide, ou un échappement YAML a corrompu une formule.

## Vérifications

```bash
npm run check      # contenu + typecheck + lint + tests unitaires + vérification des réponses (pytest)
npm run test:e2e   # parcours complet sur un build de production (Chrome installé)
```

Les tests Python nécessitent un venv : `python3 -m venv .venv && .venv/bin/pip install pytest pyyaml`.

## Déploiement (Vercel)

Variables d'environnement à définir : `APP_PIN`, `SESSION_SECRET` (`openssl rand -base64 48`).
Le limiteur anti-bruteforce est en mémoire : sur un hébergement serverless il est réinitialisé à chaque
démarrage d'instance ; un PIN plus long (6 à 8 chiffres) renforce nettement la sécurité.
