---
title: Ch13 — Pièges classiques et conseils de rédaction
summary: Fausses contraposées, loi des petits nombres, fausses récurrences, erreurs de typage, cas limites, et les règles d'une rédaction qui convainc le correcteur.
tags: [erreurs, rédaction, contre-exemples, examen]
minutes: 45
---

## 1. Objectifs

Ce chapitre rassemble les erreurs qui coûtent le plus de points à l'examen, et la façon de les éviter. À la fin, tu dois savoir :

- écrire une **contraposée** correcte (et reconnaître une réciproque déguisée) ;
- ne jamais conclure à partir de **quelques cas** ;
- auditer une **récurrence** ;
- **typer** chaque objet avant de l'utiliser ;
- penser aux **cas limites** ;
- rédiger une preuve **lisible et convaincante**.

## 2. Erreurs de logique

### 2.1 Les contraposées incorrectes

:::example[Une propriété des suites réelles]
Soient $(U_n)$ et $(V_n)$ deux suites réelles. Si les deux suites admettent une limite, alors leur produit $(U_n V_n)$ aussi.
:::

- **Contraposée correcte** : si $(U_n V_n)$ n'a pas de limite, alors $(U_n)$ n'a pas de limite **ou** $(V_n)$ n'a pas de limite. (La négation de « A et B » est « non A **ou** non B ».)
- **Faux** : « si $(U_n V_n)$ n'a pas de limite, alors **aucune** des deux suites n'a de limite ». Contre-exemple : $U_n = 1$ et $V_n = (-1)^n$ ; le produit $(-1)^n$ n'a pas de limite, mais $(U_n)$ converge.
- **Faux aussi** (réciproque) : « si le produit converge, les deux suites convergent ». Contre-exemple : $U_n = V_n = (-1)^n$, dont le produit vaut constamment $1$.

### 2.2 La loi des petits nombres

« $P(0)$ est vraie, $P(1)$ est vraie, $P(2)$ est vraie, $P(3)$ est vraie… donc $\forall n,\ P(n)$. » **Non.** Quelques vérifications ne prouvent jamais un énoncé universel.

:::example[Un polynôme célèbre]
$n^2 + n + 41$ est premier pour $n = 0, 1, 2, \ldots, 39$ — quarante valeurs de suite ! Et pourtant, pour $n = 40$ : $40^2 + 40 + 41 = 1681 = 41^2$.
:::

::item{id="ch13-petits-nombres"}

### 2.3 Les fausses récurrences

- **Mauvaise initialisation** : vouloir prouver $\forall n \in \mathbb{N}^*,\ P(n)$ en initialisant en $n = 0$ ou $n = 2$.
- **Initialisation manquante** : supposer $P(n)$ et $P(n+1)$ pour prouver $P(n+2)$, mais ne vérifier que $P(0)$ au lieu de $P(0)$ **et** $P(1)$.
- **Mauvaise variable** : vouloir prouver, pour un $k$ fixé, $\forall n,\ P(n, k)$ par récurrence sur $k$ au lieu de $n$ — alors que $k$ n'est parfois même pas un entier.
- **Mauvaise profondeur** : utiliser $P(n)$ et $P(n-1)$ pour prouver $P(n+1)$ dans une récurrence **simple**.
- **Mauvais rang** : utiliser $P(n - k)$ dans l'hérédité sans avoir supposé $n \ge k$.
- **Mauvaise hypothèse de récurrence** : supposer « $\forall n,\ P(n)$ » — c'est la conclusion !

## 3. Erreurs de typage

:::example[Une bijection entre fonctions et uplets]
Soient $n, p \in \mathbb{N}^*$ avec $p \le n$, $\mathcal{F}$ l'ensemble des fonctions **injectives** $\{1, \ldots, p\} \to \{1, \ldots, n\}$, et $A_n^p$ l'ensemble des $p$-uplets de $\{1, \ldots, n\}^p$ dont les composantes sont **deux à deux distinctes**. Montrer que $\mathcal{F}$ et $A_n^p$ sont équipotents.
:::

Les éléments de $\mathcal{F}$ sont des **fonctions**, ceux de $A_n^p$ des **uplets**. La bijection doit transformer une fonction en uplet : $\Phi : f \in \mathcal{F} \mapsto (f(1), \ldots, f(p)) \in A_n^p$.

