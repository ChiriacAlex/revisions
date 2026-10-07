---
title: Ch1 ter — Fonctions trigonométriques, règles de Bioche, intégrales abéliennes
summary: "Primitives de sinᵐ·cosⁿ, de sin(mx)cos(nx), règles de Bioche, fonctions hyperboliques, intégrales abéliennes (racines n-ièmes et racines de trinômes) et changements de variable trigonométriques."
tags: [chapitre 1, trigonométrie, Bioche, intégrales abéliennes]
minutes: 90
---

## 1. Objectifs

Ici, l'intégrande contient des $\sin$, $\cos$, $\cosh$, $\sinh$ ou des racines. Le but est toujours de **se ramener à une fraction rationnelle** (chapitre précédent) par un bon changement de variable. Tu dois savoir :

- traiter $\int \sin^m x \cos^n x\,dx$ selon la parité de $m$ et $n$ ;
- transformer $\sin(mx)\cos(nx)$ en somme ;
- choisir le changement de variable avec les **règles de Bioche** ;
- traiter les **intégrales abéliennes** $\int F\left(x, \sqrt[n]{\frac{ax + b}{cx + d}}\right)dx$ et $\int F\left(x, \sqrt{ax^2 + bx + c}\right)dx$.

## 2. Les intégrales sinᵐ x cosⁿ x

:::method[Selon la parité]
1. **$m$ impair** ($m = 2k + 1$) : on garde un $\sin x$ et on écrit $\sin^{2k} x = (1 - \cos^2 x)^k$. Avec $t = \cos x$ ($dt = -\sin x\,dx$) :
$\int \sin^m x \cos^n x\,dx = -\int (1 - t^2)^k t^n\,dt$.
2. **$n$ impair** ($n = 2k + 1$) : on garde un $\cos x$, $\cos^{2k} x = (1 - \sin^2 x)^k$, et $t = \sin x$ :
$\int \sin^m x \cos^n x\,dx = \int (1 - t^2)^k t^m\,dt$.
3. **$m$ et $n$ pairs** : on **linéarise** avec $\sin^2 x = \frac{1 - \cos 2x}{2}$, $\cos^2 x = \frac{1 + \cos 2x}{2}$, $\sin x\cos x = \frac{\sin 2x}{2}$.
:::

:::example[Les quatre exemples du cours]
- $\int \sin^3 x \cos^2 x\,dx = -\int (1 - t^2)t^2\,dt = \frac{\cos^5 x}{5} - \frac{\cos^3 x}{3} + C$ ($t = \cos x$).
- $\int \cos^5 x\,dx = \int (1 - t^2)^2\,dt = \sin x - \frac{2\sin^3 x}{3} + \frac{\sin^5 x}{5} + C$ ($t = \sin x$).
- $\int \sin^2 x\cos^2 x\,dx = \frac{1}{4}\int \sin^2 2x\,dx = \frac{1}{8}\int(1 - \cos 4x)\,dx = \frac{x}{8} - \frac{\sin 4x}{32} + C$.
- $\int \sin^2 x\cos^4 x\,dx = \frac{1}{8}\int (1 + \cos 2x - \cos^2 2x - \cos^3 2x)\,dx = \frac{x}{16} - \frac{\sin 4x}{64} + \frac{\sin^3 2x}{48} + C$.
:::

:::example[Puissances paires seules]
$\int \sin^2 x\,dx = \frac{x}{2} - \frac{\sin 2x}{4} + C$, $\quad \int \cos^2 x\,dx = \frac{x}{2} + \frac{\sin 2x}{4} + C$, $\quad \int \tan^2 x\,dx = \int\left(\frac{1}{\cos^2 x} - 1\right)dx = \tan x - x + C$.
:::

## 3. Produits sin(mx) cos(nx)

On transforme le produit en somme (voir le formulaire de trigonométrie) :
$$\cos a\cos b = \tfrac{1}{2}[\cos(a - b) + \cos(a + b)], \quad \sin a\sin b = \tfrac{1}{2}[\cos(a - b) - \cos(a + b)], \quad \sin a\cos b = \tfrac{1}{2}[\sin(a + b) + \sin(a - b)].$$

:::example[Exemple]
$\int \cos 5x \sin 3x\,dx = \frac{1}{2}\int (\sin 8x - \sin 2x)\,dx = \frac{\cos 2x}{4} - \frac{\cos 8x}{16} + C$.
:::

## 4. Règles de Bioche

Soit à calculer $\int f(x)\,dx$ avec $f$ fraction rationnelle en $\sin x$ et $\cos x$. On regarde l'**élément différentiel** $\omega(x) = f(x)\,dx$ (le $dx$ compte : changer $x$ en $-x$ change $dx$ en $-dx$).

