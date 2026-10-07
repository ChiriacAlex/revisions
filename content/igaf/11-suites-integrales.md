---
title: Ch4 — Suites d'intégrales et convergence dominée
summary: "Peut-on échanger limite et intégrale ? Convergence simple, fonctions continues par morceaux (sur un segment et sur un intervalle quelconque), contre-exemples (masse qui se concentre, qui s'échappe), et le théorème de convergence dominée."
tags: [chapitre 4, convergence simple, continuité par morceaux, convergence dominée]
minutes: 100
---

## 1. Le problème

On rencontre souvent des intégrales qui dépendent d'un entier $n$ : $I_n = \int_I f_n(x)\,dx$. Que vaut $\lim_{n \to +\infty} I_n$ ? La tentation est de « passer la limite sous l'intégrale » :
$$\lim_{n \to +\infty}\int_I f_n(x)\,dx \overset{?}{=} \int_I \lim_{n \to +\infty}f_n(x)\,dx.$$

:::warning[Cette égalité est souvent fausse]
Échanger deux opérations (limite et intégrale) **se justifie**. Tout le chapitre consiste à trouver **quand** on en a le droit. L'outil principal : le **théorème de convergence dominée**.
:::

## 2. Convergence simple

:::definition[Convergence simple]
Une suite de fonctions $f_n : I \to \mathbb{R}$ **converge simplement** vers $f$ sur $I$ si, **pour chaque $x \in I$ fixé**, $\lim_{n \to +\infty}f_n(x) = f(x)$.

On **fixe $x$**, puis on fait tendre $n$ vers l'infini.
:::

:::example[f_n(x) = xⁿ sur [0, 1]]
Pour $0 \le x < 1$, $x^n \to 0$ ; pour $x = 1$, $1^n = 1$. La limite simple est
$f(x) = 0$ si $0 \le x < 1$, et $f(1) = 1$.
Chaque $f_n$ est continue, mais la limite **ne l'est pas** : la convergence simple ne conserve pas la continuité.
:::

:::example[Wooclap 1 du cours : limite simple nulle ?]
- $x^n$ sur $[0, 1]$ : **non** (limite $1$ en $x = 1$).
- $x^n$ sur $\left[0, \frac{1}{2}\right]$ : **oui**.
- $nx^n\ln x$ sur $]0, 1]$ (et $0$ en $0$) : **oui** ($n x^n \to 0$ pour $x < 1$ par croissances comparées, et $\ln 1 = 0$).
- $x^n\cos\frac{1}{nx}$ sur $]0, 1]$ : **non** (en $x = 1$, $\cos\frac{1}{n} \to 1$).
- $\frac{1}{x^n}\cos\frac{1}{nx}$ sur $]0, 1]$ : **non** (pour $x < 1$, $\frac{1}{x^n} \to +\infty$).
:::

:::example[La masse qui se concentre (crossover avec PBS)]
$f_n(x) = \frac{n}{\sqrt{2\pi}}e^{-n^2x^2/2}$ est la densité de la loi normale $\mathcal{N}\left(0, \frac{1}{n^2}\right)$. Pour $x \ne 0$, $f_n(x) \to 0$. Mais $\int_{\mathbb{R}}f_n = 1$ pour tout $n$ (c'est une densité). Donc
$$\lim_n \int_{\mathbb{R}}f_n = 1 \ne 0 = \int_{\mathbb{R}}\lim_n f_n.$$
La courbe devient de plus en plus **étroite et haute** : l'aire reste $1$, mais se concentre en un point.
:::

:::key[Message important]
La convergence simple, à elle seule, **ne permet pas** de passer la limite sous l'intégrale. Il faut une hypothèse supplémentaire.
:::

::item{id="suites-simple"}

## 3. Fonctions continues par morceaux

:::definition[Sur un segment]
$f : [a, b] \to \mathbb{R}$ est **continue par morceaux** s'il existe une subdivision $a = x_0 < x_1 < \cdots < x_n = b$ telle que, sur chaque $]x_{i-1}, x_i[$, $f$ est continue et admet des **limites finies** en $x_{i-1}^+$ et $x_i^-$. Autrement dit, chaque morceau se prolonge en une fonction continue sur $[x_{i-1}, x_i]$.

Conséquence : un **nombre fini** de discontinuités, toutes des **sauts finis**.
:::

:::property[Test pratique]
Si, en un point $c$ du segment, une limite latérale **n'existe pas** ou est **infinie**, $f$ n'est **pas** continue par morceaux.
Exemple : $f(x) = \sin\frac{1}{x}$ sur $]0, 1]$, $f(0) = 0$, sur $[0, 1]$ : $\sin\frac{1}{x}$ n'a pas de limite en $0^+$ (elle vaut $1$ en $u_n = \frac{1}{\pi/2 + 2n\pi}$ et $-1$ en $v_n = \frac{1}{3\pi/2 + 2n\pi}$, deux suites qui tendent vers $0$). Donc pas continue par morceaux sur $[0, 1]$.
À l'inverse, $x\sin\frac{1}{x}$ (prolongée par $0$) est **continue** sur $\mathbb{R}$ : $\left|x\sin\frac{1}{x}\right| \le |x| \to 0$ (gendarmes).
:::

