---
title: Ch4 — Logique quantifiée
summary: Quantificateurs ∀, ∃, ∃!, leurs motifs de preuve en hypothèse et en conclusion, l'ensemble vide et les quantificateurs multiples.
tags: [quantificateurs, existence, unicité]
minutes: 50
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- lire et écrire des énoncés avec $\forall$, $\exists$, $\exists!$ ;
- appliquer le bon motif selon que le quantificateur est dans le **but** ou dans une **hypothèse** ;
- prouver une **existence** (exhiber un témoin) et une **unicité** ;
- raisonner sur l'**ensemble vide** ($\forall x \in \emptyset$ est toujours vrai, $\exists x \in \emptyset$ toujours faux) ;
- formaliser une phrase avec plusieurs quantificateurs, en respectant leur **portée**.

:::intuition[Le fil conducteur]
Une proposition peut dépendre d'une variable : « $n$ est pair ou impair » a un sens pour un entier, pas pour un réel. Les quantificateurs disent **pour quelles valeurs** la propriété doit tenir : **toutes** ($\forall$), **au moins une** ($\exists$), **exactement une** ($\exists!$). En Python, $\forall$ s'écrit `all(...)` et $\exists$ s'écrit `any(...)` — tu les utiliseras dans le projet.
:::

## 2. Le quantificateur universel $\forall$

:::definition[Quantificateur universel]
Pour un ensemble $E$ et une proposition $P(x)$ dépendant d'une variable $x$, la proposition $\forall x \in E,\ P(x)$ signifie « pour tout $x$ appartenant à $E$, $P(x)$ est vraie ». On dit que $x$ est **quantifiée** par $\forall x \in E$.
:::

Exemple : $\forall x \in \mathbb{R},\ x^2 \ge 0$ est vraie.

:::pattern[$\forall$]
**But.** Montrer que $\forall x \in E,\ P(x)$.

- Soit $x \in E$… *(un $x$ **quelconque** : on ne choisit pas sa valeur)*
- … alors $P(x)$ est vraie.
:::

:::warning[« Soit » ≠ « par exemple »]
Vérifier $P(1)$, $P(2)$ et $P(3)$ ne prouve **pas** $\forall x,\ P(x)$. « Soit $x \in E$ » signifie : je prends un élément **arbitraire**, sur lequel je ne sais rien d'autre que $x \in E$, et ma preuve doit marcher pour lui.
:::

:::exercise[Exercice du cours 1]
Montrer que $\forall n, m \in \mathbb{N},\ n^2 + m^2 \ge 2nm$.
:::

:::hint[Indice]
Fais tout passer du même côté et reconnais une identité remarquable.
:::

:::correction
**But.** Montrons que pour tous $n, m \in \mathbb{N}$, $n^2 + m^2 \ge 2nm$.

Soient $n, m \in \mathbb{N}$. Alors $n^2 + m^2 - 2nm = (n - m)^2 \ge 0$, car un carré est positif. Donc $n^2 + m^2 \ge 2nm$. $\square$

