---
title: TD — Lois continues (exercices corrigés)
summary: Densités à paramètre, probabilités et fonctions de répartition, simulation d'une uniforme, exponentielle et absence de mémoire, loi normale, changements de variable.
kind: td
tags: [TD, densité, exponentielle, loi normale, changement de variable]
minutes: 120
---

:::note[Comment travailler ce TD]
Ces exercices entraînent exactement les compétences du chapitre 1 : vérifier une densité, passer de $f$ à $F$, calculer des probabilités, utiliser les lois usuelles, et changer de variable **par la fonction de répartition**. Dessine toujours la densité avant de calculer.
:::

## Exercice 1 — Densités à paramètre

Pour chaque fonction, déterminer les $k \in \mathbb{R}$ pour lesquels $f$ est une densité. Si c'est le cas, pour $X$ de densité $f$ : (a) donner sa fonction de répartition ; (b) donner un intervalle central à 95 %.

1. $f(x) = \frac{k}{x^2}$ si $x \ge 2$, $0$ sinon.
2. $f(x) = k\,e^{-2|x|}$ pour tout $x \in \mathbb{R}$.
3. $f(x) = k\,x(2 - x)$ si $x \in [0, 2]$, $0$ sinon.
4. $f(x) = k\,e^{x}$ pour tout $x \in \mathbb{R}$.

:::hint[Indice]
Positivité d'abord (signe de $k$), puis $\int_\mathbb{R} f = 1$. Pour 4, l'intégrale converge-t-elle ?
:::

:::correction
**1.** Positivité : $k \ge 0$. $\int_2^{+\infty} \frac{k}{x^2}dx = k\left[-\frac{1}{x}\right]_2^{+\infty} = \frac{k}{2}$, donc $k = 2$.
(a) $F(x) = 0$ si $x < 2$, et $F(x) = \int_2^x \frac{2}{t^2}dt = 1 - \frac{2}{x}$ si $x \ge 2$.
(b) $F(a) = 0{,}025 \iff a = \frac{2}{0{,}975} \approx 2{,}051$ et $F(b) = 0{,}975 \iff b = \frac{2}{0{,}025} = 80$. Intervalle $[2{,}05 ;\ 80]$ — très dissymétrique : la loi a une « queue lourde » à droite.

**2.** Positivité : $k \ge 0$. Par parité, $\int_\mathbb{R} k e^{-2|x|}dx = 2k\int_0^{+\infty} e^{-2x}dx = 2k \cdot \frac{1}{2} = k$, donc $k = 1$.
(a) Pour $x < 0$ : $F(x) = \int_{-\infty}^x e^{2t}dt = \frac{e^{2x}}{2}$. Pour $x \ge 0$ : $F(x) = \frac{1}{2} + \int_0^x e^{-2t}dt = 1 - \frac{e^{-2x}}{2}$. (Raccord en 0 : $\frac{1}{2}$ des deux côtés ✔.)
(b) Par symétrie, $[a, b] = [-b, b]$ avec $1 - \frac{e^{-2b}}{2} = 0{,}975$, soit $e^{-2b} = 0{,}05$ et $b = \frac{\ln 20}{2} \approx 1{,}498$. Intervalle $\approx [-1{,}50 ;\ 1{,}50]$.

**3.** $x(2 - x) \ge 0$ sur $[0, 2]$ : $k \ge 0$. $\int_0^2 kx(2-x)dx = k\left[x^2 - \frac{x^3}{3}\right]_0^2 = k\left(4 - \frac{8}{3}\right) = \frac{4k}{3}$, donc $k = \frac{3}{4}$.
(a) $F(x) = 0$ si $x < 0$ ; $F(x) = \frac{3}{4}\left(x^2 - \frac{x^3}{3}\right) = \frac{3x^2}{4} - \frac{x^3}{4}$ si $0 \le x \le 2$ ; $F(x) = 1$ si $x > 2$.
(b) Il faut résoudre $\frac{3a^2 - a^3}{4} = 0{,}025$, une équation de degré 3 : numériquement (par dichotomie) $a \approx 0{,}189$, et par symétrie de la densité autour de 1, $b = 2 - a \approx 1{,}811$.

