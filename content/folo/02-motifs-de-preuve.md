---
title: Ch2 — Les motifs de preuve
summary: Conjonction, disjonction, équivalence, preuve par l'absurde, contraposée, disjonction de cas — et comment choisir.
tags: [motifs de preuve, absurde, contraposée, équivalences logiques]
minutes: 60
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- découper un but contenant $\wedge$, $\vee$ ou $\Leftrightarrow$ en **sous-buts** ;
- rédiger une preuve **par l'absurde** et une preuve **par contraposée**, et ne pas les confondre ;
- connaître par cœur les **équivalences logiques usuelles** (De Morgan, distributivité, contraposée…) ;
- réfuter une fausse équivalence avec un **contre-exemple** ;
- utiliser une **disjonction de cas**.

:::intuition[Le fil conducteur]
Une preuve se construit comme un programme : on commence par le **squelette** (les motifs, les sous-buts), puis on remplit chaque trou. La **structure de l'énoncé** dicte presque toujours le squelette : un « et » se coupe en deux, une équivalence se prouve dans les deux sens, une implication difficile se retourne par contraposée.
:::

## 2. Conjonction et disjonction

Les théorèmes contiennent souvent des $\wedge$ et des $\vee$, parfois cachés : « $n$ est pair et positif », « $x \le 0$ ou $x \ge 1$ ». Il faut parfois **réécrire** l'énoncé pour les faire apparaître. Rappel : le $\vee$ mathématique est **inclusif**.

:::pattern[$\wedge$ en conclusion]
**But.** Montrer que $P \Rightarrow (Q \wedge R)$.

- Supposons $P$ vraie…
  - **Sous-but 1.** Montrer que $Q$ est vraie.
  - **Sous-but 2.** Montrer que $R$ est vraie.
:::

On **découpe** un but complexe en sous-preuves plus simples.

:::pattern[$\wedge$ en hypothèse]
**But.** Montrer que $(P \wedge Q) \Rightarrow R$.

- Si $P$ est vraie…
- … et $Q$ est vraie…
- … alors $R$ est vraie.
:::

Une hypothèse « $P$ et $Q$ » te donne **deux** faits utilisables.

:::pattern[$\vee$ en hypothèse]
**But.** Montrer que $(P \vee Q) \Rightarrow R$.

- **Sous-but 1.** Montrer que $P \Rightarrow R$ : si $P$ est vraie… alors $R$ est vraie.
- **Sous-but 2.** Montrer que $Q \Rightarrow R$ : si $Q$ est vraie… alors $R$ est vraie.
:::

Une hypothèse « $P$ ou $Q$ » ne dit pas **laquelle** est vraie : il faut traiter les **deux** cas.

## 3. L'équivalence

:::theorem[Double implication]
$P \Leftrightarrow Q$ est vraie si et seulement si $P \Rightarrow Q$ **et** $Q \Rightarrow P$ sont vraies.
:::

:::pattern[$\Leftrightarrow$]
**But.** Montrer que $P \Leftrightarrow Q$.

- **Sous-but 1.** Montrer que $P \Rightarrow Q$ : si $P$ est vraie… alors $Q$ est vraie.
- **Sous-but 2.** Montrer que $Q \Rightarrow P$ : si $Q$ est vraie… alors $P$ est vraie.
:::

:::warning[Ne prouve pas un seul sens]
C'est l'oubli le plus fréquent à l'examen : on prouve le sens « facile » et on oublie l'autre. Annonce explicitement les deux sous-buts (« ($\Rightarrow$) … » puis « ($\Leftarrow$) … »).
:::

## 4. Motifs fondés sur la négation

### 4.1 La preuve par l'absurde

