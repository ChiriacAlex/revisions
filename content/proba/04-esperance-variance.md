---
title: Ch2 — Espérance et variance
summary: La valeur moyenne et la dispersion d'une variable aléatoire, discrète ou continue — définitions, König-Huygens, propriétés, existence, inégalités de Markov et Tchebychev, loi des grands nombres.
tags: [chapitre 2, espérance, variance, Tchebychev]
minutes: 70
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- calculer l'**espérance** d'une variable discrète (somme) ou continue (intégrale) ;
- calculer la **variance** avec la formule de **König-Huygens**, et l'**écart-type** ;
- utiliser la **linéarité** de l'espérance et la règle $V(aX + b) = a^2 V(X)$ ;
- reconnaître quand une espérance ou une variance **n'existe pas** ;
- connaître les espérances et variances des lois usuelles ;
- appliquer l'inégalité de **Bienaymé-Tchebychev** et comprendre la **loi des grands nombres**.

:::intuition[Le fil conducteur]
On lance un dé équilibré : quel résultat obtient-on **en moyenne** après de nombreux lancers ? C'est l'**espérance** $E(X)$. Mais deux jeux de même moyenne peuvent avoir des risques très différents : la **variance** $V(X)$ mesure à quel point les résultats **s'écartent** de cette moyenne.
:::

## 2. L'espérance

:::definition[Espérance]
- **Variable discrète** de loi $(x_i, p_i)_i$ : $E[X] = \sum_i x_i\, P(X = x_i)$.
- **Variable continue** de densité $f$ : $E[X] = \int_{-\infty}^{+\infty} x\, f(x)\,dx$.
:::

La formule continue est la limite de la formule discrète : en découpant l'axe en petits intervalles de largeur $\delta x$, $P(x_i \le X \le x_i + \delta x) \approx f(x_i)\,\delta x$, donc $E[X] \approx \sum_i x_i f(x_i)\,\delta x$. On remplace encore $\sum$ par $\int$.

