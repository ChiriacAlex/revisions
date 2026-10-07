# Révisions

Site personnel de révision : cours rédigés, quiz auto-corrigés, TD corrigés, labo Python (Python dans le navigateur).

## Accès

Le site est protégé par un **code PIN** ; une fois le PIN saisi, la session dure **1 heure** (cookie HttpOnly signé),
puis le PIN est redemandé. Le PIN et le secret de session sont dans `.env.local` (jamais versionné) :

```bash
APP_PIN=…
SESSION_SECRET=…   # >= 32 caractères : openssl rand -base64 48
```

## Lancer en permanence sur le Mac (Docker + nginx)

```bash
docker compose up -d --build     # http://localhost:3217
```

Deux conteneurs : `app` (serveur Next autonome) et `nginx` devant (compression, cache de Python/Pyodide).
`restart: unless-stopped` : ils redémarrent tout seuls avec Docker Desktop (activer « Start Docker Desktop
when you sign in » dans ses réglages). Après une modification des cours : relancer la même commande.
Arrêter : `docker compose down`. Logs : `docker compose logs -f app`.

## Développer

```bash
npm install
npm run dev                  # http://localhost:3000 (lit .env.local)
```

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
   expression Python…) recalculé par `npm run verify:py`. Pour l'analyse, l'expression peut utiliser `calc`
   (`verify/calculus.py`, SymPy + mpmath) : `calc.antiderivative_ok(f, F)` dérive la primitive proposée,
   `calc.integral(f, a, b)` calcule une intégrale (généralisée), `calc.series_coeff`, `calc.limit`, `calc.identity`.
   Les calculs écrits dans la prose sont vérifiés dans `verify/test_*_facts.py`.

Le build échoue si : une directive est inconnue, un quiz n'a pas de bonne réponse ou d'explication, un quiz
n'est jamais affiché, une formule LaTeX est invalide, ou un échappement YAML a corrompu une formule.

## Vérifications

```bash
npm run check      # contenu + typecheck + lint + tests unitaires + vérification des réponses (pytest)
npm run test:e2e   # serveur de production (PIN, session, pages, labo Python) avec le Chrome installé
```

La CI GitHub (`.github/workflows/ci.yml`) relance ces vérifications à chaque push ; le site n'est plus publié en ligne.

Les tests Python nécessitent un venv : `python3 -m venv .venv && .venv/bin/pip install pytest pyyaml sympy mpmath`.
