---
title: TD 2 — Espérance et variance (corrigé)
summary: Feuille « PBS 1 — II. Espérance et variance » entièrement corrigée — densité en 3/x⁴, lois sans espérance ou sans variance, uniforme, exponentielle, normale, Tchebychev et convergence en probabilité.
kind: td
tags: [TD, espérance, variance, lois usuelles, Tchebychev]
minutes: 120
---

:::note[Comment travailler ce TD]
Les questions marquées (TD1) dans l'énoncé reprennent des calculs du TD précédent (fonctions de répartition, densités) : elles sont corrigées dans le [TD lois continues](../td-lois-continues/). Ici on se concentre sur les **espérances et variances**. Méthode générale : $E[X] = \int x f$, puis $E[X^2] = \int x^2 f$, puis König-Huygens.
:::

## Exercice 1 — Espérance et variance

1. Soit $X$ de densité $f(x) = \frac{3}{x^4}$ si $x \ge 1$, $0$ sinon. Déterminer l'espérance, la variance et l'écart-type de $X$.
2. Imaginer une densité $g$ telle qu'une variable $Y$ de densité $g$ n'ait **pas d'espérance**.
3. Imaginer une densité $h$ telle qu'une variable $Z$ de densité $h$ ait une espérance mais **pas de variance**.

:::hint[Indice]
Tout repose sur $\int_1^{+\infty} \frac{dx}{x^\alpha}$, qui converge si et seulement si $\alpha > 1$ (et vaut alors $\frac{1}{\alpha - 1}$).
:::

