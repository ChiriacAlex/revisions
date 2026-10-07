---
title: "Ch3 bis — Méthodes : comment montrer qu'une intégrale converge"
summary: "Les 5 méthodes (définition, changement de variable, IPP, comparaison, convergence absolue), quand utiliser chacune, la règle xᵅf(x), l'organigramme d'étude et les 9 séries d'exercices des slides entièrement corrigées."
kind: sheet
tags: [méthode, convergence, organigramme, exercices corrigés]
minutes: 150
---

## 1. Avant tout : où est le problème ?

:::method[Le réflexe n°1]
1. **Repérer tous les points problématiques** : bornes infinies, bornes où $f$ n'est pas bornée, singularités intérieures.
2. **Découper** l'intégrale pour n'avoir qu'**un** point problématique par morceau.
3. **Étudier chaque morceau séparément**, au voisinage de son point problématique.
4. **Conclure** : l'intégrale converge si et seulement si **tous** les morceaux convergent.

Si la fonction est bornée sur un intervalle borné, il n'y a **pas** de problème (« fausse impropreté ») : par exemple $\frac{\sin x}{x}$ près de $0$ se prolonge par continuité.
:::

## 2. Les cinq méthodes et quand les utiliser

:::key[Tableau de choix]
| méthode | signal typique |
|---|---|
| **1. Définition** (primitive puis limite) | je sais calculer une primitive : $e^{-x}$, $\frac{1}{1 + x^2}$, $\frac{1}{x^{3/2}}$… |
| **2. Changement de variable** | une fonction composée et sa dérivée : $\frac{1}{x(\ln x)^\alpha}$, $f'(x)g(f(x))$ |
| **3. Intégration par parties** | un produit qui se simplifie en dérivant : $x^\alpha\ln x$, $x^\alpha e^x$, $\frac{\sin x}{x}$ |
| **4. Comparaison** (majoration, minoration, équivalent, DL) | $f \ge 0$ près du point, mais pas de primitive simple |
| **5. Convergence absolue** | $f$ change de signe : $\sin x$, $\cos x$, $(-1)^n$… |
:::

### Méthode 1 — La définition

:::example[Calcul direct]
- $\int_1^x \frac{dt}{t^{3/2}} = 2\left(1 - \frac{1}{\sqrt{x}}\right) \le 2$ : fonction positive, $F$ bornée, donc convergence (valeur $2$).
- $\int_0^x \frac{dt}{1 + t^2} = \arctan x \to \frac{\pi}{2}$ : $\int_0^{+\infty}\frac{dx}{1 + x^2} = \frac{\pi}{2}$.
:::

### Méthode 2 — Changement de variable

:::example[∫ₑ^∞ dx/(x (ln x)²)]
$u = \ln x$, $du = \frac{dx}{x}$ ; $x = e \Rightarrow u = 1$ ; $x \to +\infty \Rightarrow u \to +\infty$. Donc $\int_e^{+\infty}\frac{dx}{x(\ln x)^2} = \int_1^{+\infty}\frac{du}{u^2} = 1$ : **convergente**.
:::

### Méthode 3 — Intégration par parties

:::example[∫₁^∞ ln x / x² dx]
$u = \ln x$, $v = -\frac{1}{x}$ : $\int_1^A \frac{\ln x}{x^2}\,dx = \left[-\frac{\ln x}{x}\right]_1^A + \int_1^A \frac{dx}{x^2}$. Comme $\frac{\ln A}{A} \to 0$ et $\int_1^{+\infty}\frac{dx}{x^2}$ converge, l'intégrale **converge** (et vaut $1$).
:::

### Méthode 4 — Comparaison

