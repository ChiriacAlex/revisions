---
title: TD 3 — Suites d'intégrales (corrigé)
summary: "Feuille « Chapitre 2 : Suites d'intégrales » (FR) et « Sequences of Integrals » (EN), distribuées sans corrigé : convergence simple, continuité par morceaux, échange limite-intégrale, convergence dominée et approximation de l'intégrale de Gauss."
kind: td
tags: [TD, convergence simple, continuité par morceaux, convergence dominée, Gauss]
minutes: 180
---

:::note[À propos de ce TD]
La feuille (en français et en anglais) est distribuée **sans corrigé** : tout ce qui suit est rédigé pour ce site, et les limites annoncées ont été vérifiées numériquement. Pour chaque question de convergence dominée, applique les **4 étapes** : limite simple, domination indépendante de $n$, intégrabilité de la dominante, conclusion.
:::

## Question 1-1 — Limites simples

a) $f_n(x) = \frac{x}{n}$, $x \in \mathbb{R}$ ; b) $g_n(x) = \frac{x^2}{n + x^2}$, $x \in \mathbb{R}$ ; c) $h_n(x) = x^n$, $x \in [0, a]$.

:::correction
- a) $x$ fixé : $\frac{x}{n} \to 0$. Limite simple : la fonction **nulle**.
- b) $x$ fixé : $n + x^2 \to +\infty$, donc $g_n(x) \to 0$ (et $g_n(0) = 0$). Limite **nulle**.
- c) Cela dépend de $a > 0$ :
  - si $a < 1$ : $x^n \to 0$ pour tout $x \in [0, a]$, limite **nulle** ;
  - si $a = 1$ : limite $0$ sur $[0, 1[$ et $1$ en $x = 1$ (fonction **discontinue**) ;
  - si $a > 1$ : pour $x > 1$, $x^n \to +\infty$ : **pas** de limite simple (finie) sur $[0, a]$.
:::

## Question 2-2 — Continuité par morceaux

Pour chaque fonction : points de discontinuité, limites latérales, conclusion.
a) $\lfloor x\rfloor$ sur $[0, 5]$ ; b) $x + 1$ sur $[-1, 0[$, $2$ en $0$, $x^2$ sur $]0, 1]$ ; c) $\sin\frac{1}{x}$ sur $]0, 1]$ et $0$ en $0$ ; d) $x\sin\frac{1}{x}$ sur $[-1, 1] \setminus \{0\}$ et $0$ en $0$ ; e) (bonus) $1$ sur $\mathbb{Q}$, $0$ ailleurs, sur $[0, 1]$.

:::correction
- a) Discontinuités en $1, 2, 3, 4$ (limite $k - 1$ à gauche, $k$ à droite) et en $5$ (limite $4$ à gauche, $f(5) = 5$). Limites finies : **continue par morceaux**.
- b) (L'énoncé écrit « $-1 \ge x < 0$ » : il faut lire $-1 \le x < 0$.) En $0$ : limite à gauche $1$, à droite $0$, et $f(0) = 2$. Une seule discontinuité, limites finies : **continue par morceaux**.
- c) Avec l'indice : $u_n = \frac{1}{\pi/2 + 2n\pi} \to 0^+$ et $v_n = \frac{1}{3\pi/2 + 2n\pi} \to 0^+$, mais $f(u_n) = 1$ et $f(v_n) = -1$. Donc $\lim_{0^+}f$ n'existe pas : **pas continue par morceaux** sur $[0, 1]$.
- d) $\left|x\sin\frac{1}{x}\right| \le |x| \to 0 = f(0)$ : $f$ est **continue** sur $[-1, 1]$, donc continue par morceaux.
- e) Tout intervalle contient des rationnels et des irrationnels : $f$ n'a de limite **nulle part** (voir 2-3). **Pas continue par morceaux.**
:::

## Question 2-3 — La fonction de Dirichlet

$f = 1$ sur $\mathbb{Q} \cap [0, 1]$, $0$ ailleurs. 1) $f\left(\frac{1}{2}\right)$, $f\left(\frac{3}{4}\right)$, $f\left(\frac{\sqrt{2}}{2}\right)$. 2) Une suite de rationnels $r_n \to \frac{1}{2}$. 3) Une suite d'irrationnels $s_n \to \frac{1}{2}$. 4) $f(r_n)$ et $f(s_n)$. 5) $f$ a-t-elle une limite en $\frac{1}{2}$ ? 6) Est-elle continue par morceaux ?

