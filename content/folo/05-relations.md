---
title: Ch5 — Relations binaires
summary: Relations, réflexivité, symétrie, antisymétrie, transitivité, relations d'équivalence et classes, relations d'ordre — la théorie derrière le projet Python.
tags: [relations, équivalence, ordre, projet]
minutes: 55
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- définir une **relation binaire** comme un ensemble de couples ;
- vérifier (et réfuter) **réflexivité, symétrie, antisymétrie, transitivité** ;
- reconnaître une **relation d'équivalence** et calculer ses **classes** ;
- prouver que les classes d'équivalence forment une **partition** ;
- reconnaître une **relation d'ordre**, partielle ou totale ;
- traduire chaque propriété en Python avec `all` / `any` (projet `folo.py`, questions 1 et 8 à 15).

:::intuition[Le fil conducteur]
Une relation, c'est simplement **la liste des couples qui sont « en relation »**. Toutes les propriétés (réflexive, symétrique…) sont des énoncés quantifiés sur cette liste. Dessine la relation comme un **graphe** (une flèche $x \to y$ pour chaque couple) : chaque propriété devient une forme visible.
:::

## 2. Relation binaire

:::definition[Relation binaire]
Une **relation binaire** de $E$ vers $F$ est une partie $R \subseteq E \times F$. On lui associe le prédicat $\sim_R$ : $x \sim_R y$ est vraie si et seulement si $(x, y) \in R$. Quand $F = E$, on parle de relation **sur** $E$.
:::

:::example
La divisibilité $\mid$ sur $\mathbb{N} \times \mathbb{N}$ : $(2, 4) \in {\mid}$, ce qu'on écrit plutôt $2 \mid 4$. L'égalité, $\le$, « avoir la même longueur » (pour des mots), « être né le même jour » sont des relations.
:::

Une relation a un **sens** : $x \sim_R y$ n'entraîne pas forcément $y \sim_R x$ ($3 \mid 6$ mais $6 \nmid 3$).

En Python (projet), une relation est un `set` de tuples : `pairs = {(1, 2), (2, 3)}`. La question 1 du projet demande de vérifier que `pairs` est bien une relation sur `es × fs`, c'est-à-dire que **chaque couple** a sa première composante dans `es` et sa seconde dans `fs` :

$$R \subseteq E \times F \iff \forall (x, y) \in R,\ (x \in E) \wedge (y \in F)$$

## 3. Les quatre propriétés d'une relation sur $E$

Soit $\sim$ une relation sur $E$ (une partie de $E \times E$). Elle est dite :

:::definition[Réflexive, symétrique, antisymétrique, transitive]
- **réflexive** si $\forall x \in E,\ x \sim x$ ;
- **symétrique** si $\forall x, y \in E,\ (x \sim y) \Rightarrow (y \sim x)$ ;
- **antisymétrique** si $\forall x, y \in E,\ \big((x \sim y) \wedge (y \sim x)\big) \Rightarrow (x = y)$ ;
- **transitive** si $\forall x, y, z \in E,\ \big((x \sim y) \wedge (y \sim z)\big) \Rightarrow (x \sim z)$.
:::

