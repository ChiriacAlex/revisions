---
title: TD 4 — Intégrales à paramètre (corrigé)
summary: "Feuille « Chapitre 3 : Intégrales à paramètre » et sa feuille EXTRA, distribuées sans corrigé : fonction Gamma, équation différentielle, taux d'accroissement, Laplace et intégrale de Dirichlet, Fourier, intégrale de Gauss et intégrale de Frullani."
kind: td
tags: [TD, intégrales à paramètre, Gamma, Dirichlet, Gauss, Frullani, Fourier]
minutes: 240
---

:::note[À propos de ce TD]
Les deux feuilles (TD et « EXTRA ») sont distribuées **sans corrigé**. Les valeurs ci-dessous ont été vérifiées numériquement. Réflexe pour chaque question : écrire $f(x, t)$, vérifier la régularité en $x$ et en $t$, puis **trouver la domination** (sur tout $I$, ou sur chaque segment $[a, b] \subset I$).
:::

## Exercice 1 — La fonction Gamma

$\Gamma(x) = \int_0^{+\infty}e^{-t}t^{x-1}\,dt$. a) Domaine de définition. b) $\Gamma(x + 1) = x\Gamma(x)$ pour $x > 0$. c) $\Gamma(n)$ pour $n \in \mathbb{N}^*$. d) Continuité de $\Gamma$ sur $]0, +\infty[$.

:::correction
**a)** Deux points à étudier. En $+\infty$ : $t^2 e^{-t}t^{x-1} = t^{x+1}e^{-t} \to 0$, donc l'intégrande est $o\left(\frac{1}{t^2}\right)$ : converge pour tout $x$. En $0$ : $e^{-t}t^{x-1} \sim \frac{1}{t^{1-x}}$ (positive), converge $\iff 1 - x < 1 \iff x > 0$. **Domaine : $]0, +\infty[$.**

**b)** Sur $[\varepsilon, A]$, IPP avec $u = t^x$, $v = -e^{-t}$ :
$\int_\varepsilon^A t^x e^{-t}\,dt = \big[-t^xe^{-t}\big]_\varepsilon^A + x\int_\varepsilon^A t^{x-1}e^{-t}\,dt$. Le crochet tend vers $0$ ($x > 0$ en $0$ ; croissances comparées en $+\infty$). Donc **$\Gamma(x + 1) = x\,\Gamma(x)$**.

**c)** $\Gamma(1) = \int_0^{+\infty}e^{-t}\,dt = 1$, puis par récurrence $\Gamma(n) = (n - 1)\Gamma(n - 1) = \cdots = (n - 1)!$.

**d)** Domination **locale** sur $[a, b]$ avec $0 < a < b$ : $|e^{-t}t^{x-1}| \le e^{-t}t^{a-1}$ si $t \le 1$ et $\le e^{-t}t^{b-1}$ si $t \ge 1$, donc $\le \varphi(t) = e^{-t}(t^{a-1} + t^{b-1})$, intégrable sur $]0, +\infty[$ (voir a). $\Gamma$ est continue sur chaque $[a, b]$, donc sur $]0, +\infty[$.
(Une domination sur tout $]0, +\infty[$ est impossible : quand $x \to 0$, l'intégrande se comporte comme $\frac{1}{t}$ près de $0$.)
:::

## Exercice 2 — Domination et équation différentielle

a) $F(x) = \int_0^{+\infty}\sin(xt)\,e^{-t^2}\,dt$ : 1) bien définie et continue sur $\mathbb{R}$ ; 2) $\mathcal{C}^1$ ; 3) équation différentielle vérifiée par $F$.
b) $G(x) = \int_0^1 \frac{t^2}{\sqrt{1 + x^4t^2}}\,dt$ : continuité sur $\mathbb{R}$ et $\lim_{x \to 0}G(x)$.

