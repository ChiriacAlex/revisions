---
title: Ch0 — Prérequis d'analyse (limites, continuité, exp, ln)
summary: "Les « prérequis très or » du cours : limites et formes indéterminées, asymptotes, croissances comparées, continuité, dérivabilité, TVI, Rolle, accroissements finis, et les fonctions exponentielle et logarithme."
tags: [prérequis, limites, continuité, exponentielle, logarithme]
minutes: 60
---

## 1. Objectifs

Ce chapitre rassemble tout ce que le cours d'intégration **suppose acquis**. Le prof les appelle les « prérequis très or » : sans eux, impossible d'étudier une intégrale généralisée. Tu dois savoir :

- calculer une limite et lever une **forme indéterminée** ;
- utiliser les **croissances comparées** ($\ln x \ll x^\alpha \ll a^x$) ;
- vérifier qu'une fonction est **continue**, **dérivable**, de classe $\mathcal{C}^1$, **continue par morceaux** ;
- appliquer le **théorème des valeurs intermédiaires**, **Rolle** et les **accroissements finis** ;
- manipuler $e^x$ et $\ln x$ sans hésiter (dérivées, primitives, limites, inégalités).

## 2. Limites

### Limite en un point

:::definition[Limite à gauche, à droite]
- $\lim_{x \to a^-} f(x)$ : on s'approche de $a$ par **valeurs inférieures** ($x < a$).
- $\lim_{x \to a^+} f(x)$ : on s'approche de $a$ par **valeurs supérieures** ($x > a$).

La limite en $a$ existe et vaut $L$ **si et seulement si** les deux limites latérales existent et valent $L$.
:::

:::intuition[Lire 0⁺ et 2⁻]
$0^+$, c'est « un tout petit nombre positif » ($0{,}00001$) ; $2^-$, c'est « juste en dessous de 2 » ($1{,}99999$). Pour $\frac{1}{x}$ : en $0^+$ on divise par un petit positif, donc $+\infty$ ; en $0^-$, $-\infty$. La limite en $0$ n'existe donc pas.
:::

### Opérations et formes indéterminées

Les règles usuelles : $+\infty + \infty = +\infty$, $(+\infty) \times (-\infty) = -\infty$, $\frac{a}{\pm\infty} = 0$, $\frac{\text{positif}}{0^+} = +\infty$, $\frac{\text{positif}}{0^-} = -\infty$…

:::warning[Les quatre formes indéterminées]
$\infty - \infty$, $\quad 0 \times \infty$, $\quad \frac{0}{0}$, $\quad \frac{\infty}{\infty}$ (et leurs cousines exponentielles $1^\infty$, $0^0$, $\infty^0$). Ce ne sont **pas** des valeurs : il faut transformer l'expression.
:::