:::correction[Voir la preuve]
- **$\Phi$ est bien définie** : pour $f$ injective, les $f(i)$ sont dans $\{1, \ldots, n\}$ et deux à deux distincts (si $i \neq j$, $f(i) \neq f(j)$), donc $\Phi(f) \in A_n^p$.
- **Réciproque** : $\Psi : (a_1, \ldots, a_p) \in A_n^p \mapsto (i \mapsto a_i)$. C'est une fonction $\{1, \ldots, p\} \to \{1, \ldots, n\}$, injective car les $a_i$ sont distincts : $\Psi(a) \in \mathcal{F}$.
- $\Phi(\Psi(a)) = (a_1, \ldots, a_p) = a$ et $\Psi(\Phi(f)) = (i \mapsto f(i)) = f$.

Donc $\mathcal{F}$ et $A_n^p$ sont équipotents, et $\mathrm{Card}(\mathcal{F}) = \mathrm{Card}(A_n^p) = n(n-1)\cdots(n-p+1) = \frac{n!}{(n-p)!}$ ($n$ choix pour $a_1$, puis $n - 1$ pour $a_2$, etc.). $\square$
:::

:::warning[Les erreurs de type typiques]
- Additionner ou soustraire des **ensembles** ; écrire $\Leftrightarrow$ entre deux ensembles ; écrire $=$ entre deux propositions.
- Confondre $x$ et $\{x\}$, $\in$ et $\subseteq$.
- Appliquer une fonction à un objet qui n'est pas dans son domaine ($f(A)$ avec $A$ une partie, alors que $f$ prend des éléments).
- Oublier de vérifier qu'une fonction construite « tombe » dans le bon ensemble d'arrivée.
:::

## 4. Les cas limites

**Est-il vrai qu'une suite périodique ne peut pas avoir de limite ?** Non : une suite **constante** est périodique (de n'importe quelle période) et converge. En fait, une suite périodique converge si et seulement si elle est constante.

Réflexe : avant de croire un énoncé, teste les **cas extrêmes** — ensemble vide, $n = 0$ ou $1$, fonction constante, relation vide, $A = B$, $A = E$…

::item{id="ch13-cas-limites"}

:::exercise[Exercice du cours 1 — Trouver des contre-exemples]
Trouver un contre-exemple à chacune de ces propriétés inventées :

1. $\left(x^{n+1} + \frac{1}{x^{n+1}}\right) = \left(x^n + \frac{1}{x^n}\right) \cdot \left(x + \frac{1}{x}\right)$
2. $(a \le x) \wedge (b \le y) \Rightarrow a - b \le x - y$
3. $E \setminus A = F \setminus A \Rightarrow E = F$
4. $\mathrm{Card}(\mathcal{P}(E \setminus A)) = \mathrm{Card}(\mathcal{P}(E)) - \mathrm{Card}(\mathcal{P}(A))$
:::

