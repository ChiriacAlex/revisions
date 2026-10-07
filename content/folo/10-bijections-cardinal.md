---
title: Ch10 — Bijections et cardinal
summary: Codages et bijections, ensembles finis et cardinal, équipotence, composition de bijections et cardinal de l'ensemble des parties.
tags: [bijections, cardinal, codage, dénombrement]
minutes: 50
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- voir une bijection comme un **changement de codage** sans perte d'information ;
- définir un ensemble **fini** et son **cardinal** ;
- prouver que deux ensembles sont **équipotents** en construisant une bijection ;
- utiliser la **composition** de bijections ;
- démontrer que $\mathrm{Card}(\mathcal{P}(E)) = 2^{\mathrm{Card}(E)}$.

:::intuition[Le fil conducteur]
Deux ensembles **équipotents** sont deux façons d'écrire les mêmes objets, comme $57$ en décimal et $111001$ en binaire. Pour **compter** un ensemble compliqué, on cherche un **codage** (une bijection) vers un ensemble facile à compter.
:::

## 2. Les codages sont des bijections

Le nombre cinquante-sept s'écrit de plusieurs façons :

| Codage | Écriture | Lecture |
|---|---|---|
| décimal | $57$ | $5 \cdot 10^1 + 7 \cdot 10^0$ |
| binaire | $111001$ | $1 \cdot 2^5 + 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0$ |
| ternaire | $2010$ | $2 \cdot 3^3 + 0 \cdot 3^2 + 1 \cdot 3^1 + 0 \cdot 3^0$ |

Passer de l'écriture décimale à l'écriture binaire, c'est une **fonction** :

- **Domaine** : les suites finies non vides de chiffres de $\{0, \ldots, 9\}$ qui ne commencent pas par $0$ (sauf « $0$ » lui-même).
- **Image** : les suites finies non vides de booléens qui ne commencent pas par $0$ (sauf « $0$ »).
- **Injective** : deux écritures décimales différentes donnent deux écritures binaires différentes.
- **Surjective** : toute écriture binaire provient d'une écriture décimale.

C'est donc une **bijection**, et sa **réciproque** (binaire → décimal) existe naturellement : l'inversibilité des bijections traduit simplement le fait que deux codages équivalents représentent les mêmes objets.

:::warning[Le domaine compte]
Sans la condition « ne commence pas par 0 », « 057 » et « 57 » donneraient la même écriture binaire : l'injectivité serait perdue. C'est pour cela qu'on fixe une forme **canonique**.
:::