:::key[Majorations utiles (boîte à outils)]
| fonction | majoration | domaine |
|---|---|---|
| $\ln x$ | $\ln x \le x - 1$ | $x > 0$ |
| $\ln(1 + x)$ | $\ln(1 + x) \le x$ | $x \ge 0$ |
| $\sin x$ | $\lvert\sin x\rvert \le \lvert x\rvert$ (et $\le 1$) | $\mathbb{R}$ |
| $1 - \cos x$ | $0 \le 1 - \cos x \le \frac{x^2}{2}$ | $\mathbb{R}$ |
| $\arctan x$ | $0 \le \arctan x \le x$ et $\le \frac{\pi}{2}$ | $x \ge 0$ |
| $e^x - 1$ | $e^x - 1 \ge x$ | $\mathbb{R}$ |
| $1 - e^{-x}$ | $1 - e^{-x} \le x$ | $\mathbb{R}$ |
| $\sqrt{1 + x} - 1$ | $\le \frac{x}{2}$ | $x \ge -1$ |
:::

:::example[Majorer, minorer, équivalent, DL]
- **Majoration** : sur $[0, 1[$, $\frac{x^3}{\sqrt{1 - x^4}} = \frac{x^3}{\sqrt{1 - x}\sqrt{1 + x}\sqrt{1 + x^2}} \le \frac{1}{\sqrt{1 - x}}$, Riemann $\alpha = \frac{1}{2}$ en $1$ : **convergente**.
- **Minoration** : pour $x \ge 1$, $\frac{x}{x + 1} \ge \frac{x}{2x} = \frac{1}{2}$, et $\int_1^{+\infty}\frac{dx}{2}$ diverge : $\int_1^{+\infty}\frac{x\,dx}{x + 1}$ **diverge**.
- **Équivalent** : $\frac{x + 1}{x^3 + 2} \underset{+\infty}{\sim} \frac{1}{x^2}$ : **convergente**.
- **Équivalent par DL** : $\frac{1 - \cos x}{x^3} \underset{0}{\sim} \frac{1}{2x}$ : **divergente** en $0$.
:::

:::method[Règle xᵅ f(x) (f positive)]
- **En $+\infty$** : s'il existe $\alpha > 1$ tel que $x^\alpha f(x)$ a une limite **finie**, l'intégrale **converge**. S'il existe $\alpha \le 1$ tel que $x^\alpha f(x) \to \ell > 0$ (ou $+\infty$), elle **diverge**.
- **En $0^+$** : s'il existe $\alpha < 1$ tel que $x^\alpha f(x)$ a une limite finie, elle **converge**. S'il existe $\alpha \ge 1$ tel que $x^\alpha f(x) \to \ell > 0$ (ou $+\infty$), elle **diverge**.
- **En un point $a$** : même chose avec $(x - a)^\alpha f(x)$.
:::

:::example[La règle en action]
- $\int_0^\pi \frac{\sin x}{x^{3/2}}\,dx$ : $x^{1/2}f(x) = \frac{\sin x}{x} \to 1$, avec $\alpha = \frac{1}{2} < 1$ : **convergente**.
- $\int_0^1 \frac{dx}{x\sin x}$ : sur $]0, 1]$, $x\sin x \le x$, donc $f(x) \ge \frac{1}{x}$ : **divergente**. (En fait $f \sim \frac{1}{x^2}$.)
- $\int_2^3 \frac{dx}{x^2(x^3 - 8)^{2/3}}$ : $x^3 - 8 = (x - 2)(x^2 + 2x + 4)$, donc $f(x) \le \frac{1}{4 \cdot 12^{2/3}}\cdot\frac{1}{(x - 2)^{2/3}}$ : **convergente** ($\alpha = \frac{2}{3}$).
- $\int_0^{\pi/2}\frac{dx}{(1 - \cos x)^{1/3}}$ : $1 - \cos x \sim \frac{x^2}{2}$, donc $f \sim \frac{2^{1/3}}{x^{2/3}}$ : **convergente**.
- $\int_1^{+\infty}\left(e^{1/t} - \cos\frac{1}{t}\right)\frac{dt}{t}$ : $e^{1/t} - \cos\frac{1}{t} = \frac{1}{t} + o\left(\frac{1}{t}\right)$, donc $f \sim \frac{1}{t^2}$ : **convergente**.
:::

### Méthode 5 — Convergence absolue