:::correction
**a) 1)** $x \mapsto \sin(xt)e^{-t^2}$ est continue, et $|\sin(xt)e^{-t^2}| \le e^{-t^2}$, intégrable sur $[0, +\infty[$ (indépendante de $x$). $F$ est **définie et continue** sur $\mathbb{R}$.

**2)** $\frac{\partial f}{\partial x}(x, t) = t\cos(xt)e^{-t^2}$, continue, et $|t\cos(xt)e^{-t^2}| \le te^{-t^2}$, intégrable (primitive $-\frac{1}{2}e^{-t^2}$). Par Leibniz, $F$ est $\mathcal{C}^1$ et $F'(x) = \int_0^{+\infty}t\cos(xt)e^{-t^2}\,dt$.

**3)** IPP avec $u = \cos(xt)$, $v = -\frac{1}{2}e^{-t^2}$ :
$$F'(x) = \left[-\frac{1}{2}\cos(xt)e^{-t^2}\right]_0^{+\infty} - \int_0^{+\infty}\frac{x}{2}\sin(xt)e^{-t^2}\,dt = \frac{1}{2} - \frac{x}{2}F(x).$$
$F$ est solution de l'équation différentielle linéaire **$F'(x) + \frac{x}{2}F(x) = \frac{1}{2}$**, avec $F(0) = 0$. (Par variation de la constante : $F(x) = \frac{1}{2}e^{-x^2/4}\int_0^x e^{s^2/4}\,ds$.)

**b)** $(x, t) \mapsto \frac{t^2}{\sqrt{1 + x^4t^2}}$ est continue, et $0 \le \frac{t^2}{\sqrt{1 + x^4t^2}} \le t^2$, intégrable sur le **segment** $[0, 1]$. $G$ est **continue** sur $\mathbb{R}$, donc $\lim_{x \to 0}G(x) = G(0) = \int_0^1 t^2\,dt = \frac{1}{3}$.
:::

## Exercice 3 — Taux d'accroissement

$F(x) = \int_0^\pi \sin(x\sin t)\,dt$. a) $F$ est $\mathcal{C}^1$ sur $\mathbb{R}$ ; $F(0)$ ? b) En déduire $\lim_{x \to 0}\frac{1}{x}\int_0^\pi \sin(x\sin t)\,dt$.

:::correction
**a)** $\frac{\partial f}{\partial x} = \sin t\cos(x\sin t)$, continue en $(x, t)$, et $|\sin t\cos(x\sin t)| \le 1$, intégrable sur le segment $[0, \pi]$. $F$ est $\mathcal{C}^1$, $F'(x) = \int_0^\pi \sin t\cos(x\sin t)\,dt$, et **$F(0) = 0$**.

**b)** C'est un taux d'accroissement : $\frac{1}{x}\int_0^\pi \sin(x\sin t)\,dt = \frac{F(x) - F(0)}{x} \to F'(0) = \int_0^\pi \sin t\,dt = 2$. **Limite : $2$.**
:::

## Exercice 4 — Transformée de Laplace et intégrale de Dirichlet

$F(x) = \int_0^{+\infty}\frac{\sin t}{t}e^{-xt}\,dt$ pour $x > 0$. a) Définition. b) $\mathcal{C}^1$ sur $]0, +\infty[$ et expression de $F'$. c) Calcul de $F'$. d) $\lim_{+\infty}F$. e) Expression de $F$. f) Valeur de $I = \int_0^{+\infty}\frac{\sin t}{t}\,dt$ (en admettant la continuité de $F$ en $0^+$).

:::correction
**a)** $\frac{\sin t}{t} \to 1$ en $0$ : on prolonge par continuité. Et $\left|\frac{\sin t}{t}e^{-xt}\right| \le e^{-xt}$ (car $|\sin t| \le t$), intégrable pour $x > 0$. $F$ est **bien définie**.

