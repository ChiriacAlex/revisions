---
title: TD 2 — Intégrales généralisées (corrigé)
summary: "Feuille « Intégrales généralisées — 1. Définition et propriétés » corrigée : intégrales exponentielles, idée fausse f → 0, Riemann, critères de comparaison (dix intégrales), énergie d'un signal, intégrales de Fresnel, loi exponentielle."
kind: td
tags: [TD, intégrales généralisées, comparaison, Fresnel, loi exponentielle, énergie]
minutes: 180
---

:::note[À propos de ce TD]
C'est la feuille de TD du chapitre 1 d'INTG (questions 1-1 à 1-8). Le corrigé distribué est globalement juste ; une erreur de signe (question 1-1 b) est signalée, et l'énergie du signal amorti, demandée mais non calculée, est donnée ici. Toutes les valeurs ont été vérifiées numériquement.
:::

## Question 1-1 — Intégrales de référence : exponentielle

Nature, selon $\alpha \in \mathbb{R}$, de a) $\int_0^{+\infty}e^{\alpha x}\,dx$ et b) $\int_{-\infty}^0 e^{\alpha x}\,dx$.

:::correction
**a)** Si $\alpha = 0$ : $\int_0^t 1\,dx = t \to +\infty$, divergence. Si $\alpha \ne 0$ : $\int_0^t e^{\alpha x}\,dx = \frac{e^{\alpha t} - 1}{\alpha}$, qui tend vers $+\infty$ si $\alpha > 0$ et vers $-\frac{1}{\alpha}$ si $\alpha < 0$.
**Converge $\iff \alpha < 0$**, et alors $\int_0^{+\infty}e^{\alpha x}\,dx = -\frac{1}{\alpha}$.

**b)** Si $\alpha = 0$ : divergence. Sinon $\int_t^0 e^{\alpha x}\,dx = \frac{1 - e^{\alpha t}}{\alpha}$ quand $t \to -\infty$ : limite $\frac{1}{\alpha}$ si $\alpha > 0$, $+\infty$ si $\alpha < 0$.
**Converge $\iff \alpha > 0$**, et alors $\int_{-\infty}^0 e^{\alpha x}\,dx = \frac{1}{\alpha}$.
:::

:::warning[Erreur dans le corrigé (1-1 b)]
La conclusion du corrigé écrit $\int_{-\infty}^0 e^{\alpha x}\,dx = -\frac{1}{\alpha}$ (recopiée du a). Pour $\alpha > 0$ ce serait **négatif**, absurde pour l'intégrale d'une fonction positive. Le calcul juste au-dessus donne bien $\frac{1}{\alpha}$.
:::

## Question 1-2 — Vrai ou faux

Si $f$ est continue sur $[a, +\infty[$ et $\lim_{+\infty} f = 0$, alors $\int_a^{+\infty} f$ converge.

:::correction
**Faux.** $f(x) = \frac{1}{x}$ sur $[1, +\infty[$ tend vers $0$, mais $\int_1^b \frac{dx}{x} = \ln b \to +\infty$.

(La réciproque est fausse aussi : $\int_1^{+\infty}\sin(x^2)\,dx$ converge alors que $\sin(x^2)$ n'a pas de limite, voir la question 1-7.)
:::

## Question 1-3 — Généralisée ? Convergente ? Valeur ?

a) $\int_0^{+\infty}\cos t\,dt$ ; b) $\int_{-\infty}^{+\infty}\frac{dx}{|x|^{4/5}}$ ; c) $\int_1^{+\infty}\frac{dx}{x^{5/4}}$.

:::correction
- a) Généralisée en $+\infty$. $\int_0^X \cos t\,dt = \sin X$, qui n'a **pas de limite** : **diverge** (même si $\sin X$ reste bornée).
- b) Généralisée en $-\infty$, en $0$ (fonction non bornée) et en $+\infty$. La fonction est paire ; on étudie $\int_0^1$ et $\int_1^{+\infty}$. En $0$ : Riemann $\alpha = \frac{4}{5} < 1$, converge. En $+\infty$ : $\alpha = \frac{4}{5} \le 1$, **diverge**. Donc l'intégrale **diverge**.
- c) Riemann en $+\infty$ avec $\alpha = \frac{5}{4} > 1$ : converge. $\int_1^X x^{-5/4}\,dx = 4 - 4X^{-1/4} \to 4$. **Valeur $4$.**
:::

## Question 1-4 — Critères de comparaison

