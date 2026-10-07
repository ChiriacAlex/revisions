---
title: Ch2 — Développements limités
summary: "Taylor-Young, DL usuels, combinaison linéaire, produit, composition, primitivation et quotient de DL, équivalents et calcul de limites — les exemples du cours recalculés."
tags: [chapitre 2, développements limités, Taylor-Young, équivalents]
minutes: 90
---

## 1. Objectifs

Un **développement limité** (DL) approche une fonction, au voisinage d'un point, par un **polynôme**. C'est l'outil n°1 pour :

- lever les formes indéterminées (calcul de limites) ;
- trouver un **équivalent** d'une fonction — exactement ce qu'il faut pour étudier la convergence d'une intégrale généralisée.

## 2. Formule de Taylor-Young

:::theorem[Taylor-Young]
Si $f$ est $n$ fois dérivable sur un intervalle $I$ contenant $a$ (à l'intérieur), alors $f$ admet un DL à l'ordre $n$ en $a$ :
$$f(x) = f(a) + \frac{f'(a)}{1!}(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x - a)^n + (x - a)^n\varepsilon(x), \qquad \lim_{x \to a}\varepsilon(x) = 0.$$
Le polynôme est la **partie régulière** ; le reste $(x - a)^n\varepsilon(x)$ se note aussi $o\big((x - a)^n\big)$.
:::

:::intuition[Ce que veut dire « ordre n »]
L'erreur commise est **négligeable devant $(x - a)^n$** : plus l'ordre est grand, plus l'approximation colle à la fonction près de $a$. Loin de $a$, un DL ne dit rien.
:::

:::property[Parité]
Si $f$ est **paire**, sa partie régulière en $0$ ne contient que des puissances **paires** ; si $f$ est **impaire**, que des puissances **impaires**. D'où le « bonus » d'un ordre : $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} + o(x^5)$ (le terme en $x^5$ est nul).
:::

## 3. Les DL usuels en 0

:::key[À connaître par cœur]
| fonction | DL en $0$ |
|---|---|
| $e^x$ | $1 + x + \frac{x^2}{2!} + \cdots + \frac{x^n}{n!} + o(x^n)$ |
| $\cosh x$ | $1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \cdots + \frac{x^{2n}}{(2n)!} + o(x^{2n+1})$ |
| $\sinh x$ | $x + \frac{x^3}{3!} + \cdots + \frac{x^{2n+1}}{(2n+1)!} + o(x^{2n+2})$ |
| $\cos x$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots + (-1)^n\frac{x^{2n}}{(2n)!} + o(x^{2n+1})$ |
| $\sin x$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots + (-1)^n\frac{x^{2n+1}}{(2n+1)!} + o(x^{2n+2})$ |
| $\tan x$ | $x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + o(x^8)$ |
| $\tanh x$ | $x - \frac{x^3}{3} + \frac{2x^5}{15} - \frac{17x^7}{315} + o(x^8)$ |
| $(1 + x)^\alpha$ | $1 + \alpha x + \frac{\alpha(\alpha - 1)}{2!}x^2 + \cdots + \frac{\alpha(\alpha - 1)\cdots(\alpha - n + 1)}{n!}x^n + o(x^n)$ |
| $\frac{1}{1 - x}$ | $1 + x + x^2 + \cdots + x^n + o(x^n)$ |
| $\frac{1}{1 + x}$ | $1 - x + x^2 - \cdots + (-1)^n x^n + o(x^n)$ |
| $\sqrt{1 + x}$ | $1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - \frac{5x^4}{128} + o(x^4)$ |
| $\frac{1}{\sqrt{1 + x}}$ | $1 - \frac{x}{2} + \frac{3x^2}{8} - \frac{5x^3}{16} + o(x^3)$ |
| $\ln(1 + x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)$ |
| $\ln(1 - x)$ | $-x - \frac{x^2}{2} - \frac{x^3}{3} - \cdots - \frac{x^n}{n} + o(x^n)$ |
| $\arctan x$ | $x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots + (-1)^n\frac{x^{2n+1}}{2n+1} + o(x^{2n+2})$ |
| $\operatorname{argth} x$ | $x + \frac{x^3}{3} + \frac{x^5}{5} + \cdots + \frac{x^{2n+1}}{2n+1} + o(x^{2n+2})$ |
| $\arcsin x$ | $x + \frac{1}{2}\cdot\frac{x^3}{3} + \frac{1 \cdot 3}{2 \cdot 4}\cdot\frac{x^5}{5} + \cdots + o(x^{2n+2})$ |
| $\operatorname{argsh} x$ | $x - \frac{1}{2}\cdot\frac{x^3}{3} + \frac{1 \cdot 3}{2 \cdot 4}\cdot\frac{x^5}{5} - \cdots + o(x^{2n+2})$ |
| $\arccos x$ | $\frac{\pi}{2} - \arcsin x$ |
:::

## 4. Opérations sur les DL

:::property[Combinaison linéaire]
Si $f$ et $g$ ont des DL à l'ordre $n$, $\lambda f + \mu g$ aussi : on combine les parties régulières.
:::

:::example[Exemples 1 et 2]
- $\frac{1}{1 - x} - e^x = (1 + x + x^2 + x^3) - \left(1 + x + \frac{x^2}{2} + \frac{x^3}{6}\right) + o(x^3) = \frac{x^2}{2} + \frac{5x^3}{6} + o(x^3)$.
- $\sqrt{1 + x} + \sqrt{1 - x} = 2 - \frac{x^2}{4} - \frac{5x^4}{64} + o(x^4)$ (les termes impairs s'annulent).
:::

:::property[Produit]
On multiplie les parties régulières et on **ne garde que les monômes de degré $\le n$**.
:::

:::example[Exemples 3 et 4]
- $\sin x\cos x = \left(x - \frac{x^3}{6} + \frac{x^5}{120}\right)\left(1 - \frac{x^2}{2} + \frac{x^4}{24}\right) + o(x^5) = x - \frac{2x^3}{3} + \frac{2x^5}{15} + o(x^5)$ ; on le retrouve avec $\frac{\sin 2x}{2}$.
- $(1 + x^3)\sqrt{1 - x} = (1 + x^3)\left(1 - \frac{x}{2} - \frac{x^2}{8} - \frac{x^3}{16}\right) + o(x^3) = 1 - \frac{x}{2} - \frac{x^2}{8} + \frac{15x^3}{16} + o(x^3)$.
- $\frac{e^x}{1 + x} = e^x \cdot \frac{1}{1 + x} = 1 + \frac{x^2}{2} - \frac{x^3}{3} + o(x^3)$.
:::

:::warning[Erreur dans le poly (exemple 4)]
Le poly donne $\frac{5x^3}{16}$ comme coefficient de $x^3$. Or le $x^3$ du facteur $1 + x^3$, multiplié par le $1$ de $\sqrt{1 - x}$, donne $+x^3$, qui s'ajoute à $-\frac{x^3}{16}$ : $1 - \frac{1}{16} = \frac{15}{16}$.
:::

:::property[Composition]
Si $g(b) = a$, on obtient le DL de $f \circ g$ en $b$ en **substituant** la partie régulière de $g$ dans celle de $f$ et en tronquant à l'ordre $n$. Il faut que la quantité substituée **tende vers 0** (le point où $f$ est développée).
:::

:::example[Exemples 6, 7, 8]
- $\sin(2x) = 2x - \frac{(2x)^3}{6} + \frac{(2x)^5}{120} + o(x^5) = 2x - \frac{4x^3}{3} + \frac{4x^5}{15} + o(x^5)$.
- $\sin(x^2) = x^2 + o(x^5)$ et $\frac{1}{1 + x^2} = 1 - x^2 + x^4 - x^6 + o(x^6)$.
- $e^{\cos x} = e^{1 - x^2/2 + o(x^3)} = e \cdot e^{-x^2/2 + o(x^3)} = e - \frac{e}{2}x^2 + o(x^3)$ (on factorise $e^1$ pour substituer une quantité qui tend vers $0$).
- $\frac{1}{1 + \cos x} = \frac{1}{2 - x^2/2 + o(x^2)} = \frac{1}{2}\cdot\frac{1}{1 - x^2/4 + o(x^2)} = \frac{1}{2} + \frac{x^2}{8} + o(x^2)$.
:::

:::property[Primitivation]
Si $f'$ a pour DL $a_0 + a_1 x + \cdots + a_n x^n + o(x^n)$, alors $f(x) = f(0) + a_0 x + a_1\frac{x^2}{2} + \cdots + a_n\frac{x^{n+1}}{n+1} + o(x^{n+1})$. **Ne pas oublier la constante $f(0)$.**
:::

:::example[ln, arctan, arcsin par primitivation]
- $\frac{1}{1 + x} = \sum (-1)^k x^k$ donne $\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$
- $\frac{1}{1 + x^2} = 1 - x^2 + x^4 - \cdots + (-1)^n x^{2n} + o(x^{2n+1})$ donne
$$\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots + (-1)^n\frac{x^{2n+1}}{2n + 1} + o(x^{2n+2}).$$
- $\frac{1}{\sqrt{1 - x^2}} = 1 + \frac{x^2}{2} + \frac{3x^4}{8} + \cdots$ donne $\arcsin x = x + \frac{x^3}{6} + \frac{3x^5}{40} + \cdots$
:::

:::warning[Erreur dans le poly (§ 3.4.2)]
Le poly écrit le terme général de $\arctan$ sous la forme $(-1)^n\frac{x^{2n+2}}{2n + 2}$. En intégrant $(-1)^n x^{2n}$, on obtient $(-1)^n\frac{x^{2n+1}}{2n + 1}$ : arctan est **impaire**, elle n'a que des puissances impaires (son propre tableau des DL usuels donne d'ailleurs la bonne formule).
:::

### Quotient

:::method[Cas où le dénominateur ne s'annule pas en 0]
Si $g(0) \ne 0$, $\frac{f}{g}$ a un DL d'ordre $n$ : on fait la **division selon les puissances croissantes** de la partie régulière de $f$ par celle de $g$, jusqu'à l'ordre $n$. Autre méthode souvent plus rapide : écrire $\frac{1}{g} = \frac{1}{g(0)}\cdot\frac{1}{1 + u}$ avec $u \to 0$, puis utiliser $\frac{1}{1 + u} = 1 - u + u^2 - \cdots$
:::

:::example[tan x à l'ordre 5]
$\tan x = \frac{x - \frac{x^3}{6} + \frac{x^5}{120}}{1 - \frac{x^2}{2} + \frac{x^4}{24}} = x + \frac{x^3}{3} + \frac{2x^5}{15} + o(x^5)$ (division selon les puissances croissantes).
:::

:::method[Cas où le dénominateur s'annule en 0]
Si $\lim_0 g = 0$ mais $\lim_0 f \ne 0$, $\frac{f}{g}$ n'a pas de DL (elle tend vers l'infini). Si les deux s'annulent, $f = a_p x^p + \cdots$ et $g = b_q x^q + \cdots$ ($a_p, b_q \ne 0$) :
- si $p < q$ : $\frac{f}{g} \to \infty$ en $0$, pas de DL ;
- si $p \ge q$ : on simplifie par $x^q$, on est ramené au cas précédent. **Pour un DL d'ordre $n$ du quotient, il faut développer $f$ et $g$ à l'ordre $n + q$.**
:::

:::example[Exemple 11 : ln(1+x)/sin x à l'ordre 3]
$\sin x = x\left(1 - \frac{x^2}{6} + o(x^3)\right)$ et $\ln(1 + x) = x\left(1 - \frac{x}{2} + \frac{x^2}{3} - \frac{x^3}{4} + o(x^3)\right)$ (développés à l'ordre $4$). Donc
$$\frac{\ln(1 + x)}{\sin x} = \left(1 - \frac{x}{2} + \frac{x^2}{3} - \frac{x^3}{4}\right)\left(1 + \frac{x^2}{6}\right) + o(x^3) = 1 - \frac{x}{2} + \frac{x^2}{2} - \frac{x^3}{3} + o(x^3).$$
:::

:::warning[Erreur dans le poly (exemple 11)]
Le poly termine sa division par $-\frac{x^3}{4}$. Le terme en $x^3$ vaut $-\frac{1}{4} + \left(-\frac{1}{2}\right)\cdot\frac{1}{6} = -\frac{1}{4} - \frac{1}{12} = -\frac{1}{3}$ (une étape de la division est oubliée).
:::

::item{id="dl-calculs"}

## 5. Application : équivalents et limites

:::key[Le premier terme non nul donne un équivalent]
Si $f(x) = a_p x^p + o(x^p)$ avec $a_p \ne 0$, alors $f(x) \underset{0}{\sim} a_p x^p$. Équivalents classiques en $0$ :
$$\sin x \sim x, \quad \tan x \sim x, \quad \ln(1 + x) \sim x, \quad e^x - 1 \sim x, \quad 1 - \cos x \sim \frac{x^2}{2}, \quad \cosh x - 1 \sim \frac{x^2}{2}, \quad \arctan x \sim x,$$
$$(1 + x)^\alpha - 1 \sim \alpha x, \qquad e^x - 1 - x \sim \frac{x^2}{2}, \qquad \sin x - x \sim -\frac{x^3}{6}.$$
On peut **multiplier, diviser, élever à une puissance** des équivalents, mais **jamais les additionner** (ni composer sans précaution).
:::

:::example[Exemple 13]
Calculer $\lim_{x \to 0^-} \frac{x^2\sqrt{\cosh x - 1}}{\sin(\tan^2 x)\ln(1 + x)}$.

- Numérateur : $\cosh x - 1 \sim \frac{x^2}{2}$, donc $\sqrt{\cosh x - 1} \sim \sqrt{\frac{x^2}{2}} = \frac{|x|}{\sqrt{2}} = -\frac{x}{\sqrt{2}}$ puisque $x < 0$. Le numérateur est équivalent à $-\frac{x^3}{\sqrt{2}}$.
- Dénominateur : $\tan^2 x \sim x^2 \to 0$, donc $\sin(\tan^2 x) \sim x^2$ ; et $\ln(1 + x) \sim x$. Le dénominateur est équivalent à $x^3$.

Donc la limite vaut $-\frac{1}{\sqrt{2}} = -\frac{\sqrt{2}}{2} \approx -0{,}707$.
:::

:::warning[Erreur dans le poly (exemple 13)]
Le poly écrit $\sqrt{\frac{x^2}{2}} = \frac{|x|}{2}$ et trouve $-\frac{1}{2}$. Or $\sqrt{\frac{x^2}{2}} = \frac{|x|}{\sqrt{2}}$ : la racine porte aussi sur le $2$. La limite est $-\frac{\sqrt{2}}{2}$.
:::

::item{id="dl-limites"}