:::example[Exemples]
- $\left|\frac{\sin x}{x^2}\right| \le \frac{1}{x^2}$ : $\int_1^{+\infty}\frac{\sin x}{x^2}\,dx$ converge absolument.
- $\left|\frac{1}{t}\sin\frac{1}{t}\right| \le \frac{1}{t^2}$ (car $|\sin u| \le |u|$) : $\int_1^{+\infty}\frac{1}{t}\sin\frac{1}{t}\,dt$ converge absolument.
:::

:::warning[Coquilles dans les slides « 5 méthodes »]
- La diapositive 2 annonce « les **dix** méthodes suivantes » puis en liste cinq.
- La diapositive 43 énonce le critère de Bertrand de façon contradictoire (« si $f \sim \frac{1}{t^\alpha(\ln t)^\beta}$ pour ($\alpha > 1$ ou ($\alpha = 1$ et $\beta > 1$))… converge dès que $\alpha > 1$ »). Le bon énoncé : **converge si $\alpha > 1$, ou si $\alpha = 1$ et $\beta > 1$**.
:::

## 3. L'organigramme d'étude

:::key[Organigramme (d'après le « CVS Study Diagram »)]
1. Repérer les points problématiques, découper, étudier chaque morceau.
2. Intégrale **à bornes finies** et fonction **bornée** ? ⟹ converge (fausse impropreté).
3. **Primitive** calculable ? ⟹ calculer sur $[a, x]$ et passer à la limite.
4. Sinon, **$f$ est-elle positive** près du point ?
   - **oui** : comparaison directe, $O$, $o$ ou **équivalent**, avec une **intégrale de référence** (Riemann, Bertrand, exponentielle) ;
   - **non** : étudier $\int|f|$. Si elle converge, $\int f$ converge. Sinon : IPP, changement de variable, critère d'Abel ou de Dirichlet.
5. **Conclure** : converge si et seulement si tous les morceaux convergent.
:::

## 4. Exercices des slides, corrigés

:::note[Comment lire ces corrigés]
Les slides donnent ces neuf séries **sans corrigé**. Pour chaque intégrale : le point problématique, la méthode, la conclusion. Les valeurs annoncées ont été vérifiées numériquement.
:::

### Série 1 — Montrer la convergence par la définition

a) $\int_0^{+\infty} e^{-x}\,dx$ ; b) $\int_0^{+\infty} x e^{-2x}\,dx$ ; d) $\int_2^{+\infty}\frac{dx}{x\ln x}$ ; e) $\int_0^1 \ln x\,dx$ ; f) $\int_0^1 \frac{\ln x}{(1 + x)^2}\,dx$.

:::correction
- a) $\int_0^x e^{-t}\,dt = 1 - e^{-x} \to 1$ : converge, vaut $1$.
- b) IPP : $\int_0^x te^{-2t}\,dt = \left[-\frac{t}{2}e^{-2t}\right]_0^x + \frac{1}{2}\int_0^x e^{-2t}\,dt \to 0 + \frac{1}{4}$ : converge, vaut $\frac{1}{4}$.
- d) **Diverge !** Une primitive de $\frac{1}{x\ln x}$ est $\ln(\ln x)$, et $\ln(\ln x) - \ln(\ln 2) \to +\infty$. (C'est Bertrand avec $\alpha = \beta = 1$.)
- e) $\int_\varepsilon^1 \ln x\,dx = \big[x\ln x - x\big]_\varepsilon^1 = -1 - \varepsilon\ln\varepsilon + \varepsilon \to -1$ : converge, vaut $-1$.
- f) IPP avec la primitive $\frac{x}{1 + x}$ de $\frac{1}{(1 + x)^2}$ (choisie pour s'annuler en $0$, ce qui tue le terme de bord en $0$) :
$\int_\varepsilon^1 \frac{\ln x}{(1 + x)^2}\,dx = \left[\frac{x\ln x}{1 + x}\right]_\varepsilon^1 - \int_\varepsilon^1 \frac{dx}{1 + x} \to 0 - \ln 2$ : converge, vaut $-\ln 2$.
:::

:::warning[Erreur dans les slides (série 1, question d)]
L'énoncé demande de « montrer que les intégrales sont **convergentes** », mais $\int_2^{+\infty}\frac{dx}{x\ln x}$ **diverge** (primitive $\ln\ln x \to +\infty$). Il ne faut pas chercher à prouver le contraire !
:::

### Série 2 — Équivalents

a) $\int_0^{+\infty}\frac{\sqrt{x}}{(1 + x)^\alpha}\,dx$ ($\alpha \in \mathbb{R}$) ; b) $\int_0^\pi \frac{dx}{(1 - \cos x)^\alpha}$ ($\alpha \in \mathbb{R}$) ; c) $\int_0^{+\infty}\frac{dx}{\sqrt{x^3 + x^2}}$ ; d) $\int_1^{+\infty}\frac{\sqrt{x}}{\ln(1 + x)}\sin\frac{1}{x^2}\,dx$ ; e) $\int_0^1 \frac{\ln x}{\sqrt{1 - x}}\,dx$.

