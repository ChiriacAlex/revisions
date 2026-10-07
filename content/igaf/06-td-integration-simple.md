---
title: TD 1 — Intégration simple (corrigé)
summary: "Les 15 exercices résolus du poly et du fichier « Intégrale simple — Exercices résolus » (FR et EN), recorrigés : linéarisation, changement de variable, IPP, fractions rationnelles, Bioche, abéliennes, intégrales définies et intégrales de Wallis."
kind: td
tags: [TD, primitives, IPP, fractions rationnelles, Wallis]
minutes: 180
---

:::note[À propos de ce TD]
Ces exercices sont ceux de la section 8 du poly « Primitives » ; le fichier « Simple Integration — Solved Problems » (et sa version française) reprend les sept premiers. Les corrigés distribués contiennent **plusieurs erreurs**, signalées ici dans des encadrés rouges. Chaque réponse ci-dessous a été vérifiée en la dérivant (ou par calcul numérique pour les intégrales définies). Méthode de contrôle à appliquer toi aussi : **dérive ta primitive**, tu dois retrouver l'intégrande.
:::

## Exercice 1 — Linéariser

Calculer a) $\int \sin^2 x\,dx$, b) $\int \cosh^2 x\,dx$, c) $\int \tan^2 x\,dx$.

:::hint[Indice]
$\sin^2 x = \frac{1 - \cos 2x}{2}$, $\cosh^2 x = \frac{1 + \cosh 2x}{2}$, $\tan^2 x = \frac{1}{\cos^2 x} - 1$.
:::

:::correction
- a) $\int \sin^2 x\,dx = \int \frac{1 - \cos 2x}{2}\,dx = \frac{x}{2} - \frac{\sin 2x}{4} + C$.
- b) $\int \cosh^2 x\,dx = \int \frac{1 + \cosh 2x}{2}\,dx = \frac{x}{2} + \frac{\sinh 2x}{4} + C$.
- c) $\int \tan^2 x\,dx = \int \left(\frac{1}{\cos^2 x} - 1\right)dx = \tan x - x + C$.
:::

:::warning[Erreur dans le corrigé (exercice 1 b)]
Le corrigé écrit $\int \cosh^2 x\,dx = \frac{x}{2} - \frac{\sinh 2x}{4}$. Le signe est faux : une primitive de $\cosh 2x$ est $+\frac{\sinh 2x}{2}$ (pas de signe moins en hyperbolique : $\sinh' = \cosh$). Vérification : $\left(\frac{x}{2} + \frac{\sinh 2x}{4}\right)' = \frac{1 + \cosh 2x}{2} = \cosh^2 x$. ✓
:::

## Exercice 2 — Changement de variable

a) $\int (x^3 + x)^5(3x^2 + 1)\,dx$ ; b) $\int \sqrt{2x + 1}\,dx$ ; c) $\int \frac{2x\,dx}{\sqrt[3]{x^2 + 1}}$ ; d) $\int \frac{\arccos x - x}{\sqrt{1 - x^2}}\,dx$ ; e) $\int \sin(2x)\,e^{\sin^2 x}\,dx$.

:::correction
- a) $u = x^3 + x$ : $\frac{(x^3 + x)^6}{6} + C$.
- b) $u = 2x + 1$ : $\frac{1}{3}(2x + 1)^{3/2} + C$.
- c) $u = x^2 + 1$ : $\frac{3}{2}(x^2 + 1)^{2/3} + C$.
- d) On sépare : $\int \frac{\arccos x}{\sqrt{1 - x^2}}\,dx + \int \frac{-x}{\sqrt{1 - x^2}}\,dx$. Pour la première, $u = \arccos x$, $du = -\frac{dx}{\sqrt{1 - x^2}}$ : $-\int u\,du = -\frac{u^2}{2}$. La seconde vaut $\sqrt{1 - x^2}$. Donc
$$\int \frac{\arccos x - x}{\sqrt{1 - x^2}}\,dx = -\frac{\arccos^2 x}{2} + \sqrt{1 - x^2} + C.$$
- e) $\sin 2x = 2\sin x\cos x$ et $t = \sin^2 x$, $dt = 2\sin x\cos x\,dx$ : $\int e^t\,dt = e^{\sin^2 x} + C$.
:::