:::intuition[Interprétation]
L'espérance est la valeur moyenne obtenue quand l'expérience est **répétée un très grand nombre de fois** (c'est la loi des grands nombres, § 7). C'est aussi le « centre de gravité » de la loi.
:::

:::example[Un dé équilibré]
$E[X] = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + \cdots + 6 \cdot \frac{1}{6} = \frac{21}{6} = 3{,}5$. Une valeur que le dé ne donne jamais : l'espérance n'est pas forcément un résultat possible.
:::

### Exemple : la compétition de tir à l'arc

Une cible de rayon $0{,}5$ m a 10 zones concentriques de même largeur, qui rapportent de 10 points (centre) à 1 point (extérieur). La flèche tombe uniformément sur la cible.

**Le score (variable discrète).** La probabilité d'une zone est proportionnelle à son aire : $P(X = x) = \frac{21 - 2x}{100}$ pour $x \in \{1, \ldots, 10\}$ (de $\frac{19}{100}$ pour 1 point à $\frac{1}{100}$ pour 10 points). Alors
$$E[X] = \sum_{x=1}^{10} x \cdot \frac{21 - 2x}{100} = \frac{21 \times 55 - 2 \times 385}{100} = 3{,}85.$$

**La distance au centre (variable continue).** $P(X \le r) = \frac{\pi r^2}{\pi\, 0{,}5^2} = 4r^2$, d'où la densité $f(x) = 8x$ sur $[0 ;\ 0{,}5]$. Alors
$$E[X] = \int_0^{0{,}5} x \cdot 8x\,dx = \left[\frac{8x^3}{3}\right]_0^{0{,}5} = \frac{1}{3} \approx 0{,}33 \text{ m}.$$

Si l'on tire un grand nombre de flèches, on marque en moyenne $3{,}85$ points, et la flèche tombe en moyenne à $0{,}33$ m du centre.

## 3. L'espérance ne suffit pas : la variance

:::example[Deux jeux de même espérance]
- **Jeu A** : on gagne 4 € ou 6 € (une chance sur deux chacun).
- **Jeu B** : on gagne 1 € ou 9 € (une chance sur deux chacun).

Les deux ont la même espérance, $5$ €, mais le jeu B est bien plus **risqué** : ses résultats sont plus dispersés.
:::

:::example[Deux types d'ampoules]
- **Type A** : la durée de vie suit une loi uniforme sur $[900, 1100]$ heures : $E = 1000$ h.
- **Type B** : 80 % des ampoules durent exactement 1000 h, mais 20 % seulement 600 h.

Le type A est prévisible (toujours entre 900 et 1100 h) ; le type B présente un risque non négligeable de panne précoce.
:::

:::warning[Erreur dans les slides du cours]
Les slides affirment que les deux types d'ampoules ont la même espérance de 1000 heures. C'est **faux pour le type B** : $E = 0{,}8 \times 1000 + 0{,}2 \times 600 = 920$ heures. De plus, la durée du type B ne prend que deux valeurs : c'est une variable **discrète**, pas continue. Le message du cours reste juste (la dispersion compte autant que la moyenne), mais retiens les bons chiffres.
:::

:::definition[Variance et écart-type]
La **variance** de $X$ mesure la dispersion autour de la moyenne :
$$V(X) = E\big[(X - E[X])^2\big].$$
L'**écart-type** est $\sigma(X) = \sqrt{V(X)}$ : il s'exprime dans la **même unité** que $X$.
:::

- Une **faible** variance : les valeurs sont proches de l'espérance, donc prévisibles et fiables.
- Une **forte** variance : grande dispersion, donc plus d'incertitude et plus de risque.

Pour les deux jeux : $V_A = \frac{(4-5)^2 + (6-5)^2}{2} = 1$ et $V_B = \frac{(1-5)^2 + (9-5)^2}{2} = 16$ : le jeu B est 16 fois plus dispersé (écart-type 4 € contre 1 €).

:::theorem[Formule de König-Huygens]
$$V(X) = E[X^2] - E[X]^2.$$
:::

:::correction[Voir la preuve]
Notons $m = E[X]$, un nombre. En développant et par linéarité de l'espérance :
$$V(X) = E[X^2 - 2mX + m^2] = E[X^2] - 2m\,E[X] + m^2 = E[X^2] - 2m^2 + m^2 = E[X^2] - m^2. \qquad \square$$
:::

Pour calculer $E[X^2]$, on utilise la **formule de transfert** : $E[X^2] = \sum x_i^2\, P(X = x_i)$ ou $\int x^2 f(x)\,dx$.

:::example[Le dé]
$E[X^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6}$, donc $V(X) = \frac{91}{6} - 3{,}5^2 = \frac{35}{12} \approx 2{,}92$ et $\sigma \approx 1{,}71$.
:::

### Retour au tir à l'arc

- **Score** : $E[X^2] = \sum_{x=1}^{10} x^2 \cdot \frac{21 - 2x}{100} = \frac{21 \times 385 - 2 \times 3025}{100} = 20{,}35$, donc $V(X) = 20{,}35 - 3{,}85^2 = 5{,}5275$ et $\sigma \approx 2{,}35$ points.
- **Distance** : $E[X^2] = \int_0^{0{,}5} x^2 \cdot 8x\,dx = 0{,}125$, donc $V(X) = 0{,}125 - \frac{1}{9} = \frac{1}{72} \approx 0{,}0139$ m² et $\sigma \approx 0{,}118$ m.

:::warning[Erreurs dans les slides du cours]
Les slides donnent $E[X^2] = 18{,}27$ et « écart-type $3{,}5$ » pour le score, puis « écart-type $0{,}016$ » pour la distance. Trois corrections :
1. $E[X^2] = 20{,}35$ (et non $18{,}27$), donc $V(X) \approx 5{,}53$ ;
2. les valeurs calculées $E[X^2] - E[X]^2$ sont des **variances**, pas des écarts-types : $\sigma = \sqrt{V}$ ;
3. pour la distance, arrondir $E[X]$ à $0{,}33$ **avant** de l'élever au carré fausse le résultat ($0{,}016$ au lieu de $\frac{1}{72} \approx 0{,}0139$). Garde les valeurs exactes ($\frac{1}{3}$) jusqu'au bout.
:::

::item{id="ev-definitions"}

## 4. Propriétés

:::theorem[Propriétés de l'espérance et de la variance]
Pour des variables admettant espérance (et variance), et des réels $a, b$ :
- **linéarité** : $E[aX + b] = a\,E[X] + b$ et $E[X + Y] = E[X] + E[Y]$ (toujours) ;
- **positivité** : si $X \ge 0$, $E[X] \ge 0$ ; et $V(X) \ge 0$ ;
- **variance d'une transformation affine** : $V(aX + b) = a^2\, V(X)$ et $\sigma(aX + b) = |a|\,\sigma(X)$ ;
- $V(X) = 0$ si et seulement si $X$ est constante (presque sûrement) ;
- si $X$ et $Y$ sont **indépendantes** : $V(X + Y) = V(X) + V(Y)$.
:::

:::correction[Voir la preuve de $V(aX + b) = a^2 V(X)$]
$E[aX + b] = am + b$ avec $m = E[X]$, donc $(aX + b) - E[aX + b] = a(X - m)$ et $V(aX + b) = E[a^2 (X - m)^2] = a^2\, V(X)$. Ajouter une constante décale toutes les valeurs **sans changer leur dispersion**.
:::

:::method[Centrer et réduire]
Si $V(X) > 0$, la variable $Z = \frac{X - E[X]}{\sigma(X)}$ vérifie $E[Z] = 0$ et $V(Z) = 1$. Réciproquement, si l'on connaît $E[Z]$ et $V(Z)$ pour une loi « de référence », on en déduit ceux de $X = m + \sigma Z$ : $E[X] = m + \sigma E[Z]$ et $V(X) = \sigma^2 V(Z)$. C'est la méthode du TD pour les lois uniforme, exponentielle et normale.
:::

## 5. Existence : quand l'espérance n'existe pas

En continu, $E[X]$ n'existe que si l'intégrale $\int_{-\infty}^{+\infty} |x|\, f(x)\,dx$ **converge** (en discret : si la série converge absolument). De même, $V(X)$ n'existe que si $E[X^2]$ est finie.

:::example[Des lois à « queue lourde »]
Sur $[1, +\infty[$ :
- $f(x) = \frac{1}{x^2}$ est une densité, mais $\int_1^{+\infty} x \cdot \frac{1}{x^2}\,dx = \int_1^{+\infty} \frac{dx}{x}$ **diverge** : pas d'espérance.
- $f(x) = \frac{2}{x^3}$ : $E[X] = \int_1^{+\infty} \frac{2}{x^2}\,dx = 2$ existe, mais $E[X^2] = \int_1^{+\infty} \frac{2}{x}\,dx$ diverge : **pas de variance**.
- $f(x) = \frac{3}{x^4}$ : espérance **et** variance existent (TD, exercice 1).

Règle : $\int_1^{+\infty} \frac{dx}{x^\alpha}$ converge si et seulement si $\alpha > 1$.
:::

::item{id="ev-existence"}

## 6. Espérances et variances des lois usuelles

| Loi | $E[X]$ | $V(X)$ |
|---|---|---|
| Bernoulli $\mathcal{B}(p)$ | $p$ | $p(1-p)$ |
| Binomiale $\mathcal{B}(n, p)$ | $np$ | $np(1-p)$ |
| Géométrique $\mathcal{G}(p)$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ |
| Poisson $\mathcal{P}(\lambda)$ | $\lambda$ | $\lambda$ |
| Uniforme $\mathcal{U}([a, b])$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| Exponentielle $\mathcal{E}(\lambda)$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| Normale $\mathcal{N}(m, \sigma^2)$ | $m$ | $\sigma^2$ |

Les démonstrations pour les lois continues sont faites dans le TD (exercices 2, 3 et 4). Exemple : pour les ampoules de type A, $V = \frac{200^2}{12} \approx 3333$ h², soit $\sigma \approx 58$ h ; pour le type B, $V = 0{,}8 \times 1000^2 + 0{,}2 \times 600^2 - 920^2 = 25\,600$ h², soit $\sigma = 160$ h : le type B est presque trois fois plus dispersé.

::item{id="ev-lois"}

## 7. Inégalités et loi des grands nombres

:::theorem[Inégalité de Markov]
Si $Y \ge 0$ admet une espérance, alors pour tout $a > 0$ : $P(Y \ge a) \le \dfrac{E[Y]}{a}$.
:::

:::correction[Voir la preuve (cas à densité)]
$E[Y] = \int_0^{+\infty} y f(y)\,dy \ge \int_a^{+\infty} y f(y)\,dy \ge \int_a^{+\infty} a f(y)\,dy = a\,P(Y \ge a)$. (Même preuve avec des sommes en discret.) $\square$
:::

:::theorem[Inégalité de Bienaymé-Tchebychev]
Si $X$ admet une variance, alors pour tout $\varepsilon > 0$ : $P\big(|X - E[X]| \ge \varepsilon\big) \le \dfrac{V(X)}{\varepsilon^2}$.
:::

:::correction[Voir la preuve]
On applique Markov à $Y = (X - E[X])^2 \ge 0$ et $a = \varepsilon^2$ : $P(|X - E[X]| \ge \varepsilon) = P(Y \ge \varepsilon^2) \le \frac{E[Y]}{\varepsilon^2} = \frac{V(X)}{\varepsilon^2}$. $\square$
:::

Interprétation : une variable s'écarte rarement de sa moyenne de plus de quelques écarts-types. Avec $\varepsilon = k\sigma$ : $P(|X - E[X]| \ge k\sigma) \le \frac{1}{k^2}$ (au plus 25 % au-delà de $2\sigma$, quelle que soit la loi).

:::theorem[Loi faible des grands nombres]
Soient $X_1, \ldots, X_n$ indépendantes, de même loi, d'espérance $m$ et de variance $\sigma^2$, et $\overline{X}_n = \frac{X_1 + \cdots + X_n}{n}$. Alors $E[\overline{X}_n] = m$, $V(\overline{X}_n) = \frac{\sigma^2}{n}$, et pour tout $\varepsilon > 0$ :
$$P\big(|\overline{X}_n - m| > \varepsilon\big) \le \frac{\sigma^2}{n\varepsilon^2} \xrightarrow[n \to +\infty]{} 0.$$
On dit que $\overline{X}_n$ **converge en probabilité** vers $m$ (preuve : TD, exercice 5).
:::

C'est ce qui justifie l'interprétation de l'espérance : la moyenne de nombreux essais se rapproche de $E[X]$.

## 8. Application : les files d'attente

Dans un centre d'appels, à un guichet ou sur une ligne de production :
- l'**espérance** prévoit le temps d'attente moyen ou le nombre moyen de clients en attente ;
- la **variance** mesure l'irrégularité : une variance élevée signifie des attentes très inégales, avec des pics qui dégradent la satisfaction.

En ajustant les temps de service ou en ouvrant des guichets aux heures de pointe, on réduit la variance des temps d'attente, et donc les pics, même à moyenne égale.

::item{id="ev-tchebychev"}

## 9. Fiche récapitulative

:::key[L'essentiel]
- $E[X] = \sum x_i P(X = x_i)$ ou $\int x f(x)\,dx$ ; elle n'existe que si la somme/l'intégrale converge **absolument**.
- $V(X) = E[(X - E[X])^2] = E[X^2] - E[X]^2$ (König-Huygens) ; $\sigma = \sqrt{V}$, dans l'unité de $X$.
- $E[aX + b] = aE[X] + b$ ; $V(aX + b) = a^2 V(X)$ ; si indépendantes, $V(X + Y) = V(X) + V(Y)$.
- Garde les valeurs **exactes** ($\frac{1}{3}$, pas $0{,}33$) jusqu'à la fin du calcul.
- Tchebychev : $P(|X - E[X]| \ge \varepsilon) \le \frac{V(X)}{\varepsilon^2}$ ; la moyenne empirique converge en probabilité vers $m$.
:::
