---
title: Ch12 — Motifs avancés : analyse-synthèse et bijections d'examen
summary: Trouver une inconnue par analyse-synthèse, construire et rédiger une bijection d'examen (partiel 2021), méthode quand on est bloqué.
tags: [analyse-synthèse, bijections, annale, méthode]
minutes: 50
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- résoudre une équation (ou trouver un objet inconnu) par **analyse-synthèse**, sans oublier la synthèse ;
- construire une bijection entre deux ensembles d'ensembles en **typant** soigneusement entrée et sortie ;
- rédiger proprement une preuve d'équipotence suivie d'un **calcul de cardinal** ;
- appliquer une méthode systématique quand tu es **bloqué**.

## 2. Analyse et synthèse

Résoudre une équation, c'est prouver une équivalence « $f(x) = 0 \iff x \in S$ ». Mais au départ, on **ne connaît pas** $S$ : il faut d'abord trouver le bon candidat, puis prouver l'équivalence. Même situation dès qu'on cherche une valeur, une fonction, une relation inconnue.

:::pattern[Analyse-synthèse]
**But.** Étant donnée une propriété $P(x)$, trouver un ensemble $S$ tel que $P(x) \iff x \in S$.

- **Analyse.** Supposons que $P(x)$ est vraie… et déduisons-en que $x \in R$ pour un certain ensemble $R$ (des **conditions nécessaires**).
- Trouvons le bon $S \subseteq R$.
- **Synthèse.** Supposons $x \in R$…
  - si on peut en déduire $P(x)$, l'équivalence est vraie avec $S = R$ ;
  - sinon, il peut exister $y \in R$ tel que $P(y)$ est fausse : prouvons que si $x \in R \setminus S$ alors $\neg P(x)$, et que si $x \in S$ alors $P(x)$.
:::

