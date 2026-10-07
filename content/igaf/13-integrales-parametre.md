---
title: Ch5 — Intégrales à paramètre
summary: "Fonctions définies par une intégrale F(x) = ∫ f(x, t) dt : théorème de continuité, de dérivation (Leibniz) et des dérivées successives sous le signe intégrale, domination locale ; fonction Gamma, transformées de Laplace et de Fourier."
tags: [chapitre 5, intégrales à paramètre, Leibniz, Gamma, Laplace, Fourier]
minutes: 90
---

## 1. Objectifs

Une **intégrale à paramètre** définit une fonction :
$$F(x) = \int_J f(x, t)\,dt,$$
où $t$ est la variable d'intégration (sur un intervalle $J$) et $x$ un **paramètre** (dans un intervalle $I$). Exemple : $\int_0^{+\infty}e^{-xt}\,dt = \frac{1}{x}$ pour $x > 0$. Questions :

- $F$ est-elle **bien définie** (l'intégrale converge-t-elle pour chaque $x$) ?
- $F$ est-elle **continue** ? **dérivable** ? Peut-on **dériver sous le signe intégrale** : $F'(x) = \int_J \frac{\partial f}{\partial x}(x, t)\,dt$ ?

Ce sont les mêmes questions qu'au chapitre précédent (échanger une limite et une intégrale), avec la même réponse : une **hypothèse de domination**.

:::intuition[Pourquoi c'est utile]
Les grandes transformations de l'ingénieur sont des intégrales à paramètre : **Laplace** $\mathcal{L}\{f\}(s) = \int_0^{+\infty}f(t)e^{-st}\,dt$ (automatique, équations différentielles), **Fourier** $\hat f(\omega) = \int_{\mathbb{R}}f(t)e^{-i\omega t}\,dt$ (signal). Savoir les dériver sous l'intégrale permet par exemple de calculer des intégrales qui n'ont pas de primitive explicite ($\int_0^{+\infty}\frac{\sin t}{t}\,dt$, $\int_0^{+\infty}e^{-t^2}\,dt$).
:::

## 2. Continuité sous le signe intégrale

:::theorem[Continuité]
On suppose :
1. pour tout $t \in J$, $x \mapsto f(x, t)$ est **continue** sur $I$ ;
2. pour tout $x \in I$, $t \mapsto f(x, t)$ est **continue par morceaux** sur $J$ ;
3. **domination** : il existe $\varphi : J \to \mathbb{R}_+$ continue par morceaux et **intégrable** sur $J$ telle que $|f(x, t)| \le \varphi(t)$ pour tous $x \in I$, $t \in J$.

Alors $F : x \mapsto \int_J f(x, t)\,dt$ est **bien définie et continue** sur $I$.
:::

:::method[La domination locale]
La continuité est une propriété **locale** : il suffit de dominer sur **tout segment** $[a, b] \subset I$ (avec une $\varphi_{a,b}$ qui peut dépendre de $a$ et $b$). C'est indispensable quand aucune domination ne marche sur tout $I$, par exemple sur $I = ]0, +\infty[$ (voir Gamma et Laplace ci-dessous).
:::

:::example[Fonction Gamma : Γ(x) = ∫₀^∞ e^{-t} t^{x-1} dt]
- **Domaine.** En $+\infty$ : $t^2\cdot e^{-t}t^{x-1} \to 0$, convergence pour tout $x$. En $0$ : $e^{-t}t^{x-1} \sim t^{x-1} = \frac{1}{t^{1-x}}$, convergence $\iff 1 - x < 1 \iff x > 0$. Donc $\Gamma$ est définie sur $]0, +\infty[$.
- **Continuité.** Sur un segment $[a, b] \subset ]0, +\infty[$ : pour $t \in ]0, 1]$, $t^{x-1} \le t^{a-1}$ ; pour $t \ge 1$, $t^{x-1} \le t^{b-1}$. Donc $|f(x, t)| \le \varphi(t) = e^{-t}\left(t^{a-1} + t^{b-1}\right)$, intégrable. $\Gamma$ est continue sur $[a, b]$, donc sur $]0, +\infty[$.
- **Relation fonctionnelle** (IPP) : $\Gamma(x + 1) = x\,\Gamma(x)$, d'où $\Gamma(n) = (n - 1)!$ ; et $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$.
:::

## 3. Dérivation sous le signe intégrale (Leibniz)

:::theorem[Leibniz]
On suppose :
1. pour tout $t \in J$, $x \mapsto f(x, t)$ est de classe $\mathcal{C}^1$ sur $I$ ;
2. pour tout $x \in I$, $t \mapsto f(x, t)$ est **intégrable** sur $J$, et $t \mapsto \frac{\partial f}{\partial x}(x, t)$ est continue par morceaux sur $J$ ;
3. **domination de la dérivée** : il existe $\psi$ intégrable sur $J$ telle que $\left|\frac{\partial f}{\partial x}(x, t)\right| \le \psi(t)$ pour tous $x \in I$, $t \in J$ (ou sur tout segment de $I$).

Alors $F$ est de classe $\mathcal{C}^1$ sur $I$ et
$$F'(x) = \int_J \frac{\partial f}{\partial x}(x, t)\,dt.$$
:::

:::theorem[Dérivées successives]
Si $x \mapsto f(x, t)$ est $\mathcal{C}^n$, si $t \mapsto \frac{\partial^k f}{\partial x^k}(x, t)$ est intégrable pour $k < n$ et continue par morceaux pour $k = n$, et si chaque dérivée $\frac{\partial^k f}{\partial x^k}$ ($1 \le k \le n$) est dominée par une $\varphi_k$ intégrable, alors $F$ est $\mathcal{C}^n$ et $F^{(k)}(x) = \int_J \frac{\partial^k f}{\partial x^k}(x, t)\,dt$. Si c'est vrai pour tout $n$, $F$ est $\mathcal{C}^\infty$.
:::

:::example[Une transformée de Laplace : ∫₀^∞ e^{-xt} dt = 1/x]
$F(x) = \int_0^{+\infty}e^{-xt}\,dt = \frac{1}{x}$ pour $x > 0$. Dériver sous l'intégrale ($\frac{\partial}{\partial x}e^{-xt} = -te^{-xt}$, dominée par $te^{-at}$ sur $[a, +\infty[$) donne $\int_0^{+\infty}te^{-xt}\,dt = \frac{1}{x^2}$, puis par récurrence $\int_0^{+\infty}t^n e^{-xt}\,dt = \frac{n!}{x^{n+1}}$ (c'est $\mathcal{L}\{t^n\}$).
:::