:::warning[Erreur dans le corrigé (exercice 2 d)]
Le corrigé écrit $-\frac{\arccos x}{2}$ au lieu de $-\frac{\arccos^2 x}{2}$ : $\int u\,du = \frac{u^2}{2}$, le carré a disparu.
:::

## Exercice 3 — Fraction puis abélienne

Calculer $I(x) = \int \frac{x\,dx}{2 - x^2 + 2x}$, puis $J(x) = \int \frac{dx}{1 + x + 2\sqrt{1 - x}}$.

:::hint[Indice]
Pour $I$ : faire apparaître la dérivée $-2x + 2$ du dénominateur, puis mettre $-x^2 + 2x + 2 = 3 - (x - 1)^2$ sous forme canonique. Pour $J$ : poser $t = \sqrt{1 - x}$.
:::

:::correction
**$I$.** $\frac{x}{-x^2 + 2x + 2} = -\frac{1}{2}\cdot\frac{-2x + 2}{-x^2 + 2x + 2} + \frac{1}{3 - (x - 1)^2}$. Le premier terme s'intègre en $-\frac{1}{2}\ln|-x^2 + 2x + 2|$. Pour le second, avec $u = x - 1$ et $a = \sqrt{3}$ : $\int \frac{du}{a^2 - u^2} = \frac{1}{2a}\ln\left|\frac{a + u}{a - u}\right|$. Donc
$$I(x) = -\frac{1}{2}\ln|-x^2 + 2x + 2| + \frac{1}{2\sqrt{3}}\ln\left|\frac{\sqrt{3} + x - 1}{\sqrt{3} - x + 1}\right| + C.$$
(Sur l'intervalle où $|x - 1| < \sqrt{3}$, le second terme s'écrit aussi $\frac{1}{\sqrt{3}}\operatorname{argth}\frac{x - 1}{\sqrt{3}}$.)

**$J$.** $t = \sqrt{1 - x}$, $x = 1 - t^2$, $dx = -2t\,dt$ et $1 + x + 2t = 2 - t^2 + 2t$ :
$$J(x) = \int \frac{-2t\,dt}{2 + 2t - t^2} = -2\,I(t) = \ln|-t^2 + 2t + 2| - \frac{1}{\sqrt{3}}\ln\left|\frac{\sqrt{3} + t - 1}{\sqrt{3} - t + 1}\right| + C, \quad t = \sqrt{1 - x}.$$
:::

:::warning[Erreur dans le corrigé (exercice 3)]
Le corrigé utilise $\int \frac{u'}{a^2 - u^2} = \frac{1}{a}\operatorname{argsh}\frac{u}{a}$ : c'est **argth** (tangente hyperbolique réciproque), pas argsh. L'argsh correspond à $\frac{u'}{\sqrt{a^2 + u^2}}$. Le corrigé de $J$ hérite de la même erreur (et écrit $-x^2 + 2x + 2$ au lieu de $-t^2 + 2t + 2$).
:::

## Exercice 4 — Intégrations par parties

a) $\int x\sin 2x\,dx$ ; b) $\int x\ln x\,dx$ ; c) $\int x^2\ln x\,dx$ ; d) $\int (x^2 + 7x - 5)\cos 2x\,dx$ ; e) $\int x^2 e^{3x}\,dx$ ; f) $\int \frac{x\arcsin x}{\sqrt{1 - x^2}}\,dx$ ; g) $\int \frac{\arcsin^2\frac{x}{2}}{\sqrt{4 - x^2}}\,dx$ ; h) $\int x\ln\frac{1 + x}{1 - x}\,dx$.