:::correction
- a) En $0$ : $f \to 0$, pas de problème. En $+\infty$ : $f \sim x^{1/2 - \alpha}$, converge $\iff \alpha - \frac{1}{2} > 1$. **Converge $\iff \alpha > \frac{3}{2}$.**
- b) En $0$ : $1 - \cos x \sim \frac{x^2}{2}$, donc $f \sim \frac{2^\alpha}{x^{2\alpha}}$ : il faut $2\alpha < 1$. En $\pi$ : $1 - \cos\pi = 2$, aucun problème. **Converge $\iff \alpha < \frac{1}{2}$.**
- c) $\sqrt{x^3 + x^2} = x\sqrt{x + 1}$. En $0$ : $f \sim \frac{1}{x}$, **divergente** (inutile d'étudier $+\infty$, où $f \sim x^{-3/2}$ converge).
- d) En $+\infty$ : $\sin\frac{1}{x^2} \sim \frac{1}{x^2}$ et $\ln(1 + x) \sim \ln x$, donc $f \sim \frac{1}{x^{3/2}\ln x}$ : **converge** (Bertrand, $\alpha = \frac{3}{2} > 1$).
- e) En $0$ : $f \sim \ln x$, intégrable. En $1$ : $\ln x \sim x - 1$, donc $f \sim -\sqrt{1 - x} \to 0$ : pas de problème. **Converge** (valeur $4\ln 2 - 4 \approx -1{,}227$).
:::

### Série 3 — Convergence absolue

a) $\int_1^{+\infty}\frac{\cos x}{x^2 + \ln x}\,dx$ ; b) $\int_2^3 \frac{1}{\sqrt{(3 - x)(x - 2)}}\sin\frac{1}{x - 2}\,dx$ ; c) $\int_0^1 \frac{1}{\sqrt{1 - x^2}}\sin\frac{1}{x}\,dx$ ; d) $\int_0^1 \frac{1}{\sqrt{x}}\cos\frac{1}{x}\,dx$.

:::correction
- a) Pour $x \ge 1$, $\ln x \ge 0$ : $|f| \le \frac{1}{x^2}$.
- b) $|f| \le \frac{1}{\sqrt{(3 - x)(x - 2)}}$, qui est $\sim \frac{1}{\sqrt{x - 2}}$ en $2$ et $\sim \frac{1}{\sqrt{3 - x}}$ en $3$ (Riemann $\alpha = \frac{1}{2}$ des deux côtés).
- c) $|f| \le \frac{1}{\sqrt{1 - x^2}} \underset{1}{\sim} \frac{1}{\sqrt{2}\sqrt{1 - x}}$ ; en $0$ la fonction est bornée.
- d) $|f| \le \frac{1}{\sqrt{x}}$.

Les quatre intégrales convergent **absolument**, donc convergent.
:::

### Série 4 — Signe quelconque

a) $\int_0^{+\infty}e^{-x}\sin x\,dx$ ; b) $\int_0^{+\infty}\frac{\sin x}{x^2 + 4}\,dx$ ; c) $\int_0^{+\infty}\frac{\cos x}{\cosh x}\,dx$ ; d) $\int_0^{1/2}\frac{x}{|\ln x|}\,dx$ ; e) $\int_0^{+\infty}\frac{\sqrt{x}}{\ln(1 + x)}\sin\frac{1}{x^2}\,dx$ ; f) $\int_1^{+\infty}\frac{\sin 5x - \sin 3x}{x^{5/3}}\,dx$.

