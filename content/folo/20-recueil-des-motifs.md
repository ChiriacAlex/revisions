---
title: Recueil des motifs de preuve
summary: Tous les motifs du cours (le « Proof Pattern Compendium ») sur une page, avec un entraînement « quel motif ? » et les formules à connaître.
kind: sheet
tags: [fiche, motifs de preuve, examen]
minutes: 25
---

## Comment utiliser cette fiche

Chaque motif donne le **squelette** de la preuve : ce que tu écris **avant** de chercher les calculs. Repère la forme du but (et des hypothèses), choisis le motif, écris les sous-buts, puis remplis.

## 1. Connecteurs logiques

:::pattern[1 · $\Rightarrow$ (implication directe)]
**But.** $P \Rightarrow Q$. — Si $P$ est vraie… alors $Q$ est vraie.
:::

:::pattern[2 · $\wedge$ en conclusion]
**But.** $P \Rightarrow (Q \wedge R)$. — Supposons $P$. **Sous-but 1** : $Q$. **Sous-but 2** : $R$.
:::

:::pattern[3 · $\wedge$ en hypothèse]
**But.** $(P \wedge Q) \Rightarrow R$. — Si $P$ est vraie… et $Q$ est vraie… alors $R$ est vraie.
:::

:::pattern[4 · $\vee$ en conclusion]
**But.** $P \Rightarrow (Q \vee R)$. — Supposons $P$ vraie et $Q$ fausse… alors $R$ doit être vraie.
:::

:::pattern[5 · $\vee$ en hypothèse]
**But.** $(P \vee Q) \Rightarrow R$. — **Sous-but 1** : $P \Rightarrow R$. **Sous-but 2** : $Q \Rightarrow R$.
:::

:::pattern[6 · $\Leftrightarrow$ (double implication)]
**But.** $P \Leftrightarrow Q$. — **Sous-but 1** : $P \Rightarrow Q$. **Sous-but 2** : $Q \Rightarrow P$.
:::

## 2. Motifs fondés sur la négation