:::correction
- a) $-\frac{x}{2}\cos 2x + \frac{1}{4}\sin 2x + C$.
- b) $\frac{x^2}{2}\ln x - \frac{x^2}{4} + C$.
- c) $u = \ln x$, $v = \frac{x^3}{3}$ : $\frac{x^3}{3}\ln x - \frac{x^3}{9} + C$.
- d) IPP répétées (tableau) : $\frac{1}{2}\left(x^2 + 7x - \frac{11}{2}\right)\sin 2x + \frac{1}{2}\left(x + \frac{7}{2}\right)\cos 2x + C$.
- e) $\left(\frac{x^2}{3} - \frac{2x}{9} + \frac{2}{27}\right)e^{3x} + C$.
- f) $u = \arcsin x$, $v' = \frac{x}{\sqrt{1 - x^2}}$, $v = -\sqrt{1 - x^2}$ : $-\sqrt{1 - x^2}\arcsin x + \int dx = -\sqrt{1 - x^2}\arcsin x + x + C$.
- g) **Pas besoin d'IPP** : avec $u = \arcsin\frac{x}{2}$, $du = \frac{1}{2}\cdot\frac{dx}{\sqrt{1 - x^2/4}} = \frac{dx}{\sqrt{4 - x^2}}$. Donc $\int u^2\,du = \frac{1}{3}\arcsin^3\frac{x}{2} + C$.
- h) $u = \ln\frac{1 + x}{1 - x}$, $u' = \frac{2}{1 - x^2}$, $v = \frac{x^2}{2}$ :
$\frac{x^2}{2}\ln\frac{1 + x}{1 - x} - \int \frac{x^2}{1 - x^2}\,dx$, et $\frac{x^2}{1 - x^2} = -1 + \frac{1}{1 - x^2}$, donc
$$\int x\ln\frac{1 + x}{1 - x}\,dx = \frac{x^2}{2}\ln\frac{1 + x}{1 - x} + x - \frac{1}{2}\ln\frac{1 + x}{1 - x} + C = \frac{x^2 - 1}{2}\ln\frac{1 + x}{1 - x} + x + C.$$
:::

:::warning[Deux erreurs dans le corrigé (exercice 4 g et h)]
- **g)** Le corrigé fait une IPP incorrecte et trouve $\frac{2}{5}\arcsin^3\frac{x}{2}$. La dérivée de ce résultat vaut $\frac{6}{5}$ de l'intégrande : c'est faux. La bonne réponse est $\frac{1}{3}\arcsin^3\frac{x}{2}$ (changement de variable direct).
- **h)** Le corrigé écrit « $+\int \frac{x^2}{1 - x^2}$ » au lieu de « $-$ » dans la formule d'IPP, d'où un résultat aux signes inversés ($-x + \frac{1}{2}\ln$ au lieu de $+x - \frac{1}{2}\ln$).
:::

## Exercice 5 — Deux IPP qui se rejoignent

Calculer $\int e^{-x}\cos x\,dx$.

:::correction
$I = \int e^{-x}\cos x\,dx$. IPP avec $u = e^{-x}$, $v' = \cos x$ : $I = e^{-x}\sin x + \int e^{-x}\sin x\,dx$. Nouvelle IPP avec $u = e^{-x}$, $v' = \sin x$ : $\int e^{-x}\sin x\,dx = -e^{-x}\cos x - I$. Donc $2I = e^{-x}(\sin x - \cos x)$ et
$$\int e^{-x}\cos x\,dx = \frac{e^{-x}}{2}(\sin x - \cos x) + C.$$
:::

## Exercice 6 — Fractions rationnelles simples

a) $\int \frac{dx}{2x + 1}$ ; b) $\int \frac{x^3\,dx}{x + 1}$ ; c) $\int \frac{2x - 1}{(x - 1)^2}\,dx$.

:::correction
- a) $\frac{1}{2}\ln|2x + 1| + C$ (attention au $\frac{1}{2}$ : $u' = 2$).
- b) $x^3 = (x + 1)(x^2 - x + 1) - 1$, donc $\frac{x^3}{x + 1} = x^2 - x + 1 - \frac{1}{x + 1}$ et l'intégrale vaut $\frac{x^3}{3} - \frac{x^2}{2} + x - \ln|x + 1| + C$.
- c) $\frac{2x - 1}{(x - 1)^2} = \frac{2(x - 1) + 1}{(x - 1)^2} = \frac{2}{x - 1} + \frac{1}{(x - 1)^2}$, d'où $2\ln|x - 1| - \frac{1}{x - 1} + C$.
:::