:::correction
- a) $|f| \le e^{-x}$ : converge absolument (valeur $\frac{1}{2}$).
- b) $|f| \le \frac{1}{x^2 + 4}$ : converge absolument.
- c) $|f| \le \frac{1}{\cosh x} \le 2e^{-x}$ : converge absolument.
- d) $f \to 0$ en $0^+$ (croissances comparées) : fausse impropreté, **converge**.
- e) En $0$ : $\ln(1 + x) \sim x$, donc $|f| \le \frac{\sqrt{x}}{\ln(1 + x)} \sim \frac{1}{\sqrt{x}}$, intégrable. En $+\infty$ : $|f| \sim \frac{1}{x^{3/2}\ln x}$. **Converge absolument.**
- f) $|f| \le \frac{2}{x^{5/3}}$ : converge absolument.
:::

### Série 5 — Au voisinage de l'infini

a) $\int_1^{+\infty}\frac{x^2 + 1}{x^3\sqrt{x}}\,dx$ ; b) $\int_1^{+\infty}\frac{\arctan t}{t^2}\,dt$ ; c) $\int_2^{+\infty}\frac{\ln(t + 1)}{t^2 + 1}\,dt$ ; d) $\int_1^{+\infty}\frac{1}{1 + t}\sin\frac{1}{t}\,dt$ ; e) $\int_1^{+\infty}\frac{\sin x\ln x}{(x + \sqrt{x})^2}\,dx$.

:::correction
- a) $f \sim \frac{1}{x^{3/2}}$ : converge.
- b) $0 \le f \le \frac{\pi/2}{t^2}$ : converge.
- c) $f \sim \frac{\ln t}{t^2} = o\left(\frac{1}{t^{3/2}}\right)$ : converge.
- d) $f \sim \frac{1}{t^2}$ : converge.
- e) $|f| \le \frac{\ln x}{x^2} = o\left(\frac{1}{x^{3/2}}\right)$ : converge absolument.
:::

### Série 6 — Au voisinage de 0 (et paramètre)

a) $\int_0^1 \left(e^{\frac{\sin x}{x}} - 1\right)dx$ ; b) $\int_1^{+\infty}\frac{dx}{(x - 1)^\alpha(x + 1)}$ ($\alpha \in \mathbb{R}$) ; c) $\int_0^{+\infty}\frac{\sqrt[3]{x + 1} - \sqrt[3]{x + 2}}{\sqrt{x}}\,dx$ ; d) $\int_0^1 \frac{dx}{\sqrt[3]{x}\sqrt{1 - x^3}\ln(1 + x)}$.

:::correction
- a) $\frac{\sin x}{x} \to 1$, donc l'intégrande tend vers $e - 1$ : fausse impropreté, **converge**.
- b) En $1$ : $f \sim \frac{1}{2(x - 1)^\alpha}$, il faut $\alpha < 1$. En $+\infty$ : $f \sim \frac{1}{x^{\alpha + 1}}$, il faut $\alpha > 0$. **Converge $\iff 0 < \alpha < 1$.**
- c) En $0$ : $f \sim \frac{1 - \sqrt[3]{2}}{\sqrt{x}}$, intégrable. En $+\infty$ : $\sqrt[3]{x + 1} - \sqrt[3]{x + 2} = x^{1/3}\left[\left(1 + \frac{1}{x}\right)^{1/3} - \left(1 + \frac{2}{x}\right)^{1/3}\right] \sim -\frac{1}{3}x^{-2/3}$, donc $f \sim -\frac{1}{3x^{7/6}}$ (signe constant) : **converge**.
- d) En $0$ : $\ln(1 + x) \sim x$, donc $f \sim \frac{1}{x^{4/3}}$ : **diverge** ($\alpha = \frac{4}{3} \ge 1$).
:::

### Série 7 — Nature

