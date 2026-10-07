---
title: Ch8 — Raisonnement par récurrence
summary: Principe de récurrence simple, sa preuve par le bon ordre de ℕ, rédaction type, exercices classiques et fausses récurrences.
tags: [récurrence, induction]
minutes: 55
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- énoncer le **principe de récurrence** et expliquer pourquoi il est vrai ;
- rédiger une récurrence **impeccable** : propriété $P(n)$ explicite, initialisation au bon rang, hérédité ;
- trouver le **lien** entre $P(n)$ et $P(n+1)$ dans les exemples classiques (sommes, inégalités, divisibilité) ;
- repérer les **fausses récurrences** (initialisation oubliée, hérédité qui ne marche pas pour tous les $n$).

:::intuition[Le fil conducteur]
La récurrence prouve des propriétés **héréditaires** sur les entiers, comme une rangée de dominos : on fait tomber le **premier** (initialisation), et on montre que **chaque** domino fait tomber le suivant (hérédité). Alors tous tombent.
:::

## 2. Le principe

:::theorem[Récurrence simple (*simple induction*)]
Soient $P$ une propriété des entiers naturels et $n_0 \in \mathbb{N}$ tels que :

- $P(n_0)$ est vraie ;
- $\forall n \ge n_0,\ P(n) \Rightarrow P(n+1)$.

Alors $\forall n \ge n_0,\ P(n)$.
:::

:::pattern[Récurrence simple]
**But.** Montrer que $\forall n \ge n_0,\ P(n)$.

- On procède par récurrence simple sur $n$. *(on l'annonce, et on écrit $P(n)$ explicitement)*
- **Initialisation (*base case*).** Montrer que $P(n_0)$ est vraie.
  - Ne l'oublie pas ! Et utilise le **bon** $n_0$.
  - Les hypothèses donnent souvent $P(n_0)$ directement.
- **Hérédité (*inductive case*).** Montrer que $\forall n \ge n_0,\ P(n) \Rightarrow P(n+1)$.
  - Soit $n \ge n_0$ tel que $P(n)$ est vraie (**hypothèse de récurrence**)…
  - Trouve une **relation** entre $P(n)$ et $P(n+1)$, puis applique $P(n)$.
  - … alors $P(n+1)$ est vraie.
- **Conclusion.** Par récurrence, $\forall n \ge n_0,\ P(n)$.
:::

:::warning[L'hypothèse de récurrence n'est pas « pour tout $n$ »]
Dans l'hérédité, on fixe **un** $n \ge n_0$ et on suppose $P(n)$ pour **ce** $n$. Écrire « supposons que $\forall n,\ P(n)$ » revient à supposer ce qu'on veut démontrer.
:::

:::exercise[Exercice du cours 1 — Somme des premiers entiers]
Montrer que $\forall n \in \mathbb{N}^*,\ 1 + 2 + \cdots + n = \frac{n(n+1)}{2}$.
:::

:::hint[Indice]
Pour passer de $n$ à $n + 1$, la somme gagne **un seul** terme : $n + 1$.
:::

:::correction
Pour $n \in \mathbb{N}^*$, notons $P(n)$ : « $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ ». Procédons par récurrence simple sur $n \ge 1$.

**Initialisation ($n = 1$).** $\sum_{k=1}^{1} k = 1$ et $\frac{1 \cdot 2}{2} = 1$ : $P(1)$ est vraie.

**Hérédité.** Soit $n \ge 1$ tel que $P(n)$ est vraie. Alors
$$\sum_{k=1}^{n+1} k = \Big(\sum_{k=1}^{n} k\Big) + (n+1) \overset{P(n)}{=} \frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2},$$
ce qui est exactement $P(n+1)$.

**Conclusion.** Par récurrence, $\forall n \in \mathbb{N}^*,\ \sum_{k=1}^n k = \frac{n(n+1)}{2}$. $\square$
:::

::item{id="ch8-somme"}

## 3. Pourquoi le principe est vrai

On veut prouver : $\big(P(n_0) \wedge (\forall n \ge n_0,\ P(n) \Rightarrow P(n+1))\big) \Rightarrow (\forall n \ge n_0,\ P(n))$.