:::definition[Sur un intervalle quelconque]
$f$ est **continue par morceaux sur un intervalle $I$** (ouvert, non borné…) si elle l'est sur **tout segment** $[a, b] \subset I$.
Il peut alors y avoir une **infinité** de discontinuités (au plus dénombrable), à condition qu'il n'y en ait qu'un nombre fini sur chaque segment.
:::

:::example[f(x) = ⌊1/x⌋ sur ]0, 1]]
Sur $\left]\frac{1}{n + 1}, \frac{1}{n}\right]$, $n \le \frac{1}{x} < n + 1$, donc $f(x) = n$ : $f$ est constante par paliers. Elle saute en chaque $\frac{1}{n}$ ($n \ge 2$) : limite $n$ à gauche, $n - 1$ à droite. Il y a une **infinité** de discontinuités, mais elles s'accumulent en $0 \notin ]0, 1]$ : sur un segment $[a, b] \subset ]0, 1]$ ($a > 0$), il n'y en a qu'un nombre fini. Donc $f$ **est** continue par morceaux sur $]0, 1]$.
De même, $\sin\frac{1}{x}$ est continue (donc continue par morceaux) sur $]0, 1]$, alors qu'elle ne l'est pas sur $[0, 1]$.
:::

:::method[Intégrer une fonction continue par morceaux]
On découpe aux points de discontinuité et on étudie chaque morceau comme une intégrale (éventuellement généralisée). $\int_I f$ converge si et seulement si **chaque morceau** converge.
Exemple (Wooclap 3) : $f(x) = \frac{1}{x^{2/3}}$ sur $]0, 1]$ et $\frac{1}{x^{3/2}}$ sur $]1, +\infty[$ : Riemann $\alpha = \frac{2}{3} < 1$ en $0$, $\alpha = \frac{3}{2} > 1$ en $+\infty$, donc $\int_0^{+\infty}f$ converge. Avec les exposants échangés, les deux morceaux divergent.
:::

:::key[Pourquoi cette classe de fonctions ?]
La continuité n'est pas nécessaire pour intégrer. Les fonctions continues par morceaux sont la bonne classe : assez larges pour inclure les fonctions en escalier, les fonctions indicatrices $\mathbb{1}_{[a, b]}$ et les **limites simples** (souvent discontinues), assez régulières pour que leurs intégrales aient un sens.
:::

::item{id="suites-cpm"}

## 4. Les contre-exemples à connaître

:::example[Fonctions bornées, et pourtant…]
- **Masse qui se concentre** (Wooclap 4) : $f_n = n\,\mathbb{1}_{[0, 1/n]}$ sur $[0, 1]$. Pour $x > 0$, $f_n(x) = 0$ dès que $\frac{1}{n} < x$ : $f_n \to 0$ (sauf en $0$, un seul point, sans influence). Mais $\int_0^1 f_n = n \cdot \frac{1}{n} = 1$. Ici les $f_n$ ne sont **pas bornées uniformément**.
- **Masse qui s'échappe à l'infini** (Wooclap 5) : $f_n(x) = e^{-(x - n)^2}$ sur $[0, +\infty[$. On a $0 \le f_n \le 1$ et $f_n(x) \to 0$ pour tout $x$, mais
$\int_0^{+\infty}f_n = \int_{-n}^{+\infty}e^{-u^2}\,du \to \sqrt{\pi} \ne 0$. La bosse se **déplace** vers $+\infty$.
- **Créneau qui glisse** (Wooclap 10) : $f_n = \mathbb{1}_{[n, n + 1]}$ : $|f_n| \le 1$, $f_n \to 0$, mais $\int_0^{+\infty}f_n = 1$.
:::

:::warning[Sur un intervalle non borné, être borné ne suffit pas]
Dans les deux derniers exemples, la borne uniforme $1$ n'est **pas intégrable** sur $[0, +\infty[$ ($\int_0^{+\infty}1\,dx = +\infty$). C'est exactement ce que corrige le théorème de convergence dominée : la borne doit être une fonction **intégrable**.
:::

:::example[Un cas où ça marche : énergie d'un signal]
$f_n(t) = \sin t + \frac{1}{n}\sin(10t)$ sur $[0, 2\pi]$ tend vers $\sin t$. Par orthogonalité ($\int_0^{2\pi}\sin t\sin 10t\,dt = 0$) :
$$E_n = \int_0^{2\pi}|f_n|^2 = \pi + \frac{\pi}{n^2} \to \pi = \int_0^{2\pi}\sin^2 t\,dt.$$
:::

:::warning[Coquille dans les slides]
La diapositive 83 affiche $E_n = \pi + \frac{\pi}{n}$ ; le calcul détaillé de l'annexe (diapositives 136-137) donne correctement $\pi + \frac{\pi}{n^2}$ : le terme vient de $\frac{1}{n^2}\int_0^{2\pi}\sin^2(10t)\,dt$.
:::

## 5. Le théorème de convergence dominée

:::definition[Fonction intégrable]
Une fonction $g$ continue par morceaux sur $I$ est **intégrable** sur $I$ si $\int_I |g|$ converge (on note $g \in L^1(I)$). Sur un segment, toute fonction continue par morceaux est intégrable.
:::

:::theorem[Convergence dominée (TCD)]
Soit $(f_n)$ une suite de fonctions continues par morceaux sur un intervalle $I$. On suppose :
1. **convergence simple** : $f_n \to f$ simplement sur $I$, avec $f$ continue par morceaux ;
2. **domination** : il existe $\varphi$ continue par morceaux, **intégrable** sur $I$, **indépendante de $n$**, telle que
$$\forall n,\ \forall x \in I, \qquad |f_n(x)| \le \varphi(x).$$
Alors les $f_n$ et $f$ sont intégrables sur $I$ et
$$\lim_{n \to +\infty}\int_I f_n(x)\,dx = \int_I f(x)\,dx.$$
:::

:::method[Appliquer le TCD en 4 étapes]
1. Calculer la **limite simple** $f(x)$ (on fixe $x$).
2. Trouver une **domination** $|f_n(x)| \le \varphi(x)$ **valable pour tout $n$** (souvent pour $n \ge 1$ ou $n \ge n_0$).
3. Vérifier que $\varphi$ est **intégrable** sur $I$ (sur un segment : une constante suffit).
4. Conclure : $\lim \int f_n = \int f$, puis calculer $\int f$.

Les valeurs de $f$ en un nombre **fini** de points (ou dénombrable) n'ont pas d'influence sur l'intégrale.
:::

:::example[Wooclaps 6 à 8 : lim ∫₀^∞ dt/(tⁿ + eᵗ)]
1. **Limite simple** : pour $0 \le t < 1$, $t^n \to 0$ donc $f_n(t) \to e^{-t}$ ; pour $t > 1$, $t^n \to +\infty$ donc $f_n(t) \to 0$ ; en $t = 1$, $f_n(1) = \frac{1}{1 + e}$ (un seul point).
2. **Domination** : $t^n + e^t \ge e^t$, donc $0 \le f_n(t) \le e^{-t}$.
3. $e^{-t}$ est intégrable sur $[0, +\infty[$.
4. $\lim_n \int_0^{+\infty}\frac{dt}{t^n + e^t} = \int_0^1 e^{-t}\,dt = 1 - \frac{1}{e} \approx 0{,}632$.
:::

:::example[Wooclap 9 : lim ∫₀^{π/2} sinⁿ x dx]
Pour $0 \le x < \frac{\pi}{2}$, $0 \le \sin x < 1$ donc $\sin^n x \to 0$ (et la valeur $1$ en $\frac{\pi}{2}$ ne compte pas). Domination : $0 \le \sin^n x \le 1$, intégrable sur le **segment** $\left[0, \frac{\pi}{2}\right]$. Donc $\lim \int_0^{\pi/2}\sin^n x\,dx = 0$ (cohérent avec Wallis : $I_n \sim \sqrt{\frac{\pi}{2n}}$).
:::

:::warning[Le TCD ne s'applique pas toujours]
Pour $f_n = \mathbb{1}_{[n, n + 1]}$, la seule domination naturelle est $\varphi = 1$, **non intégrable** sur $[0, +\infty[$. Aucune fonction intégrable ne domine toutes les $f_n$ : le TCD ne s'applique pas, et la conclusion est d'ailleurs fausse ($1 \ne 0$).
:::

::item{id="suites-tcd"}

## 6. À retenir

:::key[Résumé]
- **Convergence simple** : $x$ fixé, $n \to \infty$. Ne suffit pas pour échanger limite et intégrale.
- **Continue par morceaux** : nombre fini de sauts finis sur chaque segment.
- **TCD** = convergence simple + **domination par une fonction intégrable indépendante de $n$**.
- Contre-exemples : masse qui se concentre ($n\mathbb{1}_{[0, 1/n]}$), qui s'échappe ($e^{-(x - n)^2}$, $\mathbb{1}_{[n, n+1]}$).
:::