:::exercise[Exercice du cours 1 — Coder des ensembles d'entiers]
Comment coder concrètement (en machine) des ensembles d'entiers, c'est-à-dire des éléments de $\mathcal{P}(\mathbb{N})$ ? Discuter les inconvénients des différentes implémentations.
:::

:::correction
Plusieurs codages, chacun avec ses limites :

1. **Liste triée sans doublon** des éléments (ex. `[2, 3, 7]`). Canonique (une seule écriture par ensemble), donc l'égalité se teste en comparant les listes. Mais ne code que les ensembles **finis** ; l'appartenance coûte une recherche (dichotomie en $O(\log n)$).
2. **Liste quelconque** (non triée, avec doublons). Facile à construire, mais **pas injective** : `[3, 2]` et `[2, 3, 3]` codent le même ensemble, donc l'égalité est coûteuse à tester.
3. **Vecteur de bits** (fonction caractéristique : bit $i$ à 1 ssi $i$ appartient à l'ensemble). Union et intersection très rapides (ET/OU bit à bit) ; mais la taille dépend du **plus grand élément**, pas du nombre d'éléments ($\{10^9\}$ coûte un milliard de bits), et seuls les ensembles **bornés** sont codables.
4. **Prédicat** (une fonction `int -> bool`, ex. « est pair »). Code aussi des ensembles **infinis** ; mais on ne peut ni énumérer ni tester l'égalité de deux ensembles en général.
5. **Table de hachage** (`set` en Python). Appartenance en $O(1)$ en moyenne, mais l'ordre est perdu et seuls les ensembles finis sont représentables.

Aucun codage par des données **finies** ne peut représenter **toutes** les parties de $\mathbb{N}$ : il y a « plus » de parties de $\mathbb{N}$ que de chaînes de caractères finies (théorème de Cantor : $\mathcal{P}(\mathbb{N})$ n'est pas dénombrable). On choisit le codage selon les opérations dont on a besoin.
:::

### Coder des graphes

Un graphe orienté sur les sommets $\{1, 2, 3\}$ est entièrement décrit par sa **matrice d'adjacence** : un booléen pour chaque couple $(i, j)$, qui vaut 1 s'il y a un arc de $i$ vers $j$. C'est une bijection entre les graphes orientés (sommets numérotés, boucles autorisées) et $\{0, 1\}^{3 \times 3}$.

:::exercise[Exercice du cours 2 — Combien de graphes orientés à 3 sommets ?]
Quel est le nombre de graphes orientés à trois sommets (numérotés 1, 2, 3) ?
:::

:::correction
Avec la matrice d'adjacence, un graphe = un choix de 0 ou 1 pour chacune des $3 \times 3 = 9$ cases : il y a $2^9 = 512$ graphes orientés (boucles $i \to i$ autorisées).

Si l'on **interdit les boucles**, seules les $9 - 3 = 6$ cases hors diagonale sont libres : $2^6 = 64$ graphes. Toujours préciser la convention ! (On compte ici des graphes à sommets **numérotés** : deux graphes qui ne diffèrent que par la numérotation sont comptés deux fois.)
:::

::item{id="ch10-graphes"}

:::key[Pourquoi s'embêter avec des bijections ?]
Pour **compter** : on choisit le codage dans lequel le dénombrement est évident (des suites de 0 et de 1, des $k$-uplets…), et on prouve que c'est une bijection.
:::

## 3. Ensembles finis et cardinal

:::definition[Ensemble fini]
Un ensemble $E$ est **fini** si $E = \emptyset$, ou s'il existe $n \in \mathbb{N}^*$ tel que $\{1, \ldots, n\}$ et $E$ sont équipotents.
:::

Intuitivement, on peut attribuer à chaque élément de $E$ un **numéro unique** entre $1$ et $n$, via une bijection $\{1, \ldots, n\} \to E$. Les deux cas sont exclusifs : un ensemble non vide n'est jamais équipotent à $\emptyset$.

:::definition[Cardinal]
Si $E$ est fini non vide, il existe un **unique** $n \in \mathbb{N}^*$ tel que $\{1, \ldots, n\}$ et $E$ sont équipotents : c'est le **cardinal** $\mathrm{Card}(E) = n$. On pose $\mathrm{Card}(\emptyset) = 0$.
:::

(L'unicité de $n$ n'est pas évidente — c'est le « principe des tiroirs » — mais on l'admet.)

:::theorem[Propriété fondamentale]
Si $E$ et $F$ sont finis et équipotents, alors $\mathrm{Card}(E) = \mathrm{Card}(F)$. *(admis)*
:::

## 4. Compter avec des bijections

:::pattern[Équipotence]
**But.** Montrer que $E$ et $F$ sont équipotents.

- Introduisons une relation candidate $f$.
- **Sous-but 1.** Montrer que $f$ est bien une **fonction** $E \to F$ (existence et unicité de l'image ; vérifier que l'image est **dans** $F$).
- **Sous-but 2.** Montrer que $f$ est une bijection :
  - soit par la définition (injective et surjective),
  - soit en exhibant $g$ telle que $g = f^{-1}$ ($f \circ g = \mathrm{Id}_F$ et $g \circ f = \mathrm{Id}_E$).
:::

:::theorem[Composée de bijections]
Si $f : E \to F$ et $g : F \to G$ sont des bijections, alors $g \circ f : E \to G$ est une bijection, et $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.
:::

$$E \xrightarrow{\ f\ } F \xrightarrow{\ g\ } G \qquad\qquad G \xrightarrow{\ g^{-1}\ } F \xrightarrow{\ f^{-1}\ } E$$

:::exercise[Exercice du cours 3 — Même cardinal implique équipotents]
Soient $E$ et $F$ deux ensembles finis tels que $\mathrm{Card}(E) = \mathrm{Card}(F)$. Montrer que $E$ et $F$ sont équipotents.
:::

:::hint[Indice]
Passe par l'ensemble intermédiaire $\{1, \ldots, n\}$ et compose des bijections. N'oublie pas le cas $n = 0$.
:::

:::correction
Soit $n = \mathrm{Card}(E) = \mathrm{Card}(F)$. Disjonction de cas.

- **Si $n = 0$** : $E = F = \emptyset$, et la fonction vide $\emptyset \to \emptyset$ est une bijection (il n'y a rien à vérifier : injectivité et surjectivité sont des énoncés universels sur l'ensemble vide).
- **Si $n \ge 1$** : par définition du cardinal, il existe des bijections $\varphi : \{1, \ldots, n\} \to E$ et $\psi : \{1, \ldots, n\} \to F$. La réciproque $\varphi^{-1} : E \to \{1, \ldots, n\}$ est une bijection, donc $\psi \circ \varphi^{-1} : E \to F$ est une bijection, comme composée de bijections.

Dans les deux cas, $E$ et $F$ sont équipotents. $\square$
:::

## 5. Le cardinal de l'ensemble des parties

:::theorem[Cardinal de $\mathcal{P}(E)$]
Si $E$ est fini et $\mathrm{Card}(E) = n$, alors $\mathrm{Card}(\mathcal{P}(E)) = 2^n$.
:::

C'est pour cela que $\mathcal{P}(E)$ est parfois noté $2^E$.

**Le bon codage.** Numérotons $E = \{e_1, \ldots, e_n\}$. Une partie $X$ est entièrement décrite par la réponse « dedans / dehors » pour chaque $e_i$, soit un mot de $n$ bits :

| | $e_1$ | $e_2$ | $e_3$ | $\cdots$ | $e_n$ |
|---|---|---|---|---|---|
| $e_i \in X$ ? | oui | non | oui | $\cdots$ | non |
| code dans $\{0,1\}^n$ | 1 | 0 | 1 | $\cdots$ | 0 |

:::correction[Voir la preuve]
Soit $E = \{e_1, \ldots, e_n\}$ de cardinal $n$ et $\mathbb{B} = \{0, 1\}$. Définissons $f : \mathcal{P}(E) \to \mathbb{B}^n$ par $f(X) = (x_1, \ldots, x_n)$, où $x_i = 1$ si $e_i \in X$ et $x_i = 0$ sinon. C'est bien une fonction (chaque $x_i$ est déterminé de façon unique).

- **Surjective** : soit $(x_1, \ldots, x_n) \in \mathbb{B}^n$. La partie $X = \{e_i \mid i \in \{1, \ldots, n\},\ x_i = 1\}$ vérifie $f(X) = (x_1, \ldots, x_n)$.
- **Injective** : soient $X, Y \in \mathcal{P}(E)$ tels que $f(X) = f(Y)$. Alors pour tout $i$, $e_i \in X \iff x_i = 1 \iff e_i \in Y$ : $X$ et $Y$ ont les mêmes éléments, donc $X = Y$.

$\mathcal{P}(E)$ et $\mathbb{B}^n$ sont équipotents, donc $\mathrm{Card}(\mathcal{P}(E)) = \mathrm{Card}(\mathbb{B}^n) = 2^n$ (on admet ici le cardinal de $\mathbb{B}^n$, justifié au chapitre 11 par le cardinal d'un produit cartésien). $\square$
:::

::item{id="ch10-parties"}

## 6. Exercices supplémentaires

:::exercise[Entraînement 1 — Pairs et entiers]
Montrer que $\mathbb{N}$ et l'ensemble $2\mathbb{N}$ des entiers pairs sont équipotents.
:::

:::correction
$f : n \in \mathbb{N} \mapsto 2n \in 2\mathbb{N}$ est une fonction (à valeurs paires). Sa réciproque candidate est $g : m \in 2\mathbb{N} \mapsto m/2 \in \mathbb{N}$ (bien définie car $m$ est pair). On a $f(g(m)) = m$ et $g(f(n)) = n$ : $f$ est une bijection. $\square$

Remarque : un ensemble **infini** peut être équipotent à une partie stricte de lui-même. C'est impossible pour un ensemble fini (une partie stricte a un cardinal strictement plus petit, ch. 11).
:::

:::exercise[Entraînement 2 — Entiers relatifs]
Montrer que $\mathbb{N}$ et $\mathbb{Z}$ sont équipotents.
:::

:::correction
On énumère $\mathbb{Z}$ en zigzag : $0, -1, 1, -2, 2, \ldots$ Formellement, $f : \mathbb{N} \to \mathbb{Z}$, $f(n) = n/2$ si $n$ est pair, $f(n) = -(n+1)/2$ si $n$ est impair. Candidate réciproque : $g(z) = 2z$ si $z \ge 0$, $g(z) = -2z - 1$ si $z < 0$.

- Si $n = 2k$ : $f(n) = k \ge 0$ et $g(k) = 2k = n$. Si $n = 2k + 1$ : $f(n) = -(k+1) < 0$ et $g(-(k+1)) = 2k + 2 - 1 = n$.
- Si $z \ge 0$ : $g(z) = 2z$ pair, $f(2z) = z$. Si $z < 0$ : $g(z) = -2z - 1$ impair, $f(-2z - 1) = -(-2z)/2 = z$.

Donc $f$ et $g$ sont réciproques : $f$ est une bijection. $\square$
:::

## 7. Fiche récapitulative

:::key[L'essentiel]
- Bijection = changement de **codage** sans perte ; la réciproque « décode ».
- $E$ fini de cardinal $n$ ⟺ $E$ équipotent à $\{1, \ldots, n\}$ ; $\mathrm{Card}(\emptyset) = 0$.
- Finis : **équipotents ⟺ même cardinal**.
- Équipotence : construire $f$, vérifier que c'est une fonction **à valeurs dans $F$**, puis bijection (définition ou réciproque).
- $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.
- $\mathrm{Card}(\mathcal{P}(E)) = 2^{\mathrm{Card}(E)}$, via $X \mapsto$ mot de bits « dedans / dehors ».
:::