**4.** Pour $k > 0$, $\int_0^{+\infty} k e^x dx$ **diverge** ; pour $k < 0$, $f$ n'est pas positive ; pour $k = 0$, l'intégrale vaut 0. **Aucune** valeur de $k$ ne convient.
:::

::item{id="tdc-k"}

## Exercice 2 — Probabilités à partir d'une densité

$X$ a pour densité $f(x) = \frac{3}{4}(1 - x^2)$ sur $[-1, 1]$, $0$ sinon.

1. Calculer $P(X \le 0)$, $P(-\frac{1}{2} \le X \le \frac{1}{2})$ et $P(X > \frac{1}{2})$.
2. Calculer la fonction de répartition $F_X$.

:::correction
**1.** La densité est paire, donc $P(X \le 0) = \frac{1}{2}$. Ensuite
$$P\left(-\tfrac{1}{2} \le X \le \tfrac{1}{2}\right) = \frac{3}{4}\int_{-1/2}^{1/2}(1 - x^2)\,dx = \frac{3}{4}\left(1 - \frac{1}{12}\right) = \frac{11}{16} = 0{,}6875,$$
et par symétrie $P(X > \frac{1}{2}) = \frac{1 - 11/16}{2} = \frac{5}{32} \approx 0{,}156$.

**2.** $F(x) = 0$ si $x < -1$ ; pour $-1 \le x \le 1$ :
$$F(x) = \frac{3}{4}\int_{-1}^x (1 - t^2)\,dt = \frac{3}{4}\left(x - \frac{x^3}{3} + \frac{2}{3}\right) = \frac{1}{2} + \frac{3x}{4} - \frac{x^3}{4} ;$$
$F(x) = 1$ si $x > 1$. Vérifications : $F(-1) = 0$, $F(0) = \frac{1}{2}$, $F(1) = 1$ ✔.
:::

## Exercice 3 — Loi uniforme et simulation

Soit $X \sim \mathcal{U}([2, 8])$.