:::method[Lever une forme indéterminée]
1. **Polynômes et fractions rationnelles en $\pm\infty$** : on garde le terme de plus haut degré. $\lim_{x \to \infty} \frac{a_n x^n + \cdots}{b_m x^m + \cdots} = \lim \frac{a_n x^n}{b_m x^m}$.
2. **Facteur commun** : on factorise le terme dominant.
3. **Quantité conjuguée** pour les racines : $\sqrt{x^2 + x} - x = \frac{x}{\sqrt{x^2 + x} + x} \to \frac{1}{2}$.
4. **Règle de L'Hôpital** (cas $\frac{0}{0}$ ou $\frac{\infty}{\infty}$) : $\lim \frac{f}{g} = \lim \frac{f'}{g'}$ si cette dernière limite existe.
5. **Équivalents et développements limités** (chapitre DL) : la méthode la plus puissante.
:::

::item{id="pre-limites"}

### Asymptotes

:::definition[Les trois asymptotes]
- **Verticale** $x = a$ : $\lim_{x \to a^\pm} f(x) = \pm\infty$.
- **Horizontale** $y = L$ : $\lim_{x \to \pm\infty} f(x) = L$.
- **Oblique** $y = ax + b$ : $\lim_{x \to \pm\infty} \big[f(x) - (ax + b)\big] = 0$. On trouve $a = \lim \frac{f(x)}{x}$ puis $b = \lim \big(f(x) - ax\big)$.

La **position** de la courbe par rapport à la droite $D : y = ax + b$ se lit sur le **signe** de $f(x) - (ax + b)$ : positif, la courbe est au-dessus.
:::

### Théorème des gendarmes et croissances comparées

:::theorem[Théorème des gendarmes]
Si, au voisinage de $a$, $g(x) \le f(x) \le h(x)$ et $\lim_a g = \lim_a h = L$, alors $\lim_a f = L$.
:::

:::example[Un classique]
$\left| x \sin\frac{1}{x} \right| \le |x| \to 0$, donc $x \sin\frac{1}{x} \to 0$ quand $x \to 0$, même si $\sin\frac{1}{x}$ n'a pas de limite.
:::

:::key[Croissances comparées en +∞]
Pour $\alpha > 0$ et $a > 1$ :
$$\ln x \ll x^\alpha \ll a^x, \qquad \lim_{x \to +\infty} \frac{\ln x}{x^\alpha} = 0, \qquad \lim_{x \to +\infty} \frac{x^\alpha}{a^x} = 0.$$
Et en $0^+$ : $\lim_{x \to 0^+} x^\alpha |\ln x|^\beta = 0$ pour $\alpha > 0$. L'exponentielle « gagne » toujours contre la puissance, et la puissance contre le logarithme.
:::

:::warning[Les croissances comparées ne règlent pas tout]
Elles servent pour les **produits et quotients**. Pour une **différence** comme $\sqrt{x^2 + x} - x$ (forme $\infty - \infty$), il faut d'abord transformer l'expression (ici, quantité conjuguée).
:::

## 3. Continuité et dérivabilité

:::definition[Continuité]
$f$ est **continue en $a$** si $\lim_{x \to a^-} f(x) = f(a) = \lim_{x \to a^+} f(x)$. Elle est continue sur un intervalle $I$ si elle l'est en tout point de $I$ : sa courbe se trace « sans lever le stylo ».
:::

:::definition[Dérivabilité]
$f$ est **dérivable en $a$** si le taux d'accroissement $\frac{f(x) - f(a)}{x - a}$ a une limite **finie** quand $x \to a$ ; il faut donc que la dérivée à droite $f'(a^+)$ et la dérivée à gauche $f'(a^-)$ existent et soient égales.

- Sur un intervalle ouvert $]a, b[$ : dérivable en tout point.
- Sur un fermé $[a, b]$ : dérivable sur $]a, b[$, et $f'(a^+)$, $f'(b^-)$ existent.

La tangente en $a$ a pour équation $y = f'(a)(x - a) + f(a)$.
:::

:::definition[Classes C⁰ et C¹]
- $f \in \mathcal{C}^0(I)$ : $f$ est continue sur $I$.
- $f \in \mathcal{C}^1(I)$ : $f$ est dérivable sur $I$ **et** $f'$ est continue. Graphiquement : une courbe sans rupture **ni angle**.
:::

:::definition[Continuité par morceaux]
$f$ est **continue par morceaux** sur $[a, b]$ s'il existe une subdivision $a = x_0 < x_1 < \cdots < x_n = b$ telle que $f$ est continue sur chaque $]x_{k-1}, x_k[$ et admet des **limites finies** à gauche et à droite en chaque $x_k$. Autrement dit : un **nombre fini de sauts**, tous de hauteur finie. (Notion centrale du chapitre « Suites d'intégrales ».)
:::

:::property[Dérivée et variations]
Si $f$ est dérivable sur un intervalle $I$ :
- $f' > 0$ sur $I$ ⟹ $f$ strictement croissante ; $f' < 0$ ⟹ strictement décroissante ; $f' = 0$ ⟹ $f$ constante ;
- si $f$ admet un extremum en un point **intérieur** $x_0$, alors $f'(x_0) = 0$ ;
- dérivable ⟹ continue (la réciproque est fausse : $|x|$ en $0$).
:::

## 4. Les grands théorèmes

:::theorem[Valeurs intermédiaires (théorème de la bijection)]
Si $f$ est **continue et strictement monotone** sur $[a, b]$, alors pour tout $k$ entre $f(a)$ et $f(b)$, l'équation $f(x) = k$ a **une unique** solution $\alpha \in [a, b]$.

Usage typique : $f$ continue strictement monotone avec $f(a) < 0 < f(b)$ ⟹ $f$ s'annule une seule fois. Pour $f(\alpha) = g(\alpha)$, on applique le théorème à $f - g$.
:::

