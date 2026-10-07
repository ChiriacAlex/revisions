---
title: Ch0 bis — Trigonométrie et fonctions réciproques
summary: "Valeurs remarquables, symétries, formules d'addition, produits ↔ sommes, angle double, linéarisation, équations, dérivées, et les fonctions arcsin, arccos, arctan : tout ce qu'il faut pour intégrer des fonctions trigonométriques."
tags: [prérequis, trigonométrie, arcsin, arctan, formulaire]
minutes: 45
---

## 1. Pourquoi ce formulaire ?

Au chapitre des primitives, presque tous les calculs « trigonométriques » se ramènent à **une formule à reconnaître** : linéariser $\sin^2$, transformer $\sin a \cos b$ en somme, reconnaître $\frac{u'}{1 + u^2}$… Ce chapitre est un **formulaire commenté** : apprends-le par cœur, chaque formule y est vérifiée.

## 2. Valeurs remarquables

| $\alpha$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ | $\frac{3\pi}{2}$ |
|---|---|---|---|---|---|---|---|
| $\cos\alpha$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-1$ | $0$ |
| $\sin\alpha$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $0$ | $-1$ |
| $\tan\alpha$ | $0$ | $\frac{1}{\sqrt{3}}$ | $1$ | $\sqrt{3}$ | non défini | $0$ | non défini |

:::intuition[Retenir le tableau]
Pour $\sin$ de $0$ à $\frac{\pi}{2}$ : $\frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2}$. Pour $\cos$, la même suite à l'envers.
:::

## 3. Symétries et périodicité

:::key[Angles associés]
- $\cos(-\alpha) = \cos\alpha$, $\sin(-\alpha) = -\sin\alpha$, $\tan(-\alpha) = -\tan\alpha$.
- $\cos(\pi - \alpha) = -\cos\alpha$, $\sin(\pi - \alpha) = \sin\alpha$, $\tan(\pi - \alpha) = -\tan\alpha$.
- $\cos(\pi + \alpha) = -\cos\alpha$, $\sin(\pi + \alpha) = -\sin\alpha$, $\tan(\pi + \alpha) = \tan\alpha$.
- $\cos\left(\frac{\pi}{2} - \alpha\right) = \sin\alpha$, $\sin\left(\frac{\pi}{2} - \alpha\right) = \cos\alpha$, $\tan\left(\frac{\pi}{2} - \alpha\right) = \cot\alpha$.
- $\cos\left(\frac{\pi}{2} + \alpha\right) = -\sin\alpha$, $\sin\left(\frac{\pi}{2} + \alpha\right) = \cos\alpha$, $\tan\left(\frac{\pi}{2} + \alpha\right) = -\cot\alpha$.
- Périodes : $2\pi$ pour $\cos$ et $\sin$, $\pi$ pour $\tan$.
- $\sin\left(n\frac{\pi}{2}\right)$ vaut $0$ ($n$ pair), $1$ ($n = 1, 5, 9, \ldots$), $-1$ ($n = 3, 7, 11, \ldots$) ; $\cos\left(n\frac{\pi}{2}\right)$ vaut $0$ ($n$ impair), $1$ ($n = 0, 4, 8, \ldots$), $-1$ ($n = 2, 6, 10, \ldots$).
:::

:::warning[Coquille dans la fiche du prof]
Sur la fiche « Formules trigonométriques », le troisième bloc (formules 7 à 9) est titré « Angle $(\pi - \alpha)$ » : il s'agit en réalité de l'angle $(\pi + \alpha)$, comme ci-dessus.
:::

## 4. Addition et angle double