:::method[Règles de Bioche]
1. Si $\omega(-x) = \omega(x)$ : poser $t = \cos x$.
2. Si $\omega(\pi - x) = \omega(x)$ : poser $t = \sin x$.
3. Si $\omega(\pi + x) = \omega(x)$ : poser $t = \tan x$ (alors $dt = (1 + t^2)\,dx$).
4. Si **deux** des trois invariances sont vraies (alors les trois le sont) : poser $t = \cos 2x$.
5. **Sinon** : $t = \tan\frac{x}{2}$, avec
$$\cos x = \frac{1 - t^2}{1 + t^2}, \qquad \sin x = \frac{2t}{1 + t^2}, \qquad \tan x = \frac{2t}{1 - t^2}, \qquad dx = \frac{2\,dt}{1 + t^2}.$$
Ce dernier changement marche **toujours**, mais donne souvent des fractions plus lourdes.
:::

:::intuition[Moyen mnémotechnique]
On pose $t$ = la fonction **invariante** par la même transformation : $\cos$ est invariant par $x \mapsto -x$, $\sin$ par $x \mapsto \pi - x$, $\tan$ par $x \mapsto \pi + x$.
:::

:::example[Exemples 37 du cours]
- **a)** $\omega = \frac{\sin t}{1 + \cos^2 t}\,dt$ est invariant par $t \mapsto -t$ (deux signes moins). On pose $u = \cos t$ : $\int = -\int \frac{du}{1 + u^2} = -\arctan(\cos t) + C$.
- **b)** $\omega = \frac{\cos t}{\sin^2 t - \cos^2 t}\,dt$ est invariant par $t \mapsto \pi - t$. Avec $u = \sin t$ : $\int \frac{du}{u^2 - (1 - u^2)} = \int \frac{du}{2u^2 - 1} = \frac{1}{2\sqrt{2}}\ln\left|\frac{\sin t - \frac{1}{\sqrt{2}}}{\sin t + \frac{1}{\sqrt{2}}}\right| + C$.
- **c)** $\omega = \frac{dt}{\cos^2 t\,(1 + \tan t)}$ est invariant par $t \mapsto \pi + t$. Avec $u = \tan t$, $du = \frac{dt}{\cos^2 t}$ : $\int \frac{du}{1 + u} = \ln|1 + \tan t| + C$.
- **d)** $\omega = \frac{dt}{1 + \cos t}$ : aucune invariance. Avec $u = \tan\frac{t}{2}$ : $\int \frac{1 + u^2}{2}\cdot\frac{2\,du}{1 + u^2} = u = \tan\frac{t}{2} + C$.
:::

:::warning[Erreur dans le poly (exemple 37 c)]
Le poly conclut $\int \frac{du}{1 + u} = \ln|u| + C = \ln|\tan t| + C$. C'est faux : $\int \frac{du}{1 + u} = \ln|1 + u|$. La bonne réponse est $\ln|1 + \tan t| + C$.
:::

::item{id="trig-bioche"}

## 5. Fonctions hyperboliques

:::method[Transposer Bioche]
Pour $\int F(\cosh x, \sinh x)\,dx$ : on regarde quel changement Bioche proposerait pour $\int F(\cos x, \sin x)\,dx$ et on prend l'**analogue hyperbolique** : $\cos x \to \cosh x$, $\sin x \to \sinh x$, $\tan x \to \tanh x$, $\cos 2x \to \cosh 2x$. Dans les autres cas, $t = \tanh\frac{x}{2}$ marche, mais **$t = e^x$ est en général plus simple** (tout devient une fraction rationnelle en $t$).
:::

:::example[Avec t = tanh(x/2)]
$\int \frac{dx}{-5 + 13\cosh x}$ : avec $t = \tanh\frac{x}{2}$, $\cosh x = \frac{1 + t^2}{1 - t^2}$ et $dx = \frac{2\,dt}{1 - t^2}$, on obtient $\int \frac{dt}{4 + 9t^2} = \frac{1}{6}\arctan\left(\frac{3}{2}\tanh\frac{x}{2}\right) + C$.
:::

## 6. Intégrales abéliennes de première espèce

Elles sont de la forme $\int F\left(x, \sqrt[n]{\frac{ax + b}{cx + d}}\right)dx$ avec $F$ rationnelle.

:::method[Poser t = la racine]
$t = \sqrt[n]{\frac{ax + b}{cx + d}}$ donne $t^n = \frac{ax + b}{cx + d}$, d'où $x = -\frac{d\,t^n - b}{c\,t^n - a}$ et $dx = -\frac{n(ad - bc)\,t^{n-1}}{(c\,t^n - a)^2}\,dt$ : on obtient une fraction rationnelle en $t$. Cas fréquent : $n = 2$ et $c = 0$, c'est-à-dire $t = \sqrt{ax + b}$.
:::

:::example[Exemples 38]
Avec $t = \sqrt{x - 1}$, $x = t^2 + 1$, $dx = 2t\,dt$ :
- $\int \frac{dx}{x + \sqrt{x - 1}} = \int \frac{2t\,dt}{t^2 + t + 1} = \ln(t^2 + t + 1) - \frac{2}{\sqrt{3}}\arctan\frac{2t + 1}{\sqrt{3}} + C$, avec $t^2 + t + 1 = x + \sqrt{x - 1}$ ;
- $\int \frac{dx}{x\sqrt{x - 1}} = \int \frac{2t\,dt}{t(t^2 + 1)} = 2\arctan\sqrt{x - 1} + C$.
:::

