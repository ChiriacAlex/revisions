---
title: Erreurs repérées dans les documents
summary: "La liste complète des erreurs trouvées dans les polys, fiches, slides et corrigés d'intégration, avec la correction vérifiée par ordinateur et le chapitre où elle est expliquée."
kind: sheet
tags: [erratum, vérification, fiche]
minutes: 15
---

## Comment ces erreurs ont été trouvées

Chaque primitive a été **dérivée** par un logiciel de calcul symbolique (SymPy), chaque intégrale **calculée numériquement** (mpmath), chaque développement limité **recalculé**. Une réponse n'est déclarée fausse que si le calcul le prouve ; ces vérifications sont rejouées automatiquement à chaque mise à jour du site.

:::warning[Que faire en examen ?]
Les corrections ci-dessous sont mathématiquement certaines. Si une question d'examen reprend telle quelle une formule fausse du poly, écris la bonne réponse **et** justifie-la en une ligne (« en dérivant on retrouve bien l'intégrande »). Un correcteur ne peut pas te reprocher un calcul vérifiable.
:::

## Fiche « Formules trigonométriques »

| où | écrit | correct |
|---|---|---|
| bloc des formules 7-9 | titre « Angle $(\pi - \alpha)$ » | angle $(\pi + \alpha)$ |
| formule 40 | $\cot\alpha - \cot\beta = \frac{\sin(\alpha - \beta)}{\sin\alpha\sin\beta}$ | $\frac{\sin(\beta - \alpha)}{\sin\alpha\sin\beta}$ |
| formule 75 | $\int \cot x\,dx = -\ln\lvert\sin x\rvert$ | $+\ln\lvert\sin x\rvert$ |
| formule 87 | $\cot x = i\frac{1 + e^{2ix}}{1 - e^{2ix}}$ | $-i\frac{1 + e^{2ix}}{1 - e^{2ix}}$ |
| tableau des réciproques | $\operatorname{arccot}(-\infty) = -\pi$ | $+\pi$ |

Détails : [Trigonométrie](../trigonometrie/).

## « Table of Basic Integrals » et poly « Primitives » (tableau 1.2)

| où | écrit | correct |
|---|---|---|
| formule 39 / tableau 1.2 | $\int \frac{dx}{\sqrt{x^2 - a^2}} = \ln\left(\frac{x}{a} - \sqrt{\frac{x^2}{a^2} - 1}\right)$ | signe $+$ : $\ln\left(\frac{x}{a} + \sqrt{\frac{x^2}{a^2} - 1}\right) = \operatorname{argch}\frac{x}{a}$ |

## Poly « Primitives » et fiche « Intégration simple : Sommaire »

| où | écrit | correct |
|---|---|---|
| tableau 2.2 et fiche, formules 5-6 | $\int u'\cos u = -\sin u$, $\int u'\sin u = \cos u$ | $\int u'\cos u = \sin u$, $\int u'\sin u = -\cos u$ |
| exemple 8 | $\int\arcsin x = x\arcsin x + \sqrt{1 + x^2}$ | $x\arcsin x + \sqrt{1 - x^2}$ |
| § 3.2, fonctions paires | $\int_{-a}^{a}f = 3\int_0^a f$ | $2\int_0^a f$ |
| exemple 19 | $A_2 = 6$ | $A_2 = 3$ (facteur $\frac{1}{2!}$ oublié) |
| exemple 20 | $B = -\frac{1}{16}$, $C = \frac{1}{4}$ | $B = -\frac{1}{64}$, $C = \frac{1}{64}$ |
| exemples 23 et 24 | $\int_1^3$ | l'intégrale passe par le pôle $x = 1$ et diverge ; les valeurs données sont celles de $\int_2^3$ |
| exemple 27 | $A_1 = -\frac{2}{5}$, résultat en $\frac{2}{5}$, $\frac{1}{10}$, $\frac{3}{10}$ | $A_1 = -\frac{2}{25}$ : $-\frac{1}{5x} - \frac{2}{25}\ln\lvert x\rvert + \frac{1}{25}\ln(x^2 + 2x + 5) - \frac{3}{50}\arctan\frac{x + 1}{2}$ |
| exemple 31 | facteur $\frac{1}{16}I_2$ | $\frac{2}{16}I_2$ ($dx = 2\,dt$) : $-\frac{x + 5}{8(x^2 + 2x + 5)} - \frac{1}{16}\arctan\frac{x + 1}{2}$ |
| exemple 37 c | $\ln\lvert\tan t\rvert$ | $\ln\lvert 1 + \tan t\rvert$ |
| exercice 1 b | $\int\cosh^2 = \frac{x}{2} - \frac{\sinh 2x}{4}$ | $\frac{x}{2} + \frac{\sinh 2x}{4}$ |
| exercice 2 d | $-\frac{\arccos x}{2} + \sqrt{1 - x^2}$ | $-\frac{\arccos^2 x}{2} + \sqrt{1 - x^2}$ |
| exercice 3 | $\operatorname{argsh}$ | $\operatorname{argth}$ (ou la forme logarithmique) |
| exercice 4 g | $\frac{2}{5}\arcsin^3\frac{x}{2}$ | $\frac{1}{3}\arcsin^3\frac{x}{2}$ |
| exercice 4 h | $\ldots - x + \frac{1}{2}\ln\frac{1 + x}{1 - x}$ | $\ldots + x - \frac{1}{2}\ln\frac{1 + x}{1 - x}$ |
| exercice 6 a | $\int\frac{dx}{2x + 1} = \ln\lvert 2x + 1\rvert$ | $\frac{1}{2}\ln\lvert 2x + 1\rvert$ |
| exercice 7 b | $C = -3$, $-3\ln\lvert x - 1\rvert$ | $C = 3$, $+3\ln\lvert x - 1\rvert$ |
| exercice 8 c | $B = \frac{1}{5}$, $+\frac{1}{5}\ln\lvert t\rvert$ | $-\frac{1}{5}\ln\lvert t\rvert$ : $\ln\lvert x\rvert - \frac{1}{5}\ln\lvert x^5 + 1\rvert + \frac{1}{5(x^5 + 1)}$ |
| exercice 10 a | $\frac{1}{2}\ln\lvert\cos x\rvert - \frac{1}{4}\ln\sin^2 x$ | $-\frac{1}{2}\ln\lvert\cos x\rvert + \frac{1}{4}\ln(1 + \sin^2 x)$ |
| exercice 11 c | coefficients doublés, $+2\ln(t^2 + 1)$ | $\ln\left\lvert\frac{t - 1}{t + 1}\right\rvert + 2\arctan t$ |
| exercice 12 d | $-\frac{1}{2}\sqrt{x - x^2} - \frac{1}{4}\arcsin(2x + 1)$ | $-\sqrt{x - x^2} - \arcsin(2x - 1)$ |

