---
title: Prérequis — Variables aléatoires discrètes
summary: Loi, fonction de répartition, espérance, variance, couples et indépendance, covariance, et les lois discrètes usuelles (Bernoulli, binomiale, géométrique, Poisson, hypergéométrique…).
tags: [prérequis, lois usuelles, espérance, variance]
minutes: 75
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- définir une **variable aléatoire** discrète et donner sa **loi** ;
- calculer et interpréter une **fonction de répartition** ;
- calculer une **espérance** (y compris de $g(X)$) et une **variance** (formule de König-Huygens) ;
- manipuler un **couple** : loi jointe, lois marginales, lois conditionnelles, **indépendance**, **covariance** ;
- **reconnaître** les lois usuelles dans un énoncé et connaître leurs espérance et variance.

:::intuition[Le fil conducteur]
Une variable aléatoire **résume** une expérience par un nombre : la somme de deux dés, le nombre de pièces défectueuses, le nombre d'essais avant un succès. Toute l'information utile est dans sa **loi** : la liste des valeurs possibles et de leurs probabilités. Espérance et variance résument cette loi par deux nombres : où est le « centre », et à quel point ça s'en écarte.
:::

## 2. Qu'est-ce qu'une variable aléatoire ?

:::definition[Variable aléatoire]
Une **variable aléatoire** (réelle) est une fonction $X : \Omega \to \mathbb{R}$ qui associe un nombre à chaque issue $\omega$ de l'expérience. Elle est **discrète** si l'ensemble de ses valeurs $X(\Omega)$ est fini ou dénombrable (on peut le numéroter $x_0, x_1, x_2, \ldots$).
:::

:::example
- On lance deux dés : $\Omega = \{1, \ldots, 6\}^2$ et $X(\omega_1, \omega_2) = \omega_1 + \omega_2$ (la somme). $X(\Omega) = \{2, \ldots, 12\}$ : discrète, finie.
- On lance une pièce jusqu'au premier pile ; $N$ = nombre de lancers. $N(\Omega) = \mathbb{N}^*$ : discrète, infinie dénombrable.
- On mesure le temps d'attente d'un bus : à valeurs dans un intervalle de $\mathbb{R}$, c'est une variable **continue** (chapitre suivant).
:::

On note $\{X = x\}$ l'événement $\{\omega \in \Omega \mid X(\omega) = x\}$, et plus généralement $\{X \in B\} = X^{-1}(B)$.

## 3. Loi et fonction de répartition

