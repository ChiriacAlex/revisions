---
title: Ch6 — Fonctions
summary: Définition formelle d'une fonction, domaine et image, composition, injections, surjections, bijections et réciproques.
tags: [fonctions, injection, surjection, bijection]
minutes: 65
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- définir une fonction comme une **relation** où chaque élément du départ a **exactement une** image ;
- distinguer **ensemble d'arrivée** et **image** ;
- prouver qu'une relation est (ou n'est pas) une fonction ;
- prouver qu'une fonction est **injective**, **surjective**, **bijective** — ou le réfuter ;
- utiliser la **réciproque** pour prouver une bijection ;
- relier tout cela aux questions 2 à 7 du projet Python.

:::intuition[La réponse du mathématicien]
Une fonction prend une entrée dans un ensemble $E$ et renvoie **une seule** valeur dans un ensemble $F$ (éventuellement différent). C'est la réponse de l'ingénieur du chapitre 1, avec des **ensembles** à la place des **types**.
:::

## 2. Définition formelle

:::definition[Fonction]
Étant donnés deux ensembles $E$ et $F$, une **fonction** (ou application) $f : E \to F$ est une relation binaire $f \subseteq E \times F$ telle que
$$\forall x \in E,\ \exists! y \in F,\ (x, y) \in f.$$
On note alors $y = f(x)$ : $x$ est **un antécédent** de $y$, et $y$ est **l'image** de $x$.
:::

:::example
$\{(x, y) \in \mathbb{R}^2 \mid x = y^2\}$ n'est **pas** une fonction de $\mathbb{R}$ dans $\mathbb{R}$ : $x = 1$ a deux images ($1$ et $-1$), et $x = -1$ n'en a aucune. Les deux conditions (existence **et** unicité) échouent.
:::

:::pattern[Fonction]
**But.** Montrer que la relation $f$ est une fonction $E \to F$.