:::correction
1) $f\left(\frac{1}{2}\right) = 1$, $f\left(\frac{3}{4}\right) = 1$, $f\left(\frac{\sqrt{2}}{2}\right) = 0$ ($\sqrt{2}$ est irrationnel).
2) $r_n = \frac{1}{2} + \frac{1}{n + 2}$ : rationnels, dans $[0, 1]$, de limite $\frac{1}{2}$.
3) $s_n = \frac{1}{2} + \frac{\sqrt{2}}{4n}$ : irrationnels (rationnel + irrationnel non nul), dans $[0, 1]$, de limite $\frac{1}{2}$.
4) $f(r_n) = 1 \to 1$ et $f(s_n) = 0 \to 0$.
5) **Non** : deux suites tendant vers $\frac{1}{2}$ ont des images de limites différentes (le même raisonnement vaut en tout point, et pour les limites latérales).
6) **Non** : les limites latérales n'existent en aucun point.
:::

## Question 3-4 — Un cas où l'échange marche

$f_n(x) = x^n$ sur $[0, 1]$. 1) Limite simple. 2) $\int_0^1 x^n\,dx$. 3) Comparer $\lim\int$ et $\int\lim$.

:::correction
1) $f = 0$ sur $[0, 1[$, $f(1) = 1$.
2) $\int_0^1 x^n\,dx = \frac{1}{n + 1}$.
3) $\lim_n \frac{1}{n + 1} = 0$ et $\int_0^1 f = 0$ (une valeur en un point ne change rien) : **égalité**. Le TCD l'explique : $|x^n| \le 1$, intégrable sur le segment.
:::

## Question 3-5 — La masse qui se concentre

$f_n(x) = n$ si $0 < x \le \frac{1}{n}$, $0$ si $x > \frac{1}{n}$. 1) Limite simple. 2) $\int_0^1 f_n$. 3) Peut-on échanger ?

:::correction
1) $x > 0$ fixé : dès que $n > \frac{1}{x}$, $f_n(x) = 0$. Limite simple **nulle**.
2) $\int_0^1 f_n = n \times \frac{1}{n} = 1$.
3) **Non** : $\lim\int f_n = 1 \ne 0 = \int\lim f_n$. Aucune fonction intégrable ne domine les $f_n$ : la plus petite majorante, $\sup_n f_n(x) \approx \frac{1}{x}$, n'est pas intégrable en $0$.
:::

## Question 3-6 — (n + 1) xⁿ

$f_n(x) = (n + 1)x^n$ sur $[0, 1[$ et $f_n(1) = 0$. 1) $\int_0^1 f_n$. 2) Limite simple $0$. 3) A-t-on $\lim\int = \int\lim$ ?

:::correction
1) $\int_0^1 (n + 1)x^n\,dx = 1$.
2) Pour $0 \le x < 1$, $(n + 1)x^n \to 0$ (croissances comparées : $x^n$ décroît géométriquement) ; et $f_n(1) = 0$. Limite **nulle**.
3) **Non** : $1 \ne 0$. La masse se concentre près de $x = 1$ ; $\sup_n f_n$ n'est pas intégrable, le TCD ne s'applique pas.
:::

::item{id="tds-echange"}

## Question 4-7 — Une domination simple

$f_n(x) = \frac{e^{-x}}{n}$ sur $[0, +\infty[$. 1) Limite simple. 2) $|f_n| \le e^{-x}$. 3) $\lim_n\int_0^{+\infty}f_n$.

:::correction
1) $f_n(x) \to 0$.
2) Pour $n \ge 1$, $\frac{1}{n} \le 1$, donc $0 \le f_n(x) \le e^{-x}$.
3) $e^{-x}$ est intégrable sur $[0, +\infty[$ : par le TCD, $\lim\int f_n = \int 0 = 0$. (Vérification directe : $\int_0^{+\infty}f_n = \frac{1}{n} \to 0$.)
:::

## Question 4-8 — Limites par convergence dominée

a) $\lim\int_0^{+\infty}\frac{\sin x}{n + x^2}\,dx$ ; b) $\lim\int_0^{+\infty}\frac{dt}{t^n + e^t}$ ; c) $\lim\int_0^{\pi/2}\sin^n x\,dx$ ; d) $\lim\int_0^{+\infty}\frac{dt}{(1 + t^2)^n}$ ; d\*\*) $\lim\int_0^{+\infty}\frac{n\ln\left(1 + \frac{x}{n}\right)}{(1 + x^2)^2}\,dx$ ; e\*\*) $\lim\int_0^{+\infty}\frac{\sin(t/n)}{t(1 + t^2)}\,dt$.