:::correction
1. $x = 1$, $n = 1$ : à gauche $1 + 1 = 2$, à droite $(1 + 1)(1 + 1) = 4$. (En développant, le membre de droite vaut le membre de gauche **plus** $x^{n-1} + \frac{1}{x^{n-1}}$, qui n'est jamais nul.)
2. $a = b = x = 0$ et $y = 10$ : $0 \le 0$ et $0 \le 10$, mais $a - b = 0 > -10 = x - y$. (Ce qui est vrai : $a - y \le x - b$ ; soustraire des inégalités ne se fait qu'en les « croisant ».)
3. $E = \{1\}$, $F = \emptyset$, $A = \{1\}$ : $E \setminus A = F \setminus A = \emptyset$, mais $E \neq F$.
4. $E = A = \{1\}$ : à gauche $\mathrm{Card}(\mathcal{P}(\emptyset)) = 1$, à droite $2 - 2 = 0$. (Ce qui est vrai pour $A \subseteq E$ : $\mathrm{Card}(\mathcal{P}(E \setminus A)) = 2^{n-k} = 2^n / 2^k$ — une **division**, pas une soustraction.)
:::

::item{id="ch13-contre-exemples"}

## 5. Bien raisonner

:::example[Retenir les définitions et propriétés usuelles]
« Soit $\{P_1, \ldots, P_n\}$ une partition d'un ensemble fini $E$. Calculer $\mathrm{Card}(E)$. » Réponse attendue : $\mathrm{Card}(E) = \sum_{i=1}^n \mathrm{Card}(P_i)$, **en citant** la propriété du cours sur les partitions.
:::

:::example[Utiliser toutes les hypothèses]
« Soient $E$ fini avec $\mathrm{Card}(E) \ge 2$ et $F$ non vide. Montrer que toute fonction constante $f : E \to F$ n'est pas injective. »

*Preuve.* Comme $\mathrm{Card}(E) \ge 2$, il existe $x, y \in E$ avec $x \neq y$. $f$ étant constante, $f(x) = f(y)$. Donc $f$ n'est pas injective. $\square$ — L'hypothèse $\mathrm{Card}(E) \ge 2$ fournit les deux éléments distincts ; « $F$ non vide » garantit qu'une fonction constante existe. Si une hypothèse ne sert à rien dans ta preuve, **méfie-toi** : soit elle est inutile, soit tu as raté quelque chose.
:::

:::example[Suivre la logique du problème]
« Montrer que $E$ et $F$ sont équipotents. Puis déterminer $\mathrm{Card}(E)$. » La seconde question **utilise** la première : $\mathrm{Card}(E) = \mathrm{Card}(F)$, et $F$ est (normalement) plus facile à compter.
:::

**Annonce ta méthode**, par exemple :

- « Nous allons prouver par récurrence simple que $\forall n \in \mathbb{N},\ P(n)$… »
- « Montrons par l'absurde que $Q(x)$ est vraie. Supposons que $\neg Q(x)$… »
- « Montrons que $E = F$ par double inclusion… »
- « Montrons que $A \Leftrightarrow B$ par double implication. Supposons $A$… »

:::exercise[Exercice du cours 2]
Soient $E$ un ensemble et $A, B \in \mathcal{P}(E)$. Montrer que $A \cap B = A \cap B^\complement$ si et seulement si $A = \emptyset$.
:::

:::hint[Indice]
Pour le sens direct, prends $x \in A$ et fais une disjonction de cas selon que $x \in B$ ou non : chaque cas mène à une contradiction.
:::

:::correction
Double implication.

- **($\Leftarrow$)** Si $A = \emptyset$, alors $A \cap B = \emptyset = A \cap B^\complement$.
- **($\Rightarrow$)** Supposons $A \cap B = A \cap B^\complement$ et montrons $A = \emptyset$ par l'absurde : soit $x \in A$.
  - Si $x \in B$ : $x \in A \cap B = A \cap B^\complement$, donc $x \notin B$. Contradiction.
  - Si $x \notin B$ : $x \in A \cap B^\complement = A \cap B$, donc $x \in B$. Contradiction.

  Aucun $x$ ne peut appartenir à $A$ : $A = \emptyset$. $\square$
:::

:::exercise[Exercice du cours 3]
Soient $E$ un ensemble et $A, B \in \mathcal{P}(E)$. Montrer que $(A \cap B^\complement) \cup (A^\complement \cap B) = B$ si et seulement si $A = \emptyset$.
:::

:::hint[Indice]
$(A \cap B^\complement) \cup (A^\complement \cap B)$ est l'ensemble des éléments qui sont dans **exactement un** des deux ensembles. Même méthode : $x \in A$, puis $x \in B$ ou non.
:::

:::correction
Notons $D = (A \cap B^\complement) \cup (A^\complement \cap B)$.

- **($\Leftarrow$)** Si $A = \emptyset$ : $A \cap B^\complement = \emptyset$ et $A^\complement \cap B = E \cap B = B$, donc $D = \emptyset \cup B = B$.
- **($\Rightarrow$)** Supposons $D = B$ et soit, par l'absurde, $x \in A$.
  - Si $x \in B$ : alors $x \in B = D$. Mais $x \notin A \cap B^\complement$ (car $x \in B$) et $x \notin A^\complement \cap B$ (car $x \in A$), donc $x \notin D$. Contradiction.
  - Si $x \notin B$ : alors $x \in A \cap B^\complement \subseteq D = B$, donc $x \in B$. Contradiction.

  Donc $A = \emptyset$. $\square$
:::

::item{id="ch13-ex2-ex3"}

## 6. Le mot de la fin : rédiger pour convaincre

:::key[Les règles d'une bonne copie]
- Le but d'une preuve est de **convaincre un lecteur informé**.
- **Annonce ton objectif** le plus tôt possible : « Nous allons prouver que $\forall x \in E,\ P(x)$. »
- **Nomme le motif** utilisé : « Prouvons cette propriété par contraposée. »
- Pour une récurrence, **précise sa nature** : simple, d'ordre $k$ ou forte. « Écrivons une preuve par récurrence d'ordre 3. »
- Tu peux **admettre les évidences** : « Évidemment, $A \cup A = A$. »
- Si tu ne sais pas prouver une étape, **admets-la explicitement** et continue : « Nous admettons qu'un tel $x$ existe. Prouvons maintenant son unicité. » Tu gagneras les points du reste.
:::
