---
title: Ch1 — Objets mathématiques et implication
summary: Variables, premiers ensembles, fonctions vues par un ingénieur, propositions, connecteurs et le premier motif de preuve.
tags: [propositions, implication, fonctions]
minutes: 45
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- expliquer pourquoi on a besoin d'un langage **formel** plutôt que du français courant ;
- nommer correctement des objets mathématiques ;
- dire ce qu'est un **ensemble**, un **singleton**, et pourquoi $\{x\} \neq x$ ;
- reconnaître une **fonction** (une entrée → **une seule** sortie, de types précis) ;
- manipuler les connecteurs $\neg, \wedge, \vee, \Rightarrow, \Leftrightarrow$ et leur **table de vérité** ;
- rédiger une preuve directe d'une implication $P \Rightarrow Q$… et repérer les fausses preuves.

:::intuition[Le fil conducteur]
Les mathématiques ne consistent pas à faire des calculs ni à apprendre par cœur : leur but est de **trouver des énoncés vrais** et de le **prouver**. Pour cela, chaque mot doit avoir un sens précis, et chaque raisonnement doit suivre un **motif** reconnu. En informatique, c'est exactement ce qu'il faut pour prouver qu'un algorithme est correct, mesurer sa complexité ou écrire un programme sans bug : une preuve rigoureuse ressemble beaucoup à un programme sans faille.
:::

## 2. Variables : nommer les objets

On manipule des objets (nombres, ensembles, fonctions…) en leur donnant des **noms**, les variables. Deux règles de bon sens :

- **deux objets différents portent des noms différents** (sinon le texte devient ambigu) ;
- **deux objets de même nature portent des noms qui se ressemblent**.

:::example
« Soient $n, m \in \mathbb{N}$ et $x, y \in \mathbb{R}$ » se lit bien mieux que « soient $n, x \in \mathbb{N}$ et $y, m \in \mathbb{R}$ » : on devine le type de chaque variable à son nom. De même, on note les ensembles avec des majuscules ($A, B, E$) et leurs éléments avec des minuscules ($a, x$).
:::

## 3. Ensembles : une première approche

:::definition[Ensemble]
Un **ensemble** (*set*) est une collection bien définie d'objets, appelés ses **éléments**. On note $x \in E$ pour « $x$ appartient à $E$ ».
:::

Exemples : $\mathbb{N}$, $\mathbb{R}$, l'ensemble $\mathbb{P}$ des nombres premiers, l'ensemble des points d'une droite.

Règles de représentation :

- **pas de doublons** : un objet est dans l'ensemble ou ne l'est pas, il n'y figure pas « deux fois » ;
- **pas d'ordre** : un ensemble fini à $n$ éléments s'écrit $\{x_1, \dots, x_n\}$, mais la numérotation est arbitraire ;
- le **singleton** $\{x\}$ est l'ensemble dont le seul élément est $x$ : ce n'est **pas** la même chose que $x$.

:::example
$\{0, 1, 2\}$ et $\{2, 1, 0, 2\}$ désignent le **même** ensemble (la seconde écriture est maladroite). En revanche, $\{0\} \neq 0$ : le premier est un ensemble, le second un nombre. De même $\emptyset \neq \{\emptyset\}$ : le premier n'a aucun élément, le second en a un (l'ensemble vide lui-même).
:::

### Le paradoxe du catalogue

La théorie « naïve » des ensembles a une faille. Imagine une bibliothèque qui suit trois règles :

1. chaque section possède un **catalogue** qui liste son contenu ;
2. certains catalogues se listent eux-mêmes, d'autres non ;
3. un **catalogue spécial** liste exactement tous les catalogues qui **ne** se listent **pas** eux-mêmes.

**Le catalogue spécial se liste-t-il lui-même ?**