:::warning[L'analyse seule ne suffit pas]
L'analyse ne donne que des **candidats** : elle prouve $P(x) \Rightarrow x \in R$, pas l'inverse. Élever au carré, multiplier par une expression qui peut être nulle… font apparaître de **fausses solutions**. La synthèse (vérifier chaque candidat) est **obligatoire**.
:::

:::exercise[Exercice du cours 1 — Une équation avec racine]
Résoudre dans $\mathbb{R}$ l'équation $x = \sqrt{2 - x}$.
:::

:::hint[Indice]
Analyse : si $x$ est solution, que dire du signe de $x$ ? Élève au carré. Synthèse : teste chaque candidat dans l'équation **de départ**.
:::

:::correction
**Analyse.** Soit $x \in \mathbb{R}$ tel que $x = \sqrt{2 - x}$. Alors $2 - x \ge 0$ (la racine existe) et $x \ge 0$ (une racine est positive). En élevant au carré : $x^2 = 2 - x$, soit $x^2 + x - 2 = 0$, c'est-à-dire $(x - 1)(x + 2) = 0$. Donc $x \in R = \{1, -2\}$.

**Synthèse.**
- $x = 1$ : $\sqrt{2 - 1} = 1 = x$. C'est une solution.
- $x = -2$ : $\sqrt{2 - (-2)} = \sqrt{4} = 2 \neq -2$. Ce n'est **pas** une solution (l'élévation au carré a perdu l'information $x \ge 0$).

**Conclusion.** L'ensemble des solutions est $S = \{1\}$. $\square$
:::

::item{id="ch12-analyse"}

## 3. Une bijection d'examen, pas à pas

:::exam[Partiel 2021]
Soient $E$ un ensemble de cardinal $n$ et $A \in \mathcal{P}(E)$ une partie de cardinal $k$. Soit $\mathcal{P}_A(E)$ l'ensemble des parties de $E$ qui **contiennent** $A$. Montrer que $\mathcal{P}_A(E)$ et $\mathcal{P}(E \setminus A)$ sont équipotents, puis déterminer le cardinal de $\mathcal{P}_A(E)$.
:::

### 3.1 Attention au typage

- $\mathcal{P}_A(E) = \{X \in \mathcal{P}(E) \mid A \subseteq X\}$ : ses éléments sont des **parties** $X$ de $E$, telles que $A \subseteq X \subseteq E$.
- $\mathcal{P}(E \setminus A)$ : ses éléments sont des parties $Y$ de $E \setminus A$, c'est-à-dire des parties de $E$ **disjointes** de $A$.
- Une bijection entre les deux prend donc **un ensemble** et rend **un ensemble**. Écrire « $f(x) = \ldots$ » avec un élément $x$ serait une erreur de type.

### 3.2 L'intuition

Une partie $X$ qui contient $A$ est entièrement déterminée par ce qu'elle contient **en plus** de $A$, c'est-à-dire $X \setminus A$, qui est une partie de $E \setminus A$. Inversement, à partir de ce « surplus » $Y$, on reconstruit $X = Y \cup A$.

- **Entrée** : $X \in \mathcal{P}_A(E)$. **Sortie** : $X \setminus A \in \mathcal{P}(E \setminus A)$.
- **Candidate réciproque** : $Y \in \mathcal{P}(E \setminus A) \mapsto Y \cup A \in \mathcal{P}_A(E)$.

### 3.3 La preuve

:::correction[Voir la preuve rédigée (ce qu'il faut écrire à l'examen)]
Définissons $\varphi : X \in \mathcal{P}_A(E) \mapsto X \setminus A$ et $\psi : Y \in \mathcal{P}(E \setminus A) \mapsto Y \cup A$.

**$\varphi$ est bien une fonction de $\mathcal{P}_A(E)$ dans $\mathcal{P}(E \setminus A)$.** Pour $X \in \mathcal{P}_A(E)$, $X \setminus A$ est défini de façon unique, et $X \setminus A \subseteq E \setminus A$ puisque $X \subseteq E$.

**$\psi$ est bien une fonction de $\mathcal{P}(E \setminus A)$ dans $\mathcal{P}_A(E)$.** Pour $Y \subseteq E \setminus A$, $Y \cup A \subseteq E$ (car $Y \subseteq E$ et $A \subseteq E$) et $A \subseteq Y \cup A$ : donc $Y \cup A \in \mathcal{P}_A(E)$.

**$\varphi \circ \psi = \mathrm{Id}$.** Soit $Y \in \mathcal{P}(E \setminus A)$. Alors $\varphi(\psi(Y)) = (Y \cup A) \setminus A = Y \setminus A = Y$, car $Y \cap A = \emptyset$ (puisque $Y \subseteq E \setminus A$).

**$\psi \circ \varphi = \mathrm{Id}$.** Soit $X \in \mathcal{P}_A(E)$. Alors $\psi(\varphi(X)) = (X \setminus A) \cup A = X \cup A = X$, car $A \subseteq X$.

Donc $\varphi$ est une bijection, de réciproque $\psi$ : $\mathcal{P}_A(E)$ et $\mathcal{P}(E \setminus A)$ sont équipotents.

**Cardinal.** Comme $A \subseteq E$, $\mathrm{Card}(E \setminus A) = n - k$ (chapitre 11). Donc
$$\mathrm{Card}(\mathcal{P}_A(E)) = \mathrm{Card}(\mathcal{P}(E \setminus A)) = 2^{n-k}. \qquad \square$$
:::

:::method[Ce qu'on attend à l'examen]
1. **Définir** explicitement les deux applications (et leurs ensembles de départ et d'arrivée).
2. **Vérifier qu'elles sont bien définies** : l'image tombe dans le bon ensemble. C'est l'étape la plus souvent oubliée.
3. Prouver $\varphi \circ \psi = \mathrm{Id}$ **et** $\psi \circ \varphi = \mathrm{Id}$, en citant l'hypothèse utilisée ($A \subseteq X$, $Y \cap A = \emptyset$).
4. **Conclure** sur l'équipotence, puis **calculer** le cardinal en citant les résultats du cours.
:::

::item{id="ch12-parties-contenant"}

:::exercise[Exercice du cours 2 — Bijections vers $\{1, \ldots, n\}$]
Soit $E$ un ensemble de cardinal $n$, $S_n$ l'ensemble des bijections $\{1, \ldots, n\} \to \{1, \ldots, n\}$, et $\mathcal{F}$ l'ensemble des bijections $E \to \{1, \ldots, n\}$. Esquisser une preuve que $\mathcal{F}$ et $S_n$ sont équipotents. Comment en déduire $\mathrm{Card}(\mathcal{F})$ ?
:::

:::hint[Indice]
Fixe une fois pour toutes une bijection $\varphi : \{1, \ldots, n\} \to E$ (elle existe car $\mathrm{Card}(E) = n$). Que dire de $h \circ \varphi$ quand $h \in \mathcal{F}$ ?
:::

:::correction
Fixons une bijection $\varphi : \{1, \ldots, n\} \to E$ (définition du cardinal ; si $n = 0$ les deux ensembles sont réduits à la fonction vide).

- $\Phi : h \in \mathcal{F} \mapsto h \circ \varphi$ : composée de deux bijections $\{1, \ldots, n\} \to E \to \{1, \ldots, n\}$, c'est bien un élément de $S_n$.
- $\Psi : \sigma \in S_n \mapsto \sigma \circ \varphi^{-1}$ : bijection $E \to \{1, \ldots, n\}$, donc un élément de $\mathcal{F}$.
- $\Phi(\Psi(\sigma)) = \sigma \circ \varphi^{-1} \circ \varphi = \sigma$ et $\Psi(\Phi(h)) = h \circ \varphi \circ \varphi^{-1} = h$.

Donc $\mathcal{F}$ et $S_n$ sont équipotents, et $\mathrm{Card}(\mathcal{F}) = \mathrm{Card}(S_n) = n!$ : pour construire une bijection de $\{1, \ldots, n\}$ dans lui-même, on choisit l'image de $1$ ($n$ choix), puis celle de $2$ ($n - 1$ choix restants), etc. $\square$
:::

## 4. Bloqué ? La méthode

:::method[Que faire quand on ne voit rien]
1. **Détermine le type des objets.** Entiers, ensembles, fonctions, ensembles d'ensembles, ensembles de fonctions ? Relis les définitions usuelles si besoin.
2. **Comprends ce qu'on te demande.** Résoudre une équation ? Prouver une équivalence ? Trouver une bijection ? Compter ?
3. **Esquisse une première preuve.** Le but impose souvent un premier motif évident, qu'on n'a même pas besoin de deviner (double implication, double inclusion, « soit… »).
4. **Ensuite seulement, travaille.** Cherche les liens entre les objets, des sous-buts plus simples, des cas particuliers pour te faire une idée.
:::

## 5. Exercices supplémentaires

:::exercise[Entraînement 1 — Encore une racine]
Résoudre dans $\mathbb{R}$ : $\sqrt{x + 3} = x + 1$.
:::

:::correction
**Analyse.** Si $\sqrt{x+3} = x + 1$, alors $x + 1 \ge 0$ et $x + 3 = (x+1)^2 = x^2 + 2x + 1$, donc $x^2 + x - 2 = 0$, soit $x \in \{1, -2\}$. **Synthèse.** $x = 1$ : $\sqrt{4} = 2 = 1 + 1$, solution. $x = -2$ : $\sqrt{1} = 1 \neq -1$, non. **Solution :** $S = \{1\}$. $\square$
:::

:::exercise[Entraînement 2 — Une équation fonctionnelle]
Trouver toutes les fonctions $f : \mathbb{R} \to \mathbb{R}$ telles que $\forall x \in \mathbb{R},\ f(x) + 2f(-x) = x$.
:::

:::correction
**Analyse.** Soit $f$ une solution et $x \in \mathbb{R}$. On applique l'hypothèse en $x$ et en $-x$ :
$$f(x) + 2f(-x) = x \qquad\text{et}\qquad f(-x) + 2f(x) = -x.$$
En multipliant la seconde par 2 et en soustrayant la première : $4f(x) - f(x) = -2x - x$, donc $f(x) = -x$. Le seul candidat est $f : x \mapsto -x$.

**Synthèse.** Pour $f(x) = -x$ : $f(x) + 2f(-x) = -x + 2x = x$. Convient.

**Conclusion.** L'unique solution est $x \mapsto -x$. $\square$
:::

## 6. Fiche récapitulative

:::key[L'essentiel]
- **Analyse** : « si $x$ est solution, alors $x \in R$ » (conditions nécessaires). **Synthèse** : vérifier les candidats dans l'énoncé **de départ**.
- Une bijection d'examen : définir $\varphi$ et $\psi$, vérifier qu'elles sont **bien définies**, prouver les **deux** compositions, conclure, puis compter.
- $\mathrm{Card}(\{X \mid A \subseteq X \subseteq E\}) = 2^{n-k}$ ; $\mathrm{Card}(S_n) = n!$.
- Bloqué : types → but → motif évident → seulement ensuite les calculs.
:::