**b)** $\frac{\partial f}{\partial x}(x, t) = -\sin t\,e^{-xt}$. Sur $[a, +\infty[$ ($a > 0$) : $|\sin t\,e^{-xt}| \le e^{-at}$, intégrable. Par Leibniz (domination locale), $F$ est $\mathcal{C}^1$ sur $]0, +\infty[$ et $F'(x) = -\int_0^{+\infty}\sin t\,e^{-xt}\,dt$.

**c)** Avec $\int_0^{+\infty}e^{-xt}\sin t\,dt = \operatorname{Im}\int_0^{+\infty}e^{(-x + i)t}\,dt = \operatorname{Im}\frac{1}{x - i} = \frac{1}{1 + x^2}$ (ou deux IPP) : **$F'(x) = -\frac{1}{1 + x^2}$**.

**d)** $|F(x)| \le \int_0^{+\infty}e^{-xt}\,dt = \frac{1}{x} \to 0$. **$\lim_{+\infty}F = 0$.**

**e)** $F(x) = C - \arctan x$ ; la limite en $+\infty$ donne $0 = C - \frac{\pi}{2}$. **$F(x) = \frac{\pi}{2} - \arctan x$.**

**f)** $I = \lim_{x \to 0^+}F(x) = \frac{\pi}{2}$. **$\int_0^{+\infty}\frac{\sin t}{t}\,dt = \frac{\pi}{2}$.**
:::

::item{id="tdp-dirichlet"}

## Exercice 5 — Régularité de la transformée de Fourier

$f$ continue et intégrable sur $\mathbb{R}$, $\hat f(\omega) = \int_{-\infty}^{+\infty}f(t)e^{-i\omega t}\,dt$. a) $\hat f$ est continue. b) Si $g(t) = tf(t)$ est intégrable : $\hat f$ est $\mathcal{C}^1$ et $\hat f'(\omega) = -i\hat g(\omega)$. c) Si tous les $t^kf(t)$ sont intégrables, $\hat f$ est $\mathcal{C}^\infty$ et $\hat f^{(k)}(\omega) = (-i)^k\,\widehat{t^kf}(\omega)$.

:::correction
**a)** $\omega \mapsto f(t)e^{-i\omega t}$ est continue et $|f(t)e^{-i\omega t}| = |f(t)|$, intégrable et indépendante de $\omega$ : $\hat f$ est **continue**.

**b)** $\frac{\partial}{\partial\omega}\left(f(t)e^{-i\omega t}\right) = -itf(t)e^{-i\omega t}$, de module $|tf(t)| = |g(t)|$, intégrable. Par Leibniz : $\hat f'(\omega) = \int -itf(t)e^{-i\omega t}\,dt = -i\,\hat g(\omega)$.

**c)** Récurrence sur $k$ : si $\hat f^{(k)}(\omega) = \int (-it)^kf(t)e^{-i\omega t}\,dt$, on dérive encore sous l'intégrale ; la dérivée $(-it)^{k+1}f(t)e^{-i\omega t}$ est dominée par $|t^{k+1}f(t)|$, intégrable. Donc $\hat f^{(k+1)}(\omega) = (-i)^{k+1}\,\widehat{t^{k+1}f}(\omega)$, et $\hat f \in \mathcal{C}^\infty$.
:::

## Exercice 6 — Une fonction C∞

$I(x) = \int_0^{+\infty}e^{ixt}e^{-t^2}\,dt$ : montrer que $I$ est $\mathcal{C}^\infty$ et exprimer $I^{(k)}$.

:::correction
$\frac{\partial^k}{\partial x^k}\left(e^{ixt}e^{-t^2}\right) = (it)^ke^{ixt}e^{-t^2}$, de module $t^ke^{-t^2}$, intégrable sur $[0, +\infty[$ pour tout $k$ (et indépendant de $x$). Donc $I \in \mathcal{C}^\infty(\mathbb{R})$ et
$$I^{(k)}(x) = i^k\int_0^{+\infty}t^ke^{ixt}e^{-t^2}\,dt.$$
:::

## Exercice EXTRA 1 — L'intégrale de Gauss

$I = \int_0^{+\infty}e^{-t^2}\,dt$, $f(x) = \int_0^x e^{-t^2}\,dt$, $g(x) = \int_0^1 \frac{e^{-(t^2 + 1)x^2}}{1 + t^2}\,dt$. a) $g$ est $\mathcal{C}^1$. b) $h = g + f^2$ vérifie $h' = 0$. c) $h(0)$. d) $\lim_{+\infty}g = 0$. e) $\lim_{+\infty}f^2$, puis $I$.