1. Donner la fonction de répartition de $X$ et $P(3 \le X \le 6)$.
2. Soit $Z = \frac{X - 2}{6}$. Déterminer la fonction de répartition de $Z$, puis sa densité.
3. On dispose de `rand()`, qui renvoie un réel uniforme dans $[0, 1[$. Comment simuler une uniforme sur $[-3, 5]$ ?

:::correction
**1.** $F(x) = 0$ si $x < 2$, $\frac{x - 2}{6}$ si $2 \le x \le 8$, $1$ si $x > 8$. $P(3 \le X \le 6) = \frac{6 - 3}{6} = \frac{1}{2}$ (longueur favorable sur longueur totale).

**2.** Pour $t \in \mathbb{R}$ : $F_Z(t) = P\left(\frac{X - 2}{6} \le t\right) = P(X \le 2 + 6t) = F_X(2 + 6t)$ (on multiplie par $6 > 0$, l'inégalité est conservée). Donc $F_Z(t) = 0$ si $t < 0$, $t$ si $0 \le t \le 1$, $1$ si $t > 1$ : $Z \sim \mathcal{U}([0, 1])$, de densité $1$ sur $[0, 1]$.

**3.** Réciproquement, si $U \sim \mathcal{U}([0, 1])$, alors $a + (b - a)U \sim \mathcal{U}([a, b])$. On prend `-3 + 8 * rand()`.
:::

## Exercice 4 — Loi exponentielle et absence de mémoire

Le temps $T$ (en heures) entre deux signalements de bug sur un projet suit une loi exponentielle de moyenne 4 heures.

1. Quel est le paramètre $\lambda$ ? Donner la densité et la fonction de répartition de $T$.
2. Calculer $P(T > 8)$, puis le temps $a$ tel que $P(T \le a) = 0{,}9$.
3. Aucun bug n'a été signalé depuis 6 heures. Quelle est la probabilité d'attendre encore au moins 2 heures ? Commenter.
4. *(Bonus)* On suppose seulement que $T \ge 0$ est **sans mémoire**, de fonction de répartition $F$ dérivable sur $\mathbb{R}_+$, avec $F(0) = 0$. Montrer que $T$ suit une loi exponentielle.

:::correction
**1.** $E[T] = \frac{1}{\lambda} = 4$, donc $\lambda = \frac{1}{4}$. $f(t) = \frac{1}{4}e^{-t/4}$ et $F(t) = 1 - e^{-t/4}$ pour $t \ge 0$ (et $0$ pour $t < 0$).

**2.** $P(T > 8) = e^{-8/4} = e^{-2} \approx 0{,}135$. Et $1 - e^{-a/4} = 0{,}9 \iff e^{-a/4} = 0{,}1 \iff a = 4\ln 10 \approx 9{,}21$ h.

**3.** Par absence de mémoire : $P(T > 8 \mid T > 6) = P(T > 2) = e^{-1/2} \approx 0{,}607$. Avoir déjà attendu 6 heures ne rend pas un signalement « plus imminent » : le modèle suppose des signalements indépendants, sans usure.

**4.** Notons $G = 1 - F$ (fonction de survie). L'absence de mémoire s'écrit $P(T > t + h \mid T > t) = P(T > h)$, soit $G(t + h) = G(t)\,G(h)$ pour tous $t, h \ge 0$. Alors
$$\frac{G(t + h) - G(t)}{h} = G(t)\,\frac{G(h) - 1}{h} = G(t)\,\frac{G(h) - G(0)}{h}.$$
En faisant tendre $h \to 0^+$ : $G'(t) = G'(0)\,G(t) = -\lambda\,G(t)$ avec $\lambda = F'(0) = f(0)$. La seule solution avec $G(0) = 1$ est $G(t) = e^{-\lambda t}$ : $F(t) = 1 - e^{-\lambda t}$, c'est une loi exponentielle (avec $\lambda > 0$ pour que $G \to 0$ en $+\infty$). $\square$
:::

::item{id="tdc-expo"}

## Exercice 5 — Loi normale

Soit $Z$ de densité $\varphi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ et de fonction de répartition $\Phi$.

1. Montrer que pour tout $\beta > 0$, $\Phi(-\beta) = 1 - \Phi(\beta)$.
2. Soient $m \in \mathbb{R}$, $\sigma > 0$ et $X = m + \sigma Z$. Exprimer $F_X$ avec $\Phi$, puis la densité de $X$. Donner un intervalle central à 95 % pour $X$ (on admet $\Phi(1{,}96) \approx 0{,}975$).
3. Le temps de réponse d'un serveur suit $\mathcal{N}(120, 15^2)$ (en ms). Quelle proportion des requêtes dépasse 150 ms ? Donner l'intervalle central à 95 %.

:::correction
**1.** Par le changement de variable $u = -t$ et la parité de $\varphi$ :
$$\Phi(-\beta) = \int_{-\infty}^{-\beta}\varphi(t)\,dt = \int_{\beta}^{+\infty}\varphi(u)\,du = 1 - \int_{-\infty}^{\beta}\varphi(u)\,du = 1 - \Phi(\beta).$$

**2.** $F_X(x) = P(m + \sigma Z \le x) = P\left(Z \le \frac{x - m}{\sigma}\right) = \Phi\left(\frac{x - m}{\sigma}\right)$ (car $\sigma > 0$). En dérivant : $f_X(x) = \frac{1}{\sigma}\varphi\left(\frac{x - m}{\sigma}\right) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-m)^2}{2\sigma^2}}$. Intervalle à 95 % : $F_X(b) = 0{,}975 \iff \frac{b - m}{\sigma} = 1{,}96$, et par symétrie $[m - 1{,}96\sigma,\ m + 1{,}96\sigma]$.

**3.** $P(X > 150) = 1 - \Phi\left(\frac{150 - 120}{15}\right) = 1 - \Phi(2) \approx 0{,}0228$ : environ 2,3 % des requêtes. Intervalle : $[120 - 29{,}4 ;\ 120 + 29{,}4] = [90{,}6 ;\ 149{,}4]$ ms.
:::

::item{id="tdc-normale"}

## Exercices supplémentaires

:::exercise[Extra 1 — Changements de variable affines]
Soit $X$ de densité $f$ et de fonction de répartition $F$. Exprimer la fonction de répartition puis une densité de $Y_1 = 3X - 2$ et de $Y_2 = -X + 4$.
:::