Les exercices 1 à 7 sont aussi ceux du fichier « Intégrale simple — Exercices résolus » (et de sa version anglaise), qui contient les **mêmes** erreurs. Détails : [Primitives](../primitives/), [Fractions rationnelles](../fractions-rationnelles/), [Trigonométrie et abéliennes](../trigo-abeliennes/), [TD 1](../td-integration-simple/).

## Slides « Chapter 1: Anti-derivatives » (EN)

| où | écrit | correct |
|---|---|---|
| slide 22 | $\int xe^x\,dx = -xe^x - e^x$ | $xe^x - e^x$ |
| slide 37 | $\int\frac{x^2 + 1}{x^2 - 5x + 6}\,dx = 5 - 5\ln\lvert x - 2\rvert + \ldots$ | $x - 5\ln\lvert x - 2\rvert + 10\ln\lvert x - 3\rvert$ |

## Poly « Les développements limités »

| où | écrit | correct |
|---|---|---|
| exemple 4 | $(1 + x^3)\sqrt{1 - x} = \ldots + \frac{5x^3}{16}$ | $\frac{15x^3}{16}$ |
| § 3.4.2 | $\arctan x = \ldots + (-1)^n\frac{x^{2n+2}}{2n + 2}$ | $(-1)^n\frac{x^{2n+1}}{2n + 1}$ |
| exemple 11 | $\frac{\ln(1 + x)}{\sin x} = \ldots - \frac{x^3}{4}$ | $-\frac{x^3}{3}$ |
| exemple 13 | $\sqrt{\frac{x^2}{2}} = \frac{\lvert x\rvert}{2}$, limite $-\frac{1}{2}$ | $\frac{\lvert x\rvert}{\sqrt{2}}$, limite $-\frac{\sqrt{2}}{2}$ |
| § 3.5.2 | « $\lim_{x \to +\infty}$ » | $\lim_{x \to 0}$ |

Détails : [Développements limités](../developpements-limites/).

## Intégrales généralisées (slides et TD)

| où | écrit | correct |
|---|---|---|
| slides « 5 méthodes », diapo 2 | « les dix méthodes » | cinq méthodes |
| slides « 5 méthodes », diapo 9 d | « montrer que $\int_2^{+\infty}\frac{dx}{x\ln x}$ converge » | elle **diverge** (primitive $\ln\ln x$) |
| slides « 5 méthodes », diapo 43 | critère de Bertrand mal énoncé | converge $\iff \alpha > 1$ ou ($\alpha = 1$ et $\beta > 1$) |
| corrigé TD, question 1-1 b | $\int_{-\infty}^0 e^{\alpha x}\,dx = -\frac{1}{\alpha}$ | $\frac{1}{\alpha}$ |
| slides chapitre 2, diapo 83 | $E_n = \pi + \frac{\pi}{n}$ | $\pi + \frac{\pi}{n^2}$ |
| feuille TD chapitre 2, question 2-2 b | « $-1 \ge x < 0$ » | $-1 \le x < 0$ |

Détails : [Méthodes](../methodes-convergence/), [TD 2](../td-integrales-generalisees/), [Suites d'intégrales](../suites-integrales/).

:::note[Et ce qui manquait]
Les feuilles de TD des chapitres 2 et 3 (suites d'intégrales, intégrales à paramètre, feuille EXTRA) et les neuf séries d'exercices des slides « 5 méthodes » sont distribuées **sans corrigé** : elles sont entièrement corrigées sur ce site. Le corrigé du TD 2 demande l'énergie du signal amorti sans la calculer : elle vaut $\frac{A^2}{4\alpha} + \frac{A^2\alpha}{4(\alpha^2 + \omega^2)}$.
:::
