---
title: Ch1 — Primitives, changement de variable, intégration par parties
summary: "Primitive et intégrale indéfinie, tableau des primitives usuelles, changement de variable, intégration par parties, intégrale définie et ses propriétés (Chasles, parité, moyenne), avec 44 exercices corrigés."
tags: [chapitre 1, primitives, changement de variable, IPP, intégrale définie]
minutes: 120
---

## 1. Objectifs

À la fin de ce chapitre, tu dois savoir :

- reconnaître une **primitive usuelle** (tableau à connaître par cœur) ;
- reconnaître une forme $u' \cdot \varphi(u)$ et faire le **changement de variable** ;
- choisir $u$ et $v'$ dans une **intégration par parties** (IPP) ;
- calculer une **intégrale définie** et utiliser ses propriétés (Chasles, parité, périodicité, inégalité de la moyenne).

## 2. Primitive d'une fonction

:::definition[Primitive]
Soit $f$ définie sur un **intervalle** $I$. Une fonction $F$ est une **primitive** de $f$ sur $I$ si $F$ est dérivable sur $I$ et $F'(x) = f(x)$ pour tout $x \in I$.
:::

:::theorem[Existence et unicité à une constante près]
Toute fonction **continue** sur un intervalle $I$ admet des primitives. Si $F$ en est une, les primitives de $f$ sont **exactement** les fonctions $F + C$ ($C$ constante).

On note $\int f(x)\,dx = F(x) + C$ (« intégrale indéfinie »). La preuve de l'unicité : si $F' = G'$, alors $(F - G)' = 0$ sur un intervalle, donc $F - G$ est constante (accroissements finis).
:::

