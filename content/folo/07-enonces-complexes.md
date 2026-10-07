---
title: Ch7 — Lire et écrire des énoncés complexes
summary: Formaliser (limite d'une suite), dépendance et ordre des quantificateurs, négation, et un problème d'examen sur une fonction d'ordre supérieur, corrigé pas à pas.
tags: [formalisation, négation, quantificateurs, annale]
minutes: 60
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- **formaliser** une propriété en nommant chaque objet et son type (exemple : la limite d'une suite) ;
- comprendre qu'une variable introduite par $\exists$ **dépend** de toutes celles quantifiées avant elle ;
- savoir quand on peut **permuter** des quantificateurs (et quand c'est interdit) ;
- **nier** mécaniquement une formule à plusieurs quantificateurs ;
- **décortiquer** un énoncé d'examen avec une fonction qui prend des ensembles en entrée, et en écrire la preuve.

:::key[La règle du chapitre]
Une proposition n'a de sens que si l'on connaît le **type** de chacune de ses variables et les **relations** entre elles. Avant de prouver quoi que ce soit : « qui est qui, et de quel type ? »
:::

## 2. Formaliser : la limite d'une suite

Soit $(U_n)_{n \ge 0} \in \mathbb{R}^\mathbb{N}$ une suite réelle. Comment formaliser « $(U_n)$ a une limite finie » ?

Intuitivement : il existe un réel dont la suite est **aussi proche qu'on veut**, **à partir d'un certain rang**. On nomme chaque objet et son ensemble :

- $\ell \in \mathbb{R}$ : la limite (unique) ;
- $\varepsilon > 0$ : la précision voulue, aussi petite qu'on veut ;
- $n_0 \in \mathbb{N}$ : le rang à partir duquel la précision est atteinte.

<figure>
<svg viewBox="0 0 360 200" role="img" aria-label="Suite qui converge vers l"><line x1="30" y1="185" x2="350" y2="185" class="stroke" stroke-width="1.5"/><line x1="30" y1="185" x2="30" y2="10" class="stroke" stroke-width="1.5"/><line x1="30" y1="100" x2="350" y2="100" class="accent" stroke-width="1.5"/><line x1="30" y1="85" x2="350" y2="85" class="ok" stroke-dasharray="5 4"/><line x1="30" y1="115" x2="350" y2="115" class="ok" stroke-dasharray="5 4"/><line x1="170" y1="20" x2="170" y2="185" class="muted" stroke-dasharray="3 3"/><text x="16" y="104" text-anchor="middle">ℓ</text><text x="342" y="80" class="muted-text">ℓ+ε</text><text x="342" y="130" class="muted-text">ℓ−ε</text><text x="170" y="198" text-anchor="middle">n₀</text><text x="345" y="198" text-anchor="end">n</text><text x="40" y="20">Uₙ</text><g class="accent-fill"><circle cx="50" cy="40" r="3"/><circle cx="70" cy="150" r="3"/><circle cx="90" cy="60" r="3"/><circle cx="110" cy="135" r="3"/><circle cx="130" cy="70" r="3"/><circle cx="150" cy="165" r="3"/><circle cx="185" cy="109" r="3"/><circle cx="205" cy="93" r="3"/><circle cx="225" cy="105" r="3"/><circle cx="245" cy="96" r="3"/><circle cx="265" cy="103" r="3"/><circle cx="285" cy="98" r="3"/><circle cx="305" cy="101" r="3"/><circle cx="325" cy="100" r="3"/></g></svg>
<figcaption>À partir du rang $n_0$, tous les termes restent dans la bande $]\ell - \varepsilon, \ell + \varepsilon[$. Plus $\varepsilon$ est petit, plus $n_0$ doit (en général) être grand.</figcaption>
</figure>

On obtient :

$$\exists \ell \in \mathbb{R},\ \forall \varepsilon > 0,\ \exists n_0 \in \mathbb{N},\ \forall n \ge n_0,\ |U_n - \ell| < \varepsilon$$

- $\ell$ ne dépend que de la suite ;
- $\varepsilon$ est **quelconque** (c'est l'« adversaire » qui le choisit) ;
- $n_0$ dépend de la suite, de $\ell$ **et** de $\varepsilon$ : plus on veut être proche, plus il faut aller loin.

:::key[Dépendance des quantificateurs]
Une variable introduite par $\exists$ **dépend de toutes les variables quantifiées avant elle**. On peut l'écrire $n_0(\varepsilon)$ pour s'en souvenir.
:::

## 3. Permuter des quantificateurs

On peut échanger deux quantificateurs **adjacents de même type** (si le domaine de l'un ne dépend pas de l'autre) :

$$\forall x \in E,\ \forall y \in F,\ P(x, y) \iff \forall y \in F,\ \forall x \in E,\ P(x, y)$$
$$\exists x \in E,\ \exists y \in F,\ P(x, y) \iff \exists y \in F,\ \exists x \in E,\ P(x, y)$$

Mais **jamais deux quantificateurs de types différents** :

$$\forall x \in E,\ \exists y \in F,\ P(x, y) \quad \not\Longleftrightarrow \quad \exists y \in F,\ \forall x \in E,\ P(x, y)$$

:::example
« Tout chien a sa queue » ($\forall$ chien, $\exists$ queue) n'est pas « il existe une queue commune à tous les chiens » ($\exists$ queue, $\forall$ chien). Le sens $\exists\forall \Rightarrow \forall\exists$ est toujours vrai (une queue commune est en particulier la queue de chacun), l'autre est faux en général.
:::

::item{id="ch7-ordre"}

## 4. Nier une formule quantifiée

:::theorem[Négation des quantificateurs]
$$\neg(\forall x \in E,\ P(x)) \iff \exists x \in E,\ \neg P(x) \qquad \neg(\exists x \in E,\ P(x)) \iff \forall x \in E,\ \neg P(x)$$
:::

- La négation d'un « pour tout » est **un contre-exemple** ;
- la négation d'un « il existe » est un « pour tout… ne… pas ».

On propage la négation **un quantificateur à la fois**, de gauche à droite, en changeant chaque $\forall$ en $\exists$ et inversement, **sans toucher aux domaines** ($\forall x \in E$ devient $\exists x \in E$, pas $\exists x \notin E$) :

$$\neg(\forall x \in E,\ \exists y \in F,\ P(x, y)) \iff \exists x \in E,\ \neg(\exists y \in F,\ P(x, y)) \iff \exists x \in E,\ \forall y \in F,\ \neg P(x, y)$$

Puis on nie la proposition finale avec les règles du chapitre 2 : $\neg(A \Rightarrow B) \iff A \wedge \neg B$, De Morgan, $\neg(a < b) \iff a \ge b$…

:::exercise[Exercice du cours 1 — Ne pas avoir de limite finie]
Écrire la négation de « $(U_n)_{n \ge 0}$ a une limite finie ».
:::

:::correction
On nie $\exists \ell \in \mathbb{R},\ \forall \varepsilon > 0,\ \exists n_0 \in \mathbb{N},\ \forall n \ge n_0,\ |U_n - \ell| < \varepsilon$ quantificateur par quantificateur :

$$\forall \ell \in \mathbb{R},\ \exists \varepsilon > 0,\ \forall n_0 \in \mathbb{N},\ \exists n \ge n_0,\ |U_n - \ell| \ge \varepsilon$$

En français : quel que soit le candidat $\ell$, on peut trouver une précision $\varepsilon$ telle que, aussi loin qu'on aille, il y a toujours un terme à distance au moins $\varepsilon$ de $\ell$. Remarque : « $\varepsilon > 0$ » et « $n \ge n_0$ » sont des **domaines** : ils ne changent pas, seule la dernière inégalité est niée.
:::

::item{id="ch7-negations"}

::item{id="ch7-limite"}

## 5. Problème d'examen : une fonction d'ordre supérieur

:::exam[Annale 2022 (examen final)]
Soient $E$ et $F$ deux ensembles et $f : E \to F$ une fonction. On définit
$$g : X \in \mathcal{P}(E) \mapsto \{y \in F \mid \exists x \in X,\ y = f(x)\} \in \mathcal{P}(F).$$
Montrer que $f$ est injective si et seulement si $\forall A, B \in \mathcal{P}(E),\ (A \cap B = \emptyset) \Rightarrow (g(A) \cap g(B) = \emptyset)$.
:::

### 5.1 Comprendre les objets (le typage)

| Objet | Type | Lecture |
|---|---|---|
| $x$, $a$, $b$ | élément de $E$ | un point de départ |
| $f(x)$ | élément de $F$ | une image |
| $A$, $B$, $X$ | élément de $\mathcal{P}(E)$, c.-à-d. **partie** de $E$ | un paquet de points de départ |
| $g$ | fonction $\mathcal{P}(E) \to \mathcal{P}(F)$ | prend un **ensemble**, rend un **ensemble** |
| $g(A)$ | partie de $F$ | l'ensemble des images des éléments de $A$ (l'« image directe » $f(A)$) |

$g$ est une fonction **d'ordre supérieur** : elle est construite à partir de $f$ et manipule des ensembles. Concrètement, $y \in g(A) \iff \exists a \in A,\ y = f(a)$.

### 5.2 L'erreur de lecture classique

:::warning[Mal lire la portée du $\forall$]
- **Faux :** « $(\forall A, B,\ A \cap B = \emptyset) \Rightarrow \ldots$ » : on lirait « si **toutes** les parties sont disjointes… », ce qui n'arrive jamais. Le $\forall$ porte sur **toute** l'implication : pour **chaque** couple $(A, B)$ de parties disjointes, leurs images sont disjointes.
- **Faux :** confondre $g(A)$ (un ensemble d'images) avec $f(A)$ appliqué « élément par élément » sans le dire, ou écrire $f(A)$ comme si $A$ était un élément de $E$.
- **Faux :** prouver la réciproque « $g(A) \cap g(B) = \emptyset \Rightarrow A \cap B = \emptyset$ » — qui est d'ailleurs vraie pour **toute** fonction $f$ (si $x \in A \cap B$, alors $f(x) \in g(A) \cap g(B)$), et ne dit donc rien sur l'injectivité.
:::

**La bonne lecture :** « $f$ est injective si et seulement si $g$ envoie deux parties disjointes sur deux parties disjointes ».

### 5.3 Le squelette

:::exercise[Exercice du cours 2 — Écrire le squelette de la preuve]
Avant toute chose, écris le squelette complet : motifs, hypothèses, sous-buts.
:::

:::correction[Voir le squelette]
**But.** $f$ injective $\iff$ (H), où (H) est « $\forall A, B \in \mathcal{P}(E),\ A \cap B = \emptyset \Rightarrow g(A) \cap g(B) = \emptyset$ ». Double implication.

**(⇒) De gauche à droite — Sous-but 1.**
- Supposons $f$ injective.
- Soient $A, B \in \mathcal{P}(E)$ tels que $A \cap B = \emptyset$. *(motif $\forall$ + implication)*
- Montrons que $g(A) \cap g(B) = \emptyset$. *(motif « ensemble vide » : par l'absurde, supposer qu'il contient un $y$)*

**(⇐) De droite à gauche — Sous-but 2.**
- Supposons (H).
- Soient $x, y \in E$ tels que $f(x) = f(y)$. Montrons que $x = y$. *(motif injectivité)*
- Par l'absurde, supposons $x \neq y$ : on va appliquer (H) à des parties **bien choisies** (motif « $\forall$ en hypothèse ») : $A = \{x\}$ et $B = \{y\}$.
- **Sous-but 3 (lemme).** Pour tout $x \in E$, $g(\{x\}) = \{f(x)\}$ — propriété de la fonction d'ordre supérieur $g$.
:::

### 5.4 Les preuves

:::exercise[Exercice du cours 3 — Terminer le sous-but 1]
Montrer que si $f$ est injective, alors pour toutes parties $A, B$ de $E$ disjointes, $g(A) \cap g(B) = \emptyset$.
:::

:::hint[Indice]
Suppose qu'un $z$ appartient à $g(A) \cap g(B)$ et **déroule la définition** de $g$ deux fois : tu obtiens deux antécédents.
:::

:::correction
Supposons $f$ injective. Soient $A, B \in \mathcal{P}(E)$ tels que $A \cap B = \emptyset$. Montrons par l'absurde que $g(A) \cap g(B) = \emptyset$.

Supposons qu'il existe $z \in g(A) \cap g(B)$.

- Comme $z \in g(A)$, il existe $a \in A$ tel que $z = f(a)$.
- Comme $z \in g(B)$, il existe $b \in B$ tel que $z = f(b)$.
- Donc $f(a) = f(b)$, et par injectivité de $f$, $a = b$.
- Alors $a \in A$ et $a = b \in B$, donc $a \in A \cap B = \emptyset$ : contradiction.

Ainsi $g(A) \cap g(B) = \emptyset$. $\square$
:::

:::exercise[Exercice du cours 4 — Le sous-but 3 : propriétés de $g$]
Montrer que pour tout $x \in E$, $g(\{x\}) = \{f(x)\}$. Puis montrer, plus généralement, que $g(\emptyset) = \emptyset$, que $A \subseteq B \Rightarrow g(A) \subseteq g(B)$ et que $g(A \cup B) = g(A) \cup g(B)$.
:::

:::correction
**$g(\{x\}) = \{f(x)\}$, par double inclusion.**
- ($\subseteq$) Soit $z \in g(\{x\})$ : il existe $a \in \{x\}$ tel que $z = f(a)$. Or $a \in \{x\}$ signifie $a = x$, donc $z = f(x)$, c'est-à-dire $z \in \{f(x)\}$.
- ($\supseteq$) Soit $z \in \{f(x)\}$, donc $z = f(x)$ avec $x \in \{x\}$ : par définition de $g$, $z \in g(\{x\})$.

**$g(\emptyset) = \emptyset$** : $z \in g(\emptyset)$ exigerait un $a \in \emptyset$, impossible.

**Croissance** : si $A \subseteq B$ et $z \in g(A)$, il existe $a \in A \subseteq B$ avec $z = f(a)$, donc $z \in g(B)$.

**Union** : $z \in g(A \cup B) \iff \exists a \in A \cup B,\ z = f(a) \iff (\exists a \in A,\ z = f(a)) \vee (\exists a \in B,\ z = f(a)) \iff z \in g(A) \cup g(B)$ (le $\exists$ se distribue sur le $\vee$). $\square$

Remarque : pour l'intersection, on a seulement $g(A \cap B) \subseteq g(A) \cap g(B)$ en général — l'égalité pour toutes parties $A, B$ équivaut justement à l'injectivité de $f$, c'est le cousin de notre problème.
:::

:::correction[Voir la fin de la preuve : sous-but 2 (⇐)]
Supposons (H). Soient $x, y \in E$ tels que $f(x) = f(y)$ ; montrons $x = y$ par l'absurde. Supposons $x \neq y$. Posons $A = \{x\}$ et $B = \{y\}$ : ce sont des parties de $E$, et $A \cap B = \emptyset$ car $x \neq y$. D'après (H), $g(A) \cap g(B) = \emptyset$. Or, par le sous-but 3, $g(A) = \{f(x)\}$ et $g(B) = \{f(y)\} = \{f(x)\}$, donc $g(A) \cap g(B) = \{f(x)\} \neq \emptyset$ : contradiction. Donc $x = y$ et $f$ est injective.

Les deux sens étant établis, $f$ est injective si et seulement si (H). $\square$
:::

:::method[Ce qu'il faut écrire à l'examen]
1. Annoncer la **double implication**.
2. Pour chaque sens, annoncer les hypothèses (« Supposons… ») et le but (« Montrons que… »), avec le motif utilisé (« par l'absurde », « soient $A, B$… »).
3. **Dérouler les définitions** ($z \in g(A)$ ⟶ « il existe $a \in A$ tel que $z = f(a)$ »).
4. Isoler les **lemmes** (ici $g(\{x\}) = \{f(x)\}$) et les prouver à part.
5. Conclure chaque sous-but explicitement, puis l'équivalence.
:::

## 6. Exercices supplémentaires

:::exercise[Entraînement 1 — Formaliser puis nier]
Soit $f : \mathbb{R} \to \mathbb{R}$. Formaliser puis nier : (a) « $f$ est majorée » ; (b) « $f$ est croissante » ; (c) « $f$ n'est pas injective » ; (d) « $f$ est surjective ».
:::

:::correction
| Énoncé | Formule | Négation |
|---|---|---|
| (a) majorée | $\exists M \in \mathbb{R},\ \forall x \in \mathbb{R},\ f(x) \le M$ | $\forall M \in \mathbb{R},\ \exists x \in \mathbb{R},\ f(x) > M$ |
| (b) croissante | $\forall x, y \in \mathbb{R},\ x \le y \Rightarrow f(x) \le f(y)$ | $\exists x, y \in \mathbb{R},\ x \le y \wedge f(x) > f(y)$ |
| (c) non injective | $\exists x, y \in \mathbb{R},\ f(x) = f(y) \wedge x \neq y$ | $\forall x, y \in \mathbb{R},\ f(x) = f(y) \Rightarrow x = y$ (injective) |
| (d) surjective | $\forall y \in \mathbb{R},\ \exists x \in \mathbb{R},\ f(x) = y$ | $\exists y \in \mathbb{R},\ \forall x \in \mathbb{R},\ f(x) \neq y$ |

Attention en (b) : la négation de « croissante » n'est **pas** « décroissante ».
:::

:::exercise[Entraînement 2 — Ordre des quantificateurs]
Comparer (A) $\forall \varepsilon > 0,\ \exists \delta > 0,\ \forall x, y \in [0, 1],\ |x - y| < \delta \Rightarrow |f(x) - f(y)| < \varepsilon$ et (B) $\exists \delta > 0,\ \forall \varepsilon > 0,\ \forall x, y \in [0, 1],\ |x - y| < \delta \Rightarrow |f(x) - f(y)| < \varepsilon$.
:::

:::correction
Dans (A), $\delta$ dépend de $\varepsilon$ : c'est la **continuité uniforme** (les fonctions continues sur $[0, 1]$ la vérifient). Dans (B), un même $\delta$ marche pour **tous** les $\varepsilon$ : si $|x - y| < \delta$, alors $|f(x) - f(y)|$ est plus petit que tout $\varepsilon > 0$, donc nul. (B) dit que $f$ est constante sur tout intervalle de longueur $< \delta$, donc constante sur $[0, 1]$ (en avançant par petits pas). (B) $\Rightarrow$ (A), mais pas l'inverse ($f(x) = x$ vérifie (A), pas (B)).
:::

## 7. Fiche récapitulative

:::key[L'essentiel]
- Formaliser = **nommer** chaque objet avec son **ensemble**, puis enchaîner les quantificateurs dans le bon **ordre**.
- Une variable sous $\exists$ dépend de toutes celles d'avant.
- On permute $\forall\forall$ ou $\exists\exists$, **jamais** $\forall\exists$ ; seul $\exists y\, \forall x \Rightarrow \forall x\, \exists y$ est toujours vrai.
- Négation : $\forall \leftrightarrow \exists$, domaines inchangés, puis on nie le cœur ($\neg(A \Rightarrow B) \iff A \wedge \neg B$).
- Face à une fonction d'ordre supérieur : **tableau des types**, déroulement des définitions ($z \in g(A) \iff \exists a \in A,\ z = f(a)$), lemmes isolés.
:::