:::correction[Voir l'analyse du paradoxe]
- S'il se liste, alors (règle 3) il fait partie des catalogues qui ne se listent pas : contradiction.
- S'il ne se liste pas, alors il fait partie des catalogues qui ne se listent pas, donc (règle 3) il doit se lister : contradiction.

Aucune des deux réponses n'est possible : la règle 3 décrit une « collection » qui **ne peut pas exister**. C'est la version bibliothèque du **paradoxe de Russell** : « l'ensemble de tous les ensembles qui ne s'appartiennent pas à eux-mêmes » n'est pas un ensemble. Leçon pratique pour ce cours : on construit toujours un ensemble **à l'intérieur d'un ensemble déjà connu** (par exemple $\{x \in E \mid P(x)\}$, voir ch. 3), jamais « tous les objets tels que… ».
:::

::item{id="ch1-ensembles"}

## 4. Fonctions : la vision de l'ingénieur

:::intuition[Réponse d'ingénieur]
Une fonction prend une **entrée d'un type donné** et renvoie **une seule valeur** d'un autre type (éventuellement le même).
:::

Cette phrase contient trois exigences, que l'exemple suivant illustre. On veut une fonction qui renvoie l'**indice** de la plus grande valeur d'un vecteur d'entiers :

```cpp
int f(std::vector<int> v) {
  int m = 0;
  for (int i = 0; i < v.size(); i++)
    if (v[i] > v[m]) m = i;
  return m;
}
```

**Trouve au moins deux problèmes** avant d'ouvrir la correction.

:::correction
1. **Le domaine (les entrées valides).** Sur le vecteur vide, `v[m]` lit `v[0]` qui n'existe pas : comportement indéfini. Le vecteur vide n'a pas de « plus grande valeur » : il n'est **pas une entrée valide**. On le dit explicitement avec `assert(v.size() != 0);`. C'est le **domaine** de la fonction : l'ensemble des entrées qu'elle accepte réellement.
2. **L'ensemble d'arrivée (le type de sortie).** Un indice n'est jamais négatif : la fonction ne renvoie que des entiers positifs ou nuls. On peut **restreindre le type de sortie** à `unsigned int`. L'**image** (les valeurs réellement atteintes) peut être plus petite que le type annoncé.
3. **La spécification est ambiguë.** Sur `[2, 3, 1, 3]`, le maximum 3 apparaît aux indices 1 et 3 : lequel renvoyer ? Le code renvoie 1 (comparaison stricte `>`), mais la spécification ne le disait pas. Une spécification correcte : « renvoie le **plus petit** indice d'un élément de valeur maximale ». Une entrée doit conduire (*yield*) à **une seule** sortie, clairement définie.
:::

À retenir : une fonction ne se résume pas à une formule ; ce peut être un programme, une règle, une construction. Mais il faut toujours vérifier :

- le **type des entrées** et le **domaine** (quelles entrées sont permises) ;
- le **type des sorties** ;
- qu'**une entrée donne une et une seule sortie**.

Une définition par « contraintes » ne garantit pas toujours l'unicité : « $y$ tel que $y^2 = x$ » ne définit pas une fonction de $\mathbb{R}_+$ dans $\mathbb{R}$, car $x = 4$ a deux candidats ($2$ et $-2$).

::item{id="ch1-fonctions"}

## 5. Propositions et connecteurs logiques

:::definition[Proposition]
Une **proposition** est un énoncé portant sur des objets mathématiques, auquel on attribue une **valeur de vérité** : vrai (V) ou faux (F).
:::

:::theorem[Tiers exclu (*law of the excluded middle*)]
Une proposition $P$ est soit vraie, soit fausse — jamais les deux, jamais aucune des deux.
:::

C'est un **axiome** : il n'existe que deux valeurs de vérité, mutuellement exclusives. On construit de nouvelles propositions à partir de $P$ et $Q$ grâce aux **connecteurs** :

| Notation | Se lit | Est vraie quand… |
|---|---|---|
| $\neg P$ | non $P$ | $P$ est fausse |
| $P \wedge Q$ | $P$ et $Q$ | les **deux** sont vraies |
| $P \vee Q$ | $P$ ou $Q$ | **au moins une** est vraie (ou inclusif) |
| $P \Rightarrow Q$ | $P$ implique $Q$ | si $P$ est vraie, alors $Q$ l'est aussi |
| $P \Leftrightarrow Q$ | $P$ équivaut à $Q$ | $P$ et $Q$ ont la **même** valeur de vérité |

Table de vérité complète :

| $P$ | $Q$ | $\neg P$ | $P \wedge Q$ | $P \vee Q$ | $P \Rightarrow Q$ | $P \Leftrightarrow Q$ |
|---|---|---|---|---|---|---|
| V | V | F | V | V | **V** | V |
| V | F | F | F | V | **F** | F |
| F | V | V | F | V | **V** | F |
| F | F | V | F | F | **V** | V |

:::warning[Le « ou » mathématique est inclusif]
« Paye l'amende **ou** va en prison » est un *ou exclusif* : pas les deux. En mathématiques, $P \vee Q$ est vrai aussi quand $P$ et $Q$ sont vraies toutes les deux.
:::

## 6. L'implication, un contrat

Les théorèmes ont presque toujours la forme « si une hypothèse $P$ est vraie, alors une conclusion $Q$ l'est aussi », c'est-à-dire $P \Rightarrow Q$.

:::key[Ce que signifie vraiment $P \Rightarrow Q$]
- $P \Rightarrow Q$ est un **contrat** : « chaque fois que $P$ est vraie, $Q$ est vraie ». Cela **ne veut pas dire** que $P$ *cause* $Q$.
- Le contrat n'est rompu que dans **un seul cas** : $P$ vraie et $Q$ fausse. Donc **si $P$ est fausse, $P \Rightarrow Q$ est vraie**, quelle que soit $Q$.
- Si $P$ et $P \Rightarrow Q$ sont vraies, alors $Q$ est vraie (*modus ponens*). C'est ainsi qu'on **utilise** un théorème.
- $Q$ vraie et $P$ fausse ne contredit pas $P \Rightarrow Q$.
:::

::item{id="ch1-implication"}

## 7. Premier motif de preuve : l'implication directe

:::pattern[Implication]
**But.** Montrer que $P \Rightarrow Q$ est vraie.

- *Si $P$ est vraie…*
  - **Avance de l'hypothèse vers la conclusion** : une suite linéaire de déductions jusqu'à atteindre $Q$.
  - **Déroule les définitions** : écris $P$ en détail, en explicitant chaque définition.
  - **Écris les propriétés évidentes** : quelles conséquences immédiates de $P$ peuvent servir de point de départ ?
- *…alors $Q$ est vraie.*
:::

On ne s'occupe **jamais** du cas « $P$ fausse » : l'implication y est automatiquement vraie. On **suppose** $P$, et on **déduit** $Q$.

:::exercise[Exercice du cours 2 — Carré d'un entier pair]
Montrer que si $n \in \mathbb{N}$ est pair (*even*), alors $n^2$ est pair.
:::

:::hint[Indice]
« $n$ est pair » se déroule en : il existe $k \in \mathbb{N}$ tel que $n = 2k$. Calcule $n^2$ et fais apparaître un facteur 2.
:::

:::correction
**But.** Montrons que pour $n \in \mathbb{N}$, ($n$ pair) $\Rightarrow$ ($n^2$ pair). *(on explicite le but)*

Soit $n \in \mathbb{N}$ un entier pair. *(on suppose l'hypothèse)*

Par définition, il existe $k \in \mathbb{N}$ tel que $n = 2k$. *(on déroule la définition)*

Alors $n^2 = (2k)^2 = 4k^2 = 2 \cdot (2k^2)$, avec $2k^2 \in \mathbb{N}$.

Donc $n^2$ est pair. *(on conclut explicitement)* $\square$
:::

## 8. Fausses preuves : deux erreurs classiques

### 8.1 Partir de la conclusion

Voici une « preuve » que $1 = 2$ :

> Supposons que $1 = 2$. Alors $0 \times 1 = 0 \times 2$, donc $0 = 0$. Or $0 = 0$ est vrai. Donc $1 = 2$ est vrai.

:::correction[Où est l'erreur ?]
Ce raisonnement a prouvé l'implication $(1 = 2) \Rightarrow (0 = 0)$, ce qui est **vrai**… mais ne dit **rien** sur $1 = 2$. Une implication vraie dont la conclusion est vraie ne rend pas l'hypothèse vraie : relis la table, la ligne « $P$ faux, $Q$ vrai » donne bien $P \Rightarrow Q$ vrai.

On ne prouve jamais un énoncé en **supposant** qu'il est vrai puis en arrivant à quelque chose de vrai. On part des **hypothèses** (ou de faits connus) et on arrive à la **conclusion**.
:::

### 8.2 La même erreur, mieux cachée

« Montrons que pour tous $x, y \in \mathbb{R}$, $xy \ge 0 \Rightarrow x + y \ge 2\sqrt{xy}$. Si $xy \ge 0$ :

$$x + y \ge 2\sqrt{xy} \;\Rightarrow\; (x+y)^2 \ge 4xy \;\Rightarrow\; x^2 - 2xy + y^2 \ge 0 \;\Rightarrow\; (x-y)^2 \ge 0$$

Or $(x-y)^2 \ge 0$ est vrai, donc la propriété est vraie. »

:::correction[Où est l'erreur ? Et la propriété est-elle vraie ?]
On est **parti de la conclusion** pour arriver à une évidence : c'est l'erreur 8.1. De plus, la première flèche « élever au carré » ne se renverse pas quand les nombres sont négatifs.

D'ailleurs la propriété est **fausse** : avec $x = y = -1$, on a $xy = 1 \ge 0$ mais $x + y = -2 < 2 = 2\sqrt{1}$. Un seul contre-exemple suffit à la réfuter.

**Ce qui est vrai** : pour tous $x, y \in \mathbb{R}$ tels que $xy \ge 0$, $|x + y| \ge 2\sqrt{xy}$. Preuve **dans le bon sens** : soient $x, y \in \mathbb{R}$ avec $xy \ge 0$ (donc $\sqrt{xy}$ existe).

$$
\begin{aligned}
(x - y)^2 &\ge 0 && \text{(un carré est positif)}\\
x^2 - 2xy + y^2 &\ge 0 \\
x^2 + 2xy + y^2 &\ge 4xy && \text{(on ajoute } 4xy \text{ des deux côtés)}\\
(x + y)^2 &\ge 4xy
\end{aligned}
$$

La racine carrée est croissante sur $\mathbb{R}_+$ et les deux membres sont positifs, donc $\sqrt{(x+y)^2} \ge \sqrt{4xy}$, c'est-à-dire $|x + y| \ge 2\sqrt{xy}$. $\square$

Chaque ligne découle de la **précédente**, en partant d'un fait vrai : c'est une vraie preuve.
:::

## 9. Exercices du cours

:::exercise[Exercice du cours 1 — Est-ce une fonction ?]
Les objets suivants sont-ils des fonctions ? Si oui, décrire leur domaine et leur image.

1. Le minimum.
2. La dérivation.
3. La primitivation (calcul d'une primitive).
4. La fonction C `malloc`.
:::

:::hint[Indice 1]
Pour chacun : quel est le **type** de l'entrée ? de la sortie ? Une entrée donne-t-elle toujours **exactement une** sortie ?
:::

:::hint[Indice 2]
Une fonction peut prendre un **ensemble** en entrée, ou une **fonction** en entrée et renvoyer une fonction.
:::

:::correction
1. **Le minimum** : en considérant des ensembles **non vides** d'entiers, c'est une fonction qui prend un ensemble et renvoie sa plus petite valeur. Attention : tout ensemble d'entiers (relatifs) n'admet pas de minimum ($\mathbb{Z}$ lui-même n'en a pas), seuls les ensembles **minorés** en ont un. Le domaine est donc l'ensemble des parties non vides et minorées de $\mathbb{Z}$ ; l'image est $\mathbb{Z}$ tout entier (tout $k$ est le minimum de $\{k\}$). Retiens qu'une fonction peut prendre un **ensemble** en entrée.
2. **La dérivation** est une fonction : elle prend une fonction réelle **dérivable** et renvoie une fonction réelle (sa dérivée), qui est unique. Une fonction peut prendre une **fonction** en entrée et renvoyer une **fonction**.
3. **La primitivation n'est pas une fonction** : une fonction admet une infinité de primitives. Pour $f : x \in \mathbb{R} \mapsto 1$, $g : x \mapsto x$ et $h : x \mapsto x + 1$ sont deux primitives différentes. Une entrée, plusieurs sorties : ce n'est pas une fonction (sauf à imposer une condition, par exemple « la primitive qui s'annule en 0 »).
4. **`malloc`** prend un entier non signé et renvoie un pointeur `void *`. Mais ce **n'est pas une fonction au sens mathématique** : deux appels avec la même entrée peuvent renvoyer des adresses différentes, selon l'état de la mémoire. Que vaut `malloc(32)` ? Il n'y a pas de réponse universelle.
:::

## 10. Fiche récapitulative

:::key[L'essentiel du chapitre]
- **Nommer** : deux objets différents → deux noms ; objets similaires → noms similaires.
- **Ensemble** : collection sans doublon ni ordre ; $\{x\} \ne x$ ; on construit toujours un ensemble à partir d'un ensemble connu (paradoxe du catalogue).
- **Fonction** : entrée d'un type → **une seule** sortie d'un type ; vérifier domaine, type de sortie, unicité.
- **Tiers exclu** : une proposition est vraie ou fausse.
- **$P \Rightarrow Q$** n'est faux que si $P$ est vrai et $Q$ faux ; c'est un contrat, pas une causalité.
- **Preuve directe** : on suppose $P$, on déroule les définitions, on avance jusqu'à $Q$. On ne part **jamais** de la conclusion.
- **Un contre-exemple suffit** pour réfuter un énoncé universel.
:::
