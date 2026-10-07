---
title: Ch1 — Loi et répartition d'une variable aléatoire continue
summary: Pourquoi le continu change tout, tribus, densités, fonction de répartition, changement de variable, et les lois uniforme, exponentielle, normale (et Gamma).
tags: [chapitre 1, densité, loi normale, exponentielle]
minutes: 90
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- distinguer variable **discrète** et variable **continue** ;
- vérifier qu'une fonction est une **densité** et s'en servir pour calculer des probabilités ;
- passer de la densité à la **fonction de répartition** et inversement ;
- déterminer la loi de $g(X)$ (**changement de variable**) sans se tromper ;
- utiliser les lois **uniforme**, **exponentielle** et **normale**, et lire une table de $\Phi$.

:::intuition[Le fil conducteur]
En discret, on donne la probabilité **de chaque valeur** et on **additionne**. En continu, chaque valeur isolée a une probabilité **nulle** : on donne une **densité** $f$ et on **intègre**. Presque tout le chapitre consiste à remplacer $\sum$ par $\int$.
:::

## 2. Pourquoi le continu pose problème

Imagine une roue de loterie numérotée de $0$ à $1$ en continu, qu'on fait tourner « au hasard ». Le résultat $X$ peut être **n'importe quel** réel de $[0, 1[$.

- La probabilité de tomber sur un intervalle est sa **longueur** : $P(0{,}2 \le X \le 0{,}5) = 0{,}3$.
- Mais la probabilité de tomber **exactement** sur $0{,}3$ est nulle : $0{,}3$ est contenu dans $[0{,}3 - \varepsilon,\ 0{,}3 + \varepsilon]$ pour tout $\varepsilon > 0$, donc $P(X = 0{,}3) \le 2\varepsilon$, pour tout $\varepsilon$.

Paradoxe apparent : chaque point a probabilité $0$, et pourtant $P(X \in [0, 1[) = 1$. Il n'y a pas de contradiction : $[0, 1[$ n'est pas une union **dénombrable** de points, on ne peut pas « additionner » ses points un par un. En continu, on ne mesure plus des **points**, on mesure des **ensembles de valeurs**, typiquement des **intervalles**.

## 3. Tribus et loi d'une variable aléatoire

On ne peut pas, en continu, attribuer une probabilité à **toutes** les parties de $\Omega$ de façon cohérente (il existe des ensembles « pathologiques », comme l'ensemble de Vitali). On se restreint à une famille d'ensembles mesurables.

:::definition[Tribu (σ-algèbre)]
Une famille $\mathcal{F}$ de parties de $\Omega$ est une **tribu** si :
- $\emptyset \in \mathcal{F}$ ;
- elle est stable par **complémentaire** : $A \in \mathcal{F} \Rightarrow A^\complement \in \mathcal{F}$ ;
- elle est stable par **union dénombrable** : $A_1, A_2, \ldots \in \mathcal{F} \Rightarrow \bigcup_n A_n \in \mathcal{F}$.
:::

Ce sont exactement les opérations du raisonnement sur les événements : « contraire », « l'un ou l'autre » (et, par complémentaire, « l'un et l'autre »).

:::example
Sur $\Omega = \{a, b, c, d\}$ : $\{\emptyset, \{a\}, \{b, c, d\}, \Omega\}$ est une tribu. En revanche $\{\emptyset, \{a\}, \Omega\}$ n'en est pas une : le complémentaire $\{b, c, d\}$ de $\{a\}$ manque. Sur $\mathbb{R}$, $\{\emptyset, \mathbb{R}\}$ est la plus petite tribu et $\mathcal{P}(\mathbb{R})$ la plus grande.
:::

Sur $\mathbb{R}$, on utilise la **tribu borélienne** $\mathcal{B}(\mathbb{R})$ : la plus petite tribu qui contient tous les intervalles. Elle contient les intervalles ouverts, fermés, semi-ouverts, les points ($\{a\} = \bigcap_n\, ]a - \frac{1}{n}, a + \frac{1}{n}[$), les ensembles dénombrables ($\mathbb{N}$, $\mathbb{Q}$) et toutes leurs unions et intersections dénombrables. **En pratique, tous les ensembles que tu rencontreras sont boréliens.**

:::definition[Loi d'une variable aléatoire]
La **loi** de $X$ est l'application $P_X : B \in \mathcal{B}(\mathbb{R}) \mapsto P(X \in B) = P(X^{-1}(B))$. Pour toute famille finie ou dénombrable $(B_n)$ de boréliens **deux à deux disjoints**, $P_X(\bigcup_n B_n) = \sum_n P_X(B_n)$.
:::

C'est la même définition qu'en discret ; seule la famille des ensembles $B$ autorisés a changé.

::item{id="pc-tribu"}

## 4. Densité de probabilité

:::definition[Densité]
Une fonction $f : \mathbb{R} \to \mathbb{R}$ est une **densité de probabilité** si :
- $f$ est **positive** et **continue par morceaux** ;
- $\int_{-\infty}^{+\infty} f(t)\,dt$ **converge et vaut 1**.

$X$ admet la densité $f$ si, pour tous $a \le b$ (et plus généralement tout borélien) : $P(a \le X \le b) = \int_a^b f(t)\,dt$.
:::

<figure><svg viewBox="0 0 360 220" role="img" aria-label="Densité 3x² et l'aire P(X ≥ 1/2)"><line x1="40" y1="180.0" x2="348" y2="180.0" class="stroke"/><line x1="40.0" y1="180" x2="40.0" y2="14" class="stroke"/><text x="40.0" y="195.0" text-anchor="middle" font-size="11">0</text><text x="176.4" y="195.0" text-anchor="middle" font-size="11">0,5</text><text x="312.7" y="195.0" text-anchor="middle" font-size="11">1</text><line x1="40" y1="130.0" x2="340" y2="130.0" class="muted" stroke-dasharray="2 4"/><text x="34" y="134.0" text-anchor="end" font-size="11">1</text><line x1="40" y1="80.0" x2="340" y2="80.0" class="muted" stroke-dasharray="2 4"/><text x="34" y="84.0" text-anchor="end" font-size="11">2</text><line x1="40" y1="30.0" x2="340" y2="30.0" class="muted" stroke-dasharray="2 4"/><text x="34" y="34.0" text-anchor="end" font-size="11">3</text><text x="350" y="184.0" font-size="12">x</text><text x="46" y="16" font-size="12">f(x)</text><path d="M176.4,142.5 L177.5,141.9 L178.6,141.2 L179.8,140.6 L180.9,140.0 L182.0,139.3 L183.2,138.7 L184.3,138.0 L185.5,137.3 L186.6,136.7 L187.7,136.0 L188.9,135.3 L190.0,134.6 L191.1,133.9 L192.3,133.2 L193.4,132.5 L194.5,131.8 L195.7,131.1 L196.8,130.4 L198.0,129.7 L199.1,129.0 L200.2,128.2 L201.4,127.5 L202.5,126.7 L203.6,126.0 L204.8,125.2 L205.9,124.5 L207.0,123.7 L208.2,123.0 L209.3,122.2 L210.5,121.4 L211.6,120.6 L212.7,119.8 L213.9,119.0 L215.0,118.2 L216.1,117.4 L217.3,116.6 L218.4,115.8 L219.5,115.0 L220.7,114.2 L221.8,113.3 L223.0,112.5 L224.1,111.7 L225.2,110.8 L226.4,110.0 L227.5,109.1 L228.6,108.2 L229.8,107.4 L230.9,106.5 L232.0,105.6 L233.2,104.7 L234.3,103.9 L235.5,103.0 L236.6,102.1 L237.7,101.2 L238.9,100.2 L240.0,99.3 L241.1,98.4 L242.3,97.5 L243.4,96.6 L244.5,95.6 L245.7,94.7 L246.8,93.7 L248.0,92.8 L249.1,91.8 L250.2,90.9 L251.4,89.9 L252.5,88.9 L253.6,88.0 L254.8,87.0 L255.9,86.0 L257.0,85.0 L258.2,84.0 L259.3,83.0 L260.5,82.0 L261.6,81.0 L262.7,80.0 L263.9,78.9 L265.0,77.9 L266.1,76.9 L267.3,75.8 L268.4,74.8 L269.5,73.7 L270.7,72.7 L271.8,71.6 L273.0,70.6 L274.1,69.5 L275.2,68.4 L276.4,67.3 L277.5,66.2 L278.6,65.2 L279.8,64.1 L280.9,63.0 L282.0,61.9 L283.2,60.7 L284.3,59.6 L285.5,58.5 L286.6,57.4 L287.7,56.2 L288.9,55.1 L290.0,54.0 L291.1,52.8 L292.3,51.7 L293.4,50.5 L294.5,49.3 L295.7,48.2 L296.8,47.0 L298.0,45.8 L299.1,44.6 L300.2,43.4 L301.4,42.2 L302.5,41.0 L303.6,39.8 L304.8,38.6 L305.9,37.4 L307.0,36.2 L308.2,35.0 L309.3,33.7 L310.5,32.5 L311.6,31.2 L312.7,30.0 L312.7,180.0 L176.4,180.0 Z" class="venn-fill"/><path d="M40.0,180.0 L41.7,180.0 L43.4,180.0 L45.1,179.9 L46.8,179.9 L48.5,179.9 L50.2,179.8 L51.9,179.7 L53.6,179.6 L55.3,179.5 L57.0,179.4 L58.8,179.3 L60.5,179.2 L62.2,179.0 L63.9,178.9 L65.6,178.7 L67.3,178.5 L69.0,178.3 L70.7,178.1 L72.4,177.9 L74.1,177.7 L75.8,177.4 L77.5,177.2 L79.2,176.9 L80.9,176.6 L82.6,176.3 L84.3,176.0 L86.0,175.7 L87.7,175.4 L89.4,175.1 L91.1,174.7 L92.8,174.4 L94.5,174.0 L96.2,173.6 L98.0,173.2 L99.7,172.8 L101.4,172.4 L103.1,172.0 L104.8,171.5 L106.5,171.1 L108.2,170.6 L109.9,170.2 L111.6,169.7 L113.3,169.2 L115.0,168.7 L116.7,168.1 L118.4,167.6 L120.1,167.1 L121.8,166.5 L123.5,165.9 L125.2,165.4 L126.9,164.8 L128.6,164.2 L130.3,163.5 L132.0,162.9 L133.8,162.3 L135.5,161.6 L137.2,161.0 L138.9,160.3 L140.6,159.6 L142.3,158.9 L144.0,158.2 L145.7,157.5 L147.4,156.7 L149.1,156.0 L150.8,155.2 L152.5,154.5 L154.2,153.7 L155.9,152.9 L157.6,152.1 L159.3,151.3 L161.0,150.5 L162.7,149.6 L164.4,148.8 L166.1,147.9 L167.8,147.0 L169.5,146.2 L171.2,145.3 L173.0,144.4 L174.7,143.4 L176.4,142.5 L178.1,141.6 L179.8,140.6 L181.5,139.6 L183.2,138.7 L184.9,137.7 L186.6,136.7 L188.3,135.7 L190.0,134.6 L191.7,133.6 L193.4,132.5 L195.1,131.5 L196.8,130.4 L198.5,129.3 L200.2,128.2 L201.9,127.1 L203.6,126.0 L205.3,124.9 L207.0,123.7 L208.8,122.6 L210.5,121.4 L212.2,120.2 L213.9,119.0 L215.6,117.8 L217.3,116.6 L219.0,115.4 L220.7,114.2 L222.4,112.9 L224.1,111.7 L225.8,110.4 L227.5,109.1 L229.2,107.8 L230.9,106.5 L232.6,105.2 L234.3,103.9 L236.0,102.5 L237.7,101.2 L239.4,99.8 L241.1,98.4 L242.8,97.0 L244.5,95.6 L246.2,94.2 L248.0,92.8 L249.7,91.4 L251.4,89.9 L253.1,88.4 L254.8,87.0 L256.5,85.5 L258.2,84.0 L259.9,82.5 L261.6,81.0 L263.3,79.4 L265.0,77.9 L266.7,76.4 L268.4,74.8 L270.1,73.2 L271.8,71.6 L273.5,70.0 L275.2,68.4 L276.9,66.8 L278.6,65.2 L280.3,63.5 L282.0,61.9 L283.8,60.2 L285.5,58.5 L287.2,56.8 L288.9,55.1 L290.6,53.4 L292.3,51.7 L294.0,49.9 L295.7,48.2 L297.4,46.4 L299.1,44.6 L300.8,42.8 L302.5,41.0 L304.2,39.2 L305.9,37.4 L307.6,35.6 L309.3,33.7 L311.0,31.9 L312.7,30.0" class="accent" stroke-width="2"/><line x1="312.7" y1="30.0" x2="312.7" y2="180.0" class="accent" stroke-dasharray="3 3"/><text x="252.7" y="152.5" text-anchor="middle" font-size="12">7/8</text></svg></figure>

*La densité $f(x) = 3x^2$ sur $[0, 1]$ (nulle ailleurs) : $P(X \ge \frac{1}{2}) = \int_{1/2}^1 3t^2\,dt = 1 - \frac{1}{8} = \frac{7}{8}$ est l'aire colorée.*

:::warning[Une densité n'est pas une probabilité]
$f(x)$ **n'est pas** $P(X = x)$ (qui vaut $0$). Et $f$ peut dépasser $1$ : sur la figure, $f(1) = 3$. Seules les **aires** sous la courbe sont des probabilités. Intuitivement, $f(x)\,dx \approx P(x \le X \le x + dx)$ : c'est une probabilité **par unité de longueur**, comme une masse volumique.
:::

:::theorem[Conséquences]
Si $X$ a une densité, alors $P(X = a) = 0$ pour tout $a$, et les bornes ne comptent pas :
$$P(a \le X \le b) = P(a < X \le b) = P(a \le X < b) = P(a < X < b) = \int_a^b f(t)\,dt.$$
:::

:::method[Vérifier qu'une fonction est une densité]
1. **Positivité** : $f(x) \ge 0$ pour tout $x$ (cela impose souvent le signe d'un paramètre).
2. **Continuité par morceaux** (en général évidente).
3. **Intégrale** : calculer $\int_{-\infty}^{+\infty} f$ en découpant selon les morceaux de $f$ (là où $f = 0$, l'intégrale est nulle) ; vérifier qu'elle **converge** et vaut $1$. Avec un paramètre $k$, l'égalité « $= 1$ » donne $k$.
4. **Dessiner** la densité : une probabilité est une aire.
:::

:::example[Trouver la constante]
$f(x) = k(1 - x^2)$ sur $[-1, 1]$, $0$ ailleurs. Positivité : $1 - x^2 \ge 0$ sur $[-1, 1]$, il faut $k \ge 0$. Intégrale : $\int_{-1}^1 k(1 - x^2)\,dx = k\left[x - \frac{x^3}{3}\right]_{-1}^{1} = \frac{4k}{3}$. Donc $f$ est une densité si et seulement si $k = \frac{3}{4}$.
:::

::item{id="pc-densite"}

## 5. Fonction de répartition d'une variable continue

La définition ne change pas : $F_X(x) = P(X \le x)$. Si $X$ a une densité $f$ :
$$F_X(x) = \int_{-\infty}^{x} f(t)\,dt : \text{ l'aire sous } f \text{ à gauche de } x.$$

:::theorem[Propriétés]
- $F_X$ est **continue** sur $\mathbb{R}$ (plus de sauts, car $P(X = a) = 0$), croissante, de limite $0$ en $-\infty$ et $1$ en $+\infty$.
- Là où $f$ est continue, $F_X$ est dérivable et $F_X' = f$ (théorème fondamental de l'analyse).
- $P(a \le X \le b) = F_X(b) - F_X(a)$.
:::

:::method[De la densité à la fonction de répartition]
1. Repérer les points où la formule de $f$ change.
2. Pour chaque zone de $x$, calculer $F(x) = \int_{-\infty}^x f$ en découpant : les morceaux où $f = 0$ comptent $0$, les morceaux entièrement à gauche de $x$ comptent leur aire totale.
3. **Vérifier** : $F$ continue aux points de raccord, de $0$ à $1$.

Dans l'autre sens, on **dérive** $F$ là où elle est dérivable ; aux quelques points restants, la valeur de $f$ est sans importance (elle ne change aucune intégrale).
:::

:::example[Pour $f(x) = 3x^2$ sur $[0, 1]$]
- $x < 0$ : $F(x) = 0$.
- $0 \le x \le 1$ : $F(x) = \int_0^x 3t^2\,dt = x^3$.
- $x > 1$ : toute l'aire est à gauche, $F(x) = 1$.

Raccords : $F(0) = 0$, $F(1) = 1$ ✔. La **médiane** $m$ vérifie $F(m) = \frac{1}{2}$ : $m = 2^{-1/3} \approx 0{,}794$.
:::

<figure><svg viewBox="0 0 360 220" role="img" aria-label="Fonction de répartition x³"><line x1="40" y1="180.0" x2="348" y2="180.0" class="stroke"/><line x1="92.9" y1="180" x2="92.9" y2="14" class="stroke"/><text x="92.9" y="195.0" text-anchor="middle" font-size="11">0</text><text x="181.2" y="195.0" text-anchor="middle" font-size="11">0,5</text><text x="269.4" y="195.0" text-anchor="middle" font-size="11">1</text><line x1="40" y1="110.4" x2="340" y2="110.4" class="muted" stroke-dasharray="2 4"/><text x="34" y="114.4" text-anchor="end" font-size="11">0,5</text><line x1="40" y1="40.9" x2="340" y2="40.9" class="muted" stroke-dasharray="2 4"/><text x="34" y="44.9" text-anchor="end" font-size="11">1</text><text x="350" y="184.0" font-size="12">x</text><text x="46" y="16" font-size="12">F(x)</text><path d="M40.0,180.0 L41.5,180.0 L43.0,180.0 L44.5,180.0 L46.0,180.0 L47.5,180.0 L49.0,180.0 L50.5,180.0 L52.0,180.0 L53.5,180.0 L55.0,180.0 L56.5,180.0 L58.0,180.0 L59.5,180.0 L61.0,180.0 L62.5,180.0 L64.0,180.0 L65.5,180.0 L67.0,180.0 L68.5,180.0 L70.0,180.0 L71.5,180.0 L73.0,180.0 L74.5,180.0 L76.0,180.0 L77.5,180.0 L79.0,180.0 L80.5,180.0 L82.0,180.0 L83.5,180.0 L85.0,180.0 L86.5,180.0 L88.0,180.0 L89.5,180.0 L91.0,180.0 L92.5,180.0 L94.0,180.0 L95.5,180.0 L97.0,180.0 L98.5,180.0 L100.0,180.0 L101.5,180.0 L103.0,180.0 L104.5,180.0 L106.0,179.9 L107.5,179.9 L109.0,179.9 L110.5,179.9 L112.0,179.8 L113.5,179.8 L115.0,179.7 L116.5,179.7 L118.0,179.6 L119.5,179.5 L121.0,179.4 L122.5,179.3 L124.0,179.2 L125.5,179.1 L127.0,179.0 L128.5,178.9 L130.0,178.7 L131.5,178.5 L133.0,178.4 L134.5,178.2 L136.0,178.0 L137.5,177.8 L139.0,177.5 L140.5,177.3 L142.0,177.0 L143.5,176.7 L145.0,176.4 L146.5,176.1 L148.0,175.8 L149.5,175.4 L151.0,175.0 L152.5,174.7 L154.0,174.2 L155.5,173.8 L157.0,173.3 L158.5,172.9 L160.0,172.4 L161.5,171.8 L163.0,171.3 L164.5,170.7 L166.0,170.1 L167.5,169.5 L169.0,168.9 L170.5,168.2 L172.0,167.5 L173.5,166.8 L175.0,166.0 L176.5,165.2 L178.0,164.4 L179.5,163.6 L181.0,162.7 L182.5,161.8 L184.0,160.9 L185.5,159.9 L187.0,158.9 L188.5,157.9 L190.0,156.9 L191.5,155.8 L193.0,154.6 L194.5,153.5 L196.0,152.3 L197.5,151.1 L199.0,149.8 L200.5,148.5 L202.0,147.2 L203.5,145.8 L205.0,144.4 L206.5,142.9 L208.0,141.4 L209.5,139.9 L211.0,138.3 L212.5,136.7 L214.0,135.1 L215.5,133.4 L217.0,131.7 L218.5,129.9 L220.0,128.1 L221.5,126.2 L223.0,124.3 L224.5,122.4 L226.0,120.4 L227.5,118.3 L229.0,116.2 L230.5,114.1 L232.0,111.9 L233.5,109.7 L235.0,107.4 L236.5,105.1 L238.0,102.7 L239.5,100.3 L241.0,97.8 L242.5,95.3 L244.0,92.7 L245.5,90.1 L247.0,87.4 L248.5,84.7 L250.0,81.9 L251.5,79.1 L253.0,76.2 L254.5,73.2 L256.0,70.2 L257.5,67.2 L259.0,64.1 L260.5,60.9 L262.0,57.7 L263.5,54.4 L265.0,51.0 L266.5,47.6 L268.0,44.2 L269.5,40.9 L271.0,40.9 L272.5,40.9 L274.0,40.9 L275.5,40.9 L277.0,40.9 L278.5,40.9 L280.0,40.9 L281.5,40.9 L283.0,40.9 L284.5,40.9 L286.0,40.9 L287.5,40.9 L289.0,40.9 L290.5,40.9 L292.0,40.9 L293.5,40.9 L295.0,40.9 L296.5,40.9 L298.0,40.9 L299.5,40.9 L301.0,40.9 L302.5,40.9 L304.0,40.9 L305.5,40.9 L307.0,40.9 L308.5,40.9 L310.0,40.9 L311.5,40.9 L313.0,40.9 L314.5,40.9 L316.0,40.9 L317.5,40.9 L319.0,40.9 L320.5,40.9 L322.0,40.9 L323.5,40.9 L325.0,40.9 L326.5,40.9 L328.0,40.9 L329.5,40.9 L331.0,40.9 L332.5,40.9 L334.0,40.9 L335.5,40.9 L337.0,40.9 L338.5,40.9 L340.0,40.9" class="accent" stroke-width="2"/><line x1="233.0" y1="110.4" x2="233.0" y2="180.0" class="ok" stroke-dasharray="3 3"/><text x="233.0" y="208.0" text-anchor="middle" font-size="11">médiane ≈ 0,79</text></svg></figure>

:::definition[Intervalle central à 95 %]
Un intervalle $[a, b]$ tel que $P(X < a) = 0{,}025$ et $P(X > b) = 0{,}025$, donc $P(a \le X \le b) = 0{,}95$. On résout $F(a) = 0{,}025$ et $F(b) = 0{,}975$.
:::

Pour $F(x) = x^3$ : $a = 0{,}025^{1/3} \approx 0{,}292$ et $b = 0{,}975^{1/3} \approx 0{,}992$.

::item{id="pc-repartition"}

## 6. Changement de variable : la loi de $g(X)$

On connaît la loi de $X$ et on veut celle de $Y = g(X)$ : $2X + 1$, $X^2$, $e^X$, $|X|$, $-\ln(X)$…

:::method[La méthode universelle : passer par la fonction de répartition]
1. Écrire $F_Y(t) = P(Y \le t) = P(g(X) \le t)$.
2. Transformer l'inégalité $g(X) \le t$ en une condition sur $X$ seul — **attention au sens** des inégalités et aux valeurs de $t$ **impossibles**.
3. Exprimer le résultat avec $F_X$.
4. **Dériver** pour obtenir la densité $f_Y = F_Y'$.

Ne cherche **jamais** à « transformer la densité directement » : on se trompe presque toujours de facteur.
:::

**Transformation affine** $Y = aX + b$ :
- si $a > 0$ : $aX + b \le t \iff X \le \frac{t - b}{a}$, donc $F_Y(t) = F_X\!\left(\frac{t-b}{a}\right)$ ;
- si $a < 0$ : diviser par $a$ **inverse** l'inégalité : $F_Y(t) = P\!\left(X \ge \frac{t-b}{a}\right) = 1 - F_X\!\left(\frac{t-b}{a}\right)$ (valable car $P(X = c) = 0$) ;
- dans les deux cas, en dérivant : $f_Y(t) = \frac{1}{|a|}\, f_X\!\left(\frac{t - b}{a}\right)$.

Le facteur $\frac{1}{|a|}$ compense l'étirement : si on étire l'axe d'un facteur 2, la densité doit être deux fois plus basse pour que l'aire reste 1.

**Autres transformations :**
- $Y = X^3$ (strictement croissante) : $F_Y(t) = F_X(\sqrt[3]{t})$ pour tout $t$.
- $Y = e^X > 0$ : $F_Y(t) = 0$ si $t \le 0$, et $F_Y(t) = F_X(\ln t)$ si $t > 0$.
- $Y = X^2$ (pas monotone) : $F_Y(t) = 0$ si $t < 0$, et $F_Y(t) = F_X(\sqrt{t}) - F_X(-\sqrt{t})$ si $t \ge 0$.
- $Y = |X|$ : $F_Y(t) = 0$ si $t < 0$, et $F_Y(t) = F_X(t) - F_X(-t)$ si $t \ge 0$.

:::warning[Les deux pièges]
- Oublier d'**inverser l'inégalité** en divisant par un nombre négatif (ou en appliquant une fonction décroissante).
- Oublier les valeurs de $t$ **impossibles** ($t < 0$ pour $X^2$, $|X|$, $e^X$) : la fonction de répartition y vaut $0$, il faut l'écrire.
:::

:::example[Une densité qui explose]
$X \sim \mathcal{U}([-1, 1])$ et $Y = X^2$. Pour $t \in [0, 1]$ : $F_Y(t) = P(-\sqrt{t} \le X \le \sqrt{t}) = \frac{2\sqrt{t}}{2} = \sqrt{t}$. Donc $f_Y(t) = \frac{1}{2\sqrt{t}}$ sur $]0, 1]$ : une densité **non bornée** au voisinage de $0$, et pourtant d'intégrale $1$.
:::

::item{id="pc-changement"}

## 7. Les lois continues usuelles

Chaque loi discrète a une « cousine » continue :

| Discrète | Continue | Point commun |
|---|---|---|
| uniforme sur $\{1, \ldots, n\}$ | uniforme sur $[a, b]$ | équiprobabilité |
| géométrique $\mathcal{G}(p)$ | exponentielle $\mathcal{E}(\lambda)$ | temps d'attente, **absence de mémoire** |
| binomiale $\mathcal{B}(n, p)$ | normale $\mathcal{N}(m, \sigma^2)$ | somme de nombreux petits effets |
| Poisson $\mathcal{P}(\lambda)$ | exponentielle, Gamma | processus d'arrivées aléatoires |

### 7.1 Loi uniforme $\mathcal{U}([a, b])$

$X$ tombe « au hasard » dans $[a, b]$, sans préférence : la probabilité d'un sous-intervalle ne dépend que de sa longueur.
$$f(x) = \frac{1}{b - a} \text{ sur } [a, b],\ 0 \text{ sinon} ; \qquad F(x) = \begin{cases} 0 & x < a \\ \frac{x - a}{b - a} & a \le x \le b \\ 1 & x > b \end{cases}$$
$E[X] = \frac{a + b}{2}$, $V(X) = \frac{(b - a)^2}{12}$, et pour $[c, d] \subseteq [a, b]$ : $P(c \le X \le d) = \frac{d - c}{b - a}$.

**Standardisation** : si $X \sim \mathcal{U}([a, b])$, alors $\frac{X - a}{b - a} \sim \mathcal{U}([0, 1])$ ; réciproquement, si $U \sim \mathcal{U}([0, 1])$, alors $a + (b - a)U \sim \mathcal{U}([a, b])$. C'est ainsi qu'on simule une uniforme quelconque avec `rand()`.

### 7.2 Loi exponentielle $\mathcal{E}(\lambda)$

Temps d'attente d'un événement qui survient « au hasard, sans usure » : prochaine requête sur un serveur, prochaine désintégration, durée de vie d'un composant électronique qui ne vieillit pas. $\lambda > 0$ est le **taux** (nombre moyen d'événements par unité de temps).
$$f(t) = \lambda e^{-\lambda t} \text{ pour } t \ge 0 ; \qquad F(t) = 1 - e^{-\lambda t} \text{ pour } t \ge 0 ; \qquad P(T > t) = e^{-\lambda t}.$$
$E[T] = \frac{1}{\lambda}$, $V(T) = \frac{1}{\lambda^2}$, médiane $\frac{\ln 2}{\lambda}$.

<figure><svg viewBox="0 0 360 220" role="img" aria-label="Densités exponentielles pour trois valeurs de lambda"><line x1="40" y1="180.0" x2="348" y2="180.0" class="stroke"/><line x1="40.0" y1="180" x2="40.0" y2="14" class="stroke"/><text x="40.0" y="195.0" text-anchor="middle" font-size="11">0</text><text x="90.0" y="195.0" text-anchor="middle" font-size="11">1</text><text x="140.0" y="195.0" text-anchor="middle" font-size="11">2</text><text x="190.0" y="195.0" text-anchor="middle" font-size="11">3</text><text x="240.0" y="195.0" text-anchor="middle" font-size="11">4</text><text x="290.0" y="195.0" text-anchor="middle" font-size="11">5</text><line x1="40" y1="141.9" x2="340" y2="141.9" class="muted" stroke-dasharray="2 4"/><text x="34" y="145.9" text-anchor="end" font-size="11">0,5</text><line x1="40" y1="103.8" x2="340" y2="103.8" class="muted" stroke-dasharray="2 4"/><text x="34" y="107.8" text-anchor="end" font-size="11">1</text><line x1="40" y1="27.6" x2="340" y2="27.6" class="muted" stroke-dasharray="2 4"/><text x="34" y="31.6" text-anchor="end" font-size="11">2</text><text x="350" y="184.0" font-size="12">t</text><text x="46" y="16" font-size="12">f(t)</text><path d="M40.0,27.6 L41.9,38.6 L43.8,48.8 L45.6,58.3 L47.5,67.1 L49.4,75.3 L51.2,82.8 L53.1,89.9 L55.0,96.4 L56.9,102.4 L58.8,108.0 L60.6,113.2 L62.5,118.0 L64.4,122.5 L66.2,126.7 L68.1,130.5 L70.0,134.1 L71.9,137.4 L73.8,140.5 L75.6,143.4 L77.5,146.0 L79.4,148.5 L81.2,150.7 L83.1,152.8 L85.0,154.8 L86.9,156.6 L88.8,158.3 L90.6,159.9 L92.5,161.3 L94.4,162.7 L96.2,163.9 L98.1,165.1 L100.0,166.2 L101.9,167.2 L103.8,168.1 L105.6,169.0 L107.5,169.8 L109.4,170.5 L111.2,171.2 L113.1,171.8 L115.0,172.4 L116.9,173.0 L118.8,173.5 L120.6,173.9 L122.5,174.4 L124.4,174.8 L126.3,175.2 L128.1,175.5 L130.0,175.8 L131.9,176.1 L133.8,176.4 L135.6,176.7 L137.5,176.9 L139.4,177.1 L141.2,177.3 L143.1,177.5 L145.0,177.7 L146.9,177.9 L148.8,178.0 L150.6,178.2 L152.5,178.3 L154.4,178.4 L156.2,178.5 L158.1,178.6 L160.0,178.7 L161.9,178.8 L163.8,178.9 L165.6,179.0 L167.5,179.1 L169.4,179.1 L171.2,179.2 L173.1,179.3 L175.0,179.3 L176.9,179.4 L178.8,179.4 L180.6,179.5 L182.5,179.5 L184.4,179.5 L186.2,179.6 L188.1,179.6 L190.0,179.6 L191.9,179.6 L193.8,179.7 L195.6,179.7 L197.5,179.7 L199.4,179.7 L201.2,179.8 L203.1,179.8 L205.0,179.8 L206.9,179.8 L208.8,179.8 L210.6,179.8 L212.5,179.8 L214.4,179.9 L216.2,179.9 L218.1,179.9 L220.0,179.9 L221.9,179.9 L223.7,179.9 L225.6,179.9 L227.5,179.9 L229.4,179.9 L231.3,179.9 L233.1,179.9 L235.0,179.9 L236.9,179.9 L238.8,179.9 L240.6,180.0 L242.5,180.0 L244.4,180.0 L246.2,180.0 L248.1,180.0 L250.0,180.0 L251.9,180.0 L253.8,180.0 L255.6,180.0 L257.5,180.0 L259.4,180.0 L261.2,180.0 L263.1,180.0 L265.0,180.0 L266.9,180.0 L268.8,180.0 L270.6,180.0 L272.5,180.0 L274.4,180.0 L276.2,180.0 L278.1,180.0 L280.0,180.0 L281.9,180.0 L283.8,180.0 L285.6,180.0 L287.5,180.0 L289.4,180.0 L291.2,180.0 L293.1,180.0 L295.0,180.0 L296.9,180.0 L298.8,180.0 L300.6,180.0 L302.5,180.0 L304.4,180.0 L306.2,180.0 L308.1,180.0 L310.0,180.0 L311.9,180.0 L313.8,180.0 L315.6,180.0 L317.5,180.0 L319.4,180.0 L321.2,180.0 L323.1,180.0 L325.0,180.0 L326.9,180.0 L328.8,180.0 L330.6,180.0 L332.5,180.0 L334.4,180.0 L336.2,180.0 L338.1,180.0 L340.0,180.0" class="accent" stroke-width="2"/><path d="M40.0,103.8 L41.9,106.6 L43.8,109.3 L45.6,111.9 L47.5,114.4 L49.4,116.8 L51.2,119.2 L53.1,121.4 L55.0,123.6 L56.9,125.6 L58.8,127.6 L60.6,129.6 L62.5,131.4 L64.4,133.2 L66.2,134.9 L68.1,136.6 L70.0,138.2 L71.9,139.7 L73.8,141.2 L75.6,142.6 L77.5,144.0 L79.4,145.3 L81.2,146.6 L83.1,147.8 L85.0,149.0 L86.9,150.2 L88.8,151.3 L90.6,152.3 L92.5,153.3 L94.4,154.3 L96.2,155.3 L98.1,156.2 L100.0,157.1 L101.9,157.9 L103.8,158.7 L105.6,159.5 L107.5,160.2 L109.4,161.0 L111.2,161.7 L113.1,162.3 L115.0,163.0 L116.9,163.6 L118.8,164.2 L120.6,164.8 L122.5,165.4 L124.4,165.9 L126.3,166.4 L128.1,166.9 L130.0,167.4 L131.9,167.9 L133.8,168.3 L135.6,168.7 L137.5,169.2 L139.4,169.6 L141.2,169.9 L143.1,170.3 L145.0,170.7 L146.9,171.0 L148.8,171.3 L150.6,171.7 L152.5,172.0 L154.4,172.3 L156.2,172.5 L158.1,172.8 L160.0,173.1 L161.9,173.3 L163.8,173.6 L165.6,173.8 L167.5,174.1 L169.4,174.3 L171.2,174.5 L173.1,174.7 L175.0,174.9 L176.9,175.1 L178.8,175.2 L180.6,175.4 L182.5,175.6 L184.4,175.8 L186.2,175.9 L188.1,176.1 L190.0,176.2 L191.9,176.3 L193.8,176.5 L195.6,176.6 L197.5,176.7 L199.4,176.9 L201.2,177.0 L203.1,177.1 L205.0,177.2 L206.9,177.3 L208.8,177.4 L210.6,177.5 L212.5,177.6 L214.4,177.7 L216.2,177.8 L218.1,177.8 L220.0,177.9 L221.9,178.0 L223.7,178.1 L225.6,178.1 L227.5,178.2 L229.4,178.3 L231.3,178.3 L233.1,178.4 L235.0,178.5 L236.9,178.5 L238.8,178.6 L240.6,178.6 L242.5,178.7 L244.4,178.7 L246.2,178.8 L248.1,178.8 L250.0,178.9 L251.9,178.9 L253.8,178.9 L255.6,179.0 L257.5,179.0 L259.4,179.1 L261.2,179.1 L263.1,179.1 L265.0,179.2 L266.9,179.2 L268.8,179.2 L270.6,179.2 L272.5,179.3 L274.4,179.3 L276.2,179.3 L278.1,179.3 L280.0,179.4 L281.9,179.4 L283.8,179.4 L285.6,179.4 L287.5,179.5 L289.4,179.5 L291.2,179.5 L293.1,179.5 L295.0,179.5 L296.9,179.6 L298.8,179.6 L300.6,179.6 L302.5,179.6 L304.4,179.6 L306.2,179.6 L308.1,179.6 L310.0,179.7 L311.9,179.7 L313.8,179.7 L315.6,179.7 L317.5,179.7 L319.4,179.7 L321.2,179.7 L323.1,179.7 L325.0,179.7 L326.9,179.8 L328.8,179.8 L330.6,179.8 L332.5,179.8 L334.4,179.8 L336.2,179.8 L338.1,179.8 L340.0,179.8" class="ok" stroke-width="2" stroke-dasharray="6 3"/><path d="M40.0,141.9 L41.9,142.6 L43.8,143.3 L45.6,144.0 L47.5,144.7 L49.4,145.3 L51.2,146.0 L53.1,146.6 L55.0,147.2 L56.9,147.8 L58.8,148.4 L60.6,149.0 L62.5,149.6 L64.4,150.1 L66.2,150.7 L68.1,151.2 L70.0,151.8 L71.9,152.3 L73.8,152.8 L75.6,153.3 L77.5,153.8 L79.4,154.3 L81.2,154.8 L83.1,155.2 L85.0,155.7 L86.9,156.2 L88.8,156.6 L90.6,157.0 L92.5,157.5 L94.4,157.9 L96.2,158.3 L98.1,158.7 L100.0,159.1 L101.9,159.5 L103.8,159.9 L105.6,160.2 L107.5,160.6 L109.4,161.0 L111.2,161.3 L113.1,161.7 L115.0,162.0 L116.9,162.3 L118.8,162.7 L120.6,163.0 L122.5,163.3 L124.4,163.6 L126.3,163.9 L128.1,164.2 L130.0,164.5 L131.9,164.8 L133.8,165.1 L135.6,165.4 L137.5,165.6 L139.4,165.9 L141.2,166.2 L143.1,166.4 L145.0,166.7 L146.9,166.9 L148.8,167.2 L150.6,167.4 L152.5,167.6 L154.4,167.9 L156.2,168.1 L158.1,168.3 L160.0,168.5 L161.9,168.7 L163.8,168.9 L165.6,169.2 L167.5,169.4 L169.4,169.6 L171.2,169.7 L173.1,169.9 L175.0,170.1 L176.9,170.3 L178.8,170.5 L180.6,170.7 L182.5,170.8 L184.4,171.0 L186.2,171.2 L188.1,171.3 L190.0,171.5 L191.9,171.7 L193.8,171.8 L195.6,172.0 L197.5,172.1 L199.4,172.3 L201.2,172.4 L203.1,172.5 L205.0,172.7 L206.9,172.8 L208.8,173.0 L210.6,173.1 L212.5,173.2 L214.4,173.3 L216.2,173.5 L218.1,173.6 L220.0,173.7 L221.9,173.8 L223.7,173.9 L225.6,174.0 L227.5,174.2 L229.4,174.3 L231.3,174.4 L233.1,174.5 L235.0,174.6 L236.9,174.7 L238.8,174.8 L240.6,174.9 L242.5,175.0 L244.4,175.1 L246.2,175.2 L248.1,175.2 L250.0,175.3 L251.9,175.4 L253.8,175.5 L255.6,175.6 L257.5,175.7 L259.4,175.8 L261.2,175.8 L263.1,175.9 L265.0,176.0 L266.9,176.1 L268.8,176.1 L270.6,176.2 L272.5,176.3 L274.4,176.3 L276.2,176.4 L278.1,176.5 L280.0,176.5 L281.9,176.6 L283.8,176.7 L285.6,176.7 L287.5,176.8 L289.4,176.9 L291.2,176.9 L293.1,177.0 L295.0,177.0 L296.9,177.1 L298.8,177.1 L300.6,177.2 L302.5,177.2 L304.4,177.3 L306.2,177.3 L308.1,177.4 L310.0,177.4 L311.9,177.5 L313.8,177.5 L315.6,177.6 L317.5,177.6 L319.4,177.7 L321.2,177.7 L323.1,177.8 L325.0,177.8 L326.9,177.8 L328.8,177.9 L330.6,177.9 L332.5,178.0 L334.4,178.0 L336.2,178.0 L338.1,178.1 L340.0,178.1" class="ko" stroke-width="2" stroke-dasharray="2 3"/><text x="67.5" y="61.9" font-size="11">λ = 2</text><text x="95.0" y="138.1" font-size="11">λ = 1</text><text x="195.0" y="166.3" font-size="11">λ = 0,5</text></svg></figure>

*Plus $\lambda$ est grand, plus les petites valeurs sont probables : l'attente moyenne $1/\lambda$ est plus courte.*

:::theorem[Absence de mémoire]
Pour tous $t_0 > 0$ et $\Delta t \ge 0$ : $P(T > t_0 + \Delta t \mid T > t_0) = P(T > \Delta t)$.
:::

:::correction[Voir la preuve]
L'événement $\{T > t_0 + \Delta t\}$ est inclus dans $\{T > t_0\}$, donc
$$P(T > t_0 + \Delta t \mid T > t_0) = \frac{P(T > t_0 + \Delta t)}{P(T > t_0)} = \frac{e^{-\lambda(t_0 + \Delta t)}}{e^{-\lambda t_0}} = e^{-\lambda \Delta t} = P(T > \Delta t). \qquad \square$$
Si l'on attend déjà depuis $t_0$, le temps qui reste à attendre a la **même loi** que si l'on venait d'arriver. Réaliste pour des requêtes indépendantes, faux pour une ampoule qui s'use. Réciproquement, l'exponentielle est la **seule** loi continue sans mémoire (sa cousine discrète, la géométrique, l'est aussi).
:::

### 7.3 Loi normale centrée réduite $\mathcal{N}(0, 1)$

Elle apparaît dès qu'une grandeur résulte de l'addition de nombreux petits effets indépendants (erreurs de mesure, tailles, notes…).
$$\varphi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}, \qquad \Phi(x) = P(Z \le x) = \int_{-\infty}^x \varphi(t)\,dt.$$
Il n'existe pas de formule de $\Phi$ avec les fonctions usuelles : on utilise une **table** (qui donne $\Phi(u)$ pour $u \ge 0$) ou une calculatrice.

<figure><svg viewBox="0 0 360 220" role="img" aria-label="Densité normale centrée réduite et intervalle à 95 %"><line x1="40" y1="180.0" x2="348" y2="180.0" class="stroke"/><line x1="190.0" y1="180" x2="190.0" y2="14" class="stroke"/><text x="108.3" y="195.0" text-anchor="middle" font-size="11">−1,96</text><text x="190.0" y="195.0" text-anchor="middle" font-size="11">0</text><text x="271.7" y="195.0" text-anchor="middle" font-size="11">1,96</text><line x1="40" y1="144.4" x2="340" y2="144.4" class="muted" stroke-dasharray="2 4"/><text x="34" y="148.4" text-anchor="end" font-size="11">0,1</text><line x1="40" y1="108.9" x2="340" y2="108.9" class="muted" stroke-dasharray="2 4"/><text x="34" y="112.9" text-anchor="end" font-size="11">0,2</text><line x1="40" y1="73.3" x2="340" y2="73.3" class="muted" stroke-dasharray="2 4"/><text x="34" y="77.3" text-anchor="end" font-size="11">0,3</text><line x1="40" y1="37.8" x2="340" y2="37.8" class="muted" stroke-dasharray="2 4"/><text x="34" y="41.8" text-anchor="end" font-size="11">0,4</text><text x="350" y="184.0" font-size="12">x</text><text x="46" y="16" font-size="12">φ(x)</text><path d="M108.3,159.2 L109.7,157.9 L111.1,156.4 L112.4,154.9 L113.8,153.4 L115.1,151.8 L116.5,150.1 L117.9,148.3 L119.2,146.5 L120.6,144.6 L121.9,142.6 L123.3,140.6 L124.7,138.5 L126.0,136.4 L127.4,134.1 L128.8,131.9 L130.1,129.5 L131.5,127.1 L132.8,124.7 L134.2,122.2 L135.6,119.6 L136.9,117.0 L138.3,114.4 L139.6,111.7 L141.0,109.0 L142.4,106.2 L143.7,103.4 L145.1,100.7 L146.4,97.9 L147.8,95.1 L149.2,92.2 L150.5,89.4 L151.9,86.6 L153.2,83.9 L154.6,81.1 L156.0,78.4 L157.3,75.7 L158.7,73.0 L160.1,70.4 L161.4,67.9 L162.8,65.4 L164.1,63.0 L165.5,60.7 L166.9,58.4 L168.2,56.3 L169.6,54.2 L170.9,52.2 L172.3,50.4 L173.7,48.6 L175.0,47.0 L176.4,45.5 L177.8,44.2 L179.1,42.9 L180.5,41.8 L181.8,40.9 L183.2,40.0 L184.6,39.4 L185.9,38.8 L187.3,38.5 L188.6,38.2 L190.0,38.2 L191.4,38.2 L192.7,38.5 L194.1,38.8 L195.4,39.4 L196.8,40.0 L198.2,40.9 L199.5,41.8 L200.9,42.9 L202.3,44.2 L203.6,45.5 L205.0,47.0 L206.3,48.6 L207.7,50.4 L209.1,52.2 L210.4,54.2 L211.8,56.3 L213.1,58.4 L214.5,60.7 L215.9,63.0 L217.2,65.4 L218.6,67.9 L219.9,70.4 L221.3,73.0 L222.7,75.7 L224.0,78.4 L225.4,81.1 L226.8,83.9 L228.1,86.6 L229.5,89.4 L230.8,92.2 L232.2,95.1 L233.6,97.9 L234.9,100.7 L236.3,103.4 L237.6,106.2 L239.0,109.0 L240.4,111.7 L241.7,114.4 L243.1,117.0 L244.4,119.6 L245.8,122.2 L247.2,124.7 L248.5,127.1 L249.9,129.5 L251.3,131.9 L252.6,134.1 L254.0,136.4 L255.3,138.5 L256.7,140.6 L258.1,142.6 L259.4,144.6 L260.8,146.5 L262.1,148.3 L263.5,150.1 L264.9,151.8 L266.2,153.4 L267.6,154.9 L268.9,156.4 L270.3,157.9 L271.7,159.2 L271.7,180.0 L108.3,180.0 Z" class="venn-fill"/><path d="M40.0,179.8 L40.6,179.8 L41.1,179.8 L41.7,179.7 L42.3,179.7 L42.8,179.7 L43.4,179.7 L44.0,179.7 L44.6,179.7 L45.1,179.7 L45.7,179.6 L46.3,179.6 L46.8,179.6 L47.4,179.6 L48.0,179.6 L48.5,179.6 L49.1,179.5 L49.7,179.5 L50.2,179.5 L50.8,179.5 L51.4,179.4 L52.0,179.4 L52.5,179.4 L53.1,179.4 L53.7,179.3 L54.2,179.3 L54.8,179.3 L55.4,179.2 L55.9,179.2 L56.5,179.2 L57.1,179.1 L57.7,179.1 L58.2,179.0 L58.8,179.0 L59.4,179.0 L59.9,178.9 L60.5,178.9 L61.1,178.8 L61.6,178.8 L62.2,178.7 L62.8,178.7 L63.3,178.6 L63.9,178.5 L64.5,178.5 L65.1,178.4 L65.6,178.4 L66.2,178.3 L66.8,178.2 L67.3,178.1 L67.9,178.1 L68.5,178.0 L69.0,177.9 L69.6,177.8 L70.2,177.7 L70.8,177.6 L71.3,177.5 L71.9,177.4 L72.5,177.3 L73.0,177.2 L73.6,177.1 L74.2,177.0 L74.7,176.9 L75.3,176.8 L75.9,176.7 L76.4,176.5 L77.0,176.4 L77.6,176.3 L78.2,176.1 L78.7,176.0 L79.3,175.8 L79.9,175.7 L80.4,175.5 L81.0,175.4 L81.6,175.2 L82.1,175.0 L82.7,174.8 L83.3,174.7 L83.8,174.5 L84.4,174.3 L85.0,174.1 L85.6,173.9 L86.1,173.7 L86.7,173.4 L87.3,173.2 L87.8,173.0 L88.4,172.7 L89.0,172.5 L89.5,172.2 L90.1,172.0 L90.7,171.7 L91.2,171.4 L91.8,171.2 L92.4,170.9 L93.0,170.6 L93.5,170.3 L94.1,170.0 L94.7,169.6 L95.2,169.3 L95.8,169.0 L96.4,168.6 L96.9,168.3 L97.5,167.9 L98.1,167.6 L98.7,167.2 L99.2,166.8 L99.8,166.4 L100.4,166.0 L100.9,165.6 L101.5,165.1 L102.1,164.7 L102.6,164.3 L103.2,163.8 L103.8,163.3 L104.3,162.9 L104.9,162.4 L105.5,161.9 L106.1,161.4 L106.6,160.8 L107.2,160.3 L107.8,159.8 L108.3,159.2 L108.3,180.0 L40.0,180.0 Z" class="ko-fill"/><path d="M271.7,159.2 L272.2,159.8 L272.8,160.3 L273.4,160.8 L273.9,161.4 L274.5,161.9 L275.1,162.4 L275.7,162.9 L276.2,163.3 L276.8,163.8 L277.4,164.3 L277.9,164.7 L278.5,165.1 L279.1,165.6 L279.6,166.0 L280.2,166.4 L280.8,166.8 L281.3,167.2 L281.9,167.6 L282.5,167.9 L283.1,168.3 L283.6,168.6 L284.2,169.0 L284.8,169.3 L285.3,169.6 L285.9,170.0 L286.5,170.3 L287.0,170.6 L287.6,170.9 L288.2,171.2 L288.8,171.4 L289.3,171.7 L289.9,172.0 L290.5,172.2 L291.0,172.5 L291.6,172.7 L292.2,173.0 L292.7,173.2 L293.3,173.4 L293.9,173.7 L294.4,173.9 L295.0,174.1 L295.6,174.3 L296.2,174.5 L296.7,174.7 L297.3,174.8 L297.9,175.0 L298.4,175.2 L299.0,175.4 L299.6,175.5 L300.1,175.7 L300.7,175.8 L301.3,176.0 L301.8,176.1 L302.4,176.3 L303.0,176.4 L303.6,176.5 L304.1,176.7 L304.7,176.8 L305.3,176.9 L305.8,177.0 L306.4,177.1 L307.0,177.2 L307.5,177.3 L308.1,177.4 L308.7,177.5 L309.2,177.6 L309.8,177.7 L310.4,177.8 L311.0,177.9 L311.5,178.0 L312.1,178.1 L312.7,178.1 L313.2,178.2 L313.8,178.3 L314.4,178.4 L314.9,178.4 L315.5,178.5 L316.1,178.5 L316.7,178.6 L317.2,178.7 L317.8,178.7 L318.4,178.8 L318.9,178.8 L319.5,178.9 L320.1,178.9 L320.6,179.0 L321.2,179.0 L321.8,179.0 L322.3,179.1 L322.9,179.1 L323.5,179.2 L324.1,179.2 L324.6,179.2 L325.2,179.3 L325.8,179.3 L326.3,179.3 L326.9,179.4 L327.5,179.4 L328.0,179.4 L328.6,179.4 L329.2,179.5 L329.8,179.5 L330.3,179.5 L330.9,179.5 L331.5,179.6 L332.0,179.6 L332.6,179.6 L333.2,179.6 L333.7,179.6 L334.3,179.6 L334.9,179.7 L335.4,179.7 L336.0,179.7 L336.6,179.7 L337.2,179.7 L337.7,179.7 L338.3,179.7 L338.9,179.8 L339.4,179.8 L340.0,179.8 L340.0,180.0 L271.7,180.0 Z" class="ko-fill"/><path d="M40.0,179.8 L41.9,179.7 L43.7,179.7 L45.6,179.6 L47.5,179.6 L49.4,179.5 L51.2,179.4 L53.1,179.4 L55.0,179.3 L56.9,179.1 L58.8,179.0 L60.6,178.9 L62.5,178.7 L64.4,178.5 L66.2,178.3 L68.1,178.0 L70.0,177.8 L71.9,177.4 L73.8,177.1 L75.6,176.7 L77.5,176.3 L79.4,175.8 L81.2,175.3 L83.1,174.7 L85.0,174.1 L86.9,173.4 L88.8,172.6 L90.6,171.7 L92.5,170.8 L94.4,169.8 L96.2,168.7 L98.1,167.5 L100.0,166.2 L101.9,164.8 L103.8,163.4 L105.6,161.7 L107.5,160.0 L109.4,158.2 L111.2,156.2 L113.1,154.1 L115.0,151.9 L116.9,149.6 L118.8,147.1 L120.6,144.5 L122.5,141.8 L124.4,139.0 L126.2,136.0 L128.1,132.9 L130.0,129.7 L131.9,126.4 L133.8,123.0 L135.6,119.5 L137.5,115.9 L139.4,112.2 L141.2,108.5 L143.1,104.7 L145.0,100.8 L146.9,97.0 L148.8,93.1 L150.6,89.2 L152.5,85.4 L154.4,81.6 L156.2,77.8 L158.1,74.1 L160.0,70.5 L161.9,67.1 L163.8,63.7 L165.6,60.5 L167.5,57.4 L169.4,54.5 L171.2,51.8 L173.1,49.3 L175.0,47.1 L176.9,45.0 L178.8,43.2 L180.6,41.7 L182.5,40.4 L184.4,39.4 L186.2,38.7 L188.1,38.3 L190.0,38.2 L191.9,38.3 L193.8,38.7 L195.6,39.4 L197.5,40.4 L199.4,41.7 L201.2,43.2 L203.1,45.0 L205.0,47.1 L206.9,49.3 L208.8,51.8 L210.6,54.5 L212.5,57.4 L214.4,60.5 L216.2,63.7 L218.1,67.1 L220.0,70.5 L221.9,74.1 L223.8,77.8 L225.6,81.6 L227.5,85.4 L229.4,89.2 L231.2,93.1 L233.1,97.0 L235.0,100.8 L236.9,104.7 L238.8,108.5 L240.6,112.2 L242.5,115.9 L244.4,119.5 L246.2,123.0 L248.1,126.4 L250.0,129.7 L251.9,132.9 L253.8,136.0 L255.6,139.0 L257.5,141.8 L259.4,144.5 L261.2,147.1 L263.1,149.6 L265.0,151.9 L266.9,154.1 L268.8,156.2 L270.6,158.2 L272.5,160.0 L274.4,161.7 L276.2,163.4 L278.1,164.8 L280.0,166.2 L281.9,167.5 L283.8,168.7 L285.6,169.8 L287.5,170.8 L289.4,171.7 L291.2,172.6 L293.1,173.4 L295.0,174.1 L296.9,174.7 L298.8,175.3 L300.6,175.8 L302.5,176.3 L304.4,176.7 L306.2,177.1 L308.1,177.4 L310.0,177.8 L311.9,178.0 L313.8,178.3 L315.6,178.5 L317.5,178.7 L319.4,178.9 L321.2,179.0 L323.1,179.1 L325.0,179.3 L326.9,179.4 L328.8,179.4 L330.6,179.5 L332.5,179.6 L334.4,179.6 L336.3,179.7 L338.1,179.7 L340.0,179.8" class="accent" stroke-width="2"/><text x="190.0" y="126.7" text-anchor="middle" font-size="12">95 %</text><text x="77.5" y="162.2" text-anchor="middle" font-size="11">2,5 %</text><text x="302.5" y="162.2" text-anchor="middle" font-size="11">2,5 %</text></svg></figure>

:::key[Symétrie et valeurs à connaître]
$\varphi$ est paire, donc les deux queues ont la même aire : $\Phi(-u) = 1 - \Phi(u)$, et $\Phi(0) = \frac{1}{2}$.

| $u$ | 1 | 1,96 | 2 | 3 |
|---|---|---|---|---|
| $\Phi(u)$ | 0,8413 | 0,9750 | 0,9772 | 0,9987 |
| $P(-u \le Z \le u) = 2\Phi(u) - 1$ | 68,3 % | 95 % | 95,4 % | 99,7 % |
:::

### 7.4 Loi normale $\mathcal{N}(m, \sigma^2)$

Si $Z \sim \mathcal{N}(0, 1)$ et $\sigma > 0$, alors $X = m + \sigma Z \sim \mathcal{N}(m, \sigma^2)$ : $m$ est le centre de la cloche (l'espérance), $\sigma$ sa largeur (l'écart-type). **Attention : le second paramètre est la variance $\sigma^2$.**
$$f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x - m)^2}{2\sigma^2}\right), \qquad F_X(x) = \Phi\!\left(\frac{x - m}{\sigma}\right).$$

:::method[Calculer $P(x_1 \le X \le x_2)$ pour $X \sim \mathcal{N}(m, \sigma^2)$]
1. **Centrer-réduire** : $Z = \frac{X - m}{\sigma} \sim \mathcal{N}(0, 1)$, donc $P(x_1 \le X \le x_2) = \Phi(u_2) - \Phi(u_1)$ avec $u_i = \frac{x_i - m}{\sigma}$.
2. Lire la table pour $u \ge 0$ ; utiliser $\Phi(-u) = 1 - \Phi(u)$ sinon.
3. Queue droite : $P(X \ge x) = 1 - \Phi\!\left(\frac{x - m}{\sigma}\right)$.
:::

:::example[Tailles]
La taille (en cm) dans une population suit $\mathcal{N}(175, 7^2)$. Alors $P(168 \le X \le 182) = \Phi(1) - \Phi(-1) = 2\Phi(1) - 1 \approx 0{,}683$ : environ 68 % des tailles sont à moins d'un écart-type de la moyenne. Et 95 % sont dans $[175 - 1{,}96 \times 7,\ 175 + 1{,}96 \times 7] \approx [161{,}3 ;\ 188{,}7]$.
:::

Stabilité : si $X \sim \mathcal{N}(m, \sigma^2)$ et $a \neq 0$, alors $aX + b \sim \mathcal{N}(am + b,\ a^2 \sigma^2)$.

### 7.5 Loi Gamma (pour la culture)

Pour $\alpha > 0$ et $\lambda > 0$ : $f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x}$ pour $x > 0$, avec $\Gamma(\alpha) = \int_0^{+\infty} x^{\alpha - 1} e^{-x}\,dx$. La fonction $\Gamma$ prolonge la factorielle : $\Gamma(n) = (n-1)!$. Pour $\alpha = 1$, on retrouve $\mathcal{E}(\lambda)$ ; pour $\alpha = n$ entier, c'est la loi du temps d'attente du $n$-ième événement (somme de $n$ exponentielles indépendantes).

### 7.6 Espérances et variances

On calcule comme en discret, en remplaçant la somme par une intégrale : $E[X] = \int_\mathbb{R} x f(x)\,dx$ et $E[g(X)] = \int_\mathbb{R} g(x) f(x)\,dx$.

| Loi | $E[X]$ | $V(X)$ |
|---|---|---|
| $\mathcal{U}([a, b])$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| $\mathcal{E}(\lambda)$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| $\mathcal{N}(m, \sigma^2)$ | $m$ | $\sigma^2$ |

::item{id="pc-lois"}

## 8. Fiche récapitulative

:::key[L'essentiel du chapitre]
- En continu, $P(X = a) = 0$ : on mesure des intervalles ; les bornes larges ou strictes ne changent rien.
- **Densité** : $f \ge 0$, continue par morceaux, $\int_\mathbb{R} f = 1$ ; $P(a \le X \le b) = \int_a^b f$ ; $f$ peut dépasser 1.
- **Répartition** : $F(x) = \int_{-\infty}^x f$, continue, croissante, de 0 à 1, $F' = f$ ; $P(a \le X \le b) = F(b) - F(a)$.
- **Changement de variable** : toujours via $F_Y(t) = P(g(X) \le t)$, puis dériver ; $f_{aX+b}(t) = \frac{1}{|a|} f_X\!\left(\frac{t - b}{a}\right)$.
- **Intervalle central à 95 %** : $F(a) = 0{,}025$, $F(b) = 0{,}975$.
:::

| Loi | Densité | Répartition | À retenir |
|---|---|---|---|
| $\mathcal{U}([a, b])$ | $\frac{1}{b-a}$ sur $[a, b]$ | $\frac{x-a}{b-a}$ sur $[a, b]$ | $\frac{X - a}{b - a} \sim \mathcal{U}([0, 1])$ |
| $\mathcal{E}(\lambda)$ | $\lambda e^{-\lambda x}$, $x \ge 0$ | $1 - e^{-\lambda x}$, $x \ge 0$ | $P(X > x) = e^{-\lambda x}$ ; sans mémoire |
| $\mathcal{N}(0, 1)$ | $\frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ | $\Phi$ (table) | $\Phi(-u) = 1 - \Phi(u)$ ; $\Phi(1{,}96) \approx 0{,}975$ |
| $\mathcal{N}(m, \sigma^2)$ | $\frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-m)^2}{2\sigma^2}}$ | $\Phi\!\left(\frac{x - m}{\sigma}\right)$ | centrer-réduire ; 95 % dans $m \pm 1{,}96\sigma$ |