:::correction
**1.** (C'est bien une densité : positive et $\int_1^{+\infty} \frac{3}{x^4}dx = \left[-\frac{1}{x^3}\right]_1^{+\infty} = 1$.)
$$E[X] = \int_1^{+\infty} x \cdot \frac{3}{x^4}\,dx = \int_1^{+\infty} \frac{3}{x^3}\,dx = \left[-\frac{3}{2x^2}\right]_1^{+\infty} = \frac{3}{2},$$
$$E[X^2] = \int_1^{+\infty} \frac{3}{x^2}\,dx = \left[-\frac{3}{x}\right]_1^{+\infty} = 3.$$
Donc $V(X) = 3 - \frac{9}{4} = \frac{3}{4}$ et $\sigma(X) = \frac{\sqrt{3}}{2} \approx 0{,}866$.

**2.** $g(x) = \frac{1}{x^2}$ si $x \ge 1$, $0$ sinon : c'est une densité ($\int_1^{+\infty} \frac{dx}{x^2} = 1$), mais $\int_1^{+\infty} x \cdot \frac{1}{x^2}\,dx = \int_1^{+\infty} \frac{dx}{x} = +\infty$ : $Y$ n'a pas d'espérance. (Autre exemple classique : la loi de Cauchy, $g(x) = \frac{1}{\pi(1 + x^2)}$ sur $\mathbb{R}$.)

**3.** $h(x) = \frac{2}{x^3}$ si $x \ge 1$, $0$ sinon : densité ($\int_1^{+\infty} \frac{2}{x^3}dx = 1$), $E[Z] = \int_1^{+\infty} \frac{2}{x^2}dx = 2$ existe, mais $E[Z^2] = \int_1^{+\infty} \frac{2}{x}\,dx = +\infty$ : pas de variance.

*Morale :* la famille $\frac{\alpha - 1}{x^\alpha}$ sur $[1, +\infty[$ a une espérance si $\alpha > 2$ et une variance si $\alpha > 3$.
:::

::item{id="td2ev-ex1"}

## Exercice 2 — Loi uniforme

1. Soit $Z \sim \mathcal{U}(0, 1)$. (a) Donner une densité de $Z$. (b) Déterminer l'espérance, la variance et l'écart-type de $Z$.
2. Soient $a < b$ et $X \sim \mathcal{U}([a, b])$. (a) Donner une densité de $X$. (b) Donner une densité de $\frac{X - a}{b - a}$. (c) En déduire l'espérance, la variance et l'écart-type de $X$.

:::correction
**1.** (a) $f_Z(x) = 1$ si $x \in [0, 1]$, $0$ sinon.
(b) $E[Z] = \int_0^1 x\,dx = \frac{1}{2}$, $E[Z^2] = \int_0^1 x^2\,dx = \frac{1}{3}$, donc $V(Z) = \frac{1}{3} - \frac{1}{4} = \frac{1}{12}$ et $\sigma(Z) = \frac{1}{\sqrt{12}} = \frac{1}{2\sqrt{3}} \approx 0{,}289$.

**2.** (a) $f_X(x) = \frac{1}{b - a}$ sur $[a, b]$, $0$ sinon.
(b) Pour $t \in [0, 1]$ : $P\left(\frac{X - a}{b - a} \le t\right) = P(X \le a + (b - a)t) = t$ ; donc $\frac{X - a}{b - a} \sim \mathcal{U}(0, 1)$, de densité $1$ sur $[0, 1]$.
(c) On écrit $X = a + (b - a)Z$ avec $Z \sim \mathcal{U}(0, 1)$. Par linéarité et par $V(\alpha Z + \beta) = \alpha^2 V(Z)$ :
$$E[X] = a + \frac{b - a}{2} = \frac{a + b}{2}, \qquad V(X) = \frac{(b - a)^2}{12}, \qquad \sigma(X) = \frac{b - a}{2\sqrt{3}}.$$
L'espérance est le milieu de l'intervalle ; la dispersion ne dépend que de sa longueur.
:::

## Exercice 3 — Loi exponentielle

1. Soit $Z \sim \mathcal{E}(1)$. (a) Donner une densité de $Z$. (b) Déterminer l'espérance, la variance et l'écart-type de $Z$.
2. Soient $\lambda > 0$ et $X \sim \mathcal{E}(\lambda)$. (a) Donner une densité de $X$. (b) Déterminer $\alpha \in \mathbb{R}$ tel que $\alpha X \sim \mathcal{E}(1)$. (c) En déduire $E(X)$, $V(X)$ et $\sigma(X)$.

:::hint[Indice]
Intégrations par parties : $\int_0^{+\infty} x e^{-x}dx$ et $\int_0^{+\infty} x^2 e^{-x}dx$ (on dérive la puissance de $x$, on intègre $e^{-x}$).
:::

:::correction
**1.** (a) $f_Z(x) = e^{-x}$ si $x \ge 0$, $0$ sinon.
(b) Par parties : $E[Z] = \int_0^{+\infty} x e^{-x}dx = \left[-x e^{-x}\right]_0^{+\infty} + \int_0^{+\infty} e^{-x}dx = 0 + 1 = 1$. Puis $E[Z^2] = \left[-x^2 e^{-x}\right]_0^{+\infty} + \int_0^{+\infty} 2x e^{-x}dx = 2E[Z] = 2$. Donc $V(Z) = 2 - 1 = 1$ et $\sigma(Z) = 1$.

**2.** (a) $f_X(x) = \lambda e^{-\lambda x}$ si $x \ge 0$, $0$ sinon.
(b) Prenons $\alpha = \lambda$. Pour $t \ge 0$ : $P(\lambda X \le t) = P\left(X \le \frac{t}{\lambda}\right) = 1 - e^{-\lambda \cdot t/\lambda} = 1 - e^{-t}$ (et $0$ si $t < 0$) : $\lambda X \sim \mathcal{E}(1)$. ($\lambda$ n'est qu'un changement d'unité de temps.)
(c) $X = \frac{1}{\lambda} Z$ avec $Z = \lambda X \sim \mathcal{E}(1)$ :
$$E[X] = \frac{1}{\lambda}, \qquad V(X) = \frac{1}{\lambda^2}, \qquad \sigma(X) = \frac{1}{\lambda}.$$
Pour l'exponentielle, l'écart-type est égal à l'espérance.
:::

::item{id="td2ev-ex2-ex3"}

## Exercice 4 — Loi normale

Soit $Z$ de densité $\varphi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$.

1. *(TD1)* Exprimer sa fonction de répartition sous forme intégrale ; on la note $\Phi$.
2. *(TD1)* Expliquer pourquoi, pour tout $\beta > 0$, $\Phi(-\beta) = 1 - \Phi(\beta)$. On admet que $\Phi(-1{,}96) = 1 - \Phi(1{,}96) = 0{,}025$.
3. Déterminer l'espérance et la variance de $Z$.
4. Soient $(m, \sigma) \in \mathbb{R} \times \mathbb{R}_+^*$ et $X = m + \sigma Z$. (a) *(TD1)* Exprimer $F_X$ avec $\Phi$, puis la densité de $X$. (b) *(TD1)* Donner un intervalle de prédiction bilatéral à 95 %. (c) Trouver l'espérance et la variance de $X$.

:::correction
**1.** $\Phi(x) = \int_{-\infty}^x \frac{1}{\sqrt{2\pi}} e^{-t^2/2}\,dt$.

**2.** $\varphi$ est paire : avec $u = -t$, $\Phi(-\beta) = \int_{-\infty}^{-\beta} \varphi(t)\,dt = \int_\beta^{+\infty} \varphi(u)\,du = 1 - \Phi(\beta)$. Les deux queues ont la même aire.

**3.** **Espérance.** $x\varphi(x)$ est **impaire** et intégrable ($|x|\varphi(x)$ décroît très vite), donc $E[Z] = \int_{-\infty}^{+\infty} x\varphi(x)\,dx = 0$. (Directement : une primitive de $x\varphi(x)$ est $-\varphi(x)$, qui tend vers $0$ en $\pm\infty$.)
**Variance.** Par parties, avec $u = x$ et $v' = x\varphi(x)$ (donc $v = -\varphi(x)$) :
$$E[Z^2] = \int_{-\infty}^{+\infty} x \cdot x\varphi(x)\,dx = \big[-x\varphi(x)\big]_{-\infty}^{+\infty} + \int_{-\infty}^{+\infty} \varphi(x)\,dx = 0 + 1 = 1.$$
Donc $V(Z) = E[Z^2] - E[Z]^2 = 1$.

**4.** (a) Comme $\sigma > 0$ : $F_X(x) = P\left(Z \le \frac{x - m}{\sigma}\right) = \Phi\left(\frac{x - m}{\sigma}\right)$, et en dérivant $f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x - m)^2}{2\sigma^2}}$.
(b) $[m - 1{,}96\sigma ;\ m + 1{,}96\sigma]$ (on résout $F_X(b) = 0{,}975$, et par symétrie pour $a$).
(c) Par linéarité : $E[X] = m + \sigma E[Z] = m$ et $V(X) = \sigma^2 V(Z) = \sigma^2$. Les paramètres de $\mathcal{N}(m, \sigma^2)$ sont exactement l'espérance et la **variance**.
:::

## Exercice 5 — Tchebychev et convergence en probabilité

Soient $X_1, \ldots, X_n$ des variables indépendantes et de même loi, d'espérance $m$ et de variance $\sigma^2$, et $\overline{X}_n = \frac{X_1 + \cdots + X_n}{n}$.

1. Déterminer l'espérance et la variance de $\overline{X}_n$.
2. Montrer que pour tout $\varepsilon > 0$, $P\big(|\overline{X}_n - m| > \varepsilon\big) \xrightarrow[n \to +\infty]{} 0$.

*On dit que $\overline{X}_n$ converge en probabilité vers $m$.*

:::hint[Indice]
Pour 2, utilise l'inégalité de Bienaymé-Tchebychev (chapitre 2, § 7) appliquée à $\overline{X}_n$.
:::

:::correction
**1.** Par linéarité : $E[\overline{X}_n] = \frac{1}{n}\sum_{i=1}^n E[X_i] = \frac{nm}{n} = m$.
Par **indépendance**, la variance d'une somme est la somme des variances, et $V\left(\frac{1}{n}S\right) = \frac{1}{n^2}V(S)$ :
$$V(\overline{X}_n) = \frac{1}{n^2}\sum_{i=1}^n V(X_i) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}.$$
La moyenne a la même espérance que chaque $X_i$, mais une dispersion $n$ fois plus petite.

**2.** Soit $\varepsilon > 0$. Par Bienaymé-Tchebychev appliquée à $\overline{X}_n$ (qui admet une variance) :
$$0 \le P\big(|\overline{X}_n - m| > \varepsilon\big) \le P\big(|\overline{X}_n - m| \ge \varepsilon\big) \le \frac{V(\overline{X}_n)}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2}.$$
Le majorant tend vers $0$ quand $n \to +\infty$ ; par encadrement, $P(|\overline{X}_n - m| > \varepsilon) \to 0$. $\square$

C'est la **loi faible des grands nombres** : la moyenne d'un grand nombre d'essais indépendants se concentre autour de l'espérance, ce qui justifie l'interprétation « $E[X]$ = moyenne à long terme ».
:::

::item{id="td2ev-ex4-ex5"}
