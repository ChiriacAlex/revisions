---
title: Examen blanc FOLO (2 h)
summary: Un sujet complet dans l'esprit de l'examen final — logique, ensembles, fonctions, récurrence, dénombrement — avec barème et corrigé détaillé.
kind: exam
tags: [examen, entraînement, barème]
minutes: 120
---

:::warning[Conditions d'examen]
Prévois **2 heures**, sans document, sans calculatrice. Rédige sur papier comme le jour J (motif annoncé, hypothèses, conclusion). N'ouvre les corrigés qu'**après** avoir terminé tout le sujet, puis note-toi avec le barème. Les quiz en fin de page permettent de vérifier rapidement les réponses numériques.
:::

## Exercice 1 — Logique (4 points)

1. *(1,5 pt)* Soit $f : \mathbb{R} \to \mathbb{R}$. On dit que $f$ est continue en $0$ si
$$\forall \varepsilon > 0,\ \exists \delta > 0,\ \forall x \in \mathbb{R},\ |x| < \delta \Rightarrow |f(x) - f(0)| < \varepsilon.$$
Écrire la négation de cette propriété, puis la traduire en français.
2. *(1,5 pt)* Montrer que pour toutes propositions $P$, $Q$, $R$ : $\big((P \Rightarrow Q) \wedge (Q \Rightarrow R)\big) \Rightarrow (P \Rightarrow R)$.
3. *(1 pt)* La proposition $\big((P \vee Q) \wedge \neg P\big) \Rightarrow Q$ est-elle toujours vraie ? Et $\big((P \Rightarrow Q) \wedge Q\big) \Rightarrow P$ ?

:::correction[Corrigé de l'exercice 1]
**1.** On échange les quantificateurs et on nie le cœur ($\neg(A \Rightarrow B) \iff A \wedge \neg B$), sans toucher aux domaines :
$$\exists \varepsilon > 0,\ \forall \delta > 0,\ \exists x \in \mathbb{R},\ |x| < \delta \wedge |f(x) - f(0)| \ge \varepsilon.$$
En français : il existe un écart $\varepsilon$ tel que, aussi près de $0$ qu'on regarde, on trouve un point dont l'image s'écarte d'au moins $\varepsilon$ de $f(0)$. *(0,5 pt pour l'échange des quantificateurs, 0,5 pt pour la négation de l'implication, 0,5 pt pour la phrase.)*

**2.** Supposons $(P \Rightarrow Q) \wedge (Q \Rightarrow R)$ et montrons $P \Rightarrow R$. Supposons $P$. Par $P \Rightarrow Q$, $Q$ est vraie ; puis par $Q \Rightarrow R$, $R$ est vraie. Donc $P \Rightarrow R$. $\square$ *(Motif annoncé : 0,5 ; deux modus ponens : 1.)* Une table de vérité à 8 lignes, complète et lisible, est aussi acceptée.

**3.** La première est **toujours vraie** (syllogisme disjonctif) : si $P \vee Q$ et $\neg P$, alors comme $P$ est fausse, c'est $Q$ qui est vraie. La seconde est **fausse** en général : $P$ fausse et $Q$ vraie rendent l'hypothèse vraie et la conclusion fausse (c'est l'erreur « affirmer le conséquent »).
:::

## Exercice 2 — Ensembles (4 points)

Soit $E$ un ensemble et $A, B, C \in \mathcal{P}(E)$.

1. *(2 pts)* Montrer que $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$.
2. *(2 pts)* Montrer que $A \cap B = A \cup B$ si et seulement si $A = B$.

:::correction[Corrigé de l'exercice 2]
**1.** Pour tout $x$ :
$$x \in A \setminus (B \cup C) \iff x \in A \wedge \neg(x \in B \vee x \in C) \iff x \in A \wedge x \notin B \wedge x \notin C$$
$$\iff (x \in A \wedge x \notin B) \wedge (x \in A \wedge x \notin C) \iff x \in (A \setminus B) \cap (A \setminus C).$$
(De Morgan, puis $P \iff P \wedge P$.) Chaque étape est une équivalence, donc l'égalité est prouvée. Une double inclusion rédigée est aussi correcte. $\square$

**2.** Double implication.
- **($\Leftarrow$)** Si $A = B$, alors $A \cap B = A \cap A = A = A \cup A = A \cup B$.
- **($\Rightarrow$)** Supposons $A \cap B = A \cup B$. Montrons $A \subseteq B$ : soit $x \in A$ ; alors $x \in A \cup B = A \cap B$, donc $x \in B$. Par symétrie des rôles de $A$ et $B$, $B \subseteq A$. Donc $A = B$. $\square$

*(Barème : 1 pt par sens ; la symétrie doit être justifiée ou le second sens écrit.)*
:::

## Exercice 3 — Fonctions (4 points)

1. *(2 pts)* Soit $f : \mathbb{N} \to \mathbb{N}$ définie par $f(n) = n + 1$ si $n$ est pair et $f(n) = n - 1$ si $n$ est impair. Montrer que $f$ est une bijection et déterminer $f^{-1}$.
2. *(2 pts)* Soit $A \in \mathcal{P}(E)$ et $g : X \in \mathcal{P}(E) \mapsto X \cup A \in \mathcal{P}(E)$. Montrer que $g$ est injective si et seulement si $A = \emptyset$. Est-elle surjective quand $A \neq \emptyset$ ?

:::correction[Corrigé de l'exercice 3]
**1.** $f$ est bien une fonction de $\mathbb{N}$ dans $\mathbb{N}$ (si $n$ est impair, $n \ge 1$ donc $n - 1 \in \mathbb{N}$). Montrons que $f \circ f = \mathrm{Id}_\mathbb{N}$ :
- si $n$ est pair, $f(n) = n + 1$ est impair, donc $f(f(n)) = n + 1 - 1 = n$ ;
- si $n$ est impair, $f(n) = n - 1$ est pair, donc $f(f(n)) = n - 1 + 1 = n$.

Donc $f$ est inversible, de réciproque elle-même : $f$ est une bijection et $f^{-1} = f$ (elle échange $2k$ et $2k + 1$). $\square$

**2.**
- **($\Leftarrow$)** Si $A = \emptyset$, $g(X) = X$ : $g = \mathrm{Id}$, injective.
- **($\Rightarrow$)** Par contraposée : supposons $A \neq \emptyset$ et soit $a \in A$. Alors $g(\emptyset) = A$ et $g(\{a\}) = \{a\} \cup A = A$, avec $\emptyset \neq \{a\}$ : $g$ n'est pas injective.

Si $A \neq \emptyset$, $g$ n'est **pas surjective** : toute image $X \cup A$ contient $A$, donc $\emptyset$ (qui ne contient pas $a$) n'a pas d'antécédent. $\square$
:::

## Exercice 4 — Récurrences (4 points)

1. *(1 pt)* Montrer que $\forall n \in \mathbb{N},\ \sum_{k=0}^{n} 2^k = 2^{n+1} - 1$.
2. *(1,5 pt)* Soit $(u_n)$ définie par $u_0 = 2$ et $u_{n+1} = 2u_n - 1$. Conjecturer puis démontrer une formule pour $u_n$.
3. *(1,5 pt)* Montrer que tout entier $n \ge 12$ s'écrit $n = 4a + 5b$ avec $a, b \in \mathbb{N}$. Préciser le type de récurrence utilisé.

:::correction[Corrigé de l'exercice 4]
**1.** Récurrence simple. $n = 0$ : $2^0 = 1 = 2^1 - 1$. Si $\sum_{k=0}^{n} 2^k = 2^{n+1} - 1$, alors $\sum_{k=0}^{n+1} 2^k = 2^{n+1} - 1 + 2^{n+1} = 2^{n+2} - 1$. $\square$

**2.** $u_0 = 2$, $u_1 = 3$, $u_2 = 5$, $u_3 = 9$ : on conjecture $u_n = 2^n + 1$. Récurrence simple : $u_0 = 2 = 2^0 + 1$ ; si $u_n = 2^n + 1$, alors $u_{n+1} = 2(2^n + 1) - 1 = 2^{n+1} + 1$. $\square$ *(0,5 pt pour la conjecture, 1 pt pour la preuve.)*

**3.** **Récurrence d'ordre 4** : $P(n)$ : « $\exists a, b \in \mathbb{N},\ n = 4a + 5b$ ».
- Initialisation : $12 = 4 \cdot 3$, $13 = 4 \cdot 2 + 5$, $14 = 4 + 5 \cdot 2$, $15 = 5 \cdot 3$.
- Hérédité : soit $n \ge 12$ tel que $P(n), \ldots, P(n+3)$. D'après $P(n)$, $n = 4a + 5b$, donc $n + 4 = 4(a + 1) + 5b$ : $P(n+4)$.

Par récurrence d'ordre 4, $\forall n \ge 12,\ P(n)$. $\square$ (Remarque : $11$ ne s'écrit pas ainsi, d'où le rang 12.)
:::

## Exercice 5 — Dénombrement (4 points)

Soit $E = \{1, \ldots, n\}$ avec $n \ge 1$.

1. *(1,5 pt)* Combien y a-t-il de couples $(X, Y) \in \mathcal{P}(E)^2$ tels que $X \cap Y = \emptyset$ ? Justifier par une bijection.
2. *(1 pt)* Combien y a-t-il de parties de $E$ ayant **au moins deux** éléments ?
3. *(1,5 pt)* Dans une promo de 12 étudiants, dont Alice et Bob, on forme un comité de 4 personnes contenant **au moins un** des deux. Combien de comités possibles ?

:::correction[Corrigé de l'exercice 5]
**1.** Pour un couple $(X, Y)$ de parties disjointes, chaque $i \in E$ est dans exactement une situation : $i \in X$, $i \in Y$, ou $i$ dans aucune des deux. L'application qui envoie $(X, Y)$ sur le mot $(c_1, \ldots, c_n) \in \{0, 1, 2\}^n$ ($c_i = 1$ si $i \in X$, $2$ si $i \in Y$, $0$ sinon) est une bijection (réciproque : $X = \{i \mid c_i = 1\}$, $Y = \{i \mid c_i = 2\}$, disjointes par construction). Il y a donc $3^n$ couples.

**2.** Complémentaire : il y a $2^n$ parties, dont $1$ de taille $0$ et $n$ de taille $1$ : $2^n - n - 1$.

**3.** Complémentaire : $\binom{12}{4} = 495$ comités en tout, dont $\binom{10}{4} = 210$ sans Alice ni Bob. Donc $495 - 210 = 285$. Vérification par partition : Alice sans Bob $\binom{10}{3} = 120$, Bob sans Alice $120$, les deux $\binom{10}{2} = 45$ : $120 + 120 + 45 = 285$.
:::

## Vérifications rapides

::item{id="exam-logique"}

::item{id="exam-denombrement"}

::item{id="exam-comite"}

:::key[Après l'examen blanc]
- Moins de 10/20 : reprends les chapitres correspondants **et** le recueil des motifs avant de refaire le sujet dans une semaine.
- Entre 10 et 15 : relis tes copies avec le corrigé : les points perdus viennent souvent de la **rédaction** (motif non annoncé, sens oublié, initialisation absente).
- Plus de 15 : entraîne-toi sur les exercices « Extra » des TD et sur les annales des chapitres 7 et 12.
:::