:::correction[Voir la preuve (par l'absurde, grâce au bon ordre)]
Supposons les deux hypothèses, et supposons par l'absurde qu'il existe $u \ge n_0$ tel que $P(u)$ est fausse. L'ensemble $H = \{n \ge n_0 \mid \neg P(n)\}$ est alors une partie **non vide** de $\mathbb{N}$ (il contient $u$).

Or $\mathbb{N}$ est **bien ordonné** : toute partie non vide de $\mathbb{N}$ admet un plus petit élément (chapitre 4, exercice 5). Soit $m$ le plus petit élément de $H$. Disjonction de cas :

- **Si $m = n_0$** : $P(m)$ est vraie par hypothèse, mais fausse car $m \in H$. Contradiction.
- **Si $m > n_0$** : alors $m - 1 \ge n_0$ et, par minimalité de $m$, $m - 1 \notin H$ : $P(m-1)$ est vraie. Par hérédité, $P(m)$ est vraie. Contradiction encore.

Donc $H$ est vide, et $\forall n \ge n_0,\ P(n)$. $\square$
:::

## 4. Exercices du cours

:::exercise[Exercice du cours 2 — Somme des carrés]
Montrer que $\forall n \in \mathbb{N}^*,\ 1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$.
:::

:::hint[Indice]
Après avoir appliqué l'hypothèse de récurrence, factorise par $(n+1)$ et vérifie que $2n^2 + 7n + 6 = (n+2)(2n+3)$.
:::

:::correction
Notons $P(n)$ : « $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$ ». Récurrence simple sur $n \ge 1$.

**Initialisation.** $1^2 = 1$ et $\frac{1 \cdot 2 \cdot 3}{6} = 1$ : $P(1)$ est vraie.

**Hérédité.** Soit $n \ge 1$ tel que $P(n)$. Alors
$$
\begin{aligned}
\sum_{k=1}^{n+1} k^2 &= \frac{n(n+1)(2n+1)}{6} + (n+1)^2 = \frac{(n+1)\big(n(2n+1) + 6(n+1)\big)}{6} \\
&= \frac{(n+1)(2n^2 + 7n + 6)}{6} = \frac{(n+1)(n+2)(2n+3)}{6},
\end{aligned}
$$
qui est $P(n+1)$, puisque $2(n+1) + 1 = 2n + 3$.

**Conclusion.** Par récurrence, la formule est vraie pour tout $n \ge 1$. $\square$
:::

:::exercise[Exercice du cours 3 — Une inégalité trigonométrique]
Montrer que $\forall n \in \mathbb{N}^*,\ \forall x \in \mathbb{R},\ |\sin(nx)| \le n\,|\sin(x)|$. On rappelle que $\sin(a + b) = \cos(a)\sin(b) + \sin(a)\cos(b)$.
:::

:::hint[Indice 1]
La récurrence porte sur $n$, **pas** sur $x$ : la propriété est $P(n)$ : « $\forall x \in \mathbb{R},\ |\sin(nx)| \le n|\sin x|$ ».
:::

:::hint[Indice 2]
Écris $\sin((n+1)x) = \sin(nx + x)$, puis utilise l'inégalité triangulaire et $|\cos| \le 1$.
:::

:::correction
Pour $n \ge 1$, notons $P(n)$ : « $\forall x \in \mathbb{R},\ |\sin(nx)| \le n|\sin(x)|$ ». Récurrence simple sur $n$.

**Initialisation.** Pour $n = 1$ : $|\sin(x)| \le |\sin(x)|$, vrai.

**Hérédité.** Soit $n \ge 1$ tel que $P(n)$. Soit $x \in \mathbb{R}$. Avec $a = nx$ et $b = x$ :
$$
\begin{aligned}
|\sin((n+1)x)| &= |\cos(nx)\sin(x) + \sin(nx)\cos(x)| \\
&\le |\cos(nx)|\,|\sin(x)| + |\sin(nx)|\,|\cos(x)| && \text{(inégalité triangulaire)}\\
&\le |\sin(x)| + |\sin(nx)| && (|\cos| \le 1)\\
&\le |\sin(x)| + n|\sin(x)| = (n+1)|\sin(x)| && (P(n) \text{ appliqué à } x).
\end{aligned}
$$
C'est $P(n+1)$, $x$ étant quelconque.

**Conclusion.** Par récurrence, $\forall n \ge 1,\ \forall x \in \mathbb{R},\ |\sin(nx)| \le n|\sin x|$. $\square$
:::

## 5. Fausses récurrences

### 5.1 Il manque quelque chose

> « Montrons par récurrence que $\forall n \in \mathbb{N}^*,\ 9 \mid 10^n + 1$. Supposons que pour un $n \in \mathbb{N}^*$, $9 \mid 10^n + 1$ : il existe $k$ tel que $10^n + 1 = 9k$. Alors $10 \times (10^n + 1) = 90k$, soit $10^{n+1} + 10 = 90k$, donc $10^{n+1} + 1 = 90k - 9 = 9(10k - 1)$ : $9 \mid 10^{n+1} + 1$. »

:::correction[Où est l'erreur ?]
L'hérédité est **juste**… mais l'**initialisation** a été oubliée, et elle est **fausse** : $10^1 + 1 = 11$ n'est pas divisible par 9. La propriété est d'ailleurs fausse pour tout $n$ : comme $10 = 9 + 1$, on a $10^n \equiv 1 \pmod 9$, donc $10^n + 1 \equiv 2 \pmod 9$. Une hérédité seule ne prouve rien : les dominos peuvent être parfaitement alignés, si le premier ne tombe pas, aucun ne tombe.
:::

### 5.2 « Je suis le meilleur prof »

> « Montrons par récurrence que toute classe de $n \in \mathbb{N}$ étudiants est unanimement d'accord avec moi.
> *Initialisation* : dans une classe de 0 étudiant, personne ne me contredit.
> *Hérédité* : supposons la propriété vraie pour toute classe de $n$ étudiants. Dans une classe de $n + 1$ étudiants, si je retire un étudiant $e_1$, les $n$ restants sont d'accord avec moi (hypothèse de récurrence). Si je remets $e_1$ et que je retire un **autre** étudiant $e_2$ (qui est d'accord avec moi), les $n$ restants, dont $e_1$, sont d'accord avec moi. Donc les $n + 1$ sont d'accord. »

:::correction[Pourquoi est-ce faux ?]
L'hérédité doit être prouvée **pour tout** $n \ge n_0$, ici dès $n = 0$. Or pour passer de $n = 0$ à $n + 1 = 1$, la classe n'a qu'**un seul** étudiant $e_1$ : il n'existe pas d'**autre** étudiant $e_2$ à retirer. L'argument suppose implicitement $n + 1 \ge 2$. Le maillon $P(0) \Rightarrow P(1)$ manque, et toute la chaîne s'effondre : $P(0)$ est vraie (vérité vide), mais $P(1)$ (« tout étudiant seul est d'accord avec moi ») est fausse.

Leçon : vérifie que ton hérédité fonctionne pour le **plus petit** $n$ concerné, pas seulement pour les « grands » $n$.
:::

::item{id="ch8-erreurs"}

## 6. Exercices supplémentaires

:::exercise[Entraînement 1 — Somme des impairs]
Montrer que $\forall n \in \mathbb{N}^*,\ 1 + 3 + 5 + \cdots + (2n - 1) = n^2$.
:::

:::correction
$P(n)$ : « $\sum_{k=1}^n (2k-1) = n^2$ ». Initialisation : $1 = 1^2$. Hérédité : si $P(n)$, alors $\sum_{k=1}^{n+1} (2k-1) = n^2 + (2n + 1) = (n+1)^2$. Par récurrence, c'est vrai pour tout $n \ge 1$. $\square$
:::

:::exercise[Entraînement 2 — Une divisibilité]
Montrer que $\forall n \in \mathbb{N},\ 3 \mid n^3 - n$.
:::

:::correction
$P(n)$ : « $3 \mid n^3 - n$ ». Initialisation : $0^3 - 0 = 0 = 3 \times 0$. Hérédité : supposons $n^3 - n = 3k$. Alors
$$(n+1)^3 - (n+1) = n^3 + 3n^2 + 3n + 1 - n - 1 = (n^3 - n) + 3(n^2 + n) = 3(k + n^2 + n).$$
Donc $3 \mid (n+1)^3 - (n+1)$. Par récurrence, c'est vrai pour tout $n \in \mathbb{N}$. $\square$
:::

:::exercise[Entraînement 3 — Le bon rang de départ]
Montrer que $\forall n \ge 4,\ 2^n \ge n^2$.
:::

:::hint[Indice]
Pour l'hérédité, il suffit de montrer $(n+1)^2 \le 2n^2$, c'est-à-dire $2n + 1 \le n^2$, vrai dès que $n \ge 3$.
:::

:::correction
$P(n)$ : « $2^n \ge n^2$ ». Initialisation ($n = 4$) : $2^4 = 16 \ge 16 = 4^2$.

Hérédité : soit $n \ge 4$ tel que $2^n \ge n^2$. Comme $n \ge 3$, $n^2 - 2n - 1 = (n-1)^2 - 2 \ge 4 - 2 > 0$, donc $2n + 1 \le n^2$. Ainsi $(n+1)^2 = n^2 + 2n + 1 \le 2n^2 \le 2 \cdot 2^n = 2^{n+1}$.

Conclusion : $\forall n \ge 4,\ 2^n \ge n^2$. Remarque : c'est **faux** pour $n = 3$ ($8 < 9$), d'où l'importance du bon $n_0$. $\square$
:::

::item{id="ch8-rang"}

## 7. Fiche récapitulative

:::key[L'essentiel]
- Annonce : « Montrons par récurrence simple sur $n \ge n_0$ la propriété $P(n)$ : … ».
- **Initialisation** au bon rang $n_0$ — jamais oubliée.
- **Hérédité** : « Soit $n \ge n_0$ tel que $P(n)$. Montrons $P(n+1)$. » Trouver le lien $P(n) \leadsto P(n+1)$ (un terme de plus dans une somme, un facteur de plus dans un produit, $\sin(nx + x)$…).
- L'hérédité doit marcher pour **tous** les $n \ge n_0$, y compris le plus petit.
- Le principe découle du **bon ordre** de $\mathbb{N}$.
:::
