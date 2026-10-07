---
title: Ch1 bis — Intégration des fractions rationnelles
summary: "Décomposition en éléments simples (partie entière, pôles simples et multiples, facteurs irréductibles), intégration des éléments de 1ʳᵉ et 2ᵈᵉ espèce, forme canonique et arctangente, récurrence des Iₙ — avec les exemples du poly recalculés."
tags: [chapitre 1, fractions rationnelles, éléments simples, arctan]
minutes: 100
---

## 1. Objectifs

Intégrer une fraction $F(x) = \frac{P(x)}{Q(x)}$ ($P$, $Q$ polynômes) se fait **toujours** de la même façon :

1. **division euclidienne** si $\deg P \ge \deg Q$ ;
2. **décomposition en éléments simples** ;
3. intégration de chaque élément simple (trois cas à connaître).

:::intuition[Pourquoi ça marche toujours]
Une fraction compliquée comme $\frac{5x - 1}{x^2 - x - 2}$ est la somme de fractions **très simples** : $\frac{2}{x + 1} + \frac{3}{x - 2}$. Or on sait intégrer $\frac{1}{x - a}$ (un logarithme). C'est le même principe que décomposer un nombre en facteurs premiers.
:::

:::example[Le premier exemple]
$\frac{5x - 1}{x^2 - x - 2} = \frac{5x - 1}{(x - 2)(x + 1)} = \frac{2}{x + 1} + \frac{3}{x - 2}$, donc
$$\int \frac{5x - 1}{x^2 - x - 2}\,dx = 2\ln|x + 1| + 3\ln|x - 2| + C = \ln\left[(x + 1)^2|x - 2|^3\right] + C.$$
:::

## 2. La décomposition en éléments simples

:::definition[Fraction irréductible, pôles]
- $F = \frac{P}{Q}$ est **irréductible** si $P$ et $Q$ n'ont aucune racine (réelle ou complexe) commune. Sinon on simplifie d'abord.
- Un **pôle** est une racine de $Q$ ; il est **d'ordre $n$** si c'est une racine de multiplicité $n$ de $Q$.
:::

:::method[Les cinq étapes]
1. **Simplifier** la fraction si $P$ et $Q$ ont une racine commune.
2. **Division euclidienne** : $P = E \cdot Q + R$ avec $\deg R < \deg Q$, d'où $F = E + \frac{R}{Q}$. La **partie entière** $E$ est nulle si $\deg P < \deg Q$.
3. **Factoriser** $Q$ sur $\mathbb{R}$ en facteurs de degré 1 et facteurs de degré 2 **sans racine réelle** ($\Delta < 0$) :
$Q(x) = (x - a_1)^{\alpha_1}\cdots(x^2 + p_1 x + q_1)^{\beta_1}\cdots$
4. **Écrire la forme** de la décomposition :
   - pour chaque $(x - a)^\alpha$ : $\frac{A_\alpha}{(x - a)^\alpha} + \cdots + \frac{A_1}{x - a}$ (éléments de **1ʳᵉ espèce**) ;
   - pour chaque $(x^2 + px + q)^\beta$ : $\frac{B_\beta x + C_\beta}{(x^2 + px + q)^\beta} + \cdots + \frac{B_1 x + C_1}{x^2 + px + q}$ (éléments de **2ᵈᵉ espèce**).
5. **Calculer les coefficients** (§ 3).
:::