:::warning[Coquille dans le corrigé (exercice 6 a)]
Le corrigé écrit $\int \frac{dx}{2x + 1} = \int \frac{u'}{u} = \ln|2x + 1|$ en posant $u = 2x + 1$, $u' = 2$ : il manque le facteur $\frac{1}{2}$, puisque le numérateur vaut $1$ et non $u' = 2$.
:::

## Exercice 7 — Éléments simples

a) $\int \frac{2x^2}{x^4 - 1}\,dx$ ; b) $\int \frac{dx}{x^2(x - 1)^3}$ ; c) $\int \frac{dx}{(x^2 + 1)^2}$.

:::correction
- a) $\frac{2x^2}{(x - 1)(x + 1)(x^2 + 1)} = \frac{1/2}{x - 1} - \frac{1/2}{x + 1} + \frac{1}{x^2 + 1}$ (en $x = 1$ : $A = \frac{2}{2 \cdot 2}$ ; en $x = -1$ : $D = \frac{2}{-2 \cdot 2}$ ; puis $x = 0$ et $x = 2$). Donc $\frac{1}{2}\ln|x - 1| - \frac{1}{2}\ln|x + 1| + \arctan x + C$.
- b) $\frac{1}{x^2(x - 1)^3} = -\frac{3}{x} - \frac{1}{x^2} + \frac{3}{x - 1} - \frac{2}{(x - 1)^2} + \frac{1}{(x - 1)^3}$. Donc
$$\int \frac{dx}{x^2(x - 1)^3} = -3\ln|x| + \frac{1}{x} + 3\ln|x - 1| + \frac{2}{x - 1} - \frac{1}{2(x - 1)^2} + C.$$
**Contrôle** : la somme des coefficients des $\frac{1}{x - a}$ doit valoir $\lim_{x \to \infty} x F(x) = 0$ : $-3 + 3 = 0$. ✓
- c) $t = \arctan x$ : $\int \cos^2 t\,dt = \frac{t}{2} + \frac{\sin 2t}{4}$, et $\frac{\sin 2t}{2} = \frac{\tan t}{1 + \tan^2 t} = \frac{x}{1 + x^2}$ : $\frac{\arctan x}{2} + \frac{x}{2(1 + x^2)} + C$.
:::

:::warning[Erreur dans le corrigé (exercice 7 b)]
Le corrigé trouve $C = -3$ (coefficient de $\frac{1}{x - 1}$) et écrit $-3\ln|x - 1|$. Le contrôle « somme des coefficients des pôles simples = 0 » montre l'erreur : $-3 - 3 \ne 0$. La bonne valeur est $C = +3$.
:::

## Exercice 8 — Pôle en 0 et facteur irréductible

a) $\int \frac{dx}{x(x^2 + 2x + 5)}$ ; b) $\int \frac{dx}{x(x^2 + 1)^2}$ ; c) $\int \frac{dx}{x(x^5 + 1)^2}$.

:::correction
- a) Voir le chapitre fractions rationnelles : $\frac{1}{5}\ln|x| - \frac{1}{10}\ln(x^2 + 2x + 5) - \frac{1}{10}\arctan\frac{x + 1}{2} + C$.
- b) $t = 1 + x^2$, $dt = 2x\,dx$ : $\int \frac{x\,dx}{x^2(x^2 + 1)^2} = \frac{1}{2}\int \frac{dt}{(t - 1)t^2}$ et $\frac{1}{(t - 1)t^2} = \frac{1}{t - 1} - \frac{1}{t} - \frac{1}{t^2}$. Donc
$\frac{1}{2(1 + x^2)} - \frac{1}{2}\ln(1 + x^2) + \frac{1}{2}\ln(x^2) + C = \frac{1}{2(1 + x^2)} + \ln|x| - \frac{1}{2}\ln(1 + x^2) + C$.
- c) $t = x^5 + 1$, $dt = 5x^4\,dx$ : $\int \frac{x^4\,dx}{x^5(x^5 + 1)^2} = \frac{1}{5}\int \frac{dt}{(t - 1)t^2} = \frac{1}{5}\left[\ln|t - 1| - \ln|t| + \frac{1}{t}\right]$, soit
$$\int \frac{dx}{x(x^5 + 1)^2} = \ln|x| - \frac{1}{5}\ln|x^5 + 1| + \frac{1}{5(x^5 + 1)} + C.$$
:::