:::correction
- **a)** Limite simple : $0$. Domination (pour $n \ge 1$) : $\left|\frac{\sin x}{n + x^2}\right| \le \frac{1}{1 + x^2}$, intégrable. **Limite $0$.**
- **b)** Limite simple $e^{-t}\mathbb{1}_{[0, 1[}$ ; domination $\frac{1}{t^n + e^t} \le e^{-t}$. **Limite $1 - \frac{1}{e} \approx 0{,}632$.**
- **c)** Limite simple $0$ sur $\left[0, \frac{\pi}{2}\right[$ ; domination par $1$ sur un segment. **Limite $0$.**
- **d)** Pour $t > 0$, $(1 + t^2)^n \to +\infty$ : limite simple $0$ (sauf en $t = 0$). Domination (pour $n \ge 1$) : $\frac{1}{(1 + t^2)^n} \le \frac{1}{1 + t^2}$, intégrable. **Limite $0$.**
- **d\*\*)** Limite simple : $n\ln\left(1 + \frac{x}{n}\right) \to x$ (car $\ln(1 + u) \sim u$). Domination : $\ln(1 + u) \le u$ donne $0 \le n\ln\left(1 + \frac{x}{n}\right) \le x$, donc $|f_n(x)| \le \frac{x}{(1 + x^2)^2}$, intégrable ($\sim \frac{1}{x^3}$ en $+\infty$). Par le TCD :
$$\lim = \int_0^{+\infty}\frac{x\,dx}{(1 + x^2)^2} = \left[-\frac{1}{2(1 + x^2)}\right]_0^{+\infty} = \frac{1}{2}.$$
- **e\*\*)** Limite simple : $\sin\frac{t}{n} \to 0$. Domination : $\left|\sin\frac{t}{n}\right| \le \frac{t}{n} \le t$, donc $|f_n(t)| \le \frac{1}{1 + t^2}$, intégrable. **Limite $0$.**
(Plus précis : $n\sin\frac{t}{n} \to t$ avec la même domination, donc $n\int f_n \to \int_0^{+\infty}\frac{dt}{1 + t^2} = \frac{\pi}{2}$ : l'intégrale se comporte comme $\frac{\pi}{2n}$.)
:::

::item{id="tds-tcd"}

## Question 5-9 — Approximation de l'intégrale de Gauss

$f_n(x) = \left(1 - \frac{x^2}{n^2}\right)^{n^2}$ si $x \in [0, n]$, $0$ sinon. Avec $1 - u \le e^{-u}$, montrer que $\lim\int_0^{+\infty}f_n = \int_0^{+\infty}e^{-x^2}\,dx$.

:::correction
**Limite simple.** $x \ge 0$ fixé : pour $n > x$, $f_n(x) = \exp\left(n^2\ln\left(1 - \frac{x^2}{n^2}\right)\right)$ et $n^2\ln\left(1 - \frac{x^2}{n^2}\right) \to -x^2$ (car $\ln(1 - u) \sim -u$). Donc $f_n(x) \to e^{-x^2}$.

**Domination.** Pour $x \in [0, n]$, $u = \frac{x^2}{n^2} \in [0, 1]$, donc $0 \le 1 - u \le e^{-u}$ ; en élevant à la puissance $n^2$ (tout est positif) : $0 \le f_n(x) \le e^{-n^2u} = e^{-x^2}$. Hors de $[0, n]$, $f_n = 0 \le e^{-x^2}$. Donc $|f_n| \le e^{-x^2}$ pour tout $n$.

**Intégrabilité.** $e^{-x^2} \le e^{-x}$ pour $x \ge 1$ : intégrable sur $[0, +\infty[$.

**Conclusion (TCD).** $\lim_n\int_0^{+\infty}f_n(x)\,dx = \int_0^{+\infty}e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}$ (valeur calculée dans le TD des intégrales à paramètre).
:::
