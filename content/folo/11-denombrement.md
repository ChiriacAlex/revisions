---
title: Ch11 — Dénombrement appliqué
summary: Union disjointe, inclusion et complémentaire, partitions, produit cartésien, combinaisons, et les exercices classiques (kebab, mots binaires, chemins).
tags: [dénombrement, partition, combinaisons, cardinal]
minutes: 65
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- utiliser le cardinal d'une **union disjointe**, d'un **complémentaire**, d'un **produit cartésien** ;
- définir une **partition** et s'en servir pour compter ;
- connaître $\mathrm{Card}(\mathcal{P}_k(E)) = \binom{n}{k}$ ;
- résoudre les exercices types : menus, mots binaires, chemins dans une grille ;
- **justifier** un dénombrement (et pas seulement donner un nombre).

:::intuition[Le fil conducteur]
On ne compte presque jamais « à la main ». On **découpe** l'ensemble en morceaux disjoints (partition), on le voit comme un **produit** de choix indépendants, on passe au **complémentaire** quand c'est plus simple, ou on le **code** par un ensemble connu (bijection, chapitre 10).
:::

## 2. Union disjointe, inclusion, complémentaire

:::theorem[Cardinal d'une union disjointe]
Si $E$ et $F$ sont finis, $\mathrm{Card}(E) = n$, $\mathrm{Card}(F) = m$ et $E \cap F = \emptyset$, alors $\mathrm{Card}(E \cup F) = n + m$.
:::

:::intuition[Fusionner deux groupes d'étudiants]
Le groupe A a $n$ étudiants numérotés de $1$ à $n$, le groupe B en a $m$ numérotés de $1$ à $m$, et personne n'est dans les deux. Pour fusionner, on garde les numéros de A et on **décale** ceux de B de $n$ : l'étudiant $j$ de B devient $n + j$. Chacun reçoit un numéro unique entre $1$ et $n + m$ : c'est une bijection $E \cup F \to \{1, \ldots, n + m\}$. (Si un étudiant était dans les deux groupes, il recevrait deux numéros : c'est pour cela qu'il faut $E \cap F = \emptyset$.)
:::

:::theorem[Inclusion et complémentaire]
Si $E \subseteq F$ sont finis, $\mathrm{Card}(E) = n$ et $\mathrm{Card}(F) = m$, alors $n \le m$ et $\mathrm{Card}(F \setminus E) = m - n$.
:::

:::exercise[Exercice du cours 1 — Prouver ces deux propriétés]
Démontrer le théorème « inclusion et complémentaire » à partir du cardinal d'une union disjointe.
:::

:::correction
Comme $E \subseteq F$, on a $F = E \cup (F \setminus E)$ (double inclusion : un élément de $F$ est dans $E$ ou n'y est pas ; et $E \subseteq F$, $F \setminus E \subseteq F$), et cette union est **disjointe** : un élément de $E$ n'est pas dans $F \setminus E$.

$F \setminus E \subseteq F$ est fini. Par le cardinal d'une union disjointe : $m = n + \mathrm{Card}(F \setminus E)$.

Donc $\mathrm{Card}(F \setminus E) = m - n$, et comme un cardinal est positif, $m - n \ge 0$, soit $n \le m$. $\square$
:::

## 3. Partitions

<figure>
<svg viewBox="0 0 220 170" role="img" aria-label="Partition d'un ensemble en quatre parties"><rect x="10" y="10" width="200" height="150" rx="6" class="ko" stroke-width="2"/><path d="M80,10 C78,40 70,55 90,62" class="accent" stroke-width="2"/><path d="M90,62 C110,45 140,55 130,80 C125,100 100,110 85,100 C70,92 75,70 90,62" class="accent" stroke-width="2"/><path d="M10,110 C40,105 60,110 85,100" class="accent" stroke-width="2"/><path d="M120,100 C140,120 150,140 145,160" class="accent" stroke-width="2"/><text x="108" y="84" text-anchor="middle">P₀</text><text x="165" y="70" text-anchor="middle">P₁</text><text x="95" y="140" text-anchor="middle">P₂</text><text x="40" y="65" text-anchor="middle">P₃</text><text x="195" y="28" text-anchor="middle" class="muted-text">E</text></svg>
<figcaption>$\mathcal{P} = \{P_0, P_1, P_2, P_3\}$ découpe $E$ en morceaux non vides, disjoints, qui recouvrent tout.</figcaption>
</figure>

:::definition[Partition]
Un ensemble d'ensembles $\mathcal{P}$ (éventuellement infini) est une **partition** de $E$ si :

- **parties non vides** : $\forall X \in \mathcal{P},\ X \subseteq E$ et $X \neq \emptyset$ ;
- **disjonction** : $\forall X, Y \in \mathcal{P},\ X \neq Y \Rightarrow X \cap Y = \emptyset$ ;
- **recouvrement** : $\forall x \in E,\ \exists X \in \mathcal{P},\ x \in X$.
:::

Les deux dernières propriétés donnent : $\forall x \in E,\ \exists! X \in \mathcal{P},\ x \in X$ — chaque élément est dans **exactement un** morceau. (Exemple déjà vu : les classes d'une relation d'équivalence, chapitre 5.)

:::pattern[Partition]
**But.** Montrer que $\mathcal{P}$ est une partition de $E$.

- **Sous-but 1.** Soit $X \in \mathcal{P}$ : montrer $X \subseteq E$ et $X \neq \emptyset$.
- **Sous-but 2.** Montrer $\forall X, Y \in \mathcal{P},\ X \neq Y \Rightarrow X \cap Y = \emptyset$ — par contraposée : supposer qu'il existe $x \in X \cap Y$, et prouver $X = Y$.
- **Sous-but 3.** Soit $x \in E$ : exhiber $P \in \mathcal{P}$ tel que $x \in P$.
:::

:::theorem[Cardinal et partition]
Si $\{P_1, \ldots, P_n\}$ est une partition d'un ensemble fini $E$, alors $\mathrm{Card}(E) = \mathrm{Card}(P_1) + \cdots + \mathrm{Card}(P_n)$.
:::

(Récurrence simple sur $n$ à partir du cardinal d'une union disjointe.)

:::exercise[Exercice du cours 2 — Cardinal d'un rectangle]
Justifier intuitivement que $\mathrm{Card}(\{1, \ldots, n\} \times \{1, \ldots, m\}) = n \cdot m$, à l'aide d'une partition bien choisie.
:::

:::correction
Pour $i \in \{1, \ldots, n\}$, posons $L_i = \{i\} \times \{1, \ldots, m\}$ (la « ligne » $i$). Les $L_i$ forment une partition de $\{1, \ldots, n\} \times \{1, \ldots, m\}$ : chaque $L_i$ est non vide ; deux lignes différentes ne partagent aucun couple (la première composante diffère) ; et tout couple $(i, j)$ est dans $L_i$.

Chaque $L_i$ est en bijection avec $\{1, \ldots, m\}$ via $j \mapsto (i, j)$, donc $\mathrm{Card}(L_i) = m$. Par le cardinal d'une partition : $\mathrm{Card} = \underbrace{m + \cdots + m}_{n \text{ fois}} = n \cdot m$. $\square$
:::

## 4. Produit cartésien

:::theorem[Cardinal d'un produit cartésien]
Si $\mathrm{Card}(E) = n$ et $\mathrm{Card}(F) = m$, alors $\mathrm{Card}(E \times F) = n \cdot m$. Plus généralement (par récurrence), pour $n \ge 2$ ensembles finis : $\mathrm{Card}(E_1 \times \cdots \times E_n) = \mathrm{Card}(E_1) \times \cdots \times \mathrm{Card}(E_n)$.
:::

En particulier $\mathrm{Card}(\{0, 1\}^n) = 2^n$, ce qui termine la preuve de $\mathrm{Card}(\mathcal{P}(E)) = 2^n$.

:::exercise[Exercice du cours 3 — Chez O'Zaman]
O'Zaman, le kebab préféré d'EPITA, propose 2 pains (pita, wrap), 3 viandes (poulet, bœuf, agneau) et 4 sauces (algérienne, ketchup, yaourt, mayonnaise).

1. Combien de sandwichs **complets** (pain, viande et sauce) ?
2. Combien de sandwichs **partiels**, auxquels il manque la sauce ou la viande ?
3. Combien de sandwichs complets **sans poulet ou sans ketchup** ?
:::

:::hint[Indice pour 2]
« Pas de viande » est une option de plus pour la viande ; « pas de sauce », une option de plus pour la sauce. Compte tous les sandwichs avec ces options, puis retire les complets.
:::

:::hint[Indice pour 3]
« Sans poulet **ou** sans ketchup » est la négation de « avec poulet **et** avec ketchup » : passe au complémentaire.
:::

:::correction
1. Un sandwich complet est un triplet (pain, viande, sauce) : $\mathrm{Card}(\text{Pains} \times \text{Viandes} \times \text{Sauces}) = 2 \times 3 \times 4 = \mathbf{24}$.
2. En ajoutant l'option « rien » : viande parmi $3 + 1$ choix, sauce parmi $4 + 1$, pain toujours présent : $2 \times 4 \times 5 = 40$ sandwichs. Les partiels sont ceux qui ne sont pas complets : $40 - 24 = \mathbf{16}$. Vérification par partition : sans sauce mais avec viande $2 \times 3 = 6$ ; sans viande mais avec sauce $2 \times 4 = 8$ ; ni l'un ni l'autre $2$ ; total $6 + 8 + 2 = 16$. *(Si l'on comprend « sans sauce **ni** viande », la réponse est $2$ : précise toujours ta lecture d'un énoncé ambigu.)*
3. Complémentaire : les complets **avec poulet et avec ketchup** sont $2 \times 1 \times 1 = 2$ (le choix du pain). Donc $24 - 2 = \mathbf{22}$. Vérification par inclusion-exclusion : sans poulet $2 \times 2 \times 4 = 16$, sans ketchup $2 \times 3 \times 3 = 18$, ni poulet ni ketchup $2 \times 2 \times 3 = 12$ : $16 + 18 - 12 = 22$.
:::

::item{id="ch11-kebab"}

## 5. Combinaisons : compter les parties de taille $k$

:::definition[Combinaisons]
Pour $E$ de cardinal $n$ et $k \in \mathbb{N}$, on note $\mathcal{P}_k(E)$ l'ensemble des parties de $E$ à $k$ éléments (les **$k$-combinaisons**).
:::

:::theorem[Nombre de combinaisons]
$\mathrm{Card}(\mathcal{P}_k(E)) = \dfrac{n!}{k!\,(n-k)!}$ si $k \le n$, et $0$ sinon. Ce nombre ne dépend que de $n$ et $k$ ; on le note $\binom{n}{k}$ (ou $C_n^k$). *(admis)*
:::

Valeurs utiles : $\binom{n}{0} = \binom{n}{n} = 1$, $\binom{n}{1} = n$, $\binom{n}{k} = \binom{n}{n-k}$ (choisir les $k$ éléments pris revient à choisir les $n - k$ laissés), $\binom{4}{2} = 6$, $\binom{5}{2} = 10$, $\binom{10}{5} = 252$.

:::exercise[Exercice du cours 4 — Mots binaires]
On considère l'alphabet $\Sigma = \{0, 1\}$.

1. Combien y a-t-il de mots binaires de longueur 4 ?
2. Combien de mots de longueur 4 contiennent exactement $i$ bits à 1, pour $i \in \{0, \ldots, 4\}$ ?
3. Quel est le nombre total de 1 dans tous les mots de longueur 4 ?
:::

:::correction
1. Un mot de longueur 4 est un élément de $\{0, 1\}^4$ : $2^4 = 16$ mots.
2. Un mot est déterminé par l'ensemble des **positions** de ses 1, une partie de $\{1, 2, 3, 4\}$ à $i$ éléments (bijection) : il y en a $\binom{4}{i}$, soit $1, 4, 6, 4, 1$ pour $i = 0, 1, 2, 3, 4$. (Total : $16$, cohérent avec 1 — c'est une partition des mots selon leur nombre de 1.)
3. En sommant sur cette partition : $0 \cdot 1 + 1 \cdot 4 + 2 \cdot 6 + 3 \cdot 4 + 4 \cdot 1 = 32$. Autre méthode : chacune des 4 positions vaut 1 dans exactement la moitié des 16 mots, soit $4 \times 8 = 32$.
:::

::item{id="ch11-mots"}

:::exercise[Exercice du cours 5 — Chemins dans une grille]
Combien y a-t-il de chemins allant du coin en bas à gauche au coin en haut à droite d'une grille de $5 \times 5$ cases, sans jamais descendre ni aller à gauche ? *(D'après* Professeur Layton et le destin perdu*.)*
:::

:::hint[Indice 1]
Code un chemin par la suite de ses pas : D (droite) ou H (haut). Combien de pas en tout ? Combien de D ?
:::

:::hint[Indice 2]
Un tel mot est déterminé par les **positions** de ses D.
:::

:::correction
**Codage.** Pour traverser 5 cases vers la droite et 5 vers le haut, tout chemin fait exactement 5 pas D et 5 pas H, soit 10 pas. Un chemin ↔ un mot de longueur 10 sur $\{D, H\}$ contenant 5 D : c'est une bijection (un chemin se lit comme un mot, un mot se dessine comme un chemin, et le chemin ne sort pas de la grille puisqu'il ne fait que 5 pas de chaque sorte).

**Second codage.** Un tel mot ↔ l'ensemble des positions des D, une partie à 5 éléments de $\{1, \ldots, 10\}$.

**Comptage.** Il y a donc $\binom{10}{5} = \frac{10!}{5!\,5!} = 252$ chemins.

*(Si « $5 \times 5$ » désigne 5 points par côté, soit 4 cases, on trouve $\binom{8}{4} = 70$ : précise ta convention. En général, pour $n \times m$ cases : $\binom{n+m}{n}$.)*
:::

::item{id="ch11-chemins"}

:::exercise[Exercice du cours 6 — La somme des combinaisons]
Montrer que $\forall n \in \mathbb{N},\ 2^n = \sum_{k=0}^{n} \binom{n}{k}$, en considérant une partition de $\mathcal{P}(E)$ pour un ensemble $E$ de cardinal $n$.
:::

:::correction
Soit $E$ de cardinal $n$. Les ensembles $\mathcal{P}_0(E), \mathcal{P}_1(E), \ldots, \mathcal{P}_n(E)$ forment une partition de $\mathcal{P}(E)$ :

- chacun est non vide (il existe une partie à $k$ éléments pour $0 \le k \le n$) et inclus dans $\mathcal{P}(E)$ ;
- ils sont disjoints : une partie n'a qu'un seul cardinal ;
- ils recouvrent $\mathcal{P}(E)$ : toute partie $X$ de $E$ a un cardinal $k \in \{0, \ldots, n\}$, donc $X \in \mathcal{P}_k(E)$.

Par le cardinal d'une partition : $\mathrm{Card}(\mathcal{P}(E)) = \sum_{k=0}^n \mathrm{Card}(\mathcal{P}_k(E))$, c'est-à-dire $2^n = \sum_{k=0}^n \binom{n}{k}$. $\square$ (On a compté le même ensemble de deux façons : c'est la technique du **double comptage**.)
:::

## 6. Exercices supplémentaires

:::exercise[Entraînement 1 — Inclusion-exclusion]
Soient $A$, $B$ finis. Montrer que $\mathrm{Card}(A \cup B) = \mathrm{Card}(A) + \mathrm{Card}(B) - \mathrm{Card}(A \cap B)$.
:::

:::correction
$A \cup B$ est l'union disjointe de $A$ et $B \setminus A$, donc $\mathrm{Card}(A \cup B) = \mathrm{Card}(A) + \mathrm{Card}(B \setminus A)$. Et $B$ est l'union disjointe de $B \setminus A$ et $A \cap B$, donc $\mathrm{Card}(B \setminus A) = \mathrm{Card}(B) - \mathrm{Card}(A \cap B)$. On combine. $\square$
:::

:::exercise[Entraînement 2 — Délégués]
Une promo de 30 étudiants élit un délégué et un suppléant (deux personnes distinctes, rôles différents), puis, séparément, un comité de 3 étudiants (sans rôles). Combien de choix pour chacun ?
:::

:::correction
- Délégué puis suppléant : un couple $(d, s)$ avec $d \neq s$ : $30 \times 29 = 870$ (l'ordre compte : les rôles sont différents).
- Comité : une partie à 3 éléments : $\binom{30}{3} = \frac{30 \cdot 29 \cdot 28}{6} = 4060$ (l'ordre ne compte pas).

Retiens la question à se poser : **l'ordre compte-t-il ?** Couples/uplets si oui, parties si non.
:::

::item{id="ch11-ordre"}

## 7. Fiche récapitulative

| Outil | Formule | Quand l'utiliser |
|---|---|---|
| union disjointe / partition | $\mathrm{Card}(E) = \sum \mathrm{Card}(P_i)$ | découper selon des **cas** exclusifs |
| complémentaire | $\mathrm{Card}(F \setminus E) = \mathrm{Card}(F) - \mathrm{Card}(E)$ | « au moins un », « ou » → compter le contraire |
| produit cartésien | $\mathrm{Card}(E \times F) = \mathrm{Card}(E)\,\mathrm{Card}(F)$ | choix **indépendants** successifs |
| parties | $\mathrm{Card}(\mathcal{P}(E)) = 2^n$ | « dedans / dehors » pour chaque élément |
| combinaisons | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | choisir $k$ éléments, **sans ordre** |
| bijection | même cardinal | coder par un objet plus simple (mots, positions) |

:::key[À retenir]
- Toujours **justifier** : partition, bijection, produit — pas seulement « $= 24$ ».
- « Ou » → complémentaire ou inclusion-exclusion.
- L'ordre compte → uplets ; l'ordre ne compte pas → parties.
- Chemins dans une grille de $n \times m$ cases : $\binom{n+m}{n}$.
:::