:::example[Exemple de forme (sans calcul)]
$\frac{x^8 + 2x^5 + 8x^4 - 3x + 1}{(x^2 + x + 1)(x - 1)^3(x + 1)} = E(x) + \frac{A_3}{(x - 1)^3} + \frac{A_2}{(x - 1)^2} + \frac{A_1}{x - 1} + \frac{A'_1}{x + 1} + \frac{Bx + C}{x^2 + x + 1}$, avec $E$ de degré $8 - 6 = 2$.
:::

## 3. Calcul des coefficients

:::method[Méthode 1 — identification]
On réduit au même dénominateur et on identifie les coefficients des numérateurs. Exemple :
$$\frac{x^2 - 3}{(x - 1)^2(x + 1)} = \frac{A}{(x - 1)^2} + \frac{B}{x - 1} + \frac{C}{x + 1}$$
donne $(B + C)x^2 + (A - 2C)x + (A - B + C) = x^2 - 3$, soit $B + C = 1$, $A - 2C = 0$, $A - B + C = -3$, d'où $(A, B, C) = \left(-1, \frac{3}{2}, -\frac{1}{2}\right)$.
:::

:::method[Méthode 2 — pôle simple : multiplier et évaluer]
Si $a$ est un pôle simple, $F(x) = \frac{A}{x - a} + G(x)$ avec $G$ sans pôle en $a$, et
$$A = \lim_{x \to a}(x - a)F(x) = \frac{P(a)}{Q'(a)}.$$
En pratique : on « cache » le facteur $(x - a)$ et on remplace $x$ par $a$ dans le reste.
:::

:::example[Trois pôles simples]
$\frac{x^2}{(x - 1)(x + 2)(x + 3)} = \frac{A}{x - 1} + \frac{B}{x + 2} + \frac{C}{x + 3}$ :
$A = \frac{1}{3 \times 4} = \frac{1}{12}$, $\quad B = \frac{4}{(-3)(1)} = -\frac{4}{3}$, $\quad C = \frac{9}{(-4)(-1)} = \frac{9}{4}$.
:::

:::method[Méthode 3 — pôle multiple d'ordre n]
Si $F(x) = \frac{P(x)}{(x - a)^n R(x)}$ avec $R(a) \ne 0$, les coefficients de $\frac{A_0}{(x - a)^n} + \frac{A_1}{(x - a)^{n-1}} + \cdots$ sont
$$A_j = \frac{1}{j!}\lim_{x \to a}\left[\frac{P(x)}{R(x)}\right]^{(j)} \qquad (A_0 = \text{la valeur}, A_1 = \text{la dérivée}, A_2 = \text{la moitié de la dérivée seconde}…).$$
**Astuces de contrôle** : $\lim_{x \to +\infty} x F(x)$ donne la somme des coefficients des $\frac{1}{x - a}$ et des $B$ ; une valeur particulière ($x = 0$) donne une dernière équation.
:::

:::example[Pôle triple]
$\frac{4x^3 + 16x^2 + 23x + 13}{(x + 1)^3(x + 2)} = \frac{A_0}{(x + 1)^3} + \frac{A_1}{(x + 1)^2} + \frac{A_2}{x + 1} + \frac{B}{x + 2}$, avec $g(x) = \frac{4x^3 + 16x^2 + 23x + 13}{x + 2}$ :
- $A_0 = g(-1) = 2$ ; $\quad A_1 = g'(-1) = 1$ ; $\quad A_2 = \frac{1}{2}g''(-1) = \frac{6}{2} = 3$ ;
- $B = \lim_{x \to -2}(x + 2)F(x) = \frac{-32 + 64 - 46 + 13}{(-1)^3} = 1$.

**Contrôle** : $A_2 + B = 4$ = coefficient dominant du numérateur (limite de $xF(x)$). ✓
$$F(x) = \frac{2}{(x + 1)^3} + \frac{1}{(x + 1)^2} + \frac{3}{x + 1} + \frac{1}{x + 2}.$$
:::

:::warning[Erreur dans le poly (exemple 19)]
Le poly obtient bien $g''(-1) = 6$ mais oublie le facteur $\frac{1}{2!}$ et écrit $A_2 = 6$. Le contrôle $A_2 + B = 4$ montre l'erreur : $6 + 1 \ne 4$. La bonne valeur est $A_2 = 3$.
:::

:::example[Pôle triple et facteur irréductible]
$g(x) = \frac{1}{(x - 1)^3(x^2 + 2x + 5)} = \frac{A_0}{(x - 1)^3} + \frac{A_1}{(x - 1)^2} + \frac{A_2}{x - 1} + \frac{Bx + C}{x^2 + 2x + 5}$.

Avec $h(x) = \frac{1}{x^2 + 2x + 5}$ : $A_0 = h(1) = \frac{1}{8}$, $A_1 = h'(1) = -\frac{2 \cdot 1 + 2}{8^2} = -\frac{1}{16}$, $A_2 = \frac{1}{2}h''(1) = \frac{1}{64}$.
Puis $\lim_{x \to +\infty} x\,g(x) = 0$ donne $A_2 + B = 0$, donc $B = -\frac{1}{64}$ ; et $g(0) = -\frac{1}{5}$ donne $-A_0 + A_1 - A_2 + \frac{C}{5} = -\frac{1}{5}$, donc $C = \frac{1}{64}$ :
$$g(x) = \frac{1}{8(x - 1)^3} - \frac{1}{16(x - 1)^2} + \frac{1}{64(x - 1)} + \frac{-x + 1}{64(x^2 + 2x + 5)}.$$
:::

:::warning[Erreur dans le poly (exemple 20)]
Le poly annonce $B = -\frac{1}{16}$ et $C = \frac{1}{4}$, ce qui contredit sa propre équation $A_2 + B = 0$ (puisque $A_2 = \frac{1}{64}$). Les bonnes valeurs sont $B = -\frac{1}{64}$ et $C = \frac{1}{64}$.
:::

:::example[Décompositions du poly (exemple 21), vérifiées]
- $\frac{x^9 + x}{(x - 1)^3(x^2 + 1)^2(x + 2)} = x + 1 + \frac{1}{6(x - 1)^3} + \frac{4}{9(x - 1)^2} + \frac{41}{27(x - 1)} + \frac{514}{675(x + 2)} + \frac{x + 3}{10(x^2 + 1)^2} - \frac{7x + 11}{25(x^2 + 1)}$
- $\frac{x^6 + 2}{(x^2 + 1)(x^2 - 16)} = x^2 + 15 - \frac{1}{17(x^2 + 1)} + \frac{2049}{68(x - 4)} - \frac{2049}{68(x + 4)}$
- $\frac{x^5 + 2x - 1}{(x - 1)^3(x + 1)} = x + 2 + \frac{1}{(x - 1)^3} + \frac{3}{(x - 1)^2} + \frac{7}{2(x - 1)} + \frac{1}{2(x + 1)}$
- $\frac{x + 1}{(x^2 + 1)^2(x^2 + x + 1)^2} = -\frac{x + 1}{(x^2 + 1)^2} - \frac{3x - 1}{x^2 + 1} - \frac{1}{(x^2 + x + 1)^2} + \frac{3x + 2}{x^2 + x + 1}$
- $\frac{x + 1}{x(x^2 + 1)^2} = \frac{1}{x} - \frac{x - 1}{(x^2 + 1)^2} - \frac{x}{x^2 + 1}$
:::

::item{id="frac-coeffs"}

## 4. Éléments de première espèce

:::key[Intégrer 1/(ax+b)ⁿ]
$$\int \frac{dx}{(ax + b)^n} = \begin{cases} \frac{1}{a}\ln|ax + b| + C & \text{si } n = 1, \\[4pt] \frac{-1}{a(n - 1)(ax + b)^{n-1}} + C & \text{si } n \ge 2. \end{cases}$$
:::

:::example[Pôle triple, intégré]
$\frac{5x^3 - 17x^2 + 19x - 13}{(x + 1)(x - 2)^3} = -\frac{1}{(x - 2)^3} + \frac{4}{(x - 2)^2} + \frac{3}{x - 2} + \frac{2}{x + 1}$, donc
$$\int \frac{5x^3 - 17x^2 + 19x - 13}{(x + 1)(x - 2)^3}\,dx = \frac{1}{2(x - 2)^2} - \frac{4}{x - 2} + 3\ln|x - 2| + 2\ln|x + 1| + C.$$
:::

## 5. Éléments de deuxième espèce : $\frac{\alpha x + \beta}{ax^2 + bx + c}$

On distingue selon le discriminant $\Delta = b^2 - 4ac$.

:::method[Cas Δ > 0 : deux racines réelles]
$ax^2 + bx + c = a(x - x_1)(x - x_2)$ : on est ramené à deux éléments de 1ʳᵉ espèce, donc deux logarithmes.
:::

:::example[Δ > 0]
$\frac{x^2 + x - 5}{x^2 - 1} = 1 + \frac{x - 4}{(x - 1)(x + 1)} = 1 + \frac{5/2}{x + 1} - \frac{3/2}{x - 1}$ (en $x = 1$ : $-3 = 2B$ ; en $x = -1$ : $-5 = -2A$). Donc
$$\int_2^3 \frac{x^2 + x - 5}{x^2 - 1}\,dx = \left[x + \frac{5}{2}\ln|x + 1| - \frac{3}{2}\ln|x - 1|\right]_2^3 = 1 + \frac{7}{2}\ln 2 - \frac{5}{2}\ln 3.$$
:::

:::warning[Erreur d'énoncé dans le poly (exemples 23 et 24)]
Le poly demande $\int_1^3$ mais calcule en réalité $\left[\ \right]_2^3$. Et $\int_1^3$ n'existe pas : la fraction a un **pôle en $x = 1$**, où $\frac{1}{x - 1}$ (ou $\frac{1}{(x - 1)^2}$) n'est pas intégrable (on le prouvera au chapitre des intégrales généralisées : c'est une intégrale de Riemann divergente). Les résultats $1 + \frac{7}{2}\ln 2 - \frac{5}{2}\ln 3$ et $17 + 11\ln 2$ sont ceux de $\int_2^3$.
:::

:::method[Cas Δ = 0 : une racine double]
$ax^2 + bx + c = a(x - x_0)^2$ : $\frac{\alpha x + \beta}{a(x - x_0)^2} = \frac{1}{a}\left(\frac{A}{(x - x_0)^2} + \frac{B}{x - x_0}\right)$, d'où un terme $-\frac{A}{x - x_0}$ et un logarithme.
:::

:::example[Δ = 0]
$\frac{2x^3 + 4x^2 - 3x + 5}{x^2 - 2x + 1} = 2x + 8 + \frac{11x - 3}{(x - 1)^2} = 2x + 8 + \frac{8}{(x - 1)^2} + \frac{11}{x - 1}$, donc
$$\int_2^3 \frac{2x^3 + 4x^2 - 3x + 5}{x^2 - 2x + 1}\,dx = \left[x^2 + 8x - \frac{8}{x - 1} + 11\ln|x - 1|\right]_2^3 = 17 + 11\ln 2.$$
:::

:::method[Cas Δ < 0 : le numérateur est la dérivée, plus une arctangente]
1. On fait apparaître $2ax + b$ (dérivée du dénominateur) au numérateur :
$$\frac{\alpha x + \beta}{ax^2 + bx + c} = \frac{\alpha}{2a} \cdot \frac{2ax + b}{ax^2 + bx + c} + \left(\beta - \frac{\alpha b}{2a}\right)\frac{1}{ax^2 + bx + c}.$$
2. Le premier morceau donne $\frac{\alpha}{2a}\ln(ax^2 + bx + c)$ (pas besoin de valeur absolue : $\Delta < 0$, le trinôme garde le signe de $a$).
3. Pour le second, **forme canonique** : $ax^2 + bx + c = a\left[(x + p)^2 + q^2\right]$ avec $p = \frac{b}{2a}$, $q = \frac{\sqrt{4ac - b^2}}{2a}$, puis
$$\int \frac{dx}{ax^2 + bx + c} = \frac{1}{aq}\arctan\frac{x + p}{q} + C.$$
:::

:::example[Δ < 0]
$\int \frac{x\,dx}{x^2 + 2x + 5} = \frac{1}{2}\int \frac{2x + 2}{x^2 + 2x + 5}\,dx - \int \frac{dx}{(x + 1)^2 + 4} = \frac{1}{2}\ln(x^2 + 2x + 5) - \frac{1}{2}\arctan\frac{x + 1}{2} + C.$
:::

:::example[Un pôle en 0 et un trinôme irréductible]
$\frac{1}{x(x^2 + 2x + 5)} = \frac{1}{5x} - \frac{x + 2}{5(x^2 + 2x + 5)}$, donc
$$\int \frac{dx}{x(x^2 + 2x + 5)} = \frac{1}{5}\ln|x| - \frac{1}{10}\ln(x^2 + 2x + 5) - \frac{1}{10}\arctan\frac{x + 1}{2} + C.$$
:::

:::example[Pôle double en 0]
$\frac{1}{x^2(x^2 + 2x + 5)} = \frac{A_0}{x^2} + \frac{A_1}{x} + \frac{Bx + C}{x^2 + 2x + 5}$ avec $h(x) = \frac{1}{x^2 + 2x + 5}$ :
$A_0 = h(0) = \frac{1}{5}$ ; $A_1 = h'(0) = -\frac{2}{5^2} = -\frac{2}{25}$ ; $B = -A_1 = \frac{2}{25}$ ; puis en $x = 1$ : $\frac{1}{8} = \frac{1}{5} - \frac{2}{25} + \frac{B + C}{8}$ donne $C = -\frac{1}{25}$. Finalement
$$\int \frac{dx}{x^2(x^2 + 2x + 5)} = -\frac{1}{5x} - \frac{2}{25}\ln|x| + \frac{1}{25}\ln(x^2 + 2x + 5) - \frac{3}{50}\arctan\frac{x + 1}{2} + C.$$
:::

:::warning[Erreur dans le poly (exemple 27)]
Le poly calcule $A_1 = h'(0) = -\frac{2x + 2}{x^2 + 2x + 5}\Big|_{x=0} = -\frac{2}{5}$ : il oublie le **carré** au dénominateur de la dérivée, $h'(x) = -\frac{2x + 2}{(x^2 + 2x + 5)^2}$. Toute la suite est fausse ($B = \frac{2}{5}$, $C = -\frac{1}{5}$, et la primitive finale). Il suffit de dériver la réponse du poly pour voir qu'on ne retrouve pas l'intégrande.
:::

:::example[Deux trinômes irréductibles]
$\frac{4x^3 - 7x^2 + 31x - 38}{(x^2 + 4)(x^2 + 9)} = \frac{3x - 2}{x^2 + 4} + \frac{x - 5}{x^2 + 9}$ (identification : $A + C = 4$, $B + D = -7$, $9A + 4C = 31$, $9B + 4D = -38$), donc
$$\int = \frac{3}{2}\ln(x^2 + 4) - \arctan\frac{x}{2} + \frac{1}{2}\ln(x^2 + 9) - \frac{5}{3}\arctan\frac{x}{3} + C.$$
:::

:::example[Avec partie entière]
$\frac{12x^4 + 190x^2 + 13x - 6}{(2x - 1)(x^2 + 16)} = 6x + 3 + \frac{3}{2x - 1} - \frac{x - 6}{x^2 + 16}$, donc
$$\int = 3x^2 + 3x + \frac{3}{2}\ln|2x - 1| - \frac{1}{2}\ln(x^2 + 16) + \frac{3}{2}\arctan\frac{x}{4} + C.$$
:::

::item{id="frac-integrer"}

## 6. Éléments de deuxième espèce d'ordre n ≥ 2

On se ramène (forme canonique, changement $t = \frac{x + p}{q}$) à $I_n = \int \frac{dt}{(1 + t^2)^n}$.

:::theorem[Récurrence des Iₙ]
Une IPP ($u = \frac{1}{(1 + t^2)^n}$, $v' = 1$) et l'écriture $\frac{t^2}{(1 + t^2)^{n+1}} = \frac{1}{(1 + t^2)^n} - \frac{1}{(1 + t^2)^{n+1}}$ donnent
$$I_1 = \arctan t, \qquad I_{n+1} = \frac{1}{2n}\,\frac{t}{(1 + t^2)^n} + \left(1 - \frac{1}{2n}\right)I_n.$$
En particulier $I_2 = \frac{1}{2}\left(\frac{t}{1 + t^2} + \arctan t\right)$ et $I_3 = \frac{3}{8}\arctan t + \frac{3}{8}\,\frac{t}{1 + t^2} + \frac{1}{4}\,\frac{t}{(1 + t^2)^2}$.
:::

:::method[Autre voie : t = tan θ]
Avec $t = \tan\theta$, $dt = (1 + \tan^2\theta)\,d\theta$ et $\frac{1}{1 + t^2} = \cos^2\theta$ : $I_n = \int \cos^{2(n-1)}\theta\,d\theta$, qu'on linéarise. Par exemple $I_2 = \int \cos^2\theta\,d\theta = \frac{\theta}{2} + \frac{\sin 2\theta}{4}$.
:::

:::example[Exemple 31]
$\int \frac{x\,dx}{(x^2 + 2x + 5)^2} = \frac{1}{2}\int \frac{2x + 2}{(x^2 + 2x + 5)^2}\,dx - \int \frac{dx}{\left[(x + 1)^2 + 4\right]^2}$.
- Le premier vaut $-\frac{1}{2(x^2 + 2x + 5)}$.
- Pour le second, $x + 1 = 2t$, $dx = 2\,dt$, $\left[(x + 1)^2 + 4\right]^2 = 16(1 + t^2)^2$ : il vaut $\frac{2}{16}I_2(t) = \frac{1}{16}\left(\frac{t}{1 + t^2} + \arctan t\right)$, avec $\frac{t}{1 + t^2} = \frac{2(x + 1)}{x^2 + 2x + 5}$.

Au total :
$$\int \frac{x\,dx}{(x^2 + 2x + 5)^2} = -\frac{x + 5}{8(x^2 + 2x + 5)} - \frac{1}{16}\arctan\frac{x + 1}{2} + C.$$
:::

:::warning[Erreur dans le poly (exemple 31)]
Le poly écrit $\int \frac{dx}{\left[(x + 1)^2 + 4\right]^2} = \frac{1}{16}I_2\left(\frac{x + 1}{2}\right)$ : il oublie le facteur $2$ venant de $dx = 2\,dt$. Son résultat final ($-\frac{1}{64}\ldots - \frac{1}{32}\arctan$) est faux ; dériver la bonne réponse redonne exactement l'intégrande.
:::
