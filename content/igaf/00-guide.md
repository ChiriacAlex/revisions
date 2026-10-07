---
title: Mode d'emploi du cours
summary: "Ce que couvre le cours d'intégration (INTG/IGAF), à quels documents de l'école correspond chaque chapitre, dans quel ordre travailler, et les acquis d'apprentissage visés."
kind: sheet
tags: [méthode, programme]
minutes: 6
---

## Ce que tu vas apprendre

Le cours d'intégration d'EPITA (« Intégrales généralisées et approximation de fonctions », Kamel Attar et Nasko Karamanov) a un but très concret : savoir **calculer** des intégrales, et décider si une intégrale **a un sens** quand l'intervalle est infini ou que la fonction explose. C'est l'outil de base des probabilités (densités, espérances), du traitement du signal (énergie, Fourier) et de l'automatique (Laplace).

:::key[Acquis d'apprentissage visés]
1. Décider de la **convergence d'une intégrale généralisée** avec les bons critères.
2. Décider de la convergence d'une **suite d'intégrales** et trouver sa limite (convergence dominée).
3. Identifier les propriétés d'une **intégrale à paramètre** (continuité, dérivabilité ; Fourier, Laplace).
4. Simplifier des expressions avec des limites de suites d'intégrales ou des intégrales à paramètre.
:::

## Plan et correspondance avec les documents de l'école

| chapitre du site | documents de l'école |
|---|---|
| Ch0 — Prérequis d'analyse | « Prérequis très or : Continuité & Dérivabilité », « Limites », « The Exponential Functions », « Les fonctions logarithmiques » |
| Ch0 bis — Trigonométrie | « Formules trigonométriques » (4 pages) |
| Ch1 — Primitives | poly « Primitives » (§ 1-3), « Intégrales — prérequis très or », « Table of Basic Integrals », slides « Chapter 1: Anti-derivatives » |
| Ch1 bis — Fractions rationnelles | poly « Primitives » (§ 4), fiche « Intégration simple : Sommaire » |
| Ch1 ter — Trigonométrie, Bioche, abéliennes | poly « Primitives » (§ 5-7), fiche « Sommaire » (page 2) |
| TD 1 — Intégration simple | poly « Primitives » (§ 8), « Intégrale simple — Exercices résolus » (FR et EN) |
| Ch2 — Développements limités | poly « Le développements limités » |
| Ch3 — Intégrales généralisées | slides « Intégrales généralisées — Chapitre 1 », slides EN « Generalized integrals — Chapter 1 » |
| Ch3 bis — Méthodes | slides « Comment montrer la convergence » (5 méthodes), « Méthode d'étude des intégrales généralisées » (organigramme) |
| TD 2 — Intégrales généralisées | feuille de TD « 1. Définition et propriétés » (énoncé + corrigé) |
| Ch4 — Suites d'intégrales | slides « Chapitre 2 : Suites d'intégrales » (K. Attar et N. Karamanov) |
| TD 3 — Suites d'intégrales | feuille « Chapitre 2 : Suites d'intégrales » / « Sequences of Integrals » |
| Ch5 — Intégrales à paramètre | feuilles « Chapitre 3 : Intégrales à paramètre » (énoncés des théorèmes) |
| TD 4 — Intégrales à paramètre | feuilles « Chapitre 3 » et « Chapitre 3 (EXTRA) » |

:::warning[Les documents de l'école contiennent des erreurs]
En vérifiant **chaque** calcul par ordinateur (dérivation des primitives, calcul numérique des intégrales, DL symboliques), j'ai trouvé une quarantaine d'erreurs dans les polys, fiches, slides et corrigés. Elles sont signalées dans les chapitres par des encadrés rouges et regroupées dans la fiche [Erreurs repérées dans les documents](../erratum/). Si ta copie reprend une formule du poly, vérifie-la d'abord ici.
:::

## Comment travailler

1. **Prérequis d'abord** (Ch0, Ch0 bis) : si tu hésites sur une dérivée ou une limite, tout le reste sera pénible.
2. **Intégration simple** (Ch1 à TD 1) : c'est du **calcul**, ça s'apprend en faisant. Fais les 44 primitives du Ch1 sans regarder les solutions.
3. **DL** (Ch2) : indispensable pour trouver les équivalents du chapitre suivant.
4. **Intégrales généralisées** (Ch3, Ch3 bis, TD 2) : apprends l'**organigramme** du Ch3 bis par cœur.
5. **Suites d'intégrales et intégrales à paramètre** (Ch4, Ch5, TD 3, TD 4) : le cœur du programme. Un seul théorème à maîtriser vraiment : la **convergence dominée** (et ses variantes de continuité et de dérivation).

:::method[Le réflexe qui évite la moitié des erreurs]
**Dérive toujours ta primitive.** Si tu ne retrouves pas l'intégrande, il y a une erreur. C'est exactement ce que fait le site pour vérifier ses propres corrigés.
:::