:::key[Formules d'addition]
$$\cos(a \pm b) = \cos a \cos b \mp \sin a \sin b, \qquad \sin(a \pm b) = \sin a \cos b \pm \cos a \sin b,$$
$$\tan(a \pm b) = \frac{\tan a \pm \tan b}{1 \mp \tan a \tan b}.$$
:::

:::key[Angle double et linéarisation]
$$\sin 2a = 2 \sin a \cos a, \qquad \cos 2a = \cos^2 a - \sin^2 a = 2\cos^2 a - 1 = 1 - 2\sin^2 a, \qquad \tan 2a = \frac{2\tan a}{1 - \tan^2 a},$$
$$\sin^2 a = \frac{1 - \cos 2a}{2}, \qquad \cos^2 a = \frac{1 + \cos 2a}{2}, \qquad \sin a \cos a = \frac{\sin 2a}{2}.$$
Ces trois dernières formules servent à **linéariser** : c'est la clé de $\int \sin^2 x\,dx$ et de tous les $\int \sin^m x \cos^n x\,dx$ avec $m, n$ pairs.
:::

## 5. Produits ↔ sommes

:::key[Produits en sommes (pour intégrer)]
$$\cos a \cos b = \tfrac{1}{2}\big[\cos(a - b) + \cos(a + b)\big],$$
$$\sin a \sin b = \tfrac{1}{2}\big[\cos(a - b) - \cos(a + b)\big],$$
$$\sin a \cos b = \tfrac{1}{2}\big[\sin(a + b) + \sin(a - b)\big].$$
Exemple : $\cos 5x \sin 3x = \frac{1}{2}\big[\sin 8x - \sin 2x\big]$.
:::

:::key[Sommes en produits (pour factoriser)]
$$\sin p + \sin q = 2 \sin\tfrac{p+q}{2}\cos\tfrac{p-q}{2}, \qquad \sin p - \sin q = 2 \sin\tfrac{p-q}{2}\cos\tfrac{p+q}{2},$$
$$\cos p + \cos q = 2 \cos\tfrac{p+q}{2}\cos\tfrac{p-q}{2}, \qquad \cos p - \cos q = -2 \sin\tfrac{p+q}{2}\sin\tfrac{p-q}{2},$$
$$\cos\alpha + \sin\alpha = \sqrt{2}\sin\left(\tfrac{\pi}{4} + \alpha\right), \qquad \cos\alpha - \sin\alpha = \sqrt{2}\sin\left(\tfrac{\pi}{4} - \alpha\right),$$
$$\cot a + \cot b = \frac{\sin(a + b)}{\sin a \sin b}, \qquad \cot a - \cot b = \frac{\sin(b - a)}{\sin a \sin b}.$$
:::

:::warning[Erreur dans la fiche du prof (formule 40)]
La fiche écrit $\cot\alpha - \cot\beta = \frac{\sin(\alpha - \beta)}{\sin\alpha \sin\beta}$ : le signe est faux. En effet $\frac{\cos\alpha}{\sin\alpha} - \frac{\cos\beta}{\sin\beta} = \frac{\sin\beta\cos\alpha - \cos\beta\sin\alpha}{\sin\alpha\sin\beta} = \frac{\sin(\beta - \alpha)}{\sin\alpha\sin\beta}$.
:::

## 6. Équations trigonométriques

:::key[Résoudre]
- $\cos x = \cos\alpha \iff x = \alpha + 2k\pi$ ou $x = -\alpha + 2k\pi$ ;
- $\sin x = \sin\alpha \iff x = \alpha + 2k\pi$ ou $x = \pi - \alpha + 2k\pi$ ;
- $\tan x = \tan\alpha \iff x = \alpha + k\pi$ ;
- cas particuliers : $\sin x = 0 \iff x = k\pi$ ; $\cos x = 0 \iff x = \frac{\pi}{2} + k\pi$ ; $\sin x = \pm 1 \iff x = \frac{\pi}{2} + k\pi$.
:::

## 7. Dérivées et primitives

:::key[Dérivées]
$\cos'(u) = -u' \sin u$, $\quad \sin'(u) = u' \cos u$, $\quad \tan'(u) = \frac{u'}{\cos^2 u} = u'(1 + \tan^2 u)$, $\quad \cot'(u) = -\frac{u'}{\sin^2 u}$, $\quad \cos^{(n)} x = \cos\left(x + n\frac{\pi}{2}\right)$, $\quad \sin^{(n)} x = \sin\left(x + n\frac{\pi}{2}\right)$.
:::

:::key[Primitives]
$$\int \cos x\,dx = \sin x, \quad \int \sin x\,dx = -\cos x, \quad \int \tan x\,dx = -\ln|\cos x|, \quad \int \cot x\,dx = \ln|\sin x|.$$
:::

:::warning[Erreur dans la fiche du prof (formule 75)]
La fiche donne $\int \cot x\,dx = -\ln|\sin x|$. C'est faux : $\cot x = \frac{\cos x}{\sin x} = \frac{u'}{u}$ avec $u = \sin x$, donc $\int \cot x\,dx = +\ln|\sin x| + C$. (La « Table of Basic Integrals » du même prof donne bien le bon signe.)
:::