(La preuve n'utilise pas que $n, m$ sont entiers : elle vaut pour tous les réels.)
:::

### 2.1 $\forall$ dans la conclusion, $\forall$ dans une hypothèse

:::pattern[$\forall$ en conclusion]
**But.** Montrer que $P \Rightarrow (\forall x \in E,\ Q(x))$.

- Supposons que $P$ est vraie.
- Soit $x \in E$…
- … alors $Q(x)$ est vraie.
:::

:::pattern[$\forall$ en hypothèse]
**But.** Montrer que $(\forall x \in E,\ P(x)) \Rightarrow Q$.

- Supposons que $\forall x \in E,\ P(x)$ est vraie.
- Considérons une ou plusieurs valeurs **particulières** $x_0, x_1, \ldots \in E$ (bien choisies).
- Évidemment, $P(x_0), P(x_1), \ldots$ sont vraies…
- … alors $Q$ est vraie.
:::

Une hypothèse universelle est une **mine** : tu peux l'appliquer à **n'importe quelle** valeur, à toi de choisir les plus utiles.

:::exercise[Exercice du cours 2]
Montrer que si $a, b, c \in \mathbb{R}$ sont tels que $\forall x \in \mathbb{R},\ a x^2 + b x + c = 0$, alors $a = b = c = 0$.
:::

:::hint[Indice]
L'hypothèse est vraie pour **tout** $x$ : choisis des valeurs de $x$ qui simplifient au maximum l'expression ($x = 0$, puis $x = 1$ et $x = -1$).
:::

:::correction
Supposons que $\forall x \in \mathbb{R},\ ax^2 + bx + c = 0$. On applique l'hypothèse à des valeurs particulières :

- $x = 0$ : $c = 0$.
- $x = 1$ : $a + b + c = 0$, donc $a + b = 0$.
- $x = -1$ : $a - b + c = 0$, donc $a - b = 0$.

En additionnant les deux dernières égalités : $2a = 0$, donc $a = 0$, puis $b = -a = 0$. Ainsi $a = b = c = 0$. $\square$
:::

## 3. Le quantificateur existentiel $\exists$

:::definition[Quantificateur existentiel]
$\exists x \in E,\ P(x)$ signifie « il existe (au moins) un $x$ appartenant à $E$ tel que $P(x)$ est vraie ».
:::

Exemple : $\exists x \in \mathbb{R},\ x^2 = 2$ est vraie (prendre $x = \sqrt{2}$).

:::pattern[$\exists$]
**But.** Montrer que $\exists x \in E,\ P(x)$.

- Exhibons une valeur **particulière** $x_0 \in E$…
- … alors $P(x_0)$ est vraie.
:::

:::pattern[$\exists$ en hypothèse]
**But.** Montrer que $(\exists x \in E,\ P(x)) \Rightarrow Q$.

- Supposons que $\exists x \in E,\ P(x)$.
- Considérons un $x_0 \in E$ tel que $P(x_0)$ est vraie… *(on ne choisit pas lequel : on le reçoit)*
- … alors $Q$ est vraie.
:::

:::pattern[$\exists$ en conclusion]
**But.** Montrer que $P \Rightarrow (\exists x \in E,\ Q(x))$.

- Supposons que $P$ est vraie.
- Exhibons une valeur particulière $x_0 \in E$…
- … $Q(x_0)$ est prouvée vraie.
:::

:::key[Qui choisit la valeur ?]
| Position | $\forall x$ | $\exists x$ |
|---|---|---|
| **dans le but** | l'adversaire choisit : « Soit $x$ » | **tu** choisis : « Posons $x_0 = \ldots$ » |
| **en hypothèse** | **tu** choisis à quoi l'appliquer | l'adversaire choisit : « Soit $x_0$ tel que… » |
:::

:::exercise[Exercice du cours 3]
Montrer que si $a, b \in \mathbb{R}$ et $a \neq 0$, alors $\exists x \in \mathbb{R},\ a x + b = 0$.
:::

:::hint[Indice]
Résous l'équation au brouillon pour **trouver** le témoin, puis présente-le et **vérifie**-le.
:::

:::correction
Supposons $a \neq 0$. Posons $x_0 = -\frac{b}{a}$, qui existe bien dans $\mathbb{R}$ car $a \neq 0$. Alors $a x_0 + b = a \cdot \left(-\frac{b}{a}\right) + b = -b + b = 0$. Donc $\exists x \in \mathbb{R},\ ax + b = 0$. $\square$

Remarque de rédaction : le calcul qui t'a permis de *trouver* $x_0$ (« $ax + b = 0 \iff x = -b/a$ ») est du brouillon ; la preuve, c'est « je pose $x_0$ et je **vérifie** ».
:::

## 4. Existence et unicité : $\exists!$

Si $\exists x \in E,\ P(x)$ est vraie, au moins un élément vérifie $P$, mais peut-être plusieurs. On introduit $\exists!x \in E$ : « il existe **exactement un** $x$ dans $E$ ».

Exemple : $\exists! x \in \mathbb{R}_+,\ x^2 = 2$ est vraie ; mais $\exists! x \in \mathbb{R},\ x^2 = 2$ est fausse ($\sqrt{2}$ et $-\sqrt{2}$).

:::pattern[$\exists!$]
**But.** Montrer que $\exists! x \in E,\ P(x)$.

- **Sous-but 1 (existence).** Montrer que $\exists x \in E,\ P(x)$, comme ci-dessus.
- **Sous-but 2 (unicité).** Montrer que $\forall x_1, x_2 \in E,\ P(x_1) \wedge P(x_2) \Rightarrow x_1 = x_2$ — par implication directe, par l'absurde ou par contraposée.
:::

:::exercise[Exercice du cours 4]
Montrer que si $a, b \in \mathbb{R}$ et $a \neq 0$, alors $\exists! x \in \mathbb{R},\ a x + b = 0$.
:::

:::correction
Supposons $a \neq 0$.

- **Existence.** C'est l'exercice 3 : $x_0 = -\frac{b}{a}$ convient.
- **Unicité.** Soient $x_1, x_2 \in \mathbb{R}$ tels que $a x_1 + b = 0$ et $a x_2 + b = 0$. En soustrayant : $a(x_1 - x_2) = 0$. Comme $a \neq 0$, on peut diviser par $a$ : $x_1 - x_2 = 0$, donc $x_1 = x_2$.

Il existe donc un unique réel $x$ tel que $ax + b = 0$. $\square$
:::

:::warning[L'unicité ne se prouve pas en « trouvant » la solution]
Écrire « la solution est $-b/a$ » ne prouve pas qu'il n'y en a pas d'autre. L'unicité se prouve en prenant **deux** solutions quelconques et en montrant qu'elles sont égales.
:::

## 5. Quantifier sur l'ensemble vide

- $\exists x \in \emptyset,\ P(x)$ est **toujours fausse**, quelle que soit $P$ : on ne peut pas trouver de $x$ dans $\emptyset$, encore moins un qui vérifie $P$.
- $\forall x \in \emptyset,\ P(x)$ est **toujours vraie**, quelle que soit $P$ (« vérité vide ») : il n'y a aucun contre-exemple possible.
- Par conséquent : $(\exists x \in E) \iff E \neq \emptyset$.

En Python : `all(p(x) for x in [])` vaut `True` et `any(p(x) for x in [])` vaut `False` — pense-y dans le projet (une relation vide sur un ensemble vide est… réflexive !).

:::pattern[Ensemble vide]
**But.** Montrer que $E = \emptyset$.

- Supposons que $E \neq \emptyset$.
- Considérons alors un $x \in E$…
- … et prouvons quelque chose de manifestement faux.
- Par l'absurde, $E = \emptyset$.
:::

::item{id="ch4-vrai-faux"}

## 6. Plusieurs quantificateurs

On peut empiler les quantificateurs : $\forall x \in E,\ \exists y \in F,\ \forall z \in G,\ P(x, y, z)$.

- Une variable doit apparaître **dans la portée** (*scope*) de son quantificateur. Évite les propositions du type $P(x) \wedge (\exists x \in E,\ Q(x))$ : le premier $x$ n'est quantifié par rien.
- Une variable n'est quantifiée **qu'une seule fois** dans une proposition : n'écris pas $\forall x \in E,\ \exists x \in F, \ldots$
- L'**ordre** des quantificateurs compte énormément (chapitre 7) : « tout chien a sa queue » n'est pas « il existe une queue commune à tous les chiens ».

:::exercise[Exercice du cours 5 — Formaliser]
Exprimer formellement : « toute partie non vide de $\mathbb{N}$ admet un minimum ».
:::

:::hint[Indice]
Quel est le type des objets ? « Partie de $\mathbb{N}$ » : un élément $A$ de $\mathcal{P}(\mathbb{N})$. « Admet un minimum » : il existe un élément de $A$ inférieur ou égal à tous les éléments de $A$.
:::

:::correction
$$\forall A \in \mathcal{P}(\mathbb{N}),\quad A \neq \emptyset \;\Rightarrow\; \big(\exists m \in A,\ \forall a \in A,\ m \le a\big)$$

Points de vigilance :

- le minimum doit appartenir à $A$ : $\exists m \in A$, pas $\exists m \in \mathbb{N}$ (sinon on définit un **minorant**, et $0$ conviendrait toujours) ;
- l'ordre $\exists m,\ \forall a$ est essentiel : avec $\forall a,\ \exists m$, on pourrait prendre $m = a$, et l'énoncé deviendrait trivial ;
- l'hypothèse $A \neq \emptyset$ est indispensable : $\emptyset$ n'a pas de minimum.

Cette propriété est le **bon ordre** de $\mathbb{N}$ : elle servira à prouver le principe de récurrence (chapitre 8).
:::

::item{id="ch4-formaliser"}

## 7. Quantificateurs et connecteurs

Certaines combinaisons se distribuent, d'autres non (les preuves sont dans le TD 1, exercices 5 et 6) :

| Équivalence | Vraie ? |
|---|---|
| $\forall x,\ (P(x) \wedge Q(x)) \iff (\forall x,\ P(x)) \wedge (\forall x,\ Q(x))$ | toujours |
| $\exists x,\ (P(x) \vee Q(x)) \iff (\exists x,\ P(x)) \vee (\exists x,\ Q(x))$ | toujours |
| $\forall x,\ (P(x) \vee Q(x))$ vs $(\forall x,\ P(x)) \vee (\forall x,\ Q(x))$ | seul $\Leftarrow$ |
| $\exists x,\ (P(x) \wedge Q(x))$ vs $(\exists x,\ P(x)) \wedge (\exists x,\ Q(x))$ | seul $\Rightarrow$ |

::item{id="ch4-distributivite"}

## 8. Fiche récapitulative

:::key[L'essentiel du chapitre]
- **$\forall$ dans le but** : « Soit $x \in E$ » (quelconque). **$\forall$ en hypothèse** : l'appliquer à des valeurs bien choisies.
- **$\exists$ dans le but** : exhiber un témoin $x_0$ et le vérifier. **$\exists$ en hypothèse** : « Soit $x_0$ tel que… » (on ne choisit pas).
- **$\exists!$** = existence + unicité ($P(x_1) \wedge P(x_2) \Rightarrow x_1 = x_2$).
- $\forall x \in \emptyset$ : toujours vrai ; $\exists x \in \emptyset$ : toujours faux ; `all([])` = `True`, `any([])` = `False`.
- Une variable par quantificateur, utilisée dans sa portée ; l'ordre des quantificateurs compte.
- $\forall$ se distribue sur $\wedge$, $\exists$ sur $\vee$ — **pas** l'inverse.
:::