:::pattern[Preuve par l'absurde (I)]
**But.** Montrer que $P$ est vraie.

- Supposons que $\neg P$ est vraie…
  - … puis démontrons une chose qui **contredit** une propriété connue, ou une hypothèse.
- Donc $P$ ne peut pas être fausse : elle est vraie.
:::

Ce motif repose sur le **tiers exclu** : $P$ est vraie ou fausse ; si « fausse » mène à une impossibilité, il ne reste que « vraie ».

:::exercise[Exercice du cours 1 — $\sqrt{2}$ est irrationnel]
Montrer que $\sqrt{2}$ est irrationnel. On rappelle que $k \in \mathbb{Q}$ si et seulement s'il existe $p, q \in \mathbb{Z}$ (avec $q \neq 0$) **premiers entre eux** (*relatively prime*) tels que $k = \frac{p}{q}$.
:::

:::hint[Indice 1]
« Irrationnel » est une négation (« pas rationnel ») : supposer le contraire donne une écriture $\sqrt{2} = \frac{p}{q}$ très concrète à manipuler. C'est le cas typique de l'absurde.
:::

:::hint[Indice 2]
Élève au carré : $p^2 = 2q^2$. Que peux-tu dire de la parité de $p$ ? Puis de $q$ ? On admet (ou on prouve, voir exercice 3) que si $p^2$ est pair, alors $p$ est pair.
:::

:::correction
**But.** Montrons par l'absurde que $\sqrt{2}$ est irrationnel.

Supposons que $\sqrt{2}$ est rationnel. Il existe alors $p, q \in \mathbb{Z}$, $q \neq 0$, premiers entre eux, tels que $\sqrt{2} = \frac{p}{q}$.

- En élevant au carré : $2 = \frac{p^2}{q^2}$, donc $p^2 = 2q^2$ : $p^2$ est pair.
- Par conséquent $p$ est pair (exercice 3 ci-dessous). Il existe donc $k \in \mathbb{Z}$ tel que $p = 2k$.
- Alors $2 = \frac{4k^2}{q^2}$, d'où $q^2 = 2k^2$ : $q^2$ est pair, donc $q$ est pair.
- Finalement $p$ et $q$ sont tous deux pairs : $2$ est un diviseur commun différent de $1$, alors qu'ils sont premiers entre eux. **C'est impossible.**

Par l'absurde, $\sqrt{2}$ est irrationnel. $\square$
:::

:::pattern[Preuve par l'absurde (II)]
**But.** Montrer que $P \Rightarrow Q$.

- Si $P$ est vraie…
- Supposons que $\neg Q$ est vraie…
  - … puis démontrons une chose qui contredit $P$ ou une propriété vraie.
- Donc $Q$ ne peut pas être fausse : elle est vraie.
:::

### 4.2 Les équivalences logiques usuelles

Elles se vérifient toutes avec une table de vérité. **À connaître par cœur** :

$$
\begin{aligned}
\neg\neg P &\iff P \\
P \wedge (Q \vee R) &\iff (P \wedge Q) \vee (P \wedge R) \\
P \vee (Q \wedge R) &\iff (P \vee Q) \wedge (P \vee R) \\
\neg(P \vee Q) &\iff \neg P \wedge \neg Q \qquad \text{(De Morgan)}\\
\neg(P \wedge Q) &\iff \neg P \vee \neg Q \qquad \text{(De Morgan)}\\
P \Rightarrow Q &\iff \neg P \vee Q \\
\neg(P \Rightarrow Q) &\iff P \wedge \neg Q \\
P \Rightarrow Q &\iff \neg Q \Rightarrow \neg P \qquad \text{(contraposée)}
\end{aligned}
$$

:::example[Vérifier une équivalence par table de vérité]
Montrons que $P \Rightarrow Q$ équivaut à $\neg P \vee Q$ : on compare les deux colonnes ligne par ligne.

| $P$ | $Q$ | $P \Rightarrow Q$ | $\neg P$ | $\neg P \vee Q$ |
|---|---|---|---|---|
| V | V | V | F | V |
| V | F | F | F | F |
| F | V | V | V | V |
| F | F | V | V | V |

Les colonnes 3 et 5 sont identiques sur **toutes** les lignes : les deux formules sont équivalentes.
:::

:::key[Nier une implication]
La négation de « $P \Rightarrow Q$ » n'est **pas** une implication : c'est « $P$ **et** non $Q$ ». Exemple : la négation de « s'il pleut, je prends mon parapluie » est « il pleut **et** je n'ai pas mon parapluie ».
:::

::item{id="ch2-negations"}

:::exercise[Exercice du cours 2 — Fausses équivalences]
Les propriétés suivantes sont-elles vraies en général ? Sinon, les réfuter avec un contre-exemple.

1. $\neg(P \Rightarrow Q) \iff (\neg P \Rightarrow \neg Q)$
2. $(P \Rightarrow Q) \iff (\neg P \Rightarrow \neg Q)$
3. $\big(P \Leftrightarrow (Q \wedge R)\big) \iff \big((P \Leftrightarrow Q) \wedge (P \Leftrightarrow R)\big)$
4. $\big((P \wedge Q) \Rightarrow R\big) \iff \big((P \Rightarrow R) \wedge (Q \Rightarrow R)\big)$
:::

:::hint[Méthode]
Pour réfuter une équivalence, il suffit de **trouver une ligne** de la table de vérité (une valeur pour $P$, $Q$, $R$) où les deux côtés diffèrent. Ensuite, on peut l'habiller d'un exemple concret.
:::

:::correction
Les quatre sont **fausses** en général.

1. Avec $P$ vraie et $Q$ vraie : $\neg(P \Rightarrow Q)$ est fausse, mais $\neg P \Rightarrow \neg Q$ est vraie (hypothèse fausse). *Exemple :* $P$ = « il pleut », $Q$ = « j'ai pris mon parapluie », pour quelqu'un qui prend son parapluie exactement quand il pleut. Alors $P \Rightarrow Q$ et $\neg P \Rightarrow \neg Q$ sont vraies toutes les deux, donc $\neg(P \Rightarrow Q)$ est fausse alors que $\neg P \Rightarrow \neg Q$ est vraie.
2. Avec $P$ fausse et $Q$ vraie : $P \Rightarrow Q$ est vraie, mais $\neg P \Rightarrow \neg Q$ est fausse. *Exemple :* $P$ = « je suis un humain », $Q$ = « je mourrai ». $P \Rightarrow Q$ est vraie, mais « si je ne suis pas un humain, je ne mourrai pas » est fausse (pense à un chat). **Une implication n'équivaut pas à son « inverse »** ; elle équivaut à sa **contraposée** $\neg Q \Rightarrow \neg P$.
3. Avec $P$ fausse, $Q$ vraie, $R$ fausse : $P \Leftrightarrow (Q \wedge R)$ vaut « F ⇔ F », donc vraie, mais $P \Leftrightarrow Q$ est fausse. *Exemple :* pour un quadrilatère $T$, $P$ = « $T$ est un carré », $Q$ = « $T$ est un losange », $R$ = « $T$ est un rectangle ». « Carré ⇔ (losange et rectangle) » est vrai, mais « carré ⇔ losange » est faux. En revanche le sens $\Leftarrow$ est **toujours vrai** : si $P$, $Q$, $R$ ont toutes la même valeur, alors $Q \wedge R$ a aussi cette valeur.
4. Avec $P$ vraie, $Q$ fausse, $R$ fausse : $(P \wedge Q) \Rightarrow R$ est vraie (hypothèse fausse), mais $P \Rightarrow R$ est fausse. *Exemple :* $P$ = « $T$ est un losange », $Q$ = « $T$ est un rectangle », $R$ = « $T$ est un carré ». « (losange et rectangle) ⇒ carré » est vrai, « losange ⇒ carré » est faux. Là encore, le sens $\Leftarrow$ est toujours vrai : $(P \Rightarrow R) \wedge (Q \Rightarrow R)$ équivaut à $(P \vee Q) \Rightarrow R$, et $P \wedge Q$ entraîne $P \vee Q$.
:::

::item{id="ch2-fausses-equivalences"}

### 4.3 La preuve par contraposée

Puisque $(P \Rightarrow Q) \iff (\neg Q \Rightarrow \neg P)$, on obtient un autre motif pour les implications :

:::pattern[Preuve par contraposée]
**But.** Montrer que $P \Rightarrow Q$.

- **But équivalent.** Montrer que $\neg Q \Rightarrow \neg P$.
  - Si $\neg Q$ est vraie…
  - … alors $\neg P$ est vraie.
:::

:::exercise[Exercice du cours 3 — Si $n^2$ est pair, $n$ est pair]
Montrer que pour $n \in \mathbb{N}$, si $n^2$ est pair, alors $n$ est pair.
:::

:::hint[Indice]
Partir de « $n^2$ est pair » ne mène nulle part (comment « extraire » $n$ ?). En revanche, « $n$ est impair » s'écrit $n = 2k + 1$ et se calcule très bien au carré.
:::

:::correction
**But.** Montrons, pour $n \in \mathbb{N}$, que ($n^2$ pair) $\Rightarrow$ ($n$ pair).

**But équivalent (contraposée).** Montrons que ($n$ impair) $\Rightarrow$ ($n^2$ impair).

Supposons $n$ impair : il existe $k \in \mathbb{N}$ tel que $n = 2k + 1$. Alors

$$n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1,$$

avec $2k^2 + 2k \in \mathbb{N}$ : $n^2$ est impair. La contraposée est prouvée, donc l'implication aussi. $\square$
:::

### 4.4 Absurde ou contraposée ?

:::warning[Ne confonds pas les deux motifs]
- **Contraposée** : on prouve $\neg Q \Rightarrow \neg P$. On **part de $\neg Q$ seul** et on doit **arriver exactement à $\neg P$**. Utile quand $\neg Q$ est plus facile à exprimer que $P$ et donne des conséquences plus intéressantes.
- **Absurde** : on **suppose $P$ et $\neg Q$ à la fois**, et on cherche **n'importe quelle** contradiction. Utile quand $\neg Q$ est plus simple que $Q$ mais que $P$ reste facile à manipuler.

Une preuve par contraposée bien rédigée n'utilise jamais $P$ : si tu te sers de $P$, tu fais en réalité une preuve par l'absurde (ce qui est correct aussi, mais annonce-le !).
:::

## 5. La disjonction de cas

D'après le tiers exclu, pour toute proposition $R$, $R \vee \neg R$ est toujours vraie. Donc $P \Rightarrow Q$ est vraie si et seulement si $(P \wedge R) \Rightarrow Q$ et $(P \wedge \neg R) \Rightarrow Q$ le sont.

:::pattern[Disjonction de cas]
**But.** Montrer que $P \Rightarrow Q$.

- Considérons une proposition $R$ (bien choisie).
- **Sous-but 1.** Montrer que $(P \wedge R) \Rightarrow Q$ : si $P$ et $R$ sont vraies… alors $Q$ est vraie.
- **Sous-but 2.** Montrer que $(P \wedge \neg R) \Rightarrow Q$ : si $P$ est vraie et $R$ fausse… alors $Q$ est vraie.
:::

Le choix de $R$ est la clé : « $n$ est pair », « $x \ge 0$ », « $a \in A$ »…

:::exercise[Exercice du cours 4 — Une somme entière]
Montrer que $\forall n \in \mathbb{N}$, $\frac{n(n+1)}{2} \in \mathbb{N}$.
:::

:::hint[Indice]
Il suffit que $n(n+1)$ soit pair. Distingue selon la parité de $n$.
:::

:::correction
**But.** Montrons que pour tout $n \in \mathbb{N}$, $\frac{n(n+1)}{2} \in \mathbb{N}$. Soit $n \in \mathbb{N}$ ; on raisonne par disjonction de cas sur la parité de $n$.

- **Sous-but 1 : $n$ pair.** Il existe $k \in \mathbb{N}$ tel que $n = 2k$. Alors $\frac{n(n+1)}{2} = \frac{2k(2k+1)}{2} = k(2k+1) \in \mathbb{N}$.
- **Sous-but 2 : $n$ impair.** Il existe $k \in \mathbb{N}$ tel que $n = 2k+1$. Alors $\frac{n(n+1)}{2} = \frac{(2k+1)(2k+2)}{2} = (2k+1)(k+1) \in \mathbb{N}$.

Dans les deux cas, $\frac{n(n+1)}{2} \in \mathbb{N}$. $\square$
:::

### 5.1 Le $\vee$ en conclusion

Pour prouver « $Q$ ou $R$ », on utilise une disjonction de cas sur $Q$ : si $Q$ est vraie, $Q \vee R$ l'est aussi, rien à faire ; il reste donc à traiter le cas où $Q$ est fausse.

:::pattern[$\vee$ en conclusion]
**But.** Montrer que $P \Rightarrow (Q \vee R)$.

- Supposons $P$ vraie.
- Supposons de plus que $Q$ est fausse…
  - … alors $R$ doit être vraie.
:::

:::example
**Montrons que pour tous réels $a, b$ : $ab = 0 \Rightarrow (a = 0 \vee b = 0)$.** Supposons $ab = 0$, et supposons de plus $a \neq 0$. Alors on peut diviser par $a$ : $b = \frac{ab}{a} = \frac{0}{a} = 0$. Donc $a = 0$ ou $b = 0$. $\square$
:::

## 6. Comment choisir son motif

:::method[Construire une preuve]
1. **La structure de l'énoncé impose souvent le motif** : une équivalence → double implication ; un « et » en conclusion → deux sous-buts ; un « ou » en hypothèse → deux cas.
2. Si la structure n'est pas évidente, **explicite toutes les hypothèses et leurs définitions**.
3. Écris le **squelette** (motifs + sous-buts) **avant** de chercher les calculs. Ne te précipite pas.
4. Tu connais le point de départ (hypothèses) et l'arrivée (conclusion) : pour trouver les étapes intermédiaires, cherche ce qui se **déduit immédiatement** des hypothèses et ce qui **suffirait** pour obtenir la conclusion.
5. Si $\neg Q$ est plus « concrète » que $Q$ (« irrationnel », « impair », « n'est pas injective »), pense à l'absurde ou à la contraposée.
:::

::item{id="ch2-quel-motif"}

## 7. Exercices supplémentaires

:::exercise[Entraînement 1 — Parité de $n^2 + n$]
Montrer que pour tout $n \in \mathbb{Z}$, $n^2 + n$ est pair.
:::

:::correction
Soit $n \in \mathbb{Z}$. Disjonction de cas sur la parité de $n$.

- Si $n = 2k$ ($k \in \mathbb{Z}$) : $n^2 + n = 4k^2 + 2k = 2(2k^2 + k)$, pair.
- Si $n = 2k + 1$ : $n^2 + n = (2k+1)^2 + (2k+1) = 4k^2 + 6k + 2 = 2(2k^2 + 3k + 1)$, pair.

Remarque : on peut aussi factoriser $n^2 + n = n(n+1)$, produit de deux entiers consécutifs dont l'un est pair. $\square$
:::

:::exercise[Entraînement 2 — Pas de plus grand entier]
Montrer par l'absurde qu'il n'existe pas de plus grand entier naturel.
:::

:::correction
Supposons qu'il existe un plus grand entier naturel $N$ : pour tout $n \in \mathbb{N}$, $n \le N$. Or $N + 1 \in \mathbb{N}$, donc $N + 1 \le N$, c'est-à-dire $1 \le 0$ : contradiction. Il n'existe donc pas de plus grand entier naturel. $\square$
:::

:::exercise[Entraînement 3 — Une contraposée]
Soit $x \in \mathbb{R}$. Montrer que si $x^2 + x < 0$, alors $x < 0$.
:::

:::correction
Par contraposée : montrons que si $x \ge 0$, alors $x^2 + x \ge 0$. Si $x \ge 0$, alors $x^2 \ge 0$ et $x \ge 0$, donc leur somme est positive : $x^2 + x \ge 0$. La contraposée étant vraie, l'implication l'est aussi. $\square$
:::

:::exercise[Entraînement 4 — Double implication]
Soit $n \in \mathbb{Z}$. Montrer que $n$ est impair si et seulement si $n^2$ est impair.
:::

:::correction
Procédons par double implication.

- **($\Rightarrow$)** Si $n = 2k+1$, alors $n^2 = 2(2k^2 + 2k) + 1$ est impair (même calcul que l'exercice 3).
- **($\Leftarrow$)** Par contraposée : si $n$ est pair, $n = 2k$, alors $n^2 = 2(2k^2)$ est pair, donc pas impair.

Les deux sens étant prouvés, l'équivalence est établie. $\square$
:::

## 8. Fiche récapitulative

| Forme du but | Motif |
|---|---|
| $P \Rightarrow Q$ | supposer $P$, déduire $Q$ |
| $P \Rightarrow (Q \wedge R)$ | deux sous-buts : $Q$, puis $R$ |
| $(P \wedge Q) \Rightarrow R$ | deux hypothèses utilisables |
| $(P \vee Q) \Rightarrow R$ | deux cas : $P \Rightarrow R$ et $Q \Rightarrow R$ |
| $P \Rightarrow (Q \vee R)$ | supposer $P$ et $\neg Q$, déduire $R$ |
| $P \Leftrightarrow Q$ | double implication |
| $P$ (difficile) | absurde : supposer $\neg P$, trouver une contradiction |
| $P \Rightarrow Q$ ($\neg Q$ plus concrète) | contraposée : supposer $\neg Q$, déduire $\neg P$ |
| $P \Rightarrow Q$ (plusieurs situations) | disjonction de cas sur une proposition $R$ |

:::key[L'essentiel]
- $\neg(P \wedge Q) \iff \neg P \vee \neg Q$, $\quad \neg(P \vee Q) \iff \neg P \wedge \neg Q$.
- $P \Rightarrow Q \iff \neg P \vee Q \iff \neg Q \Rightarrow \neg P$ ; mais $P \Rightarrow Q$ **n'équivaut pas** à $\neg P \Rightarrow \neg Q$.
- $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$.
- Annonce **toujours** le motif utilisé.
:::