<figure class="venn-row">
<svg viewBox="0 0 160 150" role="img" aria-label="Relation réflexive"><defs><marker id="rel-arr-1" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 z" class="accent-fill"/></marker></defs><circle cx="30" cy="95" r="11" class="accent"/><circle cx="130" cy="95" r="11" class="accent"/><circle cx="80" cy="40" r="11" class="accent"/><text x="30" y="100" text-anchor="middle">1</text><text x="130" y="100" text-anchor="middle">2</text><text x="80" y="45" text-anchor="middle">3</text><path d="M73,31 C60,5 100,5 87,31" class="accent" marker-end="url(#rel-arr-1)"/><path d="M23,104 C10,130 50,130 37,104" class="accent" marker-end="url(#rel-arr-1)"/><path d="M123,104 C110,130 150,130 137,104" class="accent" marker-end="url(#rel-arr-1)"/><text x="80" y="146" text-anchor="middle">réflexive</text></svg>
<svg viewBox="0 0 160 150" role="img" aria-label="Relation symétrique"><defs><marker id="rel-arr-2" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 z" class="accent-fill"/></marker></defs><circle cx="30" cy="95" r="11" class="accent"/><circle cx="130" cy="95" r="11" class="accent"/><circle cx="80" cy="40" r="11" class="accent"/><text x="30" y="100" text-anchor="middle">1</text><text x="130" y="100" text-anchor="middle">2</text><text x="80" y="45" text-anchor="middle">3</text><line x1="41" y1="91" x2="117" y2="91" class="accent" marker-end="url(#rel-arr-2)"/><line x1="119" y1="99" x2="43" y2="99" class="accent" marker-end="url(#rel-arr-2)"/><line x1="35" y1="84" x2="70" y2="46" class="accent" marker-end="url(#rel-arr-2)"/><line x1="76" y1="51" x2="41" y2="89" class="accent" marker-end="url(#rel-arr-2)"/><text x="80" y="146" text-anchor="middle">symétrique</text></svg>
<svg viewBox="0 0 160 150" role="img" aria-label="Relation antisymétrique"><defs><marker id="rel-arr-3" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 z" class="accent-fill"/></marker></defs><circle cx="30" cy="95" r="11" class="accent"/><circle cx="130" cy="95" r="11" class="accent"/><circle cx="80" cy="40" r="11" class="accent"/><text x="30" y="100" text-anchor="middle">1</text><text x="130" y="100" text-anchor="middle">2</text><text x="80" y="45" text-anchor="middle">3</text><line x1="41" y1="95" x2="117" y2="95" class="accent" marker-end="url(#rel-arr-3)"/><line x1="37" y1="87" x2="71" y2="49" class="accent" marker-end="url(#rel-arr-3)"/><line x1="87" y1="48" x2="121" y2="85" class="accent" marker-end="url(#rel-arr-3)"/><path d="M23,104 C10,130 50,130 37,104" class="accent" marker-end="url(#rel-arr-3)"/><text x="80" y="146" text-anchor="middle">antisymétrique</text></svg>
<svg viewBox="0 0 160 150" role="img" aria-label="Relation transitive"><defs><marker id="rel-arr-4" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 z" class="accent-fill"/></marker></defs><circle cx="30" cy="95" r="11" class="accent"/><circle cx="130" cy="95" r="11" class="accent"/><circle cx="80" cy="40" r="11" class="accent"/><text x="30" y="100" text-anchor="middle">1</text><text x="130" y="100" text-anchor="middle">2</text><text x="80" y="45" text-anchor="middle">3</text><line x1="37" y1="87" x2="71" y2="49" class="accent" marker-end="url(#rel-arr-4)"/><line x1="87" y1="48" x2="121" y2="85" class="accent" marker-end="url(#rel-arr-4)"/><line x1="41" y1="95" x2="117" y2="95" class="ok" stroke-dasharray="4 3" marker-end="url(#rel-arr-4)"/><text x="80" y="146" text-anchor="middle">transitive</text></svg>
</figure>

Lecture des graphes : **réflexive** = une boucle sur **chaque** sommet ; **symétrique** = toute flèche a sa flèche retour ; **antisymétrique** = jamais d'aller-retour entre deux sommets **distincts** (les boucles sont permises) ; **transitive** = tout chemin $x \to y \to z$ a son **raccourci** $x \to z$ (en pointillés).

:::warning[Antisymétrique n'est pas « non symétrique »]
- Une relation peut être **à la fois** symétrique et antisymétrique : l'égalité, ou la relation vide.
- Une relation peut n'être **ni l'une ni l'autre** : sur $\{1, 2, 3\}$, $\{(1, 2), (2, 1), (2, 3)\}$.
:::

:::note[Une variante de définition dans les slides]
Les slides (*Advanced Inductive Proofs*) écrivent l'antisymétrie avec $\Leftrightarrow$ : $\big((x \sim y) \wedge (y \sim x)\big) \Leftrightarrow (x = y)$. Le sens $\Leftarrow$ ajoute « $x \sim x$ pour tout $x$ », c'est-à-dire la **réflexivité**. Pour une relation d'ordre (toujours réflexive), les deux versions coïncident. Mais pour une relation quelconque, utilise la version avec $\Rightarrow$ : c'est celle de l'énoncé du projet, et les tests officiels l'exigent (ils vérifient que $<$ est antisymétrique, alors que $<$ n'est pas réflexive).
:::

:::warning[Le piège de la vérité vide]
Une relation sur un ensemble **vide** est réflexive (« pour tout $x \in \emptyset$… » est toujours vrai). La relation **vide** sur un ensemble non vide est symétrique, antisymétrique et transitive (aucun couple, donc aucun contre-exemple), mais **pas réflexive**.
:::

:::exercise[Exercice — Le faux théorème]
« Toute relation symétrique et transitive est réflexive. *Preuve* : soit $x \in E$ et $y$ tel que $x \sim y$. Par symétrie $y \sim x$, puis par transitivité $x \sim x$. » Où est l'erreur ?
:::

:::correction
La preuve suppose qu'il **existe** un $y$ tel que $x \sim y$ : rien ne le garantit. Contre-exemple : sur $E = \{1, 2\}$, la relation $\{(1, 1)\}$ est symétrique et transitive, mais pas réflexive ($2 \not\sim 2$, car $2$ n'est en relation avec personne). La « preuve » est correcte uniquement pour les $x$ qui ont au moins un voisin.
:::

::item{id="ch5-proprietes"}

## 4. Relations d'équivalence et classes

:::definition[Relation d'équivalence]
Une relation d'**équivalence** sur $E$ est une relation **réflexive, symétrique et transitive**. On la note souvent $\equiv$.
:::

Elle formalise l'idée « avoir la même caractéristique » : même reste modulo 3, même longueur, même date de naissance…

:::definition[Classe d'équivalence]
Pour $x \in E$, la **classe** de $x$ est l'ensemble des éléments équivalents à $x$ :
$$[x]_\equiv = \{y \in E \mid x \equiv y\}.$$
:::

:::example[Congruence modulo 3 sur $\{0, \ldots, 8\}$]
$x \equiv y$ si et seulement si $3 \mid (x - y)$. Les classes sont $[0] = \{0, 3, 6\}$, $[1] = \{1, 4, 7\}$, $[2] = \{2, 5, 8\}$, et par exemple $[4] = [1]$ : deux éléments équivalents ont la **même** classe.
:::

<figure>
<svg viewBox="0 0 360 90" role="img" aria-label="Partition de 0 à 8 en trois classes modulo 3"><rect x="5" y="10" width="110" height="50" rx="10" class="accent"/><rect x="125" y="10" width="110" height="50" rx="10" class="accent"/><rect x="245" y="10" width="110" height="50" rx="10" class="accent"/><text x="60" y="41" text-anchor="middle">0 · 3 · 6</text><text x="180" y="41" text-anchor="middle">1 · 4 · 7</text><text x="300" y="41" text-anchor="middle">2 · 5 · 8</text><text x="60" y="80" text-anchor="middle" class="muted-text">[0]</text><text x="180" y="80" text-anchor="middle" class="muted-text">[1] = [4] = [7]</text><text x="300" y="80" text-anchor="middle" class="muted-text">[2]</text></svg>
<figcaption>Les classes d'équivalence découpent l'ensemble en morceaux disjoints qui le recouvrent : une partition.</figcaption>
</figure>

:::theorem[Les classes forment une partition]
Soit $\equiv$ une relation d'équivalence sur $E$. Alors :

1. chaque classe est non vide : $x \in [x]$ ;
2. deux classes sont égales ou disjointes : $[x] \cap [y] \neq \emptyset \Rightarrow [x] = [y]$ ;
3. les classes recouvrent $E$ : tout $x \in E$ appartient à une classe.

De plus, $x \equiv y \iff [x] = [y]$.
:::

:::correction[Voir la preuve]
1. Par réflexivité, $x \equiv x$, donc $x \in [x]$ : la classe est non vide.
3. Découle de 1 : $x \in [x]$.
2. Supposons qu'il existe $z \in [x] \cap [y]$ : $x \equiv z$ et $y \equiv z$. Par symétrie $z \equiv y$, puis par transitivité $x \equiv y$. Montrons $[y] \subseteq [x]$ : soit $w \in [y]$, donc $y \equiv w$ ; avec $x \equiv y$ et la transitivité, $x \equiv w$, donc $w \in [x]$. Par symétrie des rôles ($y \equiv x$ aussi), $[x] \subseteq [y]$. D'où $[x] = [y]$.

Enfin, si $x \equiv y$, alors $y \in [x] \cap [y]$ (car $y \in [y]$), donc $[x] = [y]$ par 2 ; réciproquement, si $[x] = [y]$, alors $y \in [y] = [x]$, donc $x \equiv y$. $\square$
:::

En Python (question 13 du projet), la classe de `e` se calcule directement par compréhension : l'ensemble des `y` de `es` tels que `(e, y)` est dans `pairs` — c'est la traduction littérale de $\{y \in E \mid e \equiv y\}$.

::item{id="ch5-classes"}

## 5. Relations d'ordre

:::definition[Relation d'ordre]
Une relation d'**ordre** (partiel) sur $E$ est une relation **réflexive, antisymétrique et transitive**. On la note souvent $\preceq$.

Elle est **totale** si deux éléments sont toujours comparables : $\forall x, y \in E,\ (x \preceq y) \vee (y \preceq x)$.
:::

| Relation | Ensemble | Ordre ? | Total ? |
|---|---|---|---|
| $\le$ | $\mathbb{R}$, $\mathbb{N}$ | oui | oui |
| $\subseteq$ | $\mathcal{P}(E)$ | oui | non dès que $E$ a 2 éléments : $\{1\} \not\subseteq \{2\}$ et $\{2\} \not\subseteq \{1\}$ |
| $\mid$ (divise) | $\mathbb{N}^*$ | oui | non : $2 \nmid 3$ et $3 \nmid 2$ |
| $\mid$ (divise) | $\mathbb{Z}^*$ | **non** : $2 \mid -2$ et $-2 \mid 2$ mais $2 \neq -2$ | — |
| $<$ | $\mathbb{R}$ | **non** : pas réflexive (c'est un ordre *strict*) | — |

<figure>
<svg viewBox="0 0 200 200" role="img" aria-label="Diagramme de la divisibilité sur les diviseurs de 12"><line x1="100" y1="168" x2="66" y2="142" class="muted"/><line x1="100" y1="168" x2="134" y2="142" class="muted"/><line x1="60" y1="118" x2="60" y2="87" class="muted"/><line x1="66" y1="118" x2="134" y2="87" class="muted"/><line x1="140" y1="118" x2="140" y2="87" class="muted"/><line x1="66" y1="63" x2="94" y2="37" class="muted"/><line x1="134" y1="63" x2="106" y2="37" class="muted"/><circle cx="100" cy="180" r="13" class="accent"/><circle cx="60" cy="130" r="13" class="accent"/><circle cx="140" cy="130" r="13" class="accent"/><circle cx="60" cy="75" r="13" class="accent"/><circle cx="140" cy="75" r="13" class="accent"/><circle cx="100" cy="25" r="13" class="accent"/><text x="100" y="185" text-anchor="middle">1</text><text x="60" y="135" text-anchor="middle">2</text><text x="140" y="135" text-anchor="middle">3</text><text x="60" y="80" text-anchor="middle">4</text><text x="140" y="80" text-anchor="middle">6</text><text x="100" y="30" text-anchor="middle">12</text></svg>
<figcaption>La divisibilité sur les diviseurs de 12 (diagramme de Hasse : $a$ est relié à $b$ au-dessus si $a \mid b$, boucles et raccourcis omis). 4 et 6 ne sont pas comparables : l'ordre n'est pas total.</figcaption>
</figure>

::item{id="ch5-ordres"}

## 6. Fonctions vues comme des relations (aperçu)

Une fonction est une relation particulière (chapitre 6). Pour une relation $\sim$ de $E$ vers $F$ :

- c'est une **fonction partielle** si chaque $x$ a **au plus une** image : $\forall x \in E,\ \forall y_1, y_2 \in F,\ (x \sim y_1) \wedge (x \sim y_2) \Rightarrow y_1 = y_2$ ;
- c'est une **fonction** si chaque $x$ a **exactement une** image : $\forall x \in E,\ \exists! y \in F,\ x \sim y$.

(Questions 2 et 3 du projet.)

## 7. Exercices

:::exercise[Exercice 1 — Cinq relations sur $\{1, 2, 3\}$]
Pour chaque relation sur $E = \{1, 2, 3\}$, dire si elle est réflexive, symétrique, antisymétrique, transitive :
$R_1 = \{(1,1), (2,2), (3,3)\}$, $R_2 = \{(1,2), (2,1)\}$, $R_3 = \{(1,2), (2,3)\}$, $R_4 = \emptyset$, $R_5 = E \times E$.
:::

:::correction
| | réflexive | symétrique | antisymétrique | transitive |
|---|---|---|---|---|
| $R_1$ (égalité) | oui | oui | oui | oui |
| $R_2$ | non (pas de boucle) | oui | non : $1 \sim 2$, $2 \sim 1$, $1 \neq 2$ | **non** : $1 \sim 2 \sim 1$ mais $(1, 1) \notin R_2$ |
| $R_3$ | non | non | oui | non : $1 \sim 2 \sim 3$ mais $(1, 3) \notin R_3$ |
| $R_4$ (vide) | non ($E \neq \emptyset$) | oui | oui | oui |
| $R_5$ (pleine) | oui | oui | non | oui |

$R_1$ est à la fois une relation d'équivalence et une relation d'ordre ; $R_5$ est une relation d'équivalence (une seule classe : $E$).
:::

::item{id="ch5-ex1"}

:::exercise[Exercice 2 — Congruence modulo $n$]
Soit $n \in \mathbb{N}^*$. Sur $\mathbb{Z}$, on pose $x \equiv y \iff n \mid (x - y)$. Montrer que c'est une relation d'équivalence et décrire ses classes.
:::

:::correction
- **Réflexive** : $x - x = 0 = n \cdot 0$, donc $n \mid 0$.
- **Symétrique** : si $x - y = nk$, alors $y - x = n(-k)$.
- **Transitive** : si $x - y = nk$ et $y - z = nl$, alors $x - z = n(k + l)$.

Les classes sont $[0], [1], \ldots, [n-1]$ : $[r] = \{r + nk \mid k \in \mathbb{Z}\}$, l'ensemble des entiers de reste $r$ dans la division par $n$. Il y a exactement $n$ classes. $\square$
:::

:::exercise[Exercice 3 — « Être proche »]
Sur $\mathbb{R}$, on pose $x \sim y \iff |x - y| \le 1$. Est-ce une relation d'équivalence ?
:::

:::correction
Elle est réflexive ($|x - x| = 0 \le 1$) et symétrique ($|x - y| = |y - x|$), mais **pas transitive** : $0 \sim 1$ et $1 \sim 2$, mais $|0 - 2| = 2 > 1$. Ce n'est donc pas une relation d'équivalence. (Morale : « être proche » ne se propage pas.)
:::

:::exercise[Exercice 4 — Divisibilité]
Montrer que la divisibilité est une relation d'ordre sur $\mathbb{N}^*$. Est-elle totale ?
:::

:::correction
- **Réflexive** : $a = 1 \cdot a$, donc $a \mid a$.
- **Antisymétrique** : si $a \mid b$ et $b \mid a$, il existe $k, l \in \mathbb{N}^*$ tels que $b = ka$ et $a = lb$. Alors $a = lka$, donc $lk = 1$ (car $a \neq 0$), d'où $k = l = 1$ (ce sont des entiers naturels non nuls) et $a = b$.
- **Transitive** : si $b = ka$ et $c = lb$, alors $c = (lk) a$, donc $a \mid c$.

Elle n'est **pas totale** : ni $2 \mid 3$ ni $3 \mid 2$. Remarque : sur $\mathbb{Z}^*$, l'antisymétrie échoue ($2 \mid -2$ et $-2 \mid 2$), car $lk = 1$ autorise $k = l = -1$. $\square$
:::

## 8. Fiche récapitulative

| Propriété | Formule | En Python (idée) |
|---|---|---|
| relation sur $E \times F$ | $\forall (x,y) \in R,\ x \in E \wedge y \in F$ | `all(x in es and y in fs for (x, y) in pairs)` |
| réflexive | $\forall x,\ x \sim x$ | `all((x, x) in pairs for x in es)` |
| symétrique | $x \sim y \Rightarrow y \sim x$ | parcourir les couples présents |
| antisymétrique | $x \sim y \wedge y \sim x \Rightarrow x = y$ | parcourir les couples présents |
| transitive | $x \sim y \wedge y \sim z \Rightarrow x \sim z$ | ne parcourir que les $z$ **reliés à** $y$ |
| équivalence | réfl. + sym. + trans. | — |
| ordre | réfl. + antisym. + trans. | — |
| ordre total | ordre + $\forall x, y,\ x \preceq y \vee y \preceq x$ | — |

:::key[À retenir]
- Une relation = un ensemble de couples ; une propriété = un énoncé quantifié sur ces couples.
- Antisymétrique ≠ non symétrique. Vérité vide : relation vide sur $E \neq \emptyset$ → symétrique, antisymétrique, transitive, pas réflexive.
- Les classes d'une relation d'équivalence forment une **partition** ; $x \equiv y \iff [x] = [y]$.
- $\le$ : ordre total ; $\subseteq$ et $\mid$ : ordres partiels.
:::