a) $\int_1^{+\infty}\frac{\cos^2 t}{t^2}\,dt$ ; b) $\int_0^{+\infty}\frac{e^{-t}}{1 + t^2}\,dt$ ; c) $\int_1^{+\infty}\frac{e^{\sin t}}{t}\,dt$ ; d) $\int_\pi^{+\infty}\frac{dt}{t + e^t}$ ; e) $\int_\pi^{+\infty}\frac{dt}{t - e^{-t}}$ ; f) $\int_{-\infty}^{+\infty}e^{-\alpha x^2}\,dx$ ($\alpha > 0$) ; g) $\int_0^{+\infty}\ln(t)\,e^{-t}\,dt$ ; h) $\int_0^{+\infty}\frac{\ln t}{t^2}\,dt$ ; i) $\int_0^{+\infty}\frac{\ln(1 + x^2)}{x^2}\,dx$ ; j) $\int_0^{+\infty}\frac{\sin(t/n)}{t(1 + t^2)}\,dt$.

:::correction
- a) $0 \le \frac{\cos^2 t}{t^2} \le \frac{1}{t^2}$ : **converge**.
- b) $0 \le \frac{e^{-t}}{1 + t^2} \le e^{-t}$ : **converge**.
- c) $\sin t \ge -1$ donc $\frac{e^{\sin t}}{t} \ge \frac{1}{e\,t} > 0$, et $\int_1^{+\infty}\frac{dt}{t}$ diverge : **diverge** (minoration).
- d) $\frac{1}{t + e^t} \underset{+\infty}{\sim} e^{-t}$ : **converge**.
- e) $e^{-t} \to 0$, donc $\frac{1}{t - e^{-t}} \sim \frac{1}{t}$ : **diverge**.
- f) Paire, on étudie $[0, +\infty[$. Pour $x \ge 1$, $x^2 \ge x$ donc $0 < e^{-\alpha x^2} \le e^{-\alpha x}$, intégrable : **converge**. (Valeur $\sqrt{\frac{\pi}{\alpha}}$, calculée au chapitre des intégrales à paramètre.)
- g) Deux problèmes. En $0$ : $f \sim \ln t$, et $\int_0^1 \ln t\,dt = -1$ converge. En $+\infty$ : $t^2 f(t) = t^2\ln(t)e^{-t} \to 0$, donc $f = o\left(\frac{1}{t^2}\right)$. **Converge** (valeur $-\gamma \approx -0{,}577$, où $\gamma$ est la constante d'Euler).
- h) En $0$ : $\int_\varepsilon^1 \frac{\ln t}{t^2}\,dt = \left[-\frac{\ln t + 1}{t}\right]_\varepsilon^1 = -1 + \frac{\ln\varepsilon + 1}{\varepsilon} \to -\infty$. **Diverge** (en $0$ ; inutile d'étudier $+\infty$).
- i) En $0$ : $\ln(1 + x^2) \sim x^2$, donc $f \to 1$ : fausse impropreté. En $+\infty$ : $f \sim \frac{2\ln x}{x^2} = o\left(\frac{1}{x^{3/2}}\right)$. **Converge** (valeur $\pi$).
- j) Sur $[1, +\infty[$ : $|f| \le \frac{1}{t(1 + t^2)} \le \frac{1}{t^3}$, converge absolument. Sur $]0, 1]$ : $f \sim \frac{1}{n}$, fausse impropreté. **Converge.**
:::

::item{id="tdig-comparaison"}

## Question 1-5 — Énergie d'un signal

L'énergie d'un signal $x$ est $E_x = \int_{-\infty}^{+\infty}|x(t)|^2\,dt$. Le signal est-il d'énergie finie (et la calculer le cas échéant) ?
a) $x(t) = \cos(\omega t)$ sur $\mathbb{R}$ ($\omega > 0$) ; b) $x(t) = Ae^{-\alpha t}\cos(\omega t)$ pour $t \ge 0$, $0$ sinon ($A, \alpha, \omega > 0$).

:::correction
**a)** $E = 2\int_0^{+\infty}\cos^2(\omega t)\,dt$ et $\int_0^X \cos^2(\omega t)\,dt = \frac{X}{2} + \frac{\sin(2\omega X)}{4\omega} \to +\infty$ (le terme oscillant est borné par $\frac{1}{4\omega}$). **Énergie infinie.** Autre argument : $\cos^2$ est $\pi$-périodique en $u = \omega t$, d'intégrale $\frac{\pi}{2}$ sur chaque période ; $N$ périodes donnent $N\frac{\pi}{2} \to +\infty$. (C'est un signal à **puissance moyenne** finie.)

**b)** $0 \le A^2e^{-2\alpha t}\cos^2(\omega t) \le A^2e^{-2\alpha t}$, intégrable : **énergie finie**. Calcul exact avec $\cos^2 = \frac{1 + \cos 2\omega t}{2}$ et $\int_0^{+\infty}e^{-at}\cos(bt)\,dt = \frac{a}{a^2 + b^2}$ :
$$E = \frac{A^2}{2}\left(\frac{1}{2\alpha} + \frac{2\alpha}{4\alpha^2 + 4\omega^2}\right) = \frac{A^2}{4\alpha} + \frac{A^2\alpha}{4(\alpha^2 + \omega^2)}.$$
L'enveloppe $Ae^{-\alpha t}$ force le signal à s'éteindre assez vite.
:::

