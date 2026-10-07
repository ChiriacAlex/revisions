---
title: Ch3 — Théorie des ensembles
summary: Appartenance, union, intersection, inclusion, égalité par double inclusion, ensemble des parties, complémentaire, produit cartésien.
tags: [ensembles, double inclusion, parties]
minutes: 60
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- traduire chaque opération ensembliste en **formule logique** sur l'appartenance ;
- prouver une inclusion (« Soit $x \in A$… ») et une égalité d'ensembles (**double inclusion**) ;
- écrire **explicitement** des ensembles ($\mathcal{P}(\{a,b,c\})$, unions, intersections…) ;
- connaître les **égalités usuelles** (De Morgan, distributivité, $A \setminus B = A \cap B^\complement$…) ;
- réfuter une fausse égalité par un **contre-exemple** minimal ;
- repérer une écriture **mal typée** (additionner des ensembles, « $\Leftrightarrow$ » entre deux ensembles…).

:::intuition[Le fil conducteur]
Tout le chapitre repose sur une seule idée : **un ensemble, c'est un prédicat**. Dire « $x \in A \cup B$ », c'est dire « $x \in A$ **ou** $x \in B$ ». Chaque opération sur les ensembles correspond à un connecteur logique, et chaque preuve sur les ensembles devient une preuve de logique sur l'appartenance d'un élément $x$.
:::

## 2. Appartenance et ensemble vide

Formellement, à un ensemble $E$ est associé le prédicat « $\in E$ » : $x$ appartient à $E$ si et seulement si l'énoncé $x \in E$ est vrai. On note $x \notin E \iff \neg(x \in E)$.

:::definition[Ensemble vide]
L'**ensemble vide** $\emptyset$ est l'ensemble auquel aucun élément n'appartient : pour tout $x$, la proposition $x \in \emptyset$ est **fausse**.
:::

## 3. Union, intersection, inclusion

:::definition[Union et intersection]
Pour deux ensembles $A$ et $B$ :

- $x \in A \cup B \iff (x \in A) \vee (x \in B)$ ;
- $x \in A \cap B \iff (x \in A) \wedge (x \in B)$.
:::

:::example
$\mathbb{Z} = \mathbb{Z}_+ \cup \mathbb{Z}_-$ ; notez que $0$ appartient aux deux (le « ou » est inclusif). L'intersection de deux droites distinctes de $\mathbb{R}^2$ est soit $\emptyset$ (droites parallèles), soit un singleton (leur point d'intersection).
:::

<figure class="venn-row">
<svg viewBox="0 0 150 122" role="img" aria-label="Union de A et B"><rect x="2" y="2" width="146" height="96" rx="6" class="muted"/><g opacity="0.38"><circle cx="58" cy="50" r="32" class="accent-fill"/><circle cx="92" cy="50" r="32" class="accent-fill"/></g><circle cx="58" cy="50" r="32" class="accent"/><circle cx="92" cy="50" r="32" class="accent"/><text x="38" y="55">A</text><text x="104" y="55">B</text><text x="10" y="18" class="muted-text">E</text><text x="75" y="117" text-anchor="middle">A ∪ B</text></svg>
<svg viewBox="0 0 150 122" role="img" aria-label="Intersection de A et B"><defs><clipPath id="venn-clip-a1"><circle cx="58" cy="50" r="32"/></clipPath></defs><rect x="2" y="2" width="146" height="96" rx="6" class="muted"/><circle cx="92" cy="50" r="32" class="venn-fill" clip-path="url(#venn-clip-a1)"/><circle cx="58" cy="50" r="32" class="accent"/><circle cx="92" cy="50" r="32" class="accent"/><text x="38" y="55">A</text><text x="104" y="55">B</text><text x="10" y="18" class="muted-text">E</text><text x="75" y="117" text-anchor="middle">A ∩ B</text></svg>
<svg viewBox="0 0 150 122" role="img" aria-label="A privé de B"><rect x="2" y="2" width="146" height="96" rx="6" class="muted"/><circle cx="58" cy="50" r="32" class="venn-fill"/><circle cx="92" cy="50" r="32" class="bg-fill"/><circle cx="58" cy="50" r="32" class="accent"/><circle cx="92" cy="50" r="32" class="accent"/><text x="38" y="55">A</text><text x="104" y="55">B</text><text x="10" y="18" class="muted-text">E</text><text x="75" y="117" text-anchor="middle">A \ B</text></svg>
<svg viewBox="0 0 150 122" role="img" aria-label="Complémentaire de A dans E"><rect x="2" y="2" width="146" height="96" rx="6" class="venn-fill"/><rect x="2" y="2" width="146" height="96" rx="6" class="muted"/><circle cx="58" cy="50" r="32" class="bg-fill"/><circle cx="58" cy="50" r="32" class="accent"/><text x="52" y="55">A</text><text x="10" y="18" class="muted-text">E</text><text x="75" y="117" text-anchor="middle">complémentaire de A</text></svg>
</figure>