- **Sous-but 1 (existence de l'image).** Soit $x \in E$… alors $\exists y \in F,\ (x, y) \in f$.
- **Sous-but 2 (unicité de l'image).** Soient $(x, y), (x, z) \in f$… alors $y = z$.
:::

C'est exactement la structure des questions 2 (« fonction partielle » = unicité seule) et 3 (« fonction » = unicité + existence) du projet.

## 3. Domaine, image, antécédents

:::definition[Domaine]
Pour $f : E \to F$, $E$ est le **domaine** $\mathrm{Dom}(f)$. L'ensemble de **toutes** les fonctions de $E$ dans $F$ se note $F^E$.
:::

Exemple : $\mathrm{Dom}(\log) = \mathbb{R}_+^*$ et $\log \in \mathbb{R}^{\mathbb{R}_+^*}$.

:::definition[Image]
L'**image** de $f : E \to F$ est la partie $\mathrm{Im}(f) = \{y \in F \mid \exists x \in E,\ (x, y) \in f\}$ de $F$.
:::

:::warning[Ensemble d'arrivée ≠ image]
Écrire $f : E \to F$ ne signifie **pas** que $F = \mathrm{Im}(f)$. Pour $\exp : \mathbb{R} \to \mathbb{R}$, $\mathrm{Im}(\exp) = \mathbb{R}_+^* \neq \mathbb{R}$. Un élément $y$ de $F$ peut avoir **zéro, un ou plusieurs** antécédents : pour $f(x) = x^2$ sur $\mathbb{R}$, $0$ a un antécédent, $1$ en a deux, $-1$ n'en a aucun.
:::

### Composition

:::theorem[Composition]
Pour $f : E \to F$ et $g : F \to G$, il existe une unique fonction $g \circ f : x \in E \mapsto g(f(x)) \in G$.
:::

Attention à l'ordre : $g \circ f$ applique **d'abord** $f$, **puis** $g$. Et les types doivent s'enchaîner : l'arrivée de $f$ doit être le départ de $g$.

:::exercise[Exercice du cours 1 — Est-ce une fonction ?]
Les relations suivantes sont-elles des fonctions ?

$$
\begin{aligned}
F_1 &= \{(x, y) \in \mathbb{R}_+ \times \mathbb{R} \mid x = \cos(y)\} \\
F_2 &= \{(x, y) \in \mathbb{R}^2 \mid x^2 + y^2 = 3\} \\
F_3 &= \{(x, y) \in \mathbb{R}^2 \mid y = x^2\} \\
F_4 &= \{(E, F) \in \mathcal{P}(\mathbb{N})^2 \mid E \subseteq F\} \\
F_5 &= \{(E, F) \in \mathcal{P}(\mathbb{N})^2 \mid F = E^\complement\} \\
F_6 &= \{((E_1, E_2), F) \in \mathcal{P}(\mathbb{N})^2 \times \mathcal{P}(\mathbb{N}) \mid F = E_1 \cap E_2\} \\
F_7 &= \{(x, y) \in \mathbb{Q} \times \mathbb{Z} \mid \exists z \in \mathbb{Z}^*,\ x = \tfrac{y}{z}\} \\
F_8 &= \{(n, m) \in \mathbb{N} \times \mathbb{N} \mid m \text{ divise } n\}
\end{aligned}
$$
:::

:::hint[Méthode]
Pour chaque relation, identifie le **départ** (premier ensemble du produit) et l'**arrivée**. Puis, pour un élément $x$ du départ, compte ses images : aucune ? une ? plusieurs ? Un seul $x$ qui échoue suffit à réfuter.
:::

:::correction
1. **$F_1$ : non.** Pour $x = 2$, aucun $y$ ne vérifie $\cos(y) = 2$ (existence). Pour $x = 1$, $y = 0$ et $y = 2\pi$ conviennent (unicité). En restreignant à $[0, 1] \times [0, \pi]$, on obtient la fonction $\arccos$.
2. **$F_2$ : non.** C'est un cercle : $x = 0$ a deux images ($\pm\sqrt{3}$), et $x = 2$ n'en a aucune.
3. **$F_3$ : oui.** C'est la fonction $x \in \mathbb{R} \mapsto x^2 \in \mathbb{R}$ : chaque $x$ a exactement une image.
4. **$F_4$ : non.** $\emptyset$ est inclus dans **toutes** les parties de $\mathbb{N}$ : il a une infinité d'images ($\emptyset$, $\{0\}$, $\mathbb{N}$…).
5. **$F_5$ : oui.** Le complémentaire d'une partie de $\mathbb{N}$ existe et est unique. (C'est même une bijection, voir l'exercice 4.)
6. **$F_6$ : oui.** Pour tout couple $(E_1, E_2)$, l'intersection $E_1 \cap E_2$ existe et est unique. Remarque : le départ est un **produit** $\mathcal{P}(\mathbb{N})^2$ — une fonction de deux variables est une fonction d'une variable « couple ».
7. **$F_7$ : non.** Pour $x = \frac{1}{2}$ : $y = 1$ convient ($z = 2$) et $y = 2$ aussi ($z = 4$). L'unicité échoue.
8. **$F_8$ : non.** $n = 6$ a quatre « images » ($1, 2, 3, 6$) ; pire, tout entier divise $0$, donc $n = 0$ en a une infinité.
:::

::item{id="ch6-fonction-ou-pas"}

:::exercise[Exercice du cours 2 — Toujours des fonctions ?]
Soit $f : E \to F$ une fonction. Les relations suivantes sont-elles toujours des fonctions ?

$$
\begin{aligned}
g_1 &= \{(y, x) \in F \times E \mid f(x) = y\} \\
g_2 &= \{(y, X) \in F \times \mathcal{P}(E) \mid \forall x \in E,\ x \in X \Leftrightarrow f(x) = y\} \\
h_1 &= \{(X, Y) \in \mathcal{P}(E) \times \mathcal{P}(F) \mid \forall x \in E,\ x \in X \Rightarrow f(x) \in Y\} \\
h_2 &= \{(X, Y) \in \mathcal{P}(E) \times \mathcal{P}(F) \mid Y = \{f(x) \mid x \in X\}\}
\end{aligned}
$$
:::

:::hint[Indice]
Commence par les **types** : $g_1$ va de $F$ vers $E$, $g_2$ de $F$ vers $\mathcal{P}(E)$, $h_1$ et $h_2$ de $\mathcal{P}(E)$ vers $\mathcal{P}(F)$. Pour $g_2$, la condition « $x \in X \Leftrightarrow f(x) = y$ » détermine-t-elle $X$ complètement ?
:::

:::correction
- **$g_1$ : pas toujours.** C'est la relation « réciproque ». Un $y$ peut n'avoir aucun antécédent (existence) ou en avoir plusieurs (unicité). Exemple : $f : x \in \mathbb{R} \mapsto x^2$ ; $y = -1$ n'a pas d'image par $g_1$, $y = 1$ en a deux. $g_1$ est une fonction **si et seulement si** $f$ est bijective.
- **$g_2$ : toujours.** Pour $y \in F$, la condition « $\forall x \in E,\ x \in X \Leftrightarrow f(x) = y$ » impose exactement $X = \{x \in E \mid f(x) = y\}$ : cet ensemble existe (existence) et deux parties qui ont les mêmes éléments sont égales (unicité). C'est l'**image réciproque** $f^{-1}(\{y\})$, éventuellement vide. Passer de « un élément » à « l'**ensemble** des éléments » a rendu la relation fonctionnelle.
- **$h_1$ : pas toujours.** $X$ est en relation avec **toute** partie $Y$ qui contient les images des éléments de $X$. Si $F \neq \emptyset$, $X = \emptyset$ est en relation avec $Y = \emptyset$ et avec $Y = F$ : deux images.
- **$h_2$ : toujours.** C'est l'**image directe** $f(X) = \{f(x) \mid x \in X\}$, qui existe et est unique pour toute partie $X$.
:::

## 4. Injections

:::definition[Injectivité]
$f : E \to F$ est **injective** (*one-to-one*) si $\forall x, y \in \mathrm{Dom}(f),\ f(x) = f(y) \Rightarrow x = y$.
:::

Autrement dit : deux éléments **distincts** ont toujours des images **distinctes** (contraposée) ; tout élément de $F$ a **au plus un** antécédent.

Exemple : $f : x \in \mathbb{R} \mapsto x^2$ n'est **pas** injective, car $f(1) = f(-1) = 1$.

:::pattern[Injectivité]
**But.** Montrer que $f : E \to F$ est injective.

- Considérons $x, y \in \mathrm{Dom}(f)$ quelconques.
- Supposons que $f(x) = f(y)$…
- … alors $x = y$.
:::

C'est une preuve d'**unicité** : la même structure que pour $\exists!$. Pour **réfuter** l'injectivité, il suffit d'exhiber $x \neq y$ avec $f(x) = f(y)$.

## 5. Surjections

:::definition[Surjectivité]
$f : E \to F$ est **surjective** (*onto*) si $\forall y \in F,\ \exists x \in E,\ y = f(x)$, c'est-à-dire si $\mathrm{Im}(f) = F$.
:::

Tout élément de $F$ a **au moins un** antécédent. Exemple : $x \in \mathbb{R} \mapsto x^2 \in \mathbb{R}$ n'est pas surjective, car $-1$ n'a pas d'antécédent.

:::pattern[Surjectivité]
**But.** Montrer que $f : E \to F$ est surjective.

- Considérons un $y \in F$ quelconque…
- … puis exhibons $x \in E$ tel que $y = f(x)$.
:::

C'est une preuve d'**existence** (on cherche $x$ au brouillon en « résolvant » $f(x) = y$, puis on le présente et on vérifie).

<figure class="venn-row">
<svg viewBox="0 0 170 130" role="img" aria-label="Injective non surjective"><defs><marker id="fn-arr" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L8,4 L0,8 z" class="accent-fill"/></marker></defs><ellipse cx="40" cy="58" rx="30" ry="48" class="muted"/><ellipse cx="130" cy="58" rx="30" ry="48" class="muted"/><circle cx="40" cy="35" r="3.5" class="accent-fill"/><circle cx="40" cy="80" r="3.5" class="accent-fill"/><circle cx="130" cy="25" r="3.5" class="accent-fill"/><circle cx="130" cy="58" r="3.5" class="accent-fill"/><circle cx="130" cy="91" r="3.5" class="ko-fill"/><circle cx="130" cy="91" r="3.5" class="ko"/><line x1="44" y1="34" x2="124" y2="26" class="accent" marker-end="url(#fn-arr)"/><line x1="44" y1="79" x2="124" y2="60" class="accent" marker-end="url(#fn-arr)"/><text x="85" y="124" text-anchor="middle">injective, pas surjective</text></svg>
<svg viewBox="0 0 170 130" role="img" aria-label="Surjective non injective"><ellipse cx="40" cy="58" rx="30" ry="48" class="muted"/><ellipse cx="130" cy="58" rx="30" ry="48" class="muted"/><circle cx="40" cy="25" r="3.5" class="accent-fill"/><circle cx="40" cy="58" r="3.5" class="accent-fill"/><circle cx="40" cy="91" r="3.5" class="accent-fill"/><circle cx="130" cy="35" r="3.5" class="accent-fill"/><circle cx="130" cy="80" r="3.5" class="accent-fill"/><line x1="44" y1="25" x2="124" y2="34" class="accent" marker-end="url(#fn-arr)"/><line x1="44" y1="58" x2="124" y2="37" class="ko" marker-end="url(#fn-arr)"/><line x1="44" y1="90" x2="124" y2="81" class="accent" marker-end="url(#fn-arr)"/><text x="85" y="124" text-anchor="middle">surjective, pas injective</text></svg>
<svg viewBox="0 0 170 130" role="img" aria-label="Bijective"><ellipse cx="40" cy="58" rx="30" ry="48" class="muted"/><ellipse cx="130" cy="58" rx="30" ry="48" class="muted"/><circle cx="40" cy="25" r="3.5" class="accent-fill"/><circle cx="40" cy="58" r="3.5" class="accent-fill"/><circle cx="40" cy="91" r="3.5" class="accent-fill"/><circle cx="130" cy="25" r="3.5" class="accent-fill"/><circle cx="130" cy="58" r="3.5" class="accent-fill"/><circle cx="130" cy="91" r="3.5" class="accent-fill"/><line x1="44" y1="25" x2="124" y2="57" class="ok" marker-end="url(#fn-arr)"/><line x1="44" y1="58" x2="124" y2="90" class="ok" marker-end="url(#fn-arr)"/><line x1="44" y1="90" x2="124" y2="27" class="ok" marker-end="url(#fn-arr)"/><text x="85" y="124" text-anchor="middle">bijective</text></svg>
</figure>

:::key[Résumé visuel]
- **Injective** : deux points **distincts** de $E$ ne pointent jamais vers le **même** point de $F$ (au plus une flèche arrive en chaque point).
- **Surjective** : **tout** point de $F$ reçoit au moins une flèche ($\exists x$ pour chaque $\forall y$).
- **Bijective** : exactement une flèche arrive en chaque point de $F$.
:::

:::exercise[Exercice du cours 3 — Fonctions affines]
Soit $(a, b) \in \mathbb{R}^* \times \mathbb{R}$. Montrer que $f : \mathbb{R} \to \mathbb{R}$, $f(x) = ax + b$, est injective et surjective.
:::

:::correction
- **Injectivité.** Soient $x, y \in \mathbb{R}$ tels que $f(x) = f(y)$ : $ax + b = ay + b$, donc $a(x - y) = 0$. Comme $a \neq 0$, $x = y$.
- **Surjectivité.** Soit $y \in \mathbb{R}$. Posons $x = \frac{y - b}{a}$ (possible car $a \neq 0$). Alors $f(x) = a \cdot \frac{y - b}{a} + b = y$.

$f$ est donc injective et surjective. $\square$ (Si $a = 0$, $f$ est constante : ni injective, ni surjective.)
:::

## 6. Bijections et réciproques

:::definition[Bijectivité]
$f : E \to F$ est **bijective** si elle est injective et surjective. Les ensembles $E$ et $F$ sont alors dits **équipotents**.
:::

Exemple : $\exp : \mathbb{R} \to \mathbb{R}_+^*$ est une bijection (mais pas $\exp : \mathbb{R} \to \mathbb{R}$).

:::pattern[Bijectivité]
**But.** Montrer que $f : E \to F$ est une bijection.

- **Sous-but 1.** Montrer que $f$ est injective (motif de l'injectivité).
- **Sous-but 2.** Montrer que $f$ est surjective (motif de la surjectivité).
:::

:::theorem[Inversibilité des bijections]
$f : E \to F$ est une bijection si et seulement s'il existe une fonction $f^{-1} : F \to E$ telle que $f \circ f^{-1} = \mathrm{Id}_F$ et $f^{-1} \circ f = \mathrm{Id}_E$. On dit que $f$ est **inversible** ; la **réciproque** $f^{-1}$ est unique, et c'est aussi une bijection.
:::

Intuitivement, $f^{-1}$ **défait** ce que $f$ a fait, à condition que ce soit réversible.

:::pattern[Bijectivité par la réciproque]
**But.** Montrer que $f : E \to F$ est une bijection.

- Introduisons une candidate $g \subseteq F \times E$ pour la réciproque, et prouvons d'abord que $g$ est bien une **fonction** $F \to E$. Puis :
- **Sous-but 1.** Montrer que $f \circ g = \mathrm{Id}_F$ : soit $y \in F$… alors $f(g(y)) = y$.
- **Sous-but 2.** Montrer que $g \circ f = \mathrm{Id}_E$ : soit $x \in E$… alors $g(f(x)) = x$.
:::

:::warning[Les deux compositions sont nécessaires]
$f \circ g = \mathrm{Id}_F$ seul ne suffit pas. Avec $f : \mathbb{N} \to \mathbb{N}$, $f(n) = \lfloor n/2 \rfloor$ et $g(n) = 2n$ : $f(g(n)) = n$ pour tout $n$, mais $g(f(1)) = 0 \neq 1$. Ici $f$ est surjective mais pas injective.
:::

:::exercise[Exercice du cours 4 — Le complémentaire est une bijection]
Soit $E$ un ensemble. Montrer que $f : \mathcal{P}(E) \to \mathcal{P}(E)$, $f(X) = X^\complement$, est une bijection.
:::

:::hint[Indice]
Quelle est la réciproque candidate ? Que vaut $(X^\complement)^\complement$ ?
:::

:::correction
D'abord, $f$ est bien une fonction de $\mathcal{P}(E)$ dans $\mathcal{P}(E)$ : pour $X \subseteq E$, $X^\complement = E \setminus X$ existe, est unique et est une partie de $E$.

Prenons comme candidate $g = f$ elle-même. Pour tout $X \in \mathcal{P}(E)$ : $f(g(X)) = (X^\complement)^\complement = X$ et $g(f(X)) = (X^\complement)^\complement = X$. Donc $f \circ f = \mathrm{Id}_{\mathcal{P}(E)}$ : $f$ est inversible, de réciproque elle-même, donc bijective. $\square$

(Une fonction égale à sa propre réciproque s'appelle une **involution**.)
:::

::item{id="ch6-inj-surj"}

## 7. Exercices supplémentaires

:::exercise[Entraînement 1 — Composition et injectivité]
Soient $f : E \to F$ et $g : F \to G$. Montrer que si $g \circ f$ est injective, alors $f$ est injective.
:::

:::correction
Supposons $g \circ f$ injective. Soient $x, y \in E$ tels que $f(x) = f(y)$. En appliquant $g$ : $g(f(x)) = g(f(y))$, c'est-à-dire $(g \circ f)(x) = (g \circ f)(y)$. Par injectivité de $g \circ f$, $x = y$. Donc $f$ est injective. $\square$

(En revanche $g$ n'est pas forcément injective : $E = \{0\}$, $F = \{0, 1\}$, $G = \{0\}$, $f(0) = 0$, $g$ constante.)
:::

:::exercise[Entraînement 2 — Composition et surjectivité]
Soient $f : E \to F$ et $g : F \to G$. Montrer que si $g \circ f$ est surjective, alors $g$ est surjective.
:::

:::correction
Supposons $g \circ f$ surjective. Soit $z \in G$. Il existe $x \in E$ tel que $g(f(x)) = z$. Posons $y = f(x) \in F$ : alors $g(y) = z$. Donc $g$ est surjective. $\square$
:::

:::exercise[Entraînement 3 — Composée de bijections]
Montrer que la composée de deux bijections $f : E \to F$ et $g : F \to G$ est une bijection, de réciproque $f^{-1} \circ g^{-1}$.
:::

:::correction
Posons $h = f^{-1} \circ g^{-1} : G \to E$. Alors $(g \circ f) \circ h = g \circ (f \circ f^{-1}) \circ g^{-1} = g \circ g^{-1} = \mathrm{Id}_G$ et $h \circ (g \circ f) = f^{-1} \circ (g^{-1} \circ g) \circ f = f^{-1} \circ f = \mathrm{Id}_E$. Par le théorème d'inversibilité, $g \circ f$ est bijective et $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ (attention à l'ordre : on défait d'abord la dernière opération). $\square$
:::

## 8. Côté projet Python (questions 4 à 7)

Dans le projet, une fonction est donnée par une **fonction Python** `g` et deux ensembles finis `es`, `fs` :

- **injection** : on peut tester $f(x) = f(y) \Rightarrow x = y$ pour tous les couples, ou remarquer qu'il n'y a **aucune collision** si et seulement si l'ensemble des images a autant d'éléments que `es` ;
- **surjection** : tout `y` de `fs` doit appartenir à l'ensemble des images `{g(x) for x in es}` ;
- **bijection** : les deux ;
- **réciproque** : si `g` est bijective, on mémorise pour chaque image son unique antécédent (un dictionnaire), et `h` renvoie l'antécédent stocké.

Le labo de la partie « Projet » te permet de tester tes fonctions avec les tests officiels.

## 9. Fiche récapitulative

| Notion | Définition | Pour prouver | Pour réfuter |
|---|---|---|---|
| fonction | $\forall x,\ \exists! y,\ (x,y) \in f$ | existence + unicité de l'image | un $x$ sans image, ou avec deux images |
| injective | $f(x) = f(y) \Rightarrow x = y$ | supposer $f(x) = f(y)$, déduire $x = y$ | $x \neq y$ avec $f(x) = f(y)$ |
| surjective | $\forall y,\ \exists x,\ f(x) = y$ | soit $y$, exhiber $x$ | un $y$ sans antécédent |
| bijective | injective et surjective | les deux, **ou** une réciproque $g$ avec $f \circ g = \mathrm{Id}$ et $g \circ f = \mathrm{Id}$ | réfuter l'une des deux |

:::key[À retenir]
- Arrivée ≠ image ; $\mathrm{Im}(f) = F$ exactement quand $f$ est surjective.
- $g \circ f$ : d'abord $f$, puis $g$ ; $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.
- $g \circ f$ injective ⇒ $f$ injective ; $g \circ f$ surjective ⇒ $g$ surjective.
- Une relation « un élément ↦ l'ensemble des éléments tels que… » est toujours une fonction (image directe, image réciproque).
:::