:::pattern[7 · Par l'absurde]
**But.** $P \Rightarrow Q$. — Si $P$ est vraie, supposons $\neg Q$… prouvons une chose qui contredit $P$ ou une propriété vraie. Donc $Q$ ne peut pas être fausse.
:::

:::pattern[8 · Par contraposée]
**But.** $P \Rightarrow Q$. — But équivalent : $\neg Q \Rightarrow \neg P$. Si $\neg Q$… alors $\neg P$.
:::

:::pattern[9 · Disjonction de cas]
**But.** $P \Rightarrow Q$. — Soit une proposition $R$. **Sous-but 1** : $(P \wedge R) \Rightarrow Q$. **Sous-but 2** : $(P \wedge \neg R) \Rightarrow Q$.
:::

## 3. Ensembles

:::pattern[10 · Inclusion simple]
**But.** $A \subseteq B$. — Soit $x \in A$… alors $x \in B$.
:::

:::pattern[11 · Double inclusion]
**But.** $A = B$. — **Sous-but 1** : $A \subseteq B$. **Sous-but 2** : $B \subseteq A$.
:::

:::pattern[20 · Ensemble vide]
**But.** $E = \emptyset$. — Supposons $E \neq \emptyset$ ; soit $x \in E$… prouvons une chose manifestement fausse. Par l'absurde, $E = \emptyset$.
:::

:::pattern[30 · Partition]
**But.** $\mathcal{P}$ est une partition de $E$. — **1** : $\forall X \in \mathcal{P},\ X \subseteq E \wedge X \neq \emptyset$. **2** : $X \neq Y \Rightarrow X \cap Y = \emptyset$ (par contraposée : un $x \in X \cap Y$ donne $X = Y$). **3** : $\forall x \in E,\ \exists X \in \mathcal{P},\ x \in X$.
:::

## 4. Quantificateurs

:::pattern[12–14 · $\forall$ (but, conclusion, hypothèse)]
- **But** $\forall x \in E,\ P(x)$ : soit $x \in E$ (quelconque)… alors $P(x)$.
- **En conclusion** $P \Rightarrow \forall x,\ Q(x)$ : supposons $P$ ; soit $x \in E$… alors $Q(x)$.
- **En hypothèse** $(\forall x,\ P(x)) \Rightarrow Q$ : applique $P$ à des valeurs **bien choisies** $x_0, x_1, \ldots$
:::

:::pattern[15–18 · $\exists$ (but, hypothèse, conclusion)]
- **But** $\exists x \in E,\ P(x)$ : exhibe un $x_0$ particulier… et vérifie $P(x_0)$.
- **En hypothèse** $(\exists x,\ P(x)) \Rightarrow Q$ : soit $x_0$ tel que $P(x_0)$ (on ne le choisit pas)… alors $Q$.
- **En conclusion** $P \Rightarrow \exists x,\ Q(x)$ : supposons $P$ ; exhibe $x_0$ ; prouve $Q(x_0)$.
:::

:::pattern[19 · $\exists!$]
**But.** $\exists! x \in E,\ P(x)$. — **Existence** : $\exists x,\ P(x)$. **Unicité** : $\forall x_1, x_2,\ P(x_1) \wedge P(x_2) \Rightarrow x_1 = x_2$.
:::

## 5. Fonctions

:::pattern[21 · Fonction]
**But.** La relation $f$ est une fonction $E \to F$. — **Existence** : soit $x \in E$… $\exists y \in F,\ (x, y) \in f$. **Unicité** : soient $(x, y), (x, z) \in f$… alors $y = z$.
:::

:::pattern[22 · Injectivité]
**But.** $f$ injective. — Soient $x, y \in \mathrm{Dom}(f)$ ; supposons $f(x) = f(y)$… alors $x = y$.
:::

:::pattern[23 · Surjectivité]
**But.** $f$ surjective. — Soit $y \in F$… exhibe $x$ tel que $y = f(x)$.
:::

:::pattern[24 · Bijectivité]
**But.** $f$ bijective. — **Sous-but 1** : injective. **Sous-but 2** : surjective.
:::

:::pattern[25 · Inversibilité]
**But.** $f$ bijective. — Introduis une candidate $g \subseteq F \times E$, montre que c'est une fonction $F \to E$, puis $f \circ g = \mathrm{Id}_F$ (soit $y \in F$, $f(g(y)) = y$) et $g \circ f = \mathrm{Id}_E$ (soit $x \in E$, $g(f(x)) = x$).
:::

:::pattern[29 · Équipotence]
**But.** $E$ et $F$ équipotents. — Introduis une relation candidate $f$. **1** : c'est une fonction $E \to F$ **bien définie**. **2** : c'est une bijection (définition, ou réciproque explicite).
:::

## 6. Récurrences

:::pattern[26 · Récurrence simple]
**But.** $\forall n \ge n_0,\ P(n)$. — **Initialisation** : $P(n_0)$. **Hérédité** : soit $n \ge n_0$ tel que $P(n)$… alors $P(n+1)$.
:::

:::pattern[27 · Récurrence d'ordre $k$]
**Initialisation** : $P(n_0), \ldots, P(n_0 + k - 1)$. **Hérédité** : soit $n \ge n_0$ tel que $P(n), \ldots, P(n+k-1)$… alors $P(n + k)$.
:::

:::pattern[28 · Récurrence forte]
**Initialisation** : $P(n_0)$. **Hérédité** : soit $n \ge n_0$ tel que $\forall k \in \{n_0, \ldots, n\},\ P(k)$… alors $P(n+1)$.
:::

## 7. Analyse-synthèse

:::pattern[31 · Analyse et synthèse]
**But.** Trouver $S$ tel que $P(x) \iff x \in S$. — **Analyse** : si $P(x)$, alors $x \in R$. Choisis $S \subseteq R$. **Synthèse** : si $x \in R \setminus S$ alors $\neg P(x)$ ; si $x \in S$ alors $P(x)$.
:::

## 8. Entraînement : quel motif ?

::item{id="motif-1"}

::item{id="motif-2"}

::item{id="motif-3"}

::item{id="motif-4"}

::item{id="motif-5"}

## 9. Formules à connaître par cœur

| Logique | Ensembles |
|---|---|
| $\neg(P \wedge Q) \iff \neg P \vee \neg Q$ | $(A \cap B)^\complement = A^\complement \cup B^\complement$ |
| $\neg(P \vee Q) \iff \neg P \wedge \neg Q$ | $(A \cup B)^\complement = A^\complement \cap B^\complement$ |
| $P \Rightarrow Q \iff \neg P \vee Q \iff \neg Q \Rightarrow \neg P$ | $A \subseteq B \iff A \cap B^\complement = \emptyset$ |
| $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$ | $A \setminus B = A \cap B^\complement$ |
| $\neg(\forall x,\ P(x)) \iff \exists x,\ \neg P(x)$ | $\forall x \in \emptyset$ : vrai ; $\exists x \in \emptyset$ : faux |
| $\neg(\exists x,\ P(x)) \iff \forall x,\ \neg P(x)$ | $\mathrm{Card}(\mathcal{P}(E)) = 2^n$ ; $\mathrm{Card}(\mathcal{P}_k(E)) = \binom{n}{k}$ |