:::warning[Les diagrammes ne sont pas des preuves]
Un diagramme de Venn aide à **deviner** une égalité ou à **trouver un contre-exemple**, mais il ne prouve rien : une preuve raisonne sur un élément $x$ quelconque.
:::

:::definition[Inclusion]
$A \subseteq B$ (« $A$ est inclus dans $B$ », « $A$ est une partie de $B$ ») si et seulement si $\forall x,\ (x \in A) \Rightarrow (x \in B)$.
:::

Tu connais déjà $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{C}$. L'inclusion étant une implication, elle hérite du motif de l'implication :

:::pattern[Inclusion simple]
**But.** Montrer que $A \subseteq B$.

- Soit $x \in A$…
- … alors $x \in B$.
:::

:::exercise[Exercice du cours 1 — Expliciter des ensembles]
Soient $A = \{a, b, c\}$ et $B = \{a, d\}$. Expliciter $A \cup A$, $A \cap A$, $A \cup B$, $A \cap B$ et $A \cap B \cup \{e\}$.
:::

:::correction
- $A \cup A = \{a, b, c\} = A$ et $A \cap A = \{a, b, c\} = A$ (un ensemble uni ou intersecté avec lui-même ne change pas).
- $A \cup B = \{a, b, c, d\}$ ($a$ n'est écrit qu'une fois : pas de doublon).
- $A \cap B = \{a\}$.
- $A \cap B \cup \{e\}$ est **ambiguë** : il n'y a pas de priorité conventionnelle entre $\cap$ et $\cup$, il faut des parenthèses !
  - $(A \cap B) \cup \{e\} = \{a, e\}$ ;
  - $A \cap (B \cup \{e\}) = \{a, b, c\} \cap \{a, d, e\} = \{a\}$.

  Les deux lectures donnent des résultats **différents** : n'écris jamais une telle expression sans parenthèses.
:::

## 4. Égalité d'ensembles : la double inclusion

:::definition[Égalité]
$A = B$ si et seulement si $\forall x,\ (x \in A) \Leftrightarrow (x \in B)$ : les deux ensembles ont exactement les mêmes éléments.
:::

Puisque $(P \Leftrightarrow Q) \iff (P \Rightarrow Q) \wedge (Q \Rightarrow P)$, on obtient $(A = B) \iff (A \subseteq B) \wedge (B \subseteq A)$.

:::pattern[Double inclusion]
**But.** Montrer que $A = B$.

- **Sous-but 1.** Montrer que $A \subseteq B$ : soit $x \in A$… alors $x \in B$.
- **Sous-but 2.** Montrer que $B \subseteq A$ : soit $x \in B$… alors $x \in A$.
:::

:::example[Une double inclusion rédigée : distributivité]
Montrons que $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$.

- ($\subseteq$) Soit $x \in A \cap (B \cup C)$. Alors $x \in A$, et $x \in B$ ou $x \in C$. Si $x \in B$, alors $x \in A \cap B$ ; si $x \in C$, alors $x \in A \cap C$. Dans les deux cas, $x \in (A \cap B) \cup (A \cap C)$.
- ($\supseteq$) Soit $x \in (A \cap B) \cup (A \cap C)$. Si $x \in A \cap B$, alors $x \in A$ et $x \in B \subseteq B \cup C$ ; si $x \in A \cap C$, alors $x \in A$ et $x \in C \subseteq B \cup C$. Dans les deux cas, $x \in A \cap (B \cup C)$.