## 7. Intégrales abéliennes de seconde espèce

Elles sont de la forme $\int F\left(x, \sqrt{ax^2 + bx + c}\right)dx$.

:::method[Changements d'Euler]
- Si $a > 0$ : poser $\sqrt{ax^2 + bx + c} = x\sqrt{a} + t$.
- Si $a < 0$ (il faut alors $\Delta \ge 0$, racines $\alpha$ et $\beta$) : poser $\sqrt{ax^2 + bx + c} = t(x - \alpha)$, c'est-à-dire $t = \sqrt{a\frac{x - \beta}{x - \alpha}}$.
:::

:::example[Exemple 39]
$\int \frac{dx}{x\sqrt{x^2 + 6x + 10}}$ : $a = 1 > 0$, on pose $\sqrt{x^2 + 6x + 10} = x + t$. Alors $x = \frac{t^2 - 10}{2(3 - t)}$ et le calcul aboutit à
$$\int \frac{dx}{x\sqrt{x^2 + 6x + 10}} = \frac{1}{\sqrt{10}}\ln\left|\frac{t - \sqrt{10}}{t + \sqrt{10}}\right| + C, \qquad t = \sqrt{x^2 + 6x + 10} - x.$$
:::

### Les racines de trinômes : substitution trigonométrique

:::method[Forme canonique puis triangle de référence]
On écrit $ax^2 + bx + c$ (à une constante près) sous l'une des trois formes, avec $u = u(x)$ affine :

| forme | changement | car |
|---|---|---|
| $k^2 - u^2$ | $u = k\sin\theta$ (ou $k\cos\theta$) | $k^2 - k^2\sin^2\theta = k^2\cos^2\theta$ |
| $k^2 + u^2$ | $u = k\sinh\theta$ (ou $k\tan\theta$) | $k^2 + k^2\sinh^2\theta = k^2\cosh^2\theta$ |
| $u^2 - k^2$ | $u = k\cosh\theta$ (ou $\frac{k}{\cos\theta}$) | $k^2\cosh^2\theta - k^2 = k^2\sinh^2\theta$ |

La racine disparaît, et on revient à $x$ à la fin (le « triangle de référence » donne $\cos\theta$, $\tan\theta$… en fonction de $u$).
:::

:::example[Exemples 40 et 41]
- $\int \frac{x^2\,dx}{\sqrt{9 - x^2}}$ : $x = 3\sin t$, $dx = 3\cos t\,dt$, $\sqrt{9 - x^2} = 3\cos t$, donc $\int 9\sin^2 t\,dt = \frac{9}{2}(t - \sin t\cos t)$, soit
$\frac{9}{2}\arcsin\frac{x}{3} - \frac{x}{2}\sqrt{9 - x^2} + C$.
- $\int \sqrt{x^2 + 2x + 5}\,dx$ : $x^2 + 2x + 5 = (x + 1)^2 + 2^2$, $x + 1 = 2\sinh t$, donc $4\int \cosh^2 t\,dt = 2t + \sinh 2t$, soit
$2\operatorname{argsh}\frac{x + 1}{2} + \frac{(x + 1)\sqrt{x^2 + 2x + 5}}{2} + C$.
- $\int \sqrt{-x^2 + 4x - 3}\,dx$ : $-x^2 + 4x - 3 = 1 - (x - 2)^2$, $x - 2 = \sin t$, donc $\int \cos^2 t\,dt = \frac{t}{2} + \frac{\sin 2t}{4}$, soit
$\frac{1}{2}\arcsin(x - 2) + \frac{(x - 2)\sqrt{-x^2 + 4x - 3}}{2} + C$.
:::

::item{id="trig-abeliennes"}

## 8. Synthèse : quel changement de variable ?

:::key[Arbre de décision]
| l'intégrande contient… | on pose… |
|---|---|
| $\sin^m x\cos^n x$, une puissance impaire | $t = \cos x$ ($m$ impair) ou $t = \sin x$ ($n$ impair) |
| $\sin^m x\cos^n x$, tout pair | linéarisation |
| $\sin(mx)\cos(nx)$ | produit → somme |
| une fraction en $\sin$, $\cos$ | Bioche ; à défaut $t = \tan\frac{x}{2}$ |
| une fraction en $\cosh$, $\sinh$ | Bioche hyperbolique ; à défaut $t = e^x$ |
| $\sqrt[n]{\frac{ax + b}{cx + d}}$ | $t$ = cette racine |
| $\sqrt{k^2 - u^2}$, $\sqrt{k^2 + u^2}$, $\sqrt{u^2 - k^2}$ | $u = k\sin\theta$, $k\sinh\theta$, $k\cosh\theta$ |
:::