:::warning[Sur un intervalle seulement]
$\ln|x|$ est une primitive de $\frac{1}{x}$ sur $]0, +\infty[$ **et** sur $]-\infty, 0[$, mais sur $\mathbb{R}^*$ (qui n'est pas un intervalle) les primitives sont $\ln|x| + C_1$ à droite et $\ln|x| + C_2$ à gauche, avec deux constantes indépendantes.
:::

### Tableau des primitives usuelles

| $f(x)$ | $\int f(x)\,dx$ | sur |
|---|---|---|
| $x^\alpha$ ($\alpha \ne -1$) | $\frac{x^{\alpha+1}}{\alpha+1}$ | $\mathbb{R}$ ou $]0, +\infty[$ selon $\alpha$ |
| $\frac{1}{x}$ | $\ln\lvert x\rvert$ | $]0, +\infty[$ ou $]-\infty, 0[$ |
| $e^x$ ; $a^x$ ($a > 0$, $a \ne 1$) | $e^x$ ; $\frac{a^x}{\ln a}$ | $\mathbb{R}$ |
| $\ln x$ | $x \ln x - x$ | $]0, +\infty[$ |
| $\sin x$ ; $\cos x$ | $-\cos x$ ; $\sin x$ | $\mathbb{R}$ |
| $\tan x$ | $-\ln\lvert\cos x\rvert$ | où $\cos x \ne 0$ |
| $\frac{1}{\cos^2 x} = 1 + \tan^2 x$ | $\tan x$ | où $\cos x \ne 0$ |
| $\frac{1}{\sin^2 x} = 1 + \cot^2 x$ | $-\cot x$ | où $\sin x \ne 0$ |
| $\cosh x$ ; $\sinh x$ ; $\tanh x$ | $\sinh x$ ; $\cosh x$ ; $\ln(\cosh x)$ | $\mathbb{R}$ |
| $\frac{1}{\cosh^2 x}$ | $\tanh x$ | $\mathbb{R}$ |
| $\frac{1}{a^2 + x^2}$ | $\frac{1}{a}\arctan\frac{x}{a}$ | $\mathbb{R}$ |
| $\frac{1}{a^2 - x^2}$ | $\frac{1}{2a}\ln\left\lvert\frac{a + x}{a - x}\right\rvert$ | hors de $\pm a$ |
| $\frac{1}{\sqrt{a^2 - x^2}}$ ($a > 0$) | $\arcsin\frac{x}{a}$ (ou $-\arccos\frac{x}{a}$) | $]-a, a[$ |
| $\frac{1}{\sqrt{x^2 + a^2}}$ | $\ln\left(x + \sqrt{x^2 + a^2}\right) = \operatorname{argsh}\frac{x}{a} + C$ | $\mathbb{R}$ |
| $\frac{1}{\sqrt{x^2 - a^2}}$ ($a > 0$) | $\ln\left\lvert x + \sqrt{x^2 - a^2}\right\rvert$ ($= \operatorname{argch}\frac{x}{a} + C$ pour $x > a$) | $\lvert x\rvert > a$ |

:::warning[Erreur dans le poly et dans la « Table of Basic Integrals »]
Les deux documents donnent $\int \frac{dx}{\sqrt{x^2 - a^2}} = \ln\left(\frac{x}{a} - \sqrt{\left(\frac{x}{a}\right)^2 - 1}\right)$, avec un **moins**. Pour $x > a$, cette expression vaut $-\operatorname{argch}\frac{x}{a}$ : sa dérivée est $-\frac{1}{\sqrt{x^2 - a^2}}$, l'opposé de ce qu'on veut. La bonne formule a un **plus** : $\ln\left(\frac{x}{a} + \sqrt{\left(\frac{x}{a}\right)^2 - 1}\right) = \operatorname{argch}\frac{x}{a}$.
:::

:::property[Linéarité, et ce qu'on n'a PAS le droit de faire]
$\int (\lambda f + \mu g) = \lambda \int f + \mu \int g$. Mais en général
$$\int f g \ne \int f \cdot \int g \qquad \text{et} \qquad \int \frac{f}{g} \ne \frac{\int f}{\int g}.$$
(Contre-exemple : $\int x \cdot x\,dx = \frac{x^3}{3}$, alors que $\frac{x^2}{2} \cdot \frac{x^2}{2} = \frac{x^4}{4}$.)
:::

## 3. Changement de variable

:::theorem[Changement de variable « naturel »]
Si $f(x) = \varphi\big(u(x)\big)\,u'(x)$ avec $\varphi$ continue de primitive $\psi$ et $u$ de classe $\mathcal{C}^1$, alors
$$\int f(x)\,dx = \int \varphi(u)\,du = \psi\big(u(x)\big) + C.$$
En pratique : on pose $u = u(x)$, on écrit $du = u'(x)\,dx$, et on remplace **tout** ($x$ et $dx$).
:::

:::key[Les formes à reconnaître]
| forme | primitive |
|---|---|
| $u' u^n$ ($n \ne -1$) | $\frac{u^{n+1}}{n+1}$ |
| $\frac{u'}{u^n}$ ($n \ne 1$) | $\frac{-1}{(n-1)u^{n-1}}$ |
| $\frac{u'}{u}$ | $\ln\lvert u\rvert$ |
| $u' e^u$ | $e^u$ |
| $u' \cos u$ | $\sin u$ |
| $u' \sin u$ | $-\cos u$ |
| $\frac{u'}{\sqrt{a^2 - u^2}}$ | $\arcsin\frac{u}{a}$ |
| $\frac{u'}{a^2 + u^2}$ | $\frac{1}{a}\arctan\frac{u}{a}$ |
| $\frac{u'}{a^2 - u^2}$ | $\frac{1}{2a}\ln\left\lvert\frac{a + u}{a - u}\right\rvert$ (ou $\frac{1}{a}\operatorname{argth}\frac{u}{a}$ si $\lvert u\rvert < a$) |
| $\frac{u'}{\sqrt{a^2 + u^2}}$ | $\operatorname{argsh}\frac{u}{a}$ |
:::

:::warning[Erreur dans le poly (tableau 2.2) et dans la fiche « Révision »]
Les deux documents écrivent $\int u' \cos u = -\sin u$ et $\int u' \sin u = \cos u$ : les **signes sont inversés**. On vérifie en dérivant : $(\sin u)' = u' \cos u$ et $(-\cos u)' = u' \sin u$. Les formules justes sont celles du tableau ci-dessus.
:::

:::example[Quatre exemples du cours]
1. $\int \tan x\,dx = \int \frac{\sin x}{\cos x}\,dx$ : avec $u = \cos x$, $u' = -\sin x$, c'est $-\int \frac{u'}{u} = -\ln\lvert\cos x\rvert + C$.
2. $\int \frac{x\,dx}{\sqrt{1 - x^2}}$ : avec $u = 1 - x^2$, $du = -2x\,dx$, c'est $-\frac{1}{2}\int \frac{du}{\sqrt{u}} = -\sqrt{u} = -\sqrt{1 - x^2} + C$.
3. $\int (x^3 + x)^5(3x^2 + 1)\,dx = \frac{(x^3 + x)^6}{6} + C$ ($u = x^3 + x$).
4. $\int \frac{2z\,dz}{\sqrt[3]{z^2 + 1}}$ : avec $u = z^2 + 1$, c'est $\int u^{-1/3}\,du = \frac{3}{2}u^{2/3} = \frac{3}{2}(z^2 + 1)^{2/3} + C$. (Poser $u = \sqrt[3]{z^2 + 1}$ marche aussi : $\int \frac{3u^2\,du}{u} = \frac{3}{2}u^2$, même résultat.)
:::

:::method[Réflexe du changement de variable]
Cherche dans l'intégrande une **fonction composée** $\varphi(u(x))$ dont la **dérivée intérieure** $u'(x)$ apparaît en facteur (à une constante près). Si $u'$ manque d'une constante, on la fait apparaître : $\int x \sin(x^2)\,dx = \frac{1}{2}\int 2x \sin(x^2)\,dx = -\frac{1}{2}\cos(x^2)$.
:::

::item{id="prim-cv"}

## 4. Intégration par parties

:::theorem[Intégration par parties]
Si $u$ et $v$ sont de classe $\mathcal{C}^1$ :
$$\int u(x)\,v'(x)\,dx = u(x)\,v(x) - \int u'(x)\,v(x)\,dx, \qquad \text{en abrégé} \qquad \int u\,dv = uv - \int v\,du.$$
Elle vient de la dérivée d'un produit : $(uv)' = u'v + uv'$.
:::

:::method[Qui est u, qui est v' ?]
On prend pour $u$ la fonction qui **se simplifie en la dérivant**, et pour $v'$ celle qu'on **sait intégrer** :
- **polynôme × ($e^{ax}$, $\cos$, $\sin$)** : $u$ = le polynôme (son degré baisse à chaque IPP, jusqu'à une constante) ;
- **polynôme × ($\ln$, $\arctan$, $\arcsin$)** : $u$ = la fonction transcendante (sa dérivée est une fraction rationnelle) et $v'$ = le polynôme ;
- **$\ln x$ ou $\arcsin x$ seul** : on écrit $1 \cdot \ln x$ et on prend $v' = 1$.
:::

:::example[Les exemples du cours]
- $\int \ln x\,dx$ : $u = \ln x$, $v' = 1$ ⟹ $x \ln x - \int x \cdot \frac{1}{x}\,dx = x \ln x - x + C$.
- $\int x e^x\,dx$ : $u = x$, $v' = e^x$ ⟹ $x e^x - \int e^x\,dx = (x - 1)e^x + C$.
- $\int x \sin 2x\,dx$ : $u = x$, $v = -\frac{1}{2}\cos 2x$ ⟹ $-\frac{x}{2}\cos 2x + \frac{1}{4}\sin 2x + C$.
- $\int x \ln x\,dx$ : $u = \ln x$, $v = \frac{x^2}{2}$ ⟹ $\frac{x^2}{2}\ln x - \frac{x^2}{4} + C$.
- $\int x^2 e^{3x}\,dx$ : deux IPP successives ⟹ $\left(\frac{x^2}{3} - \frac{2x}{9} + \frac{2}{27}\right)e^{3x} + C$.
:::

:::example[Arcsinus]
$\int \arcsin x\,dx$ : $u = \arcsin x$, $v' = 1$, donc $u' = \frac{1}{\sqrt{1 - x^2}}$, $v = x$ :
$$\int \arcsin x\,dx = x \arcsin x - \int \frac{x\,dx}{\sqrt{1 - x^2}} = x \arcsin x + \sqrt{1 - x^2} + C$$
(la dernière intégrale est l'exemple 2 du § 3).
:::

:::warning[Erreur dans le poly (exemple 8)]
Le poly conclut $\int \arcsin x\,dx = x \arcsin x + \sqrt{1 + x^2}$, avec un **plus** sous la racine. C'est faux : la dérivée de $\sqrt{1 + x^2}$ est $\frac{x}{\sqrt{1 + x^2}}$, pas $-\frac{x}{\sqrt{1 - x^2}}$. Il faut $\sqrt{1 - x^2}$, ce qui est d'ailleurs cohérent avec le domaine $[-1, 1]$ de l'arcsinus.
:::

:::example[L'astuce de l'intégrale qui revient]
$I = \int e^x \sin x\,dx$. Deux IPP (avec $u = e^x$ les deux fois) donnent
$$I = -e^x \cos x + \int e^x \cos x\,dx = -e^x \cos x + e^x \sin x - I.$$
On retrouve $I$ ! On résout : $2I = e^x(\sin x - \cos x)$, donc $I = \frac{e^x}{2}(\sin x - \cos x) + C$.
:::

::item{id="prim-ipp"}

## 5. Intégrale définie

:::definition[Intégrale de Riemann]
Si $f$ est continue sur $[a, b]$, on découpe $[a, b]$ en $n$ morceaux de largeur $h = \frac{b - a}{n}$ ($x_i = a + ih$). Les sommes $I_n = \sum_{i=1}^{n} f(x_{i-1})(x_i - x_{i-1})$ (aires de rectangles) **convergent** quand $n \to \infty$ ; la limite est $\int_a^b f(x)\,dx$. Toute fonction continue (ou continue par morceaux) sur un segment est ainsi intégrable.
:::

:::theorem[Théorème fondamental de l'analyse]
- Si $f$ est continue sur $[a, b]$ et $F$ une primitive de $f$ : $\int_a^b f(x)\,dx = \big[F(x)\big]_a^b = F(b) - F(a)$.
- Si $F(x) = \int_a^{u(x)} h(t)\,dt$ avec $h$ continue et $u$ dérivable : $F'(x) = h\big(u(x)\big)\,u'(x)$.
:::

:::property[Propriétés de l'intégrale définie]
- **Bornes confondues** : $\int_a^a f = 0$ ; **échange des bornes** : $\int_b^a f = -\int_a^b f$.
- **Chasles** : $\int_a^b f = \int_a^c f + \int_c^b f$.
- **Linéarité** : $\int_a^b (\lambda f + \mu g) = \lambda\int_a^b f + \mu\int_a^b g$.
- **Positivité, croissance** (si $a \le b$) : $f \le g$ sur $[a, b]$ ⟹ $\int_a^b f \le \int_a^b g$.
- **Parité** : si $f$ est paire, $\int_{-a}^{a} f = 2\int_0^a f$ ; si $f$ est impaire, $\int_{-a}^{a} f = 0$.
- **Périodicité** : si $f$ est $T$-périodique, $\int_a^{a+T} f = \int_0^T f$.
:::

:::warning[Erreur dans le poly (propriété des fonctions paires)]
Le poly écrit $\int_{-a}^{a} f(x)\,dx = 3\int_0^a f(x)\,dx$ pour $f$ paire. Le bon coefficient est **2** : par symétrie, l'aire de $-a$ à $0$ est égale à celle de $0$ à $a$. Exemple : $\int_{-1}^{1} x^2\,dx = \frac{2}{3} = 2 \times \frac{1}{3}$.
:::

:::theorem[Inégalité et égalité de la moyenne]
- Si $m \le f \le M$ sur $[a, b]$ : $m \le \frac{1}{b - a}\int_a^b f(t)\,dt \le M$.
- Si $f$ est **continue** sur $[a, b]$, il existe $c \in [a, b]$ tel que $f(c) = \frac{1}{b - a}\int_a^b f(t)\,dt$ : c'est la **valeur moyenne** de $f$, la hauteur du rectangle de même aire.
:::

:::theorem[Changement de variable et IPP dans une intégrale définie]
- Si $\varphi : [\alpha, \beta] \to [a, b]$ est $\mathcal{C}^1$ et $f$ continue : $\int_{\varphi(\alpha)}^{\varphi(\beta)} f(x)\,dx = \int_\alpha^\beta f\big(\varphi(t)\big)\varphi'(t)\,dt$. **On change aussi les bornes.**
- $\int_a^b u v' = \big[uv\big]_a^b - \int_a^b u' v$.
:::

:::key[Calcul d'aire]
- Aire entre $C_f$, l'axe des abscisses et $x = a$, $x = b$ (si $f \ge 0$) : $\int_a^b f(x)\,dx$.
- Aire entre $C_f$ et $C_g$ (si $f \ge g$) : $\int_a^b \big[f(x) - g(x)\big]dx$.
- Aire entre $C_f$ et la droite $y = m$ (si $f \ge m$) : $\int_a^b \big[f(x) - m\big]dx$.
:::

::item{id="prim-definie"}

## 6. Entraînement : 44 primitives corrigées

Ce sont les deux listes d'exercices du poly (changement de variable puis intégration par parties). Chaque réponse a été **vérifiée en la dérivant**. Cherche d'abord seul, puis déplie la solution. Toutes les réponses sont « $+ C$ ».

### Changement de variable

1. $\int (x^3 + x)^5(3x^2 + 1)\,dx$ $\quad$ 2. $\int (3x + 2)(3x^2 + 4x)^4\,dx$ $\quad$ 3. $\int \sqrt{2x + 1}\,dx$ $\quad$ 4. $\int x\sqrt{2x + 1}\,dx$
5. $\int \frac{2x\,dx}{\sqrt[3]{x^2 + 1}}$ $\quad$ 6. $\int 2(2x + 4)^5\,dx$ $\quad$ 7. $\int 7\sqrt{7x - 1}\,dx$ $\quad$ 8. $\int 2x(x^2 + 5)^{-4}\,dx$
9. $\int \frac{4x^3}{(x^4 + 1)^2}\,dx$ $\quad$ 10. $\int x^2 \sin(x^3)\,dx$ $\quad$ 11. $\int \frac{(1 + \sqrt{x})^{1/3}}{\sqrt{x}}\,dx$ $\quad$ 12. $\int x \sin(2x^2)\,dx$

:::solution[Solutions 1 à 12]
1. $u = x^3 + x$ : $\frac{(x^3 + x)^6}{6}$.
2. $u = 3x^2 + 4x$, $u' = 2(3x + 2)$ : $\frac{(3x^2 + 4x)^5}{10}$.
3. $u = 2x + 1$ : $\frac{1}{3}(2x + 1)^{3/2}$.
4. $u = 2x + 1$, $x = \frac{u - 1}{2}$, $dx = \frac{du}{2}$ : $\frac{1}{4}\int (u^{3/2} - u^{1/2})\,du = \frac{(2x + 1)^{5/2}}{10} - \frac{(2x + 1)^{3/2}}{6}$.
5. $u = x^2 + 1$ : $\frac{3}{2}(x^2 + 1)^{2/3}$.
6. $u = 2x + 4$ : $\frac{(2x + 4)^6}{6}$.
7. $u = 7x - 1$ : $\frac{2}{3}(7x - 1)^{3/2}$.
8. $u = x^2 + 5$ : $-\frac{1}{3(x^2 + 5)^3}$.
9. $u = x^4 + 1$ : $-\frac{1}{x^4 + 1}$.
10. $u = x^3$ : $-\frac{1}{3}\cos(x^3)$.
11. $u = 1 + \sqrt{x}$, $du = \frac{dx}{2\sqrt{x}}$ : $2\int u^{1/3}\,du = \frac{3}{2}(1 + \sqrt{x})^{4/3}$.
12. $u = 2x^2$ : $-\frac{1}{4}\cos(2x^2)$.
:::

13. $\int \left(1 - \cos\frac{x}{2}\right)^2 \sin\frac{x}{2}\,dx$ $\quad$ 14. $\int \frac{9x^2}{\sqrt{1 - x^3}}\,dx$ $\quad$ 15. $\int \frac{1}{x^2}\cos^2\frac{1}{x}\,dx$ $\quad$ 16. $\int \sqrt{x}\,\sin^2(x^{3/2} - 1)\,dx$
17. $\int \frac{dx}{\sqrt{5x + 8}}$ $\quad$ 18. $\int x\sqrt[4]{1 - x^2}\,dx$ $\quad$ 19. $\int \frac{dx}{\sqrt{x}(1 + \sqrt{x})^2}$ $\quad$ 20. $\int \sin^5\frac{x}{3}\cos\frac{x}{3}\,dx$
21. $\int \frac{\sin(2x + 1)}{\cos^2(2x + 1)}\,dx$ $\quad$ 22. $\int \frac{1}{x^2}\cos\left(\frac{1}{x} - 1\right)dx$

:::solution[Solutions 13 à 22]
13. $u = 1 - \cos\frac{x}{2}$, $du = \frac{1}{2}\sin\frac{x}{2}\,dx$ : $\frac{2}{3}\left(1 - \cos\frac{x}{2}\right)^3$.
14. $u = 1 - x^3$, $du = -3x^2\,dx$ : $-3\int u^{-1/2} = -6\sqrt{1 - x^3}$.
15. $u = \frac{1}{x}$, $du = -\frac{dx}{x^2}$ : $-\int \cos^2 u\,du = -\frac{1}{2x} - \frac{1}{4}\sin\frac{2}{x}$.
16. $u = x^{3/2} - 1$, $du = \frac{3}{2}\sqrt{x}\,dx$ : $\frac{2}{3}\int \sin^2 u = \frac{x^{3/2} - 1}{3} - \frac{\sin(2x^{3/2} - 2)}{6}$.
17. $\frac{2}{5}\sqrt{5x + 8}$.
18. $u = 1 - x^2$ : $-\frac{1}{2}\int u^{1/4} = -\frac{2}{5}(1 - x^2)^{5/4}$.
19. $u = 1 + \sqrt{x}$, $du = \frac{dx}{2\sqrt{x}}$ : $2\int u^{-2} = -\frac{2}{1 + \sqrt{x}}$.
20. $u = \sin\frac{x}{3}$, $du = \frac{1}{3}\cos\frac{x}{3}\,dx$ : $3\int u^5 = \frac{1}{2}\sin^6\frac{x}{3}$.
21. $u = \cos(2x + 1)$, $du = -2\sin(2x + 1)\,dx$ : $-\frac{1}{2}\int u^{-2} = \frac{1}{2\cos(2x + 1)}$.
22. $u = \frac{1}{x} - 1$, $du = -\frac{dx}{x^2}$ : $-\sin\left(\frac{1}{x} - 1\right)$.
:::

23. $\int \frac{\cos(\sqrt{x} + 3)}{\sqrt{x}}\,dx$ $\quad$ 24. $\int \frac{1}{x^2}\sqrt{2 - \frac{1}{x}}\,dx$ $\quad$ 25. $\int \frac{1}{x^2}\sin\frac{1}{x}\cos\frac{1}{x}\,dx$ $\quad$ 26. $\int \frac{1}{x^3}\sqrt{\frac{x^2 - 1}{x^2}}\,dx$
27. $\int x\sqrt{4 - x}\,dx$ $\quad$ 28. $\int (x + 1)^2(1 - x)^5\,dx$ $\quad$ 29. $\int (x + 5)(x - 5)^{1/3}\,dx$ $\quad$ 30. $\int x^3\sqrt{x^2 + 1}\,dx$
31. $\int 3x^5\sqrt{x^3 + 1}\,dx$ $\quad$ 32. $\int \frac{x}{(x^2 - 4)^3}\,dx$ $\quad$ 33. $\int \frac{x}{(x - 4)^3}\,dx$

:::solution[Solutions 23 à 33]
23. $u = \sqrt{x} + 3$ : $2\sin(\sqrt{x} + 3)$.
24. $u = 2 - \frac{1}{x}$, $du = \frac{dx}{x^2}$ : $\frac{2}{3}\left(2 - \frac{1}{x}\right)^{3/2}$.
25. $u = \frac{1}{x}$ : $-\int \sin u \cos u\,du = -\frac{1}{2}\sin^2\frac{1}{x}$.
26. $\sqrt{\frac{x^2 - 1}{x^2}} = \sqrt{1 - \frac{1}{x^2}}$ ; $u = 1 - \frac{1}{x^2}$, $du = \frac{2\,dx}{x^3}$ : $\frac{1}{3}\left(1 - \frac{1}{x^2}\right)^{3/2}$.
27. $u = 4 - x$, $x = 4 - u$ : $\frac{2}{5}(4 - x)^{5/2} - \frac{8}{3}(4 - x)^{3/2}$.
28. $u = 1 - x$, $x + 1 = 2 - u$ : $-\frac{2}{3}(1 - x)^6 + \frac{4}{7}(1 - x)^7 - \frac{1}{8}(1 - x)^8$.
29. $u = x - 5$, $x + 5 = u + 10$ : $\frac{3}{7}(x - 5)^{7/3} + \frac{15}{2}(x - 5)^{4/3}$.
30. $u = x^2 + 1$, $x^3\,dx = \frac{1}{2}(u - 1)\,du$ : $\frac{(x^2 + 1)^{5/2}}{5} - \frac{(x^2 + 1)^{3/2}}{3}$.
31. $u = x^3 + 1$, $3x^5\,dx = (u - 1)\,du$ : $\frac{2}{5}(x^3 + 1)^{5/2} - \frac{2}{3}(x^3 + 1)^{3/2}$.
32. $u = x^2 - 4$ : $-\frac{1}{4(x^2 - 4)^2}$.
33. $u = x - 4$, $x = u + 4$ : $\int (u^{-2} + 4u^{-3})\,du = -\frac{1}{x - 4} - \frac{2}{(x - 4)^2}$.
:::

### Intégration par parties

34. $\int x\ln x\,dx$ $\quad$ 35. $\int x\sin x\,dx$ $\quad$ 36. $\int x^2\sin x\,dx$ $\quad$ 37. $\int x\cos x\,dx$ $\quad$ 38. $\int x^2\cos x\,dx$ $\quad$ 39. $\int x e^x\,dx$
40. $\int x\arctan x\,dx$ $\quad$ 41. $\int x^3\sin x\,dx$ $\quad$ 42. $\int x^3\cos x\,dx$ $\quad$ 43. $\int x\sin x\cos x\,dx$ $\quad$ 44. $\int x\sin^2 x\,dx$

:::solution[Solutions 34 à 44]
34. $u = \ln x$ : $\frac{x^2}{2}\ln x - \frac{x^2}{4}$.
35. $u = x$ : $-x\cos x + \sin x$.
36. Deux IPP : $-x^2\cos x + 2x\sin x + 2\cos x$.
37. $x\sin x + \cos x$.
38. $x^2\sin x + 2x\cos x - 2\sin x$.
39. $(x - 1)e^x$.
40. $u = \arctan x$, $v = \frac{x^2 + 1}{2}$ (astuce : on choisit la primitive $\frac{x^2 + 1}{2}$ plutôt que $\frac{x^2}{2}$, et le reste vaut $\int \frac{1}{2} = \frac{x}{2}$) : $\frac{x^2 + 1}{2}\arctan x - \frac{x}{2}$.
41. Trois IPP : $-x^3\cos x + 3x^2\sin x + 6x\cos x - 6\sin x$.
42. $x^3\sin x + 3x^2\cos x - 6x\sin x - 6\cos x$.
43. $x\sin x\cos x = \frac{x}{2}\sin 2x$ : $-\frac{x}{4}\cos 2x + \frac{1}{8}\sin 2x$.
44. $x\sin^2 x = \frac{x}{2} - \frac{x}{2}\cos 2x$ : $\frac{x^2}{4} - \frac{x}{4}\sin 2x - \frac{1}{8}\cos 2x$.
:::

:::method[Le « tableau » pour les IPP répétées]
Pour $\int P(x) \cdot g(x)$ avec $P$ polynôme : colonne de gauche $P, P', P'', \ldots$ jusqu'à $0$ ; colonne de droite $g$ puis ses primitives successives $G_1, G_2, \ldots$ On multiplie en diagonale avec des signes alternés $+, -, +, \ldots$ Exemple : $\int (x^2 + 7x - 5)\cos 2x\,dx = \frac{1}{2}\left(x^2 + 7x - \frac{11}{2}\right)\sin 2x + \frac{1}{2}\left(x + \frac{7}{2}\right)\cos 2x + C$.
:::