D'où l'égalité. $\square$
:::

## 5. L'ensemble des parties

:::definition[Ensemble des parties]
Pour un ensemble $E$, on note $\mathcal{P}(E)$ l'**ensemble des parties** (*power set*) de $E$ : $X \in \mathcal{P}(E) \iff X \subseteq E$.
:::

$\mathcal{P}(E)$ est un **ensemble d'ensembles**. Pour tout ensemble $E$, on a toujours $\emptyset \in \mathcal{P}(E)$ et $E \in \mathcal{P}(E)$.

:::warning[$\in$ ou $\subseteq$ ?]
Avec $E = \{1, 2\}$ : $1 \in E$, $\{1\} \subseteq E$, $\{1\} \in \mathcal{P}(E)$, mais $1 \notin \mathcal{P}(E)$ (les éléments de $\mathcal{P}(E)$ sont des **ensembles**). Avant d'écrire $\in$ ou $\subseteq$, demande-toi toujours quel est le **type** de chaque côté.
:::

:::exercise[Exercice du cours 2 — Les parties de $\{a, b, c\}$]
Expliciter $\mathcal{P}(\{a, b, c\})$.
:::

:::hint[Méthode]
Range les parties par taille : 0 élément, 1, 2, puis 3.
:::

:::correction
$$\mathcal{P}(\{a,b,c\}) = \big\{\emptyset,\ \{a\},\ \{b\},\ \{c\},\ \{a,b\},\ \{a,c\},\ \{b,c\},\ \{a,b,c\}\big\}$$

Il y a $8 = 2^3$ parties : pour construire une partie, on décide pour chacun des 3 éléments s'il est dedans ou non ($2 \times 2 \times 2$ choix). On le démontrera au chapitre 10 : $\mathrm{Card}(\mathcal{P}(E)) = 2^{\mathrm{Card}(E)}$.
:::

::item{id="ch3-parties"}

## 6. Différence et complémentaire

:::definition[Différence]
$x \in A \setminus B \iff (x \in A) \wedge (x \notin B)$.
:::

$B$ n'a pas besoin d'être inclus dans $A$ : $\{0, 1, 2, 3\} \setminus \{1, 3, 4\} = \{0, 2\}$.

:::definition[Complémentaire]
Soit un ensemble de référence $E$ (souvent implicite) et $A \subseteq E$. Le **complémentaire** de $A$ dans $E$ est $A^\complement = E \setminus A$.
:::

Le complémentaire **dépend de $E$** : pour $A = \{0\}$, $A^\complement = \mathbb{N}^*$ dans $\mathbb{N}$, mais $A^\complement = \mathbb{R}^*$ dans $\mathbb{R}$.

## 7. Ensembles et logique : le dictionnaire

| Ensembles | Logique (sur « $x \in \cdot$ ») |
|---|---|
| $A \cup B$ | $P \vee Q$ |
| $A \cap B$ | $P \wedge Q$ |
| $A \subseteq B$ | $P \Rightarrow Q$ |
| $A = B$ | $P \Leftrightarrow Q$ |
| $A^\complement$ | $\neg P$ |

Grâce à ce dictionnaire, chaque équivalence logique du chapitre 2 donne une égalité d'ensembles. Pour $A, B, C \in \mathcal{P}(E)$ :

$$
\begin{aligned}
(A^\complement)^\complement &= A & A \cup A^\complement &= E \\
A \setminus B &= A \cap B^\complement & \emptyset^\complement &= E \\
(A \cup B)^\complement &= A^\complement \cap B^\complement & (A \cap B)^\complement &= A^\complement \cup B^\complement \\
A \cap (B \cup C) &= (A \cap B) \cup (A \cap C) & A \cup (B \cap C) &= (A \cup B) \cap (A \cup C)
\end{aligned}
$$

$$A \subseteq B \iff A \cap B^\complement = \emptyset$$