:::example[Transformée de Fourier]
Si $f$ est continue et intégrable sur $\mathbb{R}$, $\hat f(\omega) = \int_{\mathbb{R}}f(t)e^{-i\omega t}\,dt$ est **continue** (domination $|f(t)e^{-i\omega t}| = |f(t)|$). Si de plus $t f(t)$ est intégrable, $\hat f$ est $\mathcal{C}^1$ et $\hat f'(\omega) = -i\,\widehat{tf}(\omega)$ (domination par $|t f(t)|$). Si tous les $t^k f(t)$ sont intégrables, $\hat f$ est $\mathcal{C}^\infty$ : **plus $f$ décroît vite, plus $\hat f$ est régulière**.
:::

::item{id="param-theoremes"}

## 4. Les grandes intégrales obtenues par cette méthode

:::key[À connaître (démontrées dans le TD)]
| intégrale | valeur | méthode |
|---|---|---|
| $\int_0^{+\infty}e^{-t^2}\,dt$ (Gauss) | $\frac{\sqrt{\pi}}{2}$ | $h = g + f^2$ constante |
| $\int_0^{+\infty}\frac{\sin t}{t}\,dt$ (Dirichlet) | $\frac{\pi}{2}$ | $F(x) = \int \frac{\sin t}{t}e^{-xt}\,dt = \frac{\pi}{2} - \arctan x$ |
| $\int_0^{+\infty}\frac{e^{-at} - e^{-bt}}{t}\,dt$ (Frullani) | $\ln\frac{b}{a}$ | $F'(x) = -\frac{1}{x}$ |
| $\Gamma(n) = \int_0^{+\infty}e^{-t}t^{n-1}\,dt$ | $(n - 1)!$ | IPP |
| $\int_{-\infty}^{+\infty}e^{-\alpha x^2}\,dx$ ($\alpha > 0$) | $\sqrt{\frac{\pi}{\alpha}}$ | Gauss et $u = \sqrt{\alpha}x$ |
:::

::item{id="param-valeurs"}
