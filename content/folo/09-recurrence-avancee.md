---
title: Ch9 — Récurrences avancées et ordres bien fondés
summary: Récurrence d'ordre k, récurrence forte, choisir la bonne récurrence, ordres totaux et bien fondés, récurrence généralisée.
tags: [récurrence forte, récurrence d'ordre k, ordre bien fondé]
minutes: 60
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- rédiger une récurrence **d'ordre $k$** (avec ses $k$ initialisations) ;
- rédiger une récurrence **forte** ;
- **choisir** entre récurrence simple, d'ordre $k$ et forte ;
- définir un ordre **total** et un ordre **bien fondé**, trouver des **éléments minimaux** ;
- comprendre la **récurrence généralisée** sur un ensemble muni d'un ordre bien fondé.

:::intuition[Le fil conducteur]
Dans une récurrence simple, chaque domino fait tomber le **suivant**. Mais parfois, pour faire tomber le domino $n + 1$, il faut les **deux** précédents (Fibonacci), ou un domino **quelconque** plus petit (décomposition en facteurs premiers). Le principe reste le même : on part des plus petits éléments et on propage la propriété vers les plus grands.
:::

## 2. Récurrence d'ordre $k$

:::theorem[Récurrence d'ordre $k$ (*depth $k$ induction*)]
Soient $P$ une propriété des entiers, $n_0 \in \mathbb{N}$ et $k \in \mathbb{N}^*$ tels que :

- $P(n_0), \ldots, P(n_0 + k - 1)$ sont vraies ;
- $\forall n \ge n_0,\ \big(P(n) \wedge \cdots \wedge P(n + k - 1)\big) \Rightarrow P(n + k)$.

Alors $\forall n \ge n_0,\ P(n)$.
:::

:::pattern[Récurrence d'ordre $k$]
**But.** Montrer que $\forall n \ge n_0,\ P(n)$.

- On procède par récurrence d'ordre $k$.
- **Initialisation.** Montrer $P(n_0), \ldots, P(n_0 + k - 1)$ — utilise le bon $k$, et prouve **les $k$** cas de base.
- **Hérédité.** Soit $n \ge n_0$ tel que $P(n), \ldots, P(n + k - 1)$ sont vraies… trouve une relation (toutes les $k$ hypothèses ne servent pas forcément)… alors $P(n + k)$ est vraie.
:::

:::exercise[Exercice du cours 1 — Fibonacci]
La suite de Fibonacci est définie par $F_0 = 1$, $F_1 = 1$ et $\forall n \in \mathbb{N},\ F_{n+2} = F_{n+1} + F_n$. Montrer que $\forall n \in \mathbb{N},\ F_n \le \left(\frac{5}{3}\right)^n$.
:::

:::hint[Indice 1]
$F_{n+2}$ dépend des **deux** termes précédents : récurrence d'ordre 2, donc **deux** initialisations.
:::

:::hint[Indice 2]
Factorise $\left(\frac{5}{3}\right)^{n+1} + \left(\frac{5}{3}\right)^{n}$ par $\left(\frac{5}{3}\right)^{n}$ et compare $1 + \frac{5}{3} = \frac{8}{3} = \frac{24}{9}$ avec $\left(\frac{5}{3}\right)^2 = \frac{25}{9}$.
:::

:::correction
Notons $P(n)$ : « $F_n \le (5/3)^n$ ». Procédons par récurrence d'ordre 2.

**Initialisation.** $F_0 = 1 \le 1 = (5/3)^0$ et $F_1 = 1 \le 5/3$.

**Hérédité.** Soit $n \in \mathbb{N}$ tel que $P(n)$ et $P(n+1)$ sont vraies. Alors
$$F_{n+2} = F_{n+1} + F_n \le \left(\tfrac{5}{3}\right)^{n+1} + \left(\tfrac{5}{3}\right)^{n} = \left(\tfrac{5}{3}\right)^{n}\left(\tfrac{5}{3} + 1\right) = \left(\tfrac{5}{3}\right)^{n} \cdot \tfrac{24}{9} \le \left(\tfrac{5}{3}\right)^{n} \cdot \tfrac{25}{9} = \left(\tfrac{5}{3}\right)^{n+2}.$$
C'est $P(n+2)$.

**Conclusion.** Par récurrence d'ordre 2, $\forall n \in \mathbb{N},\ F_n \le (5/3)^n$. $\square$
:::

::item{id="ch9-fibonacci"}

:::exercise[Exercice du cours 2 — Payer avec des pièces de 3 et de 5]
Montrer que pour tout entier $n \ge 8$, il existe $a, b \in \mathbb{N}$ tels que $n = 3a + 5b$.
:::

:::hint[Indice]
Si $n$ s'écrit $3a + 5b$, alors $n + 3$ aussi (une pièce de 3 de plus). Quelle récurrence cela suggère-t-il, et combien d'initialisations faut-il ?
:::

:::correction
**Méthode 1 : récurrence d'ordre 3.** Notons $P(n)$ : « $\exists a, b \in \mathbb{N},\ n = 3a + 5b$ ».

- **Initialisation** ($n = 8, 9, 10$) : $8 = 3 \cdot 1 + 5 \cdot 1$, $9 = 3 \cdot 3 + 5 \cdot 0$, $10 = 3 \cdot 0 + 5 \cdot 2$.
- **Hérédité.** Soit $n \ge 8$ tel que $P(n)$, $P(n+1)$, $P(n+2)$. D'après $P(n)$, $n = 3a + 5b$, donc $n + 3 = 3(a + 1) + 5b$ : $P(n+3)$ est vraie (seule $P(n)$ a servi).

Par récurrence d'ordre 3, $\forall n \ge 8,\ P(n)$.

**Méthode 2 : récurrence simple avec disjonction de cas.** Initialisation : $8 = 3 + 5$. Hérédité : soit $n \ge 8$ avec $n = 3a + 5b$.
- Si $b \ge 1$ : on remplace une pièce de 5 par deux pièces de 3 : $n + 1 = 3(a + 2) + 5(b - 1)$.
- Si $b = 0$ : $n = 3a \ge 8$, donc $a \ge 3$ ; on remplace trois pièces de 3 par deux pièces de 5 : $n + 1 = 3(a - 3) + 5 \cdot 2$.

Dans les deux cas $P(n+1)$ est vraie. $\square$

Remarque : $7$ ne s'écrit pas $3a + 5b$ ; c'est le plus grand entier dans ce cas, d'où le $n_0 = 8$.
:::

::item{id="ch9-pieces"}

## 3. Récurrence forte

:::theorem[Récurrence forte (*strong induction*)]
Soient $P$ une propriété des entiers et $n_0 \in \mathbb{N}$ tels que :

- $P(n_0)$ est vraie ;
- $\forall n \ge n_0,\ \big(\forall k \in \{n_0, \ldots, n\},\ P(k)\big) \Rightarrow P(n + 1)$.

Alors $\forall n \ge n_0,\ P(n)$.
:::

:::pattern[Récurrence forte]
**But.** Montrer que $\forall n \ge n_0,\ P(n)$.

- On procède par récurrence forte sur $n$.
- **Initialisation.** Montrer $P(n_0)$.
- **Hérédité.** Soit $n \ge n_0$ tel que $\forall k \in \{n_0, \ldots, n\},\ P(k)$… relie $P(n + 1)$ à un ou plusieurs $P(k)$ (le rang $k$ peut dépendre de $n$ et être inconnu)… alors $P(n + 1)$.
:::

:::exercise[Exercice du cours 3 — Décomposition en facteurs premiers]
Montrer que tout entier $n \ge 2$ peut s'écrire comme un produit de nombres premiers.
:::

:::hint[Indice]
Si $n + 1$ n'est pas premier, il s'écrit $a \times b$ avec $2 \le a, b \le n$. On ne sait pas **lesquels** : il faut pouvoir appliquer l'hypothèse à **n'importe quel** rang plus petit.
:::

:::correction
$P(n)$ : « $n$ est un produit de nombres premiers » (un nombre premier seul compte comme un produit d'un facteur). Récurrence forte sur $n \ge 2$.

**Initialisation.** $2$ est premier : $P(2)$ est vraie.

**Hérédité.** Soit $n \ge 2$ tel que $P(k)$ est vraie pour tout $k \in \{2, \ldots, n\}$. Disjonction de cas :
- si $n + 1$ est premier, $P(n+1)$ est vraie ;
- sinon, $n + 1 = ab$ avec $a, b$ entiers tels que $2 \le a \le n$ et $2 \le b \le n$ (un diviseur non trivial). Par hypothèse de récurrence forte, $a$ et $b$ sont des produits de nombres premiers, donc $n + 1 = ab$ aussi.

**Conclusion.** Par récurrence forte, tout $n \ge 2$ est un produit de nombres premiers. $\square$

Une récurrence **simple** ne suffit pas : connaître la décomposition de $n$ ne dit rien sur celle de $n + 1$.
:::

:::exercise[Exercice du cours 4 — Une suite moyenne]
Soit $(u_n)$ définie par $u_0 = 1$ et $\forall n \in \mathbb{N},\ u_{n+1} = \frac{u_0 + \cdots + u_n}{n + 1}$. Montrer que $\forall n \in \mathbb{N},\ u_n = 1$.
:::

:::correction
$P(n)$ : « $u_n = 1$ ». Récurrence forte.

**Initialisation.** $u_0 = 1$.

**Hérédité.** Soit $n \in \mathbb{N}$ tel que $u_0 = \cdots = u_n = 1$. Alors $u_{n+1} = \frac{1 + \cdots + 1}{n+1} = \frac{n+1}{n+1} = 1$ ($n + 1$ termes).

Par récurrence forte, $\forall n,\ u_n = 1$. $\square$ (Ici $u_{n+1}$ dépend de **tous** les termes précédents : le nombre d'hypothèses utilisées grandit avec $n$.)
:::

## 4. Choisir la bonne récurrence

| Situation | Récurrence |
|---|---|
| lien direct entre $P(n+1)$ et $P(n)$ | **simple** |
| il existe un $k$ **fixe** tel que $P(n+k)$ se déduit de $P(n), \ldots, P(n+k-1)$ ($k$ ne doit pas dépendre de $n$) | **d'ordre $k$** ($k$ initialisations) |
| $P(n+1)$ se déduit d'un ou plusieurs $P(i)$ plus petits, dont le rang $i$ est inconnu ou dépend de $n$ | **forte** |

::item{id="ch9-choix"}

## 5. Relations d'ordre et récurrence généralisée

Le principe de récurrence part des **plus petits** éléments et propage la propriété vers les plus grands. Pour le prouver (ch. 8), on a utilisé l'existence d'un plus petit élément dans toute partie non vide de $\mathbb{N}$. On généralise cette idée à d'autres ensembles ordonnés.

Rappel (chapitre 5) : un **ordre** $\preceq$ est une relation réflexive, antisymétrique et transitive. Il est **total** si deux éléments sont toujours comparables.

:::definition[Élément minimal, ordre bien fondé]
Soit $\preceq$ un ordre sur $E$ et $F \subseteq E$. Un élément $x$ est **minimal** dans $F$ si $x \in F$ et s'il n'existe aucun $y \in F \setminus \{x\}$ tel que $y \preceq x$.

L'ordre $\preceq$ est **bien fondé** si toute partie **non vide** de $E$ admet (au moins) un élément minimal.
:::

| Ordre | Total ? | Bien fondé ? |
|---|---|---|
| $\le$ sur $\mathbb{N}$ | oui | oui |
| $\le$ sur $\mathbb{Z}$ ou $\mathbb{R}$ | oui | **non** : $\mathbb{Z}$ lui-même n'a pas d'élément minimal ; dans $\mathbb{R}$, $]0, 1]$ non plus |
| $\subseteq$ sur les parties **finies** de $\mathbb{N}$ | non : $\{1\} \not\subseteq \{2\}$ et $\{2\} \not\subseteq \{1\}$ | oui |
| divisibilité sur $\mathbb{N}^*$ | non | oui |

:::warning[Minimal ≠ plus petit]
Un élément minimal n'est pas forcément comparable aux autres, et il peut y en avoir **plusieurs** : dans $\{\{1\}, \{2\}, \{1, 2\}\}$ ordonné par $\subseteq$, $\{1\}$ et $\{2\}$ sont tous deux minimaux, mais aucun n'est « le plus petit ».
:::

::item{id="ch9-ordres"}

:::theorem[Récurrence généralisée]
Soient $E$ un ensemble, $\preceq$ un ordre **bien fondé** sur $E$ et $P$ une propriété sur $E$ telles que :

- $P(x)$ est vraie pour tout élément **minimal** $x$ de $E$ ;
- pour tout $x \in E$ : si $P(y)$ est vraie pour tous les $y \preceq x$ avec $y \neq x$, alors $P(x)$ est vraie.

Alors $\forall x \in E,\ P(x)$.
:::

La récurrence forte sur $\mathbb{N}$ en est le cas particulier « $\le$ sur $\{n \ge n_0\}$ » (seul élément minimal : $n_0$).

:::example[La décomposition en facteurs premiers, vue autrement]
Sur $E = \{n \in \mathbb{N} \mid n \ge 2\}$ ordonné par la **divisibilité**, les éléments minimaux sont exactement les **nombres premiers** (un nombre premier n'a pas d'autre diviseur $\ge 2$ que lui-même). La décomposition en facteurs premiers est vraie pour les éléments minimaux, et si $n$ n'est pas premier, $n = ab$ où $a$ et $b$ sont des diviseurs stricts de $n$, pour lesquels on suppose la propriété : c'est la récurrence généralisée.
:::

## 6. Fiche récapitulative

:::key[L'essentiel]
- **Ordre $k$** : $k$ initialisations, hérédité « $P(n), \ldots, P(n+k-1) \Rightarrow P(n+k)$ » ; $k$ fixe.
- **Forte** : hérédité « $P(n_0), \ldots, P(n) \Rightarrow P(n+1)$ » ; utile quand le rang utilisé est inconnu (diviseurs, découpages).
- Toujours **annoncer** le type de récurrence (« par récurrence d'ordre 2… »).
- **Bien fondé** : toute partie non vide a un élément minimal ; c'est ce qui rend une récurrence possible.
- $\le$ sur $\mathbb{N}$ : total et bien fondé ; $\subseteq$ (parties finies) et $\mid$ : bien fondés mais pas totaux.
:::