## 8. Formules d'Euler

$$\cos x = \frac{e^{ix} + e^{-ix}}{2}, \qquad \sin x = \frac{e^{ix} - e^{-ix}}{2i}, \qquad \tan x = i\,\frac{1 - e^{2ix}}{1 + e^{2ix}}, \qquad \cot x = i\,\frac{e^{2ix} + 1}{e^{2ix} - 1}.$$

:::warning[Erreur dans la fiche du prof (formule 87)]
La fiche écrit $\cot x = i\frac{1 + e^{2ix}}{1 - e^{2ix}}$ : c'est l'opposé. Comme $\cot = \frac{1}{\tan}$, on a $\cot x = \frac{1 + e^{2ix}}{i(1 - e^{2ix})} = -i\,\frac{1 + e^{2ix}}{1 - e^{2ix}}$.
:::

## 9. Fonctions réciproques

:::definition[arcsin, arccos, arctan]
- $\arcsin : [-1, 1] \to \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ : $y = \sin x \iff x = \arcsin y$ (pour $x$ dans cet intervalle) ;
- $\arccos : [-1, 1] \to [0, \pi]$ ;
- $\arctan : \mathbb{R} \to \left]-\frac{\pi}{2}, \frac{\pi}{2}\right[$, avec $\lim_{\pm\infty} \arctan = \pm\frac{\pi}{2}$ ;
- $\operatorname{arccot} : \mathbb{R} \to ]0, \pi[$, avec $\lim_{-\infty} \operatorname{arccot} = \pi$ et $\lim_{+\infty} \operatorname{arccot} = 0$.
:::

:::warning[Coquille dans la fiche du prof]
Le tableau de valeurs indique $\operatorname{arccot}(-\infty) = -\pi$. Avec la convention de la fiche ($\operatorname{arccot}$ à valeurs dans $]0, \pi[$, et $\operatorname{arccot}(-x) = \pi - \operatorname{arccot} x$), la bonne valeur est $+\pi$ (180°).
:::

:::key[Propriétés et dérivées]
- $\arcsin(-x) = -\arcsin x$, $\arccos(-x) = \pi - \arccos x$, $\arctan(-x) = -\arctan x$, et $\arcsin x + \arccos x = \frac{\pi}{2}$.
- $\sin(\arccos x) = \cos(\arcsin x) = \sqrt{1 - x^2}$.
- $\arcsin' x = \frac{1}{\sqrt{1 - x^2}}$, $\quad \arccos' x = -\frac{1}{\sqrt{1 - x^2}}$, $\quad \arctan' x = \frac{1}{1 + x^2}$, et avec une fonction $u$ : $\big(\arctan u\big)' = \frac{u'}{1 + u^2}$, etc.
- Valeurs : $\arcsin\frac{1}{2} = \frac{\pi}{6}$, $\arccos\frac{1}{2} = \frac{\pi}{3}$, $\arctan 1 = \frac{\pi}{4}$, $\arctan\sqrt{3} = \frac{\pi}{3}$, $\arctan\frac{1}{\sqrt{3}} = \frac{\pi}{6}$.
:::

::item{id="trigo-formules"}

::item{id="trigo-valeurs"}