:::definition[Loi d'une variable discrète]
La **loi** de $X$ est la donnée des probabilités $p_X(x) = P(X = x)$ pour $x \in X(\Omega)$. Elles vérifient $p_X(x) \ge 0$ et $\sum_{x \in X(\Omega)} p_X(x) = 1$. Pour tout ensemble $B$ : $P(X \in B) = \sum_{x \in B} p_X(x)$.
:::

:::example[Somme de deux dés équilibrés]
Les 36 couples sont équiprobables ; on compte ceux qui donnent chaque somme :

| $k$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $36\,P(X = k)$ | 1 | 2 | 3 | 4 | 5 | 6 | 5 | 4 | 3 | 2 | 1 |

Soit $P(X = k) = \frac{6 - |k - 7|}{36}$. La somme des probabilités vaut bien $\frac{36}{36} = 1$.
:::

:::definition[Fonction de répartition]
La **fonction de répartition** de $X$ est $F_X : \mathbb{R} \to [0, 1]$, $F_X(x) = P(X \le x)$.
:::

Pour une variable discrète, $F_X$ est **en escalier** : elle saute de $P(X = x)$ en chaque valeur $x$, et reste constante entre deux valeurs. Ses propriétés (vraies pour toute variable aléatoire) :

- $F_X$ est croissante, à valeurs dans $[0, 1]$ ;
- $\lim_{x \to -\infty} F_X(x) = 0$ et $\lim_{x \to +\infty} F_X(x) = 1$ ;
- $F_X$ est continue **à droite** (au point de saut, elle prend la valeur « du haut »).

:::key[Calculer avec $F_X$]
- $P(X \le a) = F_X(a)$ et $P(X > a) = 1 - F_X(a)$ ;
- $P(a < X \le b) = F_X(b) - F_X(a)$ ;
- $P(X < a) = F_X(a^-)$ (limite à gauche) : en discret, attention aux inégalités **strictes** — pour des valeurs entières, $P(X < a) = F_X(a - 1)$.
:::

::item{id="pd-repartition"}

## 4. Espérance

:::definition[Espérance]
Si la série converge absolument, l'**espérance** de $X$ est $E[X] = \sum_{x \in X(\Omega)} x \, P(X = x)$ : la moyenne des valeurs, pondérée par leurs probabilités.
:::

Exemples : pour un dé, $E[X] = \frac{1 + 2 + \cdots + 6}{6} = \frac{7}{2}$ ; pour la somme de deux dés, $E[X] = 7$ (par symétrie de la loi autour de 7, ou par linéarité : $\frac{7}{2} + \frac{7}{2}$).

:::theorem[Propriétés de l'espérance]
- **Linéarité** : $E[aX + bY + c] = a\,E[X] + b\,E[Y] + c$ (toujours, même sans indépendance).
- **Formule de transfert** : $E[g(X)] = \sum_{x} g(x)\, P(X = x)$ — pas besoin de calculer la loi de $g(X)$.
- **Positivité** : si $X \ge 0$, alors $E[X] \ge 0$.
:::

:::warning[$E[g(X)] \neq g(E[X])$ en général]
Pour un dé : $E[X^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15{,}17$, alors que $E[X]^2 = \frac{49}{4} = 12{,}25$.
:::

## 5. Variance et écart-type

:::definition[Variance]
$V(X) = E\big[(X - E[X])^2\big]$ mesure la dispersion autour de la moyenne. L'**écart-type** est $\sigma(X) = \sqrt{V(X)}$, dans la même unité que $X$.
:::

:::theorem[Formule de König-Huygens]
$$V(X) = E[X^2] - E[X]^2.$$
De plus, $V(aX + b) = a^2\, V(X)$ : ajouter une constante ne change pas la dispersion, multiplier par $a$ la multiplie par $a^2$.
:::

Pour un dé : $V(X) = \frac{91}{6} - \frac{49}{4} = \frac{35}{12} \approx 2{,}92$. Pour la somme de deux dés (indépendants) : $V = 2 \times \frac{35}{12} = \frac{35}{6}$.

:::method[Calculer une variance en pratique]
1. Calculer $E[X]$.
2. Calculer $E[X^2] = \sum x^2 P(X = x)$ (formule de transfert).
3. $V(X) = E[X^2] - E[X]^2$. Vérifier que le résultat est **positif** (sinon, il y a une erreur).
:::

::item{id="pd-esperance"}

## 6. Couples de variables aléatoires

### 6.1 Loi jointe, lois marginales

La **loi jointe** du couple $(X, Y)$ est la donnée des $P(X = x, Y = y)$. On retrouve les **lois marginales** en sommant sur l'autre variable :
$$P(X = x) = \sum_{y} P(X = x, Y = y), \qquad P(Y = y) = \sum_x P(X = x, Y = y).$$

:::example[Un couple à valeurs dans $\{0, 1\}^2$]
| | $Y = 0$ | $Y = 1$ | **loi de $X$** |
|---|---|---|---|
| $X = 0$ | 0,1 | 0,3 | **0,4** |
| $X = 1$ | 0,2 | 0,4 | **0,6** |
| **loi de $Y$** | **0,3** | **0,7** | 1 |

Les marges (en gras) sont les sommes des lignes et des colonnes.
:::

### 6.2 Formule de transfert, lois conditionnelles

- $E[g(X, Y)] = \sum_{x, y} g(x, y)\, P(X = x, Y = y)$. Ici : $E[XY] = 1 \times 1 \times 0{,}4 = 0{,}4$.
- **Loi conditionnelle** de $Y$ sachant $X = x$ (si $P(X = x) > 0$) : $P(Y = y \mid X = x) = \frac{P(X = x, Y = y)}{P(X = x)}$. Ici : $P(Y = 0 \mid X = 1) = \frac{0{,}2}{0{,}6} = \frac{1}{3}$ et $P(Y = 1 \mid X = 1) = \frac{2}{3}$.

### 6.3 Indépendance

:::definition[Variables indépendantes]
$X$ et $Y$ sont **indépendantes** si $\forall x, y,\ P(X = x, Y = y) = P(X = x)\, P(Y = y)$.
:::

Dans l'exemple : $P(X = 0, Y = 0) = 0{,}1$ mais $P(X = 0) P(Y = 0) = 0{,}4 \times 0{,}3 = 0{,}12$ : **pas indépendantes**. Un seul couple $(x, y)$ qui ne vérifie pas l'égalité suffit.

### 6.4 Covariance et corrélation

:::definition[Covariance, corrélation]
$\mathrm{Cov}(X, Y) = E\big[(X - E[X])(Y - E[Y])\big] = E[XY] - E[X]\,E[Y]$, et $\rho(X, Y) = \frac{\mathrm{Cov}(X, Y)}{\sigma(X)\,\sigma(Y)} \in [-1, 1]$.
:::

Dans l'exemple : $\mathrm{Cov}(X, Y) = 0{,}4 - 0{,}6 \times 0{,}7 = -0{,}02$.

:::theorem[Variance d'une somme]
$V(X + Y) = V(X) + V(Y) + 2\,\mathrm{Cov}(X, Y)$. Si $X$ et $Y$ sont **indépendantes**, alors $E[XY] = E[X]E[Y]$, donc $\mathrm{Cov}(X, Y) = 0$ et $V(X + Y) = V(X) + V(Y)$.
:::

:::warning[Covariance nulle ≠ indépendance]
Soit $X$ uniforme sur $\{-1, 0, 1\}$ et $Y = X^2$. Alors $E[X] = 0$ et $E[XY] = E[X^3] = 0$, donc $\mathrm{Cov}(X, Y) = 0$. Pourtant $Y$ est une **fonction** de $X$ : $P(X = 0, Y = 0) = \frac{1}{3}$ alors que $P(X = 0)P(Y = 0) = \frac{1}{3} \times \frac{1}{3} = \frac{1}{9}$. L'indépendance entraîne une covariance nulle, mais pas l'inverse.
:::

::item{id="pd-couple"}

## 7. Les lois discrètes usuelles

### 7.1 Uniforme sur $\{1, \ldots, n\}$

Tous les résultats sont équiprobables : $P(X = k) = \frac{1}{n}$. $E[X] = \frac{n+1}{2}$, $V(X) = \frac{n^2 - 1}{12}$. *Exemple : un dé équilibré ($n = 6$).*

### 7.2 Bernoulli $\mathcal{B}(p)$

Une expérience à deux issues, « succès » ($X = 1$) avec probabilité $p$, « échec » ($X = 0$) sinon. $E[X] = p$, $V(X) = p(1 - p)$.

### 7.3 Binomiale $\mathcal{B}(n, p)$

**Nombre de succès** en $n$ répétitions **indépendantes** d'une même épreuve de Bernoulli $\mathcal{B}(p)$ :
$$P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}, \quad k \in \{0, \ldots, n\}.$$
$E[X] = np$ et $V(X) = np(1 - p)$.

:::correction[D'où vient la formule ?]
Une suite de $n$ résultats avec exactement $k$ succès a probabilité $p^k (1-p)^{n-k}$ (indépendance). Il y a $\binom{n}{k}$ telles suites (choix des positions des succès, ch. 11 de FOLO). Et comme $X = X_1 + \cdots + X_n$ avec des $X_i \sim \mathcal{B}(p)$ indépendantes, la linéarité donne $E[X] = np$ et l'indépendance donne $V(X) = np(1-p)$.
:::

### 7.4 Géométrique $\mathcal{G}(p)$

**Rang du premier succès** dans une suite d'épreuves de Bernoulli indépendantes :
$$P(X = k) = (1 - p)^{k - 1}\, p, \quad k \in \mathbb{N}^*.$$
$E[X] = \frac{1}{p}$, $V(X) = \frac{1 - p}{p^2}$, et $P(X > k) = (1 - p)^k$ (les $k$ premiers essais sont des échecs).

**Absence de mémoire** : $P(X > k + m \mid X > k) = P(X > m)$ — avoir déjà échoué $k$ fois ne change rien pour la suite.

### 7.5 Poisson $\mathcal{P}(\lambda)$

Nombre d'**événements rares** sur une période (appels, pannes, requêtes) :
$$P(X = k) = e^{-\lambda} \frac{\lambda^k}{k!}, \quad k \in \mathbb{N}.$$
$E[X] = V(X) = \lambda$.

- Si $X \sim \mathcal{P}(\lambda)$ et $Y \sim \mathcal{P}(\mu)$ sont **indépendantes**, alors $X + Y \sim \mathcal{P}(\lambda + \mu)$.
- **Approximation** : si $n$ est grand et $p$ petit (en pratique $n \ge 30$, $p \le 0{,}1$, $np \le 10$), $\mathcal{B}(n, p) \approx \mathcal{P}(np)$.

### 7.6 Binomiale négative $\mathcal{BN}(r, p)$

Rang du **$r$-ième** succès : $P(X = k) = \binom{k-1}{r-1} p^r (1 - p)^{k - r}$ pour $k \ge r$ (le dernier essai est un succès, et on place les $r - 1$ autres parmi les $k - 1$ premiers). $E[X] = \frac{r}{p}$, $V(X) = \frac{r(1-p)}{p^2}$. Pour $r = 1$, on retrouve la loi géométrique.

### 7.7 Hypergéométrique $\mathcal{H}(N, K, n)$

Tirage **sans remise** de $n$ objets dans une population de $N$ objets dont $K$ « gagnants » ; $X$ = nombre de gagnants tirés :
$$P(X = k) = \frac{\binom{K}{k}\binom{N - K}{n - k}}{\binom{N}{n}}.$$
Avec $p = K/N$ : $E[X] = np$ et $V(X) = np(1 - p)\,\frac{N - n}{N - 1}$. *(Certains cours paramètrent par $(N, p, n)$ avec $K = Np$.)* Avec remise, on aurait une binomiale $\mathcal{B}(n, p)$ : même espérance, variance un peu plus grande.

### 7.8 Multinomiale

Généralisation de la binomiale à $m$ issues de probabilités $p_1, \ldots, p_m$ : sur $n$ épreuves indépendantes, la probabilité d'obtenir $n_1$ fois l'issue 1, …, $n_m$ fois l'issue $m$ ($n_1 + \cdots + n_m = n$) est $\frac{n!}{n_1! \cdots n_m!} p_1^{n_1} \cdots p_m^{n_m}$.

### 7.9 Synthèse

| Loi | Situation | $P(X = k)$ | $E[X]$ | $V(X)$ |
|---|---|---|---|---|
| $\mathcal{U}(\{1..n\})$ | équiprobabilité | $1/n$ | $\frac{n+1}{2}$ | $\frac{n^2-1}{12}$ |
| $\mathcal{B}(p)$ | succès / échec | $p^k(1-p)^{1-k}$ | $p$ | $p(1-p)$ |
| $\mathcal{B}(n, p)$ | nb de succès sur $n$ essais indépendants | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| $\mathcal{G}(p)$ | rang du 1er succès | $(1-p)^{k-1}p$ | $1/p$ | $(1-p)/p^2$ |
| $\mathcal{P}(\lambda)$ | événements rares | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ |
| $\mathcal{BN}(r, p)$ | rang du $r$-ième succès | $\binom{k-1}{r-1}p^r(1-p)^{k-r}$ | $r/p$ | $r(1-p)/p^2$ |
| $\mathcal{H}(N, K, n)$ | tirage sans remise | $\binom{K}{k}\binom{N-K}{n-k}/\binom{N}{n}$ | $np$ | $np(1-p)\frac{N-n}{N-1}$ |

::item{id="pd-reconnaitre"}

## 8. Exercices corrigés

:::exercise[Exercice 1 — Une urne]
Une urne contient 3 boules rouges et 2 bleues. On tire 2 boules **sans remise** ; $X$ est le nombre de boules rouges tirées. Donner la loi de $X$, son espérance et sa variance.
:::

:::correction
Il y a $\binom{5}{2} = 10$ tirages équiprobables.
- $P(X = 0) = \frac{\binom{2}{2}}{10} = \frac{1}{10}$ (les deux bleues) ;
- $P(X = 1) = \frac{3 \times 2}{10} = \frac{6}{10}$ (une rouge parmi 3, une bleue parmi 2) ;
- $P(X = 2) = \frac{\binom{3}{2}}{10} = \frac{3}{10}$.

Somme : $1$. $E[X] = 0 + 0{,}6 + 0{,}6 = 1{,}2$ et $E[X^2] = 0{,}6 + 4 \times 0{,}3 = 1{,}8$, donc $V(X) = 1{,}8 - 1{,}44 = 0{,}36$.

C'est une loi hypergéométrique ($N = 5$, $K = 3$, $n = 2$) : $np = 2 \times 0{,}6 = 1{,}2$ et $np(1-p)\frac{N - n}{N - 1} = 1{,}2 \times 0{,}4 \times \frac{3}{4} = 0{,}36$. ✔
:::

:::exercise[Exercice 2 — Changement d'unité]
La température $X$ (en °C) d'une salle serveur a pour espérance 20 et pour écart-type 5. Quelles sont l'espérance et l'écart-type de la température $Y$ en degrés Fahrenheit, sachant que $Y = 1{,}8\,X + 32$ ?
:::

:::correction
Linéarité : $E[Y] = 1{,}8 \times 20 + 32 = 68$. Variance : $V(Y) = 1{,}8^2 \times V(X) = 3{,}24 \times 25 = 81$, donc $\sigma(Y) = 9$ (soit $1{,}8 \times 5$ : l'écart-type est multiplié par $|a|$, le décalage $+32$ ne compte pas).
:::

:::exercise[Exercice 3 — Un jeu de grattage]
Un ticket coûte 2 €. On gagne 100 € avec probabilité $\frac{1}{100}$, 10 € avec probabilité $\frac{1}{20}$, rien sinon. Le jeu est-il favorable au joueur ?
:::

:::correction
Soit $L$ le lot : $E[L] = 100 \times \frac{1}{100} + 10 \times \frac{1}{20} = 1 + 0{,}5 = 1{,}5$ €. Le gain net est $G = L - 2$, donc $E[G] = -0{,}5$ € : en moyenne, le joueur **perd** 50 centimes par ticket. Le jeu est défavorable.
:::

:::exercise[Exercice 4 — Avec ou sans remise]
Un sac contient 10 jetons dont 4 gagnants. On en tire 3. Donner la loi du nombre $X$ de jetons gagnants (a) sans remise, (b) avec remise. Comparer espérances et variances.
:::

:::correction
**(a) Sans remise** : $\mathcal{H}(10, 4, 3)$, avec $\binom{10}{3} = 120$ :
$P(X = 0) = \frac{\binom{6}{3}}{120} = \frac{1}{6}$, $P(X = 1) = \frac{4 \times 15}{120} = \frac{1}{2}$, $P(X = 2) = \frac{6 \times 6}{120} = \frac{3}{10}$, $P(X = 3) = \frac{4}{120} = \frac{1}{30}$.
$E[X] = 3 \times 0{,}4 = 1{,}2$ ; $V(X) = 1{,}2 \times 0{,}6 \times \frac{7}{9} = 0{,}56$.

**(b) Avec remise** : $\mathcal{B}(3, 0{,}4)$ : $P(X = k) = \binom{3}{k} 0{,}4^k\, 0{,}6^{3-k}$, soit $0{,}216$ ; $0{,}432$ ; $0{,}288$ ; $0{,}064$.
$E[X] = 1{,}2$ ; $V(X) = 3 \times 0{,}4 \times 0{,}6 = 0{,}72$.

Même espérance ; le tirage sans remise est **moins dispersé** (facteur $\frac{N - n}{N - 1} = \frac{7}{9}$).
:::

:::exercise[Exercice 5 — Pièces défectueuses]
Une usine produit des composants défectueux avec probabilité $p = 0{,}002$, indépendamment. Dans un lot de 1000 composants, quelle est la probabilité de n'en trouver aucun défectueux ? Au plus deux ? Comparer avec l'approximation de Poisson.
:::

:::correction
$X \sim \mathcal{B}(1000;\ 0{,}002)$. Exactement : $P(X = 0) = 0{,}998^{1000} \approx 0{,}1351$.

Approximation : $n$ grand, $p$ petit, $np = 2$ : $X \approx \mathcal{P}(2)$. $P(X = 0) \approx e^{-2} \approx 0{,}1353$ (écart de l'ordre de $3 \times 10^{-4}$) et $P(X \le 2) \approx e^{-2}\left(1 + 2 + \frac{2^2}{2}\right) = 5e^{-2} \approx 0{,}677$ (valeur exacte $\approx 0{,}677$).
:::

:::exercise[Exercice 6 — Essayer jusqu'à réussir]
Un programme réussit un test avec probabilité $0{,}3$ à chaque exécution, indépendamment. $N$ est le nombre d'exécutions jusqu'au premier succès. Calculer $E[N]$, $P(N > 3)$ et $P(N > 5 \mid N > 2)$.
:::

:::correction
$N \sim \mathcal{G}(0{,}3)$. $E[N] = \frac{1}{0{,}3} \approx 3{,}33$. $P(N > 3) = 0{,}7^3 = 0{,}343$ (trois échecs). Par absence de mémoire, $P(N > 5 \mid N > 2) = P(N > 3) = 0{,}343$. Vérification : $\frac{P(N > 5)}{P(N > 2)} = \frac{0{,}7^5}{0{,}7^2} = 0{,}7^3$.
:::

::item{id="pd-exercices"}

## 9. Fiche récapitulative

:::key[L'essentiel]
- Loi : $p(x) \ge 0$, $\sum p(x) = 1$ ; $P(X \in B) = \sum_{x \in B} p(x)$.
- $F(x) = P(X \le x)$ : escalier, croissante, de 0 à 1, continue à droite ; attention aux inégalités strictes.
- $E[X] = \sum x\,p(x)$, linéaire ; $E[g(X)] = \sum g(x) p(x)$ (transfert).
- $V(X) = E[X^2] - E[X]^2$ ; $V(aX + b) = a^2 V(X)$.
- Indépendance ⇒ $\mathrm{Cov} = 0$ et $V(X+Y) = V(X) + V(Y)$ ; la réciproque est fausse.
- Lois : Bernoulli, binomiale (nb de succès), géométrique (rang du 1er succès, sans mémoire), Poisson ($E = V = \lambda$, approxime la binomiale), hypergéométrique (sans remise).
:::