:::example[De Morgan, prouvé par la logique]
Pour $x \in E$ : $x \in (A \cup B)^\complement \iff \neg(x \in A \vee x \in B) \iff (x \notin A) \wedge (x \notin B) \iff x \in A^\complement \cap B^\complement$. Chaque $\iff$ est une équivalence logique connue : on a prouvé les deux inclusions d'un coup. Cette rédaction « par chaîne d'équivalences » n'est valable que si **chaque** étape est réellement une équivalence.
:::

::item{id="ch3-egalites"}

## 8. Exercices du cours

:::exercise[Exercice du cours 3 — Vrai en général ?]
Les propriétés suivantes sont-elles vraies en général, pour $A, B, C \in \mathcal{P}(E)$ ? Sinon, les réfuter par un contre-exemple.

1. $A = B \iff A \cup C = B \cup C$
2. $A = B \iff A \cap B = A$
3. $A \cup B = C \iff A \cup C = B$
4. $A \subseteq B \cup C \iff (A \subseteq B) \vee (A \subseteq C)$
5. $A \subseteq B \cap C \iff (A \subseteq B) \wedge (A \subseteq C)$
6. $A = B \iff A \setminus C = B \setminus C$
7. $(A \subseteq C) \wedge (B \subseteq C) \implies A \subseteq B$
8. $A \cup B = C \iff A = C \setminus B$
9. $A \cup B + A \cap B = A + B \iff A \cup B = A + B - A \cup B$
10. $B \setminus A \iff B \cap A^\complement$
:::

:::hint[Méthode]
Pour un contre-exemple, prends des ensembles **minuscules** : $\emptyset$, $\{1\}$, $\{2\}$, $\{1, 2\}$. Essaie systématiquement les cas où un ensemble est vide ou où deux ensembles sont égaux. Et pour 9 et 10, regarde d'abord si l'écriture **a un sens**.
:::