:::warning[Erreur dans le corrigé (exercice 8 c)]
Le corrigé décompose $\frac{1}{(t - 1)t^2}$ avec $B = +\frac{1}{5}$ devant $\frac{1}{t}$ et écrit $+\frac{1}{5}\ln|t|$ : le bon coefficient de $\frac{1}{t}$ est $-1$ (avant le facteur $\frac{1}{5}$), donc $-\frac{1}{5}\ln|t|$. Contrôle en $t \to \infty$ : $t \cdot \frac{1}{(t - 1)t^2} \to 0$, donc les coefficients de $\frac{1}{t - 1}$ et $\frac{1}{t}$ sont opposés.
:::

## Exercice 9 — Deux changements de variable

Calculer $\int \frac{x^3}{(1 + x^2)^3}\,dx$ a) avec $t = 1 + x^2$ ; b) avec $\theta = \arctan x$ ; c) vérifier l'accord des résultats.

:::correction
- a) $x^3\,dx = \frac{1}{2}(t - 1)\,dt$ : $\frac{1}{2}\int (t^{-2} - t^{-3})\,dt = -\frac{1}{2t} + \frac{1}{4t^2}$, soit $\frac{1}{4(1 + x^2)^2} - \frac{1}{2(1 + x^2)} + C$.
- b) $x = \tan\theta$, $dx = (1 + \tan^2\theta)\,d\theta$ : $\int \frac{\tan^3\theta}{(1 + \tan^2\theta)^2}\,d\theta = \int \sin^3\theta\cos\theta\,d\theta = \frac{\sin^4\theta}{4}$, et $\sin^2\theta = \frac{x^2}{1 + x^2}$ : $\frac{1}{4}\left(\frac{x^2}{1 + x^2}\right)^2 + C'$.
- c) $\frac{1}{4}\left(\frac{x^2}{1 + x^2}\right)^2 = \frac{1}{4}\left(1 - \frac{1}{1 + x^2}\right)^2 = \frac{1}{4} - \frac{1}{2(1 + x^2)} + \frac{1}{4(1 + x^2)^2}$ : les deux résultats diffèrent de la **constante** $\frac{1}{4}$. Ce n'est pas une contradiction : deux primitives d'une même fonction diffèrent d'une constante.
:::

## Exercice 10 — Fonctions trigonométriques et hyperboliques

a) $\int \frac{\tan x}{1 + \sin^2 x}\,dx$ ; b) $\int \frac{dx}{-5 + 13\cosh x}$ ; c) $\int \frac{dx}{\cos^4 x}$ ; d) $\int \frac{dx}{\sin^2 x - \cos^2 x}$.

:::correction
- a) Invariance par $x \mapsto -x$ : $t = \cos x$, $dt = -\sin x\,dx$. $\frac{\tan x}{1 + \sin^2 x} = \frac{\sin x}{\cos x\,(2 - \cos^2 x)}$, donc $\int = -\int \frac{dt}{t(2 - t^2)}$. Et $\frac{1}{t(2 - t^2)} = \frac{1}{2t} + \frac{t}{2(2 - t^2)}$. D'où
$$\int \frac{\tan x}{1 + \sin^2 x}\,dx = -\frac{1}{2}\ln|\cos x| + \frac{1}{4}\ln(1 + \sin^2 x) + C$$
(car $2 - \cos^2 x = 1 + \sin^2 x$).
- b) $t = \tanh\frac{x}{2}$ : $\frac{1}{6}\arctan\left(\frac{3}{2}\tanh\frac{x}{2}\right) + C$.
- c) Invariance par $x \mapsto \pi + x$ : $t = \tan x$, $\frac{dx}{\cos^4 x} = (1 + t^2)\,dt$, donc $\tan x + \frac{\tan^3 x}{3} + C$.
- d) $\sin^2 x - \cos^2 x = -\cos 2x$, donc $\int = -\frac{1}{2}\int \frac{du}{\cos u}$ ($u = 2x$). Avec $t = \tan\frac{u}{2} = \tan x$ : $\int \frac{du}{\cos u} = \int \frac{2\,dt}{1 - t^2}$, d'où
$$\int \frac{dx}{\sin^2 x - \cos^2 x} = -\frac{1}{2}\ln\left|\frac{1 + \tan x}{1 - \tan x}\right| + C \quad \left(= -\operatorname{argth}(\tan x) \text{ si } |\tan x| < 1\right).$$
:::