:::correction
**a)** $\frac{\partial}{\partial x}\frac{e^{-(t^2 + 1)x^2}}{1 + t^2} = -2x\,e^{-(t^2 + 1)x^2}$ (le $1 + t^2$ se simplifie), continue en $(x, t)$ ; sur $[0, 1]$ (segment) et pour $|x| \le M$, elle est bornée par $2M$. Donc $g$ est $\mathcal{C}^1$ et $g'(x) = -2x\int_0^1 e^{-(t^2 + 1)x^2}\,dt$.

**b)** $g'(x) = -2e^{-x^2}\int_0^1 xe^{-x^2t^2}\,dt$ ; avec $u = xt$ : $\int_0^1 xe^{-x^2t^2}\,dt = \int_0^x e^{-u^2}\,du = f(x)$. Donc $g'(x) = -2e^{-x^2}f(x) = -2f'(x)f(x) = -(f^2)'(x)$. **$h' = 0$** : $h$ est constante.

**c)** $h(0) = g(0) + 0 = \int_0^1 \frac{dt}{1 + t^2} = \frac{\pi}{4}$.

**d)** $0 \le g(x) \le e^{-x^2}\int_0^1 \frac{dt}{1 + t^2} = \frac{\pi}{4}e^{-x^2} \to 0$.

**e)** $f^2 = \frac{\pi}{4} - g \to \frac{\pi}{4}$, et $f \ge 0$ sur $[0, +\infty[$, donc $f(x) \to \frac{\sqrt{\pi}}{2}$. **$I = \int_0^{+\infty}e^{-t^2}\,dt = \frac{\sqrt{\pi}}{2}$**, et par parité $\int_{\mathbb{R}}e^{-t^2}\,dt = \sqrt{\pi}$.
:::

## Exercice EXTRA 2 — L'intégrale de Frullani

$F(x) = \int_0^{+\infty}\frac{e^{-xt} - e^{-t}}{t}\,dt$ pour $x > 0$. a) Convergence. b) $\frac{\partial f}{\partial x}$. c) Hypothèses de Leibniz sur $[a, b] \subset ]0, +\infty[$. d) $F'(x) = -\int_0^{+\infty}e^{-xt}\,dt$. e) $F'$ puis $F$ (avec $F(1) = 0$). f) $\int_0^{+\infty}\frac{e^{-at} - e^{-bt}}{t}\,dt$ pour $a, b > 0$.

:::correction
**a)** En $0$ : $e^{-xt} - e^{-t} = (1 - x)t + o(t)$, donc l'intégrande tend vers $1 - x$ : fausse impropreté. En $+\infty$ : pour $t \ge 1$, $\left|\frac{e^{-xt} - e^{-t}}{t}\right| \le e^{-xt} + e^{-t}$, intégrable. **Converge** pour tout $x > 0$.

**b)** $\frac{\partial f}{\partial x}(x, t) = -e^{-xt}$ (le $t$ se simplifie).

**c)** Sur $[a, b]$ : $|-e^{-xt}| \le e^{-at}$, intégrable sur $[0, +\infty[$ ; la régularité est claire.

**d)** Par Leibniz, $F$ est $\mathcal{C}^1$ sur $]0, +\infty[$ et $F'(x) = -\int_0^{+\infty}e^{-xt}\,dt$.

**e)** $F'(x) = -\frac{1}{x}$, donc $F(x) = -\ln x + C$, et $F(1) = 0$ donne $C = 0$ : **$F(x) = -\ln x$**.

**f)** Avec $t = \frac{s}{b}$ : $\int_0^{+\infty}\frac{e^{-at} - e^{-bt}}{t}\,dt = \int_0^{+\infty}\frac{e^{-(a/b)s} - e^{-s}}{s}\,ds = F\left(\frac{a}{b}\right) = \ln\frac{b}{a}$.
:::

::item{id="tdp-frullani"}