:::theorem[Rolle]
Si $f$ est continue sur $[a, b]$, dérivable sur $]a, b[$ et $f(a) = f(b)$, alors il existe $c \in ]a, b[$ tel que $f'(c) = 0$ (une tangente horizontale).
:::

:::theorem[Accroissements finis]
Si $f$ est continue sur $[a, b]$ et dérivable sur $]a, b[$, il existe $c \in ]a, b[$ tel que
$$f'(c) = \frac{f(b) - f(a)}{b - a}.$$
Conséquences : $f' = 0$ sur un intervalle ⟹ $f$ constante ; $f' = g'$ ⟹ $f = g + \text{constante}$. C'est exactement pourquoi deux primitives diffèrent d'une constante.
:::

::item{id="pre-theoremes"}

## 5. L'exponentielle

:::definition[Exponentielle]
$y = e^x \iff x = \ln y$ (pour $x \in \mathbb{R}$, $y > 0$). C'est l'unique fonction égale à sa dérivée avec $e^0 = 1$ : en tout point, la pente de la tangente vaut la hauteur de la courbe.
:::

:::key[Formulaire de l'exponentielle]
- **Dérivées** : $(e^x)' = e^x$, $\big(e^{ax+b}\big)' = a\,e^{ax+b}$, $\big(e^{u}\big)' = u'\,e^{u}$. Exemple : $\big(x e^{-x^2}\big)' = (1 - 2x^2)\,e^{-x^2}$.
- **Primitives** : $\int u' e^u = e^u$, $\int e^{ax}\sin(bx)\,dx = \frac{e^{ax}}{a^2 + b^2}\big(a \sin bx - b \cos bx\big)$, $\int e^{ax}\cos(bx)\,dx = \frac{e^{ax}}{a^2 + b^2}\big(a \cos bx + b \sin bx\big)$.
- **Propriétés** : $e^{a+b} = e^a e^b$, $e^{a-b} = \frac{e^a}{e^b}$, $(e^a)^r = e^{ra}$, $e^{-a} = \frac{1}{e^a}$.
- **Limites** : $\lim_{-\infty} e^x = 0$, $\lim_{+\infty} e^x = +\infty$, $\lim_{+\infty} \frac{e^x}{x^n} = +\infty$, $\lim_{-\infty} x^n e^x = 0$, $\lim_{0} \frac{e^x - 1}{x} = 1$.
- **(In)équations** : $e^x = e^y \iff x = y$ ; $e^x < a \iff x < \ln a$ ($a > 0$) ; $e^x < 0$ est impossible.
- **Liens avec ln** : $e^{\ln x} = x$ ($x > 0$), $\ln(e^x) = x$, $a^x = e^{x \ln a}$. Exemple : $e^{2 \ln 3} = 9$.
:::

:::definition[Fonctions hyperboliques]
$$\cosh x = \frac{e^x + e^{-x}}{2}, \qquad \sinh x = \frac{e^x - e^{-x}}{2}, \qquad \tanh x = \frac{\sinh x}{\cosh x}.$$
$\cosh^2 x - \sinh^2 x = 1$ et $\cosh x + \sinh x = e^x$. Dérivées : $\cosh' = \sinh$, $\sinh' = \cosh$ (pas de signe moins, contrairement à cos).
:::

## 6. Le logarithme népérien

:::definition[Logarithme]
$\ln x = \int_1^x \frac{dt}{t}$ pour $x > 0$ : c'est l'aire sous l'hyperbole $\frac{1}{t}$ entre $1$ et $x$ (comptée négativement si $x < 1$).
:::

:::key[Formulaire du logarithme]
- **Domaine** : $\ln u(x)$ existe si $u(x) > 0$ ; $\ln|u(x)|$ si $u(x) \ne 0$. Exemple : $\ln(x - 2)$ est défini sur $]2, +\infty[$.
- **Dérivées** : $(\ln x)' = \frac{1}{x}$, $\big(\ln|u|\big)' = \frac{u'}{u}$, $(\ln x)^{(k)} = (-1)^{k-1}\frac{(k-1)!}{x^k}$.
- **Primitives** : $\int \frac{dx}{x} = \ln|x|$, $\int \frac{u'}{u} = \ln|u|$, $\int \ln x\,dx = x\ln x - x$.
- **Propriétés** : $\ln(ab) = \ln a + \ln b$, $\ln\frac{a}{b} = \ln a - \ln b$, $\ln(a^r) = r \ln a$, $\ln\sqrt{a} = \frac{1}{2}\ln a$.
- **Limites** : $\lim_{0^+} \ln x = -\infty$, $\lim_{+\infty} \ln x = +\infty$, $\lim_{0^+} x^n \ln x = 0$, $\lim_{+\infty} \frac{\ln x}{x^n} = 0$ ($n > 0$), $\lim_0 \frac{\ln(1+x)}{x} = 1$, $\lim_1 \frac{\ln x}{x - 1} = 1$.
- **Inégalités** : $\ln x \le x - 1$ ($x > 0$) et $\frac{x}{1 + x} \le \ln(1 + x) \le x$ ($x > -1$).
- **Logarithme de base $a$** : $\log_a x = \frac{\ln x}{\ln a}$, et $a^x = b \iff x = \log_a b$.
:::

:::key[Deux intégrales du logarithme à connaître]
- $\int_0^1 x^\alpha \ln x\,dx = -\frac{1}{(\alpha + 1)^2}$ pour $\alpha > -1$ (et $\int_0^1 \ln x\,dx = -1$).
- **Bertrand** : $\int_2^{+\infty} \frac{dx}{x^\alpha (\ln x)^\beta}$ converge $\iff$ $\alpha > 1$, ou ($\alpha = 1$ et $\beta > 1$). Ces deux résultats reviennent sans cesse au chapitre des intégrales généralisées.
:::

::item{id="pre-exp-ln"}