:::correction
- $F_{Y_1}(t) = P(3X - 2 \le t) = P\left(X \le \frac{t + 2}{3}\right) = F\left(\frac{t+2}{3}\right)$, donc $f_{Y_1}(t) = \frac{1}{3} f\left(\frac{t + 2}{3}\right)$.
- $F_{Y_2}(t) = P(-X + 4 \le t) = P(X \ge 4 - t) = 1 - F(4 - t)$ ($X$ continue), donc $f_{Y_2}(t) = f(4 - t)$ (le signe moins de la dérivée composée compense celui devant $F$).
:::

:::exercise[Extra 2 — Fonctions d'une exponentielle]
Soit $X \sim \mathcal{E}(1)$. Déterminer la fonction de répartition et la densité de $Y = X^2$ et de $W = e^X$.
:::

:::correction
- $Y = X^2 \ge 0$ : $F_Y(t) = 0$ si $t < 0$. Pour $t \ge 0$, comme $X \ge 0$ : $X^2 \le t \iff X \le \sqrt{t}$, donc $F_Y(t) = 1 - e^{-\sqrt{t}}$, et $f_Y(t) = \frac{e^{-\sqrt{t}}}{2\sqrt{t}}$ pour $t > 0$.
- $W = e^X \ge 1$ (car $X \ge 0$) : $F_W(t) = 0$ si $t < 1$. Pour $t \ge 1$ : $e^X \le t \iff X \le \ln t$, donc $F_W(t) = 1 - e^{-\ln t} = 1 - \frac{1}{t}$, et $f_W(t) = \frac{1}{t^2}$ pour $t > 1$ (une loi de Pareto). Attention aux valeurs impossibles $t < 1$.
:::

:::exercise[Extra 3 — Valeur absolue d'une uniforme]
Soit $X \sim \mathcal{U}([-2, 1])$. Déterminer la fonction de répartition puis une densité de $|X|$.
:::

:::hint[Indice]
$|X|$ prend ses valeurs dans $[0, 2]$. Distingue $t \in [0, 1]$ (l'intervalle $[-t, t]$ est entièrement dans $[-2, 1]$) et $t \in [1, 2]$ (seul $[-t, 1]$ compte).
:::

:::correction
La densité de $X$ est $\frac{1}{3}$ sur $[-2, 1]$.
- $t < 0$ : $F(t) = 0$.
- $0 \le t \le 1$ : $F(t) = P(-t \le X \le t) = \frac{2t}{3}$.
- $1 \le t \le 2$ : $F(t) = P(-t \le X \le 1) = \frac{1 + t}{3}$.
- $t > 2$ : $F(t) = 1$.

Raccords : $F(1) = \frac{2}{3}$ des deux côtés, $F(2) = 1$ ✔. Densité : $\frac{2}{3}$ sur $[0, 1]$, $\frac{1}{3}$ sur $]1, 2]$, $0$ ailleurs (deux fois plus de chances d'être « petit » : les valeurs de $[-1, 1]$ se replient sur $[0, 1]$).
:::

:::exercise[Extra 4 — Simuler une exponentielle avec `rand()`]
Soit $U \sim \mathcal{U}([0, 1[)$ et $\lambda > 0$. Montrer que $T = -\frac{\ln(1 - U)}{\lambda}$ suit la loi $\mathcal{E}(\lambda)$.
:::

:::correction
$T \ge 0$ car $1 - U \in\, ]0, 1]$. Pour $t \ge 0$ : $T \le t \iff \ln(1 - U) \ge -\lambda t \iff 1 - U \ge e^{-\lambda t} \iff U \le 1 - e^{-\lambda t}$ (la fonction $\ln$ est croissante, et on multiplie par $-\frac{1}{\lambda} < 0$ en inversant l'inégalité). Donc $F_T(t) = P(U \le 1 - e^{-\lambda t}) = 1 - e^{-\lambda t}$ : c'est la fonction de répartition de $\mathcal{E}(\lambda)$. $\square$ C'est la **méthode d'inversion** : $T = F^{-1}(U)$, utilisée par les bibliothèques de simulation.
:::

::item{id="tdc-changement"}