a) $\int_0^{+\infty}(1 + x + x^2)e^{-x}\,dx$ ; b) $\int_0^{+\infty}e^{-x^2}\,dx$ ; c) $\int_0^1 \frac{\ln x}{(1 + x)\sqrt{x}}\,dx$ ; d) $\int_0^{+\infty}\frac{x\ln x}{(1 + x^2)^2}\,dx$ ; e) $\int_0^{\pi/2}\ln(\sin x)\,dx$.

:::correction
- a) $x^2 f(x) \to 0$ en $+\infty$ : converge (valeur $1 + 1 + 2 = 4$, car $\int_0^{+\infty}x^n e^{-x}\,dx = n!$).
- b) Pour $x \ge 1$, $0 < e^{-x^2} \le e^{-x}$ : converge (valeur $\frac{\sqrt{\pi}}{2}$, intégrale de Gauss).
- c) En $0$ : $|f| \sim \frac{|\ln x|}{\sqrt{x}}$ et $x^{3/4}\cdot\frac{|\ln x|}{\sqrt{x}} = x^{1/4}|\ln x| \to 0$ : converge ($\alpha = \frac{3}{4}$).
- d) En $0$ : $f \to 0$. En $+\infty$ : $f \sim \frac{\ln x}{x^3}$ : converge. (Avec $x \mapsto \frac{1}{x}$ on montre que la valeur est $0$.)
- e) En $0$ : $\ln(\sin x) = \ln x + \ln\frac{\sin x}{x} \sim \ln x$, intégrable : converge (valeur $-\frac{\pi}{2}\ln 2$).
:::

### Série 8 — Divergence

a) $\int_1^{+\infty}\frac{dx}{\sqrt{1 + x}}$ ; b) $\int_0^{\pi/2}\frac{dx}{1 - \cos x}$ ; c) $\int_0^1 \frac{dx}{\sqrt{x\tan x}}$.

:::correction
- a) $f \sim \frac{1}{x^{1/2}}$ en $+\infty$ : **diverge**.
- b) $f \sim \frac{2}{x^2}$ en $0$ : **diverge**.
- c) $\tan x \sim x$, donc $f \sim \frac{1}{x}$ en $0$ : **diverge**.
:::

### Série 9 — Règle (x − a)ᵅ f(x)

a) $\int_1^2 \frac{dx}{\sqrt{(x - 1)(2 - x)}}$ ; b) $\int_1^2 \frac{\ln(x + 1)}{\sin^2(x - 1)}\,dx$ ; c) $\int_1^3 \frac{dx}{\sqrt{x^3 - 1}}$ ; d) $\int_a^b \frac{dx}{\sqrt{(x^2 - a^2)(b^2 - x^2)}}$ ($0 < a < b$) ; e) $\int_1^{+\infty}\frac{dx}{(x - \cos a)(x^2 - 1)^{2/3}}$ ($a \in ]0, \pi]$).

:::correction
- a) $(x - 1)^{1/2}f \to 1$ en $1$, $(2 - x)^{1/2}f \to 1$ en $2$ : **converge** (valeur $\pi$, avec $x = \frac{3}{2} + \frac{1}{2}\sin\theta$).
- b) En $1$ : $f \sim \frac{\ln 2}{(x - 1)^2}$ : **diverge**.
- c) $x^3 - 1 = (x - 1)(x^2 + x + 1) \sim 3(x - 1)$ : $f \sim \frac{1}{\sqrt{3}\sqrt{x - 1}}$ : **converge**.
- d) En $a$ : $f \sim \frac{1}{\sqrt{2a(b^2 - a^2)}}\cdot\frac{1}{\sqrt{x - a}}$ ; en $b$, de même avec $\sqrt{b - x}$ : **converge**.
- e) $a \in ]0, \pi]$ donne $1 - \cos a > 0$, donc $x - \cos a$ ne s'annule pas sur $[1, +\infty[$. En $1$ : $(x^2 - 1)^{2/3} \sim (2(x - 1))^{2/3}$, $\alpha = \frac{2}{3} < 1$. En $+\infty$ : $f \sim \frac{1}{x^{7/3}}$. **Converge.**
:::

::item{id="meth-choix"}

::item{id="meth-valeurs"}
