---
title: Mode d'emploi du cours
summary: Programme, barème, méthode de travail et lexique anglais ↔ français.
kind: sheet
tags: [méthode, programme, lexique]
minutes: 8
---

## Ce que tu vas apprendre

Le cours **Logical Formalism** (FOLO) d'EPITA n'est pas un cours de calcul. Son but est de t'apprendre à **écrire des preuves rigoureuses** : lire un énoncé, comprendre les objets en jeu, choisir la bonne méthode et rédiger un raisonnement qu'un correcteur ne peut pas contester.

À la fin, tu dois savoir :

- repérer dans un énoncé les **types** des objets (entier, ensemble, fonction, ensemble d'ensembles…), les **quantificateurs** et les **relations** entre eux ;
- **formaliser** une phrase en formule logique ($\forall$, $\exists$, $\Rightarrow$, $\wedge$, $\vee$, $\neg$) ;
- **décomposer** un énoncé compliqué en sous-énoncés plus simples ;
- appliquer le bon **motif de preuve** (*proof pattern*) : implication directe, contradiction, contraposée, double implication, double inclusion, disjonction de cas, récurrence, bijection, analyse-synthèse ;
- **compter** les éléments d'un ensemble en trouvant un « codage » (une bijection) plus simple à dénombrer.

:::key[La règle d'or du cours]
Une preuve n'est pas une suite de calculs : c'est un **argument structuré**. Le correcteur attend que tu annonces ton but et ton motif de preuve (« Montrons par contraposée que… », « Procédons par double inclusion… ») avant d'écrire la moindre ligne de calcul.
:::

## Programme et correspondance avec les slides

| Ici | Slides du cours (Moodle) | Idée centrale |
|---|---|---|
| Ch. 1 — Objets et implication | *Introduction*, *Mathematical Objects* | variables, ensembles, fonctions, propositions, $\Rightarrow$ |
| Ch. 2 — Motifs de preuve | *More Proof Patterns* | $\wedge$, $\vee$, $\Leftrightarrow$, contradiction, contraposée, cas |
| Ch. 3 — Ensembles | *Set Theory* | $\cup$, $\cap$, $\subseteq$, $\mathcal{P}(E)$, complémentaire, produit |
| Ch. 4 — Quantificateurs | *Quantified Logic* | $\forall$, $\exists$, $\exists!$, ensemble vide |
| Ch. 5 — Relations binaires | *Functions*, *Advanced Inductive Proofs*, projet | symétrie, réflexivité, transitivité, équivalence, ordre |
| Ch. 6 — Fonctions | *Functions* | fonction, image, injection, surjection, bijection, réciproque |
| Ch. 7 — Énoncés complexes | *Parsing Complex Propositions* | ordre et négation des quantificateurs, fonctions d'ordre supérieur |
| Ch. 8 — Récurrence | *Inductive Proofs* | récurrence simple, pièges |
| Ch. 9 — Récurrence avancée | *Advanced Inductive Proofs* | récurrence d'ordre $k$, forte, ordres bien fondés |
| Ch. 10 — Bijections et cardinal | *Bijections and Cardinality* | ensembles finis, équipotence, $\mathrm{Card}(\mathcal{P}(E)) = 2^n$ |
| Ch. 11 — Dénombrement | *Applied Combinatorics* | partitions, produit cartésien, combinaisons |
| Ch. 12 — Motifs avancés | *Advanced Proof Patterns* | analyse-synthèse, bijections d'examen |
| Ch. 13 — Pièges et conseils | *Tips and Mistakes* | erreurs classiques, contre-exemples, rédaction |

Les **slides « Answer »** sont vides dans la version étudiante : toutes les corrections des exercices du cours sont rédigées ici, dans la section « Exercices du cours » de chaque chapitre.

## Évaluation

| Épreuve | Points | Ce qui est attendu |
|---|---|---|
| Projet de programmation (`folo.py`) | 2 | 15 fonctions Python sur les relations et fonctions, notées automatiquement |
| Partiel (*mid-term*) | 3 | problèmes courts, preuves rigoureuses |
| Examen final écrit | 15 | problèmes courts, **corrigé à la main** : la rédaction compte |

:::warning[Le projet est noté par un robot]
Un fichier qui ne s'exécute pas (`python3 folo.py`) vaut **0**, sans recours. Respecte exactement les noms et signatures des fonctions du modèle. Le labo Python de la partie « Projet » te permet de lancer les tests officiels directement dans le navigateur.
:::

## Comment travailler avec ce site

1. **Lis le chapitre** en entier une première fois, sans tout comprendre.
2. **Fais les quiz** au fil de l'eau : ils sont corrigés immédiatement, avec une explication pour chaque réponse (même pour les bonnes).
3. **Cherche les exercices du cours sur papier** avant d'ouvrir les indices, puis la correction. Les indices sont progressifs : n'ouvre le suivant que si tu bloques encore.
4. **Rédige** : pour une preuve, écris d'abord le **squelette** (le motif, les sous-buts), puis remplis-le. Compare ensuite ta rédaction à la correction, pas seulement ta « réponse ».
5. **Fais le TD correspondant**, puis les exercices « Extra ».
6. Avant le partiel ou l'examen : le **recueil des motifs de preuve**, la **fiche express** et l'**examen blanc**.

:::method[Que faire quand on bloque ?]
1. **Quel est le type des objets ?** Entier, réel, ensemble, ensemble d'ensembles, fonction, ensemble de fonctions… Relis les définitions.
2. **Que me demande-t-on ?** Une équivalence, une égalité d'ensembles, une existence, un dénombrement…
3. **Le motif s'impose souvent tout seul** : une équivalence se prouve par double implication, une égalité d'ensembles par double inclusion, un « pour tout » commence par « Soit… ».
4. **Seulement ensuite**, cherche les liens entre hypothèses et conclusion (propriétés immédiates, définitions déroulées).
:::

## Lexique anglais ↔ français

Les slides et l'examen sont en anglais. Les termes à reconnaître immédiatement :

| Anglais | Français | Anglais | Français |
|---|---|---|---|
| proof pattern | motif (schéma) de preuve | induction | récurrence |
| statement, proposition | énoncé, proposition | base case / inductive case | initialisation / hérédité |
| claim, goal, subgoal | affirmation, but, sous-but | strong induction | récurrence forte |
| proof by contradiction | preuve par l'absurde | depth $k$ induction | récurrence d'ordre $k$ |
| proof by contraposition | preuve par contraposée | set, subset | ensemble, sous-ensemble (partie) |
| case disjunction | disjonction de cas | power set | ensemble des parties |
| law of the excluded middle | tiers exclu | complement | complémentaire |
| if and only if (iff) | si et seulement si (ssi) | Cartesian product | produit cartésien |
| counter-example | contre-exemple | binary relation | relation binaire |
| for all / there exists | pour tout / il existe | equivalence class | classe d'équivalence |
| scope (of a quantifier) | portée | partial / total order | ordre partiel / total |
| well-founded | bien fondé | function, map | fonction, application |
| domain, image | ensemble de départ, image | one-to-one, injective | injective |
| onto, surjective | surjective | bijection, one-to-one correspondence | bijection |
| inverse | réciproque | equipotent | équipotents |
| cardinality | cardinal | finite / infinite | fini / infini |
| $k$-combination | combinaison à $k$ éléments | partition | partition |
| even / odd | pair / impair | relatively prime | premiers entre eux |
| nonnegative | positif ou nul | lower bound / upper bound | minorant / majorant |
| yields | conduit à | analysis and synthesis | analyse-synthèse |