:::warning[Erreur dans le corrigé (exercice 10 a)]
Le corrigé écrit la décomposition puis intègre **sans le signe moins** venant de $dt = -\sin x\,dx$, et écrit $\ln|1 - t^2|$ au lieu de $\ln|2 - t^2|$. Sa réponse $\frac{1}{2}\ln|\cos x| - \frac{1}{4}\ln\sin^2 x$ ne redonne pas l'intégrande quand on la dérive.
:::

## Exercice 11 — Intégrales abéliennes

a) $\int \frac{1}{1 - x}\sqrt{\frac{x}{1 - x}}\,dx$ ; b) $\int \frac{dx}{x - 2 + \sqrt{x^2 - 2x + 2}}$ ; c) $\int \frac{1}{x}\sqrt{\frac{1 - x}{1 + x}}\,dx$.

:::correction
- a) $t = \sqrt{\frac{x}{1 - x}}$, $x = \frac{t^2}{1 + t^2}$, $dx = \frac{2t\,dt}{(1 + t^2)^2}$, $\frac{1}{1 - x} = 1 + t^2$ : $\int \frac{2t^2}{1 + t^2}\,dt = 2t - 2\arctan t$, soit $2\sqrt{\frac{x}{1 - x}} - 2\arctan\sqrt{\frac{x}{1 - x}} + C$.
- b) $a = 1 > 0$ : $\sqrt{x^2 - 2x + 2} = x + t$, $x = \frac{2 - t^2}{2(1 + t)}$. On trouve $\int = \frac{t}{2} + \ln|t| - \frac{1}{2}\ln|1 + t| + C$ avec $t = \sqrt{x^2 - 2x + 2} - x$.
- c) $t = \sqrt{\frac{1 - x}{1 + x}}$, $x = \frac{1 - t^2}{1 + t^2}$, $dx = \frac{-4t\,dt}{(1 + t^2)^2}$ : l'intégrale devient $\int \frac{-4t^2\,dt}{(1 - t^2)(1 + t^2)}$, et
$\frac{-4t^2}{(1 - t^2)(1 + t^2)} = \frac{1}{t - 1} - \frac{1}{t + 1} + \frac{2}{1 + t^2}$. Donc
$$\int \frac{1}{x}\sqrt{\frac{1 - x}{1 + x}}\,dx = \ln\left|\frac{t - 1}{t + 1}\right| + 2\arctan t + C, \qquad t = \sqrt{\frac{1 - x}{1 + x}}.$$
:::

:::warning[Erreur dans le corrigé (exercice 11 c)]
Le corrigé décompose en $\frac{2}{t - 1} - \frac{2}{1 + t} + 4\frac{1 + t}{1 + t^2}$ (coefficients doublés) et obtient $2\ln|t - 1| - 2\ln|t + 1| + 4\arctan t + 2\ln(t^2 + 1)$. En dérivant, on ne retrouve pas l'intégrande. La bonne décomposition est ci-dessus.
:::

## Exercice 12 — Racines de trinômes

a) $\int \sqrt{1 + (x + 2)^2}\,dx$ ; b) $\int \frac{dx}{\sqrt{x^2 + 2x}}$ ; c) $\int \frac{dx}{\sqrt{-9x^2 - 6x + 3}}$ ; d) $\int \frac{2x - 3}{\sqrt{4x - 4x^2}}\,dx$ ; e) $\int \frac{(8x - 3)\,dx}{\sqrt{-4x^2 + 12x - 5}}$.