## Question 1-6 — Calculs

a) $\int_0^{+\infty}\frac{dx}{1 + x^2}$ ; b) $\int_0^{+\infty}\frac{dx}{2 + x^2}$ ; c) en déduire $\int_0^{+\infty}\frac{3 + 2x^2}{(1 + x^2)(2 + x^2)}\,dx$.

:::correction
- a) $\arctan X \to \frac{\pi}{2}$ : **$\frac{\pi}{2}$**.
- b) $\frac{1}{\sqrt{2}}\arctan\frac{X}{\sqrt{2}} \to \frac{\pi}{2\sqrt{2}}$ : **$\frac{\pi}{2\sqrt{2}} = \frac{\pi\sqrt{2}}{4}$**.
- c) Avec $u = x^2$ : $\frac{3 + 2u}{(1 + u)(2 + u)} = \frac{1}{1 + u} + \frac{1}{2 + u}$, donc l'intégrande vaut $\frac{1}{1 + x^2} + \frac{1}{2 + x^2}$, et par linéarité (les deux convergent) : **$\frac{\pi}{2}\left(1 + \frac{1}{\sqrt{2}}\right) = \frac{\pi(2 + \sqrt{2})}{4}$**.
:::

## Question 1-7 — Intégrales de Fresnel

a) Absolue convergence de $\int_1^{+\infty}\frac{\sin x}{x^{3/2}}\,dx$. b) Par IPP, nature de $\int_1^{+\infty}\frac{\cos x}{\sqrt{x}}\,dx$. c) Par changement de variable, convergence de $\int_1^{+\infty}\cos(x^2)\,dx$. d) Nature de $\int_1^{+\infty}\sin(x^2)\,dx$. e) Convergence de $\int_0^{+\infty}\cos(x^2)\,dx$ et $\int_0^{+\infty}\sin(x^2)\,dx$.

:::correction
- a) $\left|\frac{\sin x}{x^{3/2}}\right| \le \frac{1}{x^{3/2}}$ : converge absolument.
- b) Sur $[1, X]$, $u = x^{-1/2}$, $v = \sin x$ : $\int_1^X \frac{\cos x}{\sqrt{x}}\,dx = \frac{\sin X}{\sqrt{X}} - \sin 1 + \frac{1}{2}\int_1^X \frac{\sin x}{x^{3/2}}\,dx$. Le terme de bord tend vers $0$ et l'intégrale converge (a) : **converge**.
- c) $u = x^2$, $dx = \frac{du}{2\sqrt{u}}$ : $\int_1^X \cos(x^2)\,dx = \frac{1}{2}\int_1^{X^2}\frac{\cos u}{\sqrt{u}}\,du$, qui converge par (b) : **converge**.
- d) Même changement puis IPP ($v = -\cos u$) : $\int_1^{X^2}\frac{\sin u}{\sqrt{u}}\,du = \left[-\frac{\cos u}{\sqrt{u}}\right]_1^{X^2} - \frac{1}{2}\int_1^{X^2}\frac{\cos u}{u^{3/2}}\,du$ : **converge**.
- e) Sur $[0, 1]$, fonctions continues : intégrales ordinaires. Sur $[1, +\infty[$ : (c) et (d). Les deux intégrales de Fresnel **convergent** (elles valent $\frac{1}{2}\sqrt{\frac{\pi}{2}}$), alors que $\cos(x^2)$ ne tend même pas vers $0$ : elles ne convergent **pas absolument**.
:::

## Question 1-8 — Loi exponentielle

$f(x) = \lambda e^{-\lambda x}$ si $x \ge 0$, $0$ sinon ($\lambda > 0$). a) $f$ est une densité ; b) $E(X)$ ; c) $V(X)$.

:::correction
- a) $f \ge 0$ et $\int_0^T \lambda e^{-\lambda x}\,dx = 1 - e^{-\lambda T} \to 1$.
- b) IPP ($u = x$, $v = -e^{-\lambda x}$) : $\int_0^T \lambda xe^{-\lambda x}\,dx = -Te^{-\lambda T} + \frac{1 - e^{-\lambda T}}{\lambda} \to \frac{1}{\lambda}$. **$E(X) = \frac{1}{\lambda}$.**
- c) $V(X) = E(X^2) - E(X)^2$. IPP ($u = x^2$) : $E(X^2) = \left[-x^2e^{-\lambda x}\right]_0^{+\infty} + 2\int_0^{+\infty}xe^{-\lambda x}\,dx = \frac{2}{\lambda}E(X) = \frac{2}{\lambda^2}$. **$V(X) = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$.**
:::

::item{id="tdig-calculs"}