:::correction
1. **Faux.** Le sens $\Rightarrow$ est vrai, mais pas $\Leftarrow$ : avec $A = \{1\}$, $B = \emptyset$, $C = \{1\}$, on a $A \cup C = B \cup C = \{1\}$ alors que $A \neq B$.
2. **Faux.** $A \cap B = A$ équivaut à $A \subseteq B$, pas à $A = B$ : avec $A = \emptyset$ et $B = \{1\}$, $A \cap B = \emptyset = A$ mais $A \neq B$.
3. **Faux.** Avec $A = \{1\}$, $B = \emptyset$, $C = \{1\}$ : $A \cup B = \{1\} = C$, mais $A \cup C = \{1\} \neq B$.
4. **Faux.** Le sens $\Leftarrow$ est vrai, pas $\Rightarrow$ : avec $A = \{1, 2\}$, $B = \{1\}$, $C = \{2\}$, $A \subseteq B \cup C$ mais $A \not\subseteq B$ et $A \not\subseteq C$. (Un « ou » ne se distribue pas sur l'inclusion.)
5. **Vrai.** ($\Rightarrow$) $B \cap C \subseteq B$ et $B \cap C \subseteq C$. ($\Leftarrow$) Soit $x \in A$ : $x \in B$ et $x \in C$, donc $x \in B \cap C$.
6. **Faux.** Le sens $\Rightarrow$ est vrai, pas $\Leftarrow$ : avec $A = \{1\}$, $B = \emptyset$, $C = \{1\}$, $A \setminus C = B \setminus C = \emptyset$ mais $A \neq B$.
7. **Faux.** Avec $A = \{1\}$, $B = \emptyset$, $C = \{1\}$ : $A$ et $B$ sont inclus dans $C$, mais $A \not\subseteq B$.
8. **Faux, dans les deux sens.** ($\Rightarrow$) avec $A = B = C = \{1\}$ : $A \cup B = C$ mais $C \setminus B = \emptyset \neq A$. ($\Leftarrow$) avec $B = \{2\}$, $C = \{1\}$, $A = C \setminus B = \{1\}$ : $A \cup B = \{1, 2\} \neq C$.
9. **Mal typé.** On ne peut pas **additionner** ni **soustraire** des ensembles : $+$ et $-$ portent sur des nombres. L'énoncé qui a un sens porte sur les cardinaux d'ensembles finis : $\mathrm{Card}(A \cup B) + \mathrm{Card}(A \cap B) = \mathrm{Card}(A) + \mathrm{Card}(B)$ (toujours vrai, voir ch. 11). Même ainsi, le membre de droite « $\mathrm{Card}(A \cup B) = \mathrm{Card}(A) + \mathrm{Card}(B) - \mathrm{Card}(A \cup B)$ » est faux en général (prendre $A = \{1\}$, $B = \emptyset$ : $1 \neq 1 + 0 - 1$) : l'équivalence est donc fausse.
10. **Mal typé.** $\Leftrightarrow$ relie deux **propositions**, or $B \setminus A$ et $B \cap A^\complement$ sont des **ensembles**. Ce qu'il fallait écrire : $B \setminus A = B \cap A^\complement$, qui est **vrai** ($x \in B \wedge x \notin A \iff x \in B \wedge x \in A^\complement$).
:::

::item{id="ch3-ex3"}

:::exercise[Exercice du cours 4 — Des égalités vraies en général ?]
Pour $A, B, C \in \mathcal{P}(E)$ :

1. $(A \setminus B) \cup B = A$
2. $(A \cup B) \setminus B = A$
3. $(A \cup B \cup B) \setminus B = A \cup B$
4. $(A \setminus B) \cup (A \cap B) = A$
5. $\emptyset \cup A = E \cap A$
6. $\emptyset \cap A = E \cup A$
7. $A + B - B = A$
8. $A \cup B \cup B = A + 2B$
9. $A \cup B = (A \cup B) \setminus (A \cap B)$
:::

:::correction
1. **Faux** : $(A \setminus B) \cup B = A \cup B$. Contre-exemple : $A = \emptyset$, $B = \{1\}$ donne $\{1\} \neq \emptyset$.
2. **Faux** : $(A \cup B) \setminus B = A \setminus B$. Contre-exemple : $A = B = \{1\}$ donne $\emptyset \neq \{1\}$.
3. **Faux** : $A \cup B \cup B = A \cup B$ et $(A \cup B) \setminus B = A \setminus B$. Contre-exemple : $A = \emptyset$, $B = \{1\}$ donne $\emptyset \neq \{1\}$.
4. **Vrai.** Soit $x \in A$ : soit $x \in B$ (alors $x \in A \cap B$), soit $x \notin B$ (alors $x \in A \setminus B$) — disjonction de cas. Réciproquement, les deux morceaux sont inclus dans $A$. (Les deux morceaux sont même disjoints : c'est une **partition** de $A$, voir ch. 11.)
5. **Vrai** : les deux valent $A$ (car $A \subseteq E$).
6. **Faux** : $\emptyset \cap A = \emptyset$ alors que $E \cup A = E$ ; c'est faux dès que $E \neq \emptyset$.
7. **Mal typé** : pas d'addition ni de soustraction d'ensembles.
8. **Mal typé** : « $2B$ » n'a pas de sens pour un ensemble. Au passage, $A \cup B \cup B = A \cup B$ (pas de doublon).
9. **Faux** en général : $(A \cup B) \setminus (A \cap B)$ est la **différence symétrique** (les éléments dans exactement un des deux). Contre-exemple : $A = B = \{1\}$ donne $\{1\} \neq \emptyset$. L'égalité est vraie si et seulement si $A \cap B = \emptyset$.
:::

::item{id="ch3-ex4"}

::item{id="ch3-types"}

## 9. Derniers outils : produit cartésien et compréhension

:::definition[Produit cartésien]
On considère des **couples** ordonnés $(x, y)$. Pour deux ensembles $U$ et $V$ :
$(x, y) \in U \times V \iff (x \in U) \wedge (y \in V)$.
:::

:::warning[Couple ≠ paire]
Le couple $(x, y)$ est **ordonné** : $(1, 2) \neq (2, 1)$. L'ensemble $\{x, y\}$ (parfois appelé « paire ») ne l'est pas : $\{1, 2\} = \{2, 1\}$. Et $(1, 1)$ est un couple valide, alors que $\{1, 1\} = \{1\}$.
:::

Exemple : $\mathbb{R}^2 = (\mathbb{R}_+ \times \mathbb{R}_+) \cup (\mathbb{R}_+ \times \mathbb{R}_-) \cup (\mathbb{R}_- \times \mathbb{R}_-) \cup (\mathbb{R}_- \times \mathbb{R}_+)$ (les quatre quadrants).

:::definition[Ensemble défini par compréhension]
Étant donnés un ensemble $E$ et une proposition $P(x)$, l'ensemble $S = \{x \in E \mid P(x)\}$ est la partie de $E$ telle que $x \in S \iff (x \in E) \wedge P(x)$.
:::

Exemple : pour $a, b \in \mathbb{R}$, $S = \{(x, y) \in \mathbb{R}^2 \mid y = ax + b\}$ est une droite du plan. On sélectionne **toujours** dans un ensemble déjà connu ($E$) : c'est ce qui évite le paradoxe du catalogue.

## 10. Exercices supplémentaires

:::exercise[Entraînement 1 — Inclusion et intersection]
Montrer que $A \subseteq B \iff A \cap B = A$.
:::

:::correction
- ($\Rightarrow$) Supposons $A \subseteq B$ et montrons $A \cap B = A$ par double inclusion. $A \cap B \subseteq A$ est immédiat. Soit $x \in A$ : comme $A \subseteq B$, $x \in B$, donc $x \in A \cap B$.
- ($\Leftarrow$) Supposons $A \cap B = A$. Soit $x \in A$ : alors $x \in A \cap B$, donc $x \in B$. Ainsi $A \subseteq B$. $\square$
:::

:::exercise[Entraînement 2 — Inclusion et complémentaires]
Soient $A, B \in \mathcal{P}(E)$. Montrer que $A \subseteq B \iff B^\complement \subseteq A^\complement$.
:::

:::correction
- ($\Rightarrow$) Supposons $A \subseteq B$. Soit $x \in B^\complement$, c'est-à-dire $x \in E$ et $x \notin B$. Si on avait $x \in A$, on aurait $x \in B$ : contradiction. Donc $x \notin A$, soit $x \in A^\complement$.
- ($\Leftarrow$) Appliquer le sens direct à $B^\complement$ et $A^\complement$ : $(A^\complement)^\complement \subseteq (B^\complement)^\complement$, c'est-à-dire $A \subseteq B$. $\square$

C'est la version « ensembles » de la contraposée.
:::

:::exercise[Entraînement 3 — Différence et intersection]
Montrer que $A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C)$.
:::

:::correction
Pour $x$ quelconque : $x \in A \setminus (B \cap C) \iff x \in A \wedge \neg(x \in B \wedge x \in C) \iff x \in A \wedge (x \notin B \vee x \notin C)$ (De Morgan) $\iff (x \in A \wedge x \notin B) \vee (x \in A \wedge x \notin C)$ (distributivité) $\iff x \in (A \setminus B) \cup (A \setminus C)$. $\square$
:::

## 11. Fiche récapitulative

:::key[L'essentiel du chapitre]
- $x \in A \cup B \iff x \in A \vee x \in B$ ; $\ x \in A \cap B \iff x \in A \wedge x \in B$ ; $\ x \in A \setminus B \iff x \in A \wedge x \notin B$.
- $A \subseteq B$ : « soit $x \in A$… alors $x \in B$ ».
- $A = B$ : **double inclusion**.
- $X \in \mathcal{P}(E) \iff X \subseteq E$ ; $\emptyset$ et $E$ sont toujours des parties de $E$ ; $\mathrm{Card}(\mathcal{P}(E)) = 2^{\mathrm{Card}(E)}$.
- De Morgan : $(A \cup B)^\complement = A^\complement \cap B^\complement$, $(A \cap B)^\complement = A^\complement \cup B^\complement$.
- $A \subseteq B \iff A \cap B^\complement = \emptyset \iff B^\complement \subseteq A^\complement$.
- **Types** : pas de $+$, $-$, $2B$ sur des ensembles ; $\Leftrightarrow$ entre propositions, $=$ entre ensembles ; $\in$ vs $\subseteq$.
- $(x, y) \neq (y, x)$ mais $\{x, y\} = \{y, x\}$.
:::