:::correction
- a) $x + 2 = \sinh t$ : $\int \cosh^2 t\,dt = \frac{t}{2} + \frac{\sinh 2t}{4}$, soit $\frac{1}{2}\operatorname{argsh}(x + 2) + \frac{(x + 2)\sqrt{1 + (x + 2)^2}}{2} + C$.
- b) $x^2 + 2x = (x + 1)^2 - 1$ : $\operatorname{argch}(x + 1) + C$ (pour $x > 0$).
- c) $-9x^2 - 6x + 3 = 4 - (3x + 1)^2$ : $\frac{1}{3}\arcsin\frac{3x + 1}{2} + C$.
- d) $\sqrt{4x - 4x^2} = 2\sqrt{x - x^2}$, et $\frac{2x - 3}{2\sqrt{x - x^2}} = -\frac{1}{2}\cdot\frac{1 - 2x}{\sqrt{x - x^2}} - \frac{1}{\sqrt{x - x^2}}$. Le premier morceau s'intègre en $-\sqrt{x - x^2}$ ; pour le second, $x - x^2 = \frac{1}{4} - \left(x - \frac{1}{2}\right)^2$, donc $\int \frac{dx}{\sqrt{x - x^2}} = \arcsin(2x - 1)$. Au total :
$$\int \frac{2x - 3}{\sqrt{4x - 4x^2}}\,dx = -\sqrt{x - x^2} - \arcsin(2x - 1) + C.$$
- e) $-4x^2 + 12x - 5 = 4 - (2x - 3)^2$ et $8x - 3 = -(-8x + 12) + 9$ : $-2\sqrt{-4x^2 + 12x - 5} + \frac{9}{2}\arcsin\left(x - \frac{3}{2}\right) + C$.
:::

:::warning[Erreur dans le corrigé (exercice 12 d)]
Le corrigé obtient $-\frac{1}{2}\sqrt{x - x^2} - \frac{1}{4}\arcsin(2x + 1)$ : il oublie le facteur $2$ de $\sqrt{4x - 4x^2} = 2\sqrt{x - x^2}$ dans une partie du calcul et écrit $2x + 1$ au lieu de $2x - 1$ dans la forme canonique. (Indice qui ne trompe pas : $\arcsin(2x + 1)$ n'est défini que pour $x \in [-1, 0]$, alors que l'intégrande vit sur $]0, 1[$.)
:::

## Exercice 13 — Changements de variable en cascade

a) $I(t) = \int \frac{dt}{(1 + t)(2 + t)}$ ; b) $J(t) = \int \frac{\ln(1 + t)}{(2 + t)^2}\,dt$, puis $K(x) = \int \frac{e^{-x}\ln(1 + e^x)}{(1 + 2e^{-x})^2}\,dx$ ; c) $M(\theta) = \int \frac{d\theta}{(\cos\theta + \sin\theta)(2\cos\theta + \sin\theta)}$.

:::correction
- a) $\frac{1}{(1 + t)(2 + t)} = \frac{1}{1 + t} - \frac{1}{2 + t}$ : $I(t) = \ln|1 + t| - \ln|2 + t| + C$.
- b) IPP, $u = \ln(1 + t)$, $v' = \frac{1}{(2 + t)^2}$, $v = -\frac{1}{2 + t}$ : $J(t) = -\frac{\ln(1 + t)}{2 + t} + I(t)$. Pour $K$, $t = e^x$ : $\frac{e^{-x}}{(1 + 2e^{-x})^2} = \frac{e^x}{(e^x + 2)^2}$ et $dx = \frac{dt}{t}$, donc $K(x) = J(e^x)$.
- c) On divise numérateur et dénominateur par $\cos^2\theta$ (invariance par $\theta \mapsto \pi + \theta$, donc $t = \tan\theta$) : $M(\theta) = \int \frac{dt}{(1 + t)(2 + t)} = I(\tan\theta) = \ln\left|\frac{1 + \tan\theta}{2 + \tan\theta}\right| + C$.
:::

## Exercice 14 — Intégrales définies

1. Calculer $\int_{-1}^{0} \frac{x^2 - 1}{2x - 1}\,dx$. En déduire $\int_{-\pi/2}^{0} \frac{\cos^3 x}{1 - 2\sin x}\,dx$.
2. a) Calculer $I = \int \frac{dx}{x(x^2 - 1)}$ et $J = \int \frac{2x\,dx}{(x^2 - 1)^2}$. b) En déduire $\int_2^3 \frac{2x}{(x^2 - 1)^2}\ln x\,dx$ sous la forme $a\ln 2 + b\ln 3$.

:::correction
**1.** $\frac{x^2 - 1}{2x - 1} = \frac{x}{2} + \frac{1}{4} - \frac{3/4}{2x - 1}$, donc
$$\int_{-1}^{0} \frac{x^2 - 1}{2x - 1}\,dx = \left[\frac{x^2}{4} + \frac{x}{4} - \frac{3}{8}\ln|2x - 1|\right]_{-1}^{0} = \frac{3}{8}\ln 3.$$
Avec $u = \sin x$ ($du = \cos x\,dx$, $\cos^2 x = 1 - u^2$, bornes $-1 \to 0$) : $\int_{-\pi/2}^{0} \frac{\cos^3 x}{1 - 2\sin x}\,dx = \int_{-1}^{0} \frac{1 - u^2}{1 - 2u}\,du = \frac{3}{8}\ln 3$ (c'est la même fraction).

**2. a)** $\frac{1}{x(x^2 - 1)} = -\frac{1}{x} + \frac{1/2}{x + 1} + \frac{1/2}{x - 1}$, donc $I = -\ln|x| + \frac{1}{2}\ln|x + 1| + \frac{1}{2}\ln|x - 1| + C$. Et $J = -\frac{1}{x^2 - 1} + C$ ($u' u^{-2}$).

**b)** IPP avec $u = \ln x$, $v = -\frac{1}{x^2 - 1}$ :
$$\int_2^3 \frac{2x\ln x}{(x^2 - 1)^2}\,dx = \left[-\frac{\ln x}{x^2 - 1}\right]_2^3 + \int_2^3 \frac{dx}{x(x^2 - 1)} = -\frac{13}{8}\ln 3 + \frac{17}{6}\ln 2.$$
:::

## Exercice 15 — Intégrales de Wallis

Pour $n \in \mathbb{N}$, $I_n = \int_0^{\pi/2} \sin^n x\,dx$.
1) Calculer $I_0$ et $I_1$. 2) Relation entre $I_n$ et $I_{n+2}$. 3) Formules de $I_{2p}$ et $I_{2p+1}$. 4) Montrer $I_{2p+1} \le I_{2p} \le I_{2p-1}$ et en déduire $\frac{I_{2p}}{I_{2p+1}} \to 1$. 5) Formule de Wallis. 6) $I_n \sim \sqrt{\frac{\pi}{2n}}$.

:::correction
1) $I_0 = \frac{\pi}{2}$, $I_1 = \big[-\cos x\big]_0^{\pi/2} = 1$.

2) IPP sur $I_{n+2} = \int \sin^{n+1}x \cdot \sin x\,dx$ avec $v = -\cos x$ : le terme de bord est nul et il reste $(n + 1)\int \sin^n x\cos^2 x\,dx = (n + 1)(I_n - I_{n+2})$. Donc
$$I_{n+2} = \frac{n + 1}{n + 2}\,I_n.$$

3) Par récurrence :
$$I_{2p} = \frac{(2p - 1)(2p - 3)\cdots 1}{2p(2p - 2)\cdots 2}\cdot\frac{\pi}{2}, \qquad I_{2p+1} = \frac{2p(2p - 2)\cdots 2}{(2p + 1)(2p - 1)\cdots 3}.$$

4) Sur $\left[0, \frac{\pi}{2}\right]$, $0 \le \sin x \le 1$, donc $\sin^{2p+1} x \le \sin^{2p} x \le \sin^{2p-1} x$ ; on intègre. Puis $1 \le \frac{I_{2p}}{I_{2p+1}} \le \frac{I_{2p-1}}{I_{2p+1}} = \frac{2p + 1}{2p} \to 1$ (relation du 2), et les gendarmes concluent.

5) $\frac{I_{2p}}{I_{2p+1}} = \frac{\pi}{2}(2p + 1)\left[\frac{(2p - 1)(2p - 3)\cdots 1}{2p(2p - 2)\cdots 2}\right]^2 \to 1$, ce qui donne la **formule de Wallis** :
$$\lim_{p \to +\infty} \frac{1}{p}\left[\frac{2p(2p - 2)\cdots 2}{(2p - 1)(2p - 3)\cdots 1}\right]^2 = \pi.$$

6) La suite $n \mapsto (n + 1)I_n I_{n+1}$ est constante (relation du 2) et vaut $I_0 I_1 = \frac{\pi}{2}$. Comme $I_n \sim I_{n+1}$ (question 4 généralisée), $I_n^2 \sim \frac{\pi}{2n}$, donc $I_n \sim \sqrt{\frac{\pi}{2n}}$.
:::

::item{id="td1-integration"}
