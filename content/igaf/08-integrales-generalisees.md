---
title: Ch3 — Intégrales généralisées (définition et propriétés)
summary: "Intégrales sur un intervalle non borné ou d'une fonction non bornée : définition par une limite, les différents types, Chasles, intégrales de référence (Riemann, exponentielle, Bertrand), critères de comparaison, convergence absolue, IPP et changement de variable."
tags: [chapitre 3, intégrales généralisées, Riemann, comparaison, convergence absolue]
minutes: 120
---

## 1. Pourquoi des intégrales généralisées ?

Jusqu'ici, on intégrait une fonction **continue** sur un **segment** $[a, b]$. Mais de nombreux calculs réels sortent de ce cadre :

- **Probabilités** : une variable aléatoire peut prendre ses valeurs sur tout $\mathbb{R}$. Pour vérifier que $f$ est une densité, il faut calculer $\int_{-\infty}^{+\infty} f(x)\,dx = 1$. Pour la loi exponentielle (temps d'attente entre deux clients d'une file, cf. cours ERO2) :
$$\int_0^{+\infty} \lambda e^{-\lambda x}\,dx = \lim_{b \to +\infty}\big[-e^{-\lambda x}\big]_0^b = \lim_{b \to +\infty}\left(1 - e^{-\lambda b}\right) = 1.$$
La probabilité que le prochain client arrive **après** $t$ vaut $P(T > t) = \int_t^{+\infty} f(s)\,ds$ : encore une borne infinie.
- **Traitement du signal** : l'énergie d'un signal est $E_x = \int_{-\infty}^{+\infty} |x(t)|^2\,dt$ ; corrélations et convolutions sont aussi des intégrales sur $\mathbb{R}$.

:::intuition[Idée essentielle du chapitre]
Une intégrale généralisée, c'est **une intégrale ordinaire suivie d'une limite**. La borne $+\infty$ n'est pas un nombre : on intègre jusqu'à $b$, puis on fait tendre $b$ vers $+\infty$. Si la limite existe et est **finie**, l'intégrale **converge** ; sinon elle **diverge**.
:::

Le cours (INTG) comporte trois parties : les intégrales généralisées (ce chapitre et le suivant), les **suites d'intégrales** $\lim_n \int f_n$ (on ne peut pas toujours échanger limite et intégrale), et les **intégrales à paramètre** $F(t) = \int f(x, t)\,dx$.

## 2. Définitions

:::definition[Intégrale généralisée]
Une intégrale est **généralisée** (ou **impropre**) si :
- l'intervalle d'intégration est **non borné** ($\int_a^{+\infty}$, $\int_{-\infty}^b$, $\int_{-\infty}^{+\infty}$), ou
- la fonction **n'est pas bornée** au voisinage d'une borne ou d'un point intérieur.
:::

:::definition[Type 1 — borne infinie]
Soit $f$ continue sur $[a, +\infty[$. L'intégrale $\int_a^{+\infty} f(t)\,dt$ **converge** si $\lim_{x \to +\infty}\int_a^x f(t)\,dt$ existe et est **finie**. On pose alors
$$\int_a^{+\infty} f(t)\,dt = \lim_{x \to +\infty}\int_a^x f(t)\,dt.$$
Exemple : $\int_0^x e^{-t}\,dt = 1 - e^{-x} \to 1$, donc $\int_0^{+\infty} e^{-t}\,dt = 1$.
:::

:::definition[Type 2 — fonction non bornée en une borne finie]
Soit $f$ continue sur $[a, b[$ et non bornée au voisinage de $b$. L'intégrale $\int_a^b f(t)\,dt$ converge si $\lim_{x \to b^-}\int_a^x f(t)\,dt$ existe et est finie.
Exemple : $\int_0^x \frac{dt}{\sqrt{4 - t}} = \big[-2\sqrt{4 - t}\big]_0^x = 4 - 2\sqrt{4 - x} \to 4$ quand $x \to 4$, donc $\int_0^4 \frac{dt}{\sqrt{4 - t}} = 4$.
:::

:::method[Deux points problématiques : on coupe]
- **Deux bornes impropres** (]a, b[, ou $\mathbb{R}$) : on choisit un $c$ entre les deux et on étudie **séparément** $\int_a^c$ et $\int_c^b$. L'intégrale converge si et seulement si **les deux** convergent :
$$\int_{-\infty}^{+\infty} f = \lim_{a \to -\infty}\int_a^c f + \lim_{b \to +\infty}\int_c^b f.$$
- **Singularité intérieure** en $c \in ]a, b[$ : $\int_a^b f$ converge si et seulement si $\int_a^c f$ et $\int_c^b f$ convergent **toutes les deux**. Une seule divergente suffit à faire diverger le tout.
:::

:::warning[Le piège de la symétrie : ∫₋₁¹ dx/x n'existe pas]
On serait tenté d'écrire « $\frac{1}{x}$ est impaire, donc $\int_{-1}^{1}\frac{dx}{x} = 0$ », ou bien « $\int_{-1}^{1}\frac{dx}{x^2} = \left[-\frac{1}{x}\right]_{-1}^{1} = -2$ ». **Les deux calculs sont faux.** Le point $0$ est une singularité intérieure : $\int_0^1 \frac{dx}{x}$ diverge vers $+\infty$ et $\int_{-1}^0 \frac{dx}{x}$ vers $-\infty$ ; on ne peut pas soustraire deux infinis. Et $\int_0^1 \frac{dx}{x^2} = +\infty$, donc $\int_{-1}^1 \frac{dx}{x^2}$ diverge (le « $-2$ » est absurde : on intègre une fonction **positive** !).
:::

::item{id="ig-nature"}

## 3. Propriétés

:::property[On peut déplacer une borne finie]
Si $f$ est continue sur $[a, b[$ et $a < c < b$, alors $\int_a^b f$ et $\int_c^b f$ sont **de même nature**, et en cas de convergence $\int_a^b f = \int_a^c f + \int_c^b f$.

*Preuve* : $\int_a^x f = \int_a^c f + \int_c^x f$, et $\int_a^c f$ est une intégrale ordinaire (finie). Donc la limite quand $x \to b$ existe pour l'une si et seulement si elle existe pour l'autre (« en passant à la limite »).

**À retenir** : la nature d'une intégrale ne dépend que du comportement de $f$ **près du point problématique**.
:::

:::property[Linéarité]
Si $\int_a^b f$ et $\int_a^b g$ convergent, alors $\int_a^b (\lambda f + \mu g)$ converge et vaut $\lambda\int_a^b f + \mu\int_a^b g$.
**Attention** : si l'une converge et l'autre diverge, la somme diverge ; si les deux divergent, on ne peut rien dire ($\int_1^{+\infty}\left(\frac{1}{x} - \frac{1}{x}\right)dx = 0$).
:::

:::warning[Une idée fausse fréquente]
« Si $f(x) \to 0$ en $+\infty$, alors $\int_a^{+\infty} f$ converge » est **faux** : $\frac{1}{x} \to 0$ mais $\int_1^b \frac{dx}{x} = \ln b \to +\infty$. Il faut que $f$ tende vers $0$ **assez vite**.
:::

## 4. Intégrales de référence

:::theorem[Intégrales de Riemann]
Pour $\alpha \in \mathbb{R}$ :
$$\int_1^{+\infty}\frac{dt}{t^\alpha} \text{ converge} \iff \alpha > 1, \qquad \int_0^1 \frac{dt}{t^\alpha} \text{ converge} \iff \alpha < 1.$$
Plus généralement, $\int_a^b \frac{dt}{(t - a)^\alpha}$ converge $\iff \alpha < 1$. Et $\alpha = 1$ diverge **des deux côtés**.
:::

:::intuition[Pourquoi ? Un calcul direct]
Pour $\alpha \ne 1$, $\int_1^x t^{-\alpha}\,dt = \frac{x^{1-\alpha} - 1}{1 - \alpha}$ : en $+\infty$, $x^{1-\alpha}$ tend vers $0$ si $\alpha > 1$ (convergence, valeur $\frac{1}{\alpha - 1}$) et vers $+\infty$ si $\alpha < 1$. En $0$, c'est l'inverse. Pour $\alpha = 1$, on a $\ln x$, qui diverge en $0$ comme en $+\infty$.

Moyen mnémotechnique : **en $+\infty$ il faut que $f$ décroisse vite** ($\alpha > 1$) ; **en $0$ il faut que $f$ n'explose pas trop vite** ($\alpha < 1$). Même règle que les séries $\sum \frac{1}{n^\alpha}$ (convergentes $\iff \alpha > 1$).
:::

:::theorem[Intégrales exponentielles]
$\int_0^{+\infty} e^{\alpha t}\,dt$ converge $\iff \alpha < 0$, et vaut alors $-\frac{1}{\alpha}$. $\quad \int_{-\infty}^0 e^{\alpha t}\,dt$ converge $\iff \alpha > 0$, et vaut alors $\frac{1}{\alpha}$.
:::

:::theorem[Intégrales de Bertrand (logarithmiques)]
$$\int_2^{+\infty}\frac{dt}{t^\alpha(\ln t)^\beta} \text{ converge} \iff \alpha > 1 \text{, ou } (\alpha = 1 \text{ et } \beta > 1).$$
$$\int_0^{1/2}\frac{dt}{t^\alpha|\ln t|^\beta} \text{ converge} \iff \alpha < 1 \text{, ou } (\alpha = 1 \text{ et } \beta > 1).$$
Quand $\alpha \ne 1$, c'est la puissance qui décide (le logarithme est négligeable) ; quand $\alpha = 1$, le logarithme départage.
:::

::item{id="ig-reference"}

## 5. Critères de comparaison (fonctions positives)

Quand on ne sait pas calculer de primitive, on **compare** $f$ à une fonction dont on connaît l'intégrale.

:::theorem[Fonction positive : converger = être majorée]
Si $f$ est continue et **positive** sur $[a, b[$, alors $\int_a^b f$ converge $\iff$ $F : x \mapsto \int_a^x f$ est **majorée** sur $[a, b[$.
(Car $F$ est croissante : croissante et majorée ⟹ limite finie.) Il suffit que $f$ soit positive **au voisinage de $b$**.
:::

:::example[Majorer]
Pour $x \ge 1$ : $0 \le \int_1^x \frac{\sin^2 t}{t^2}\,dt \le \int_1^x \frac{dt}{t^2} = 1 - \frac{1}{x} \le 1$. L'intégrale $\int_1^{+\infty}\frac{\sin^2 t}{t^2}\,dt$ converge.
:::

:::warning[La positivité est indispensable]
$\varphi(x) = \int_0^x \sin t\,dt = 1 - \cos x$ est bornée ($0 \le \varphi \le 2$), et pourtant $\int_0^{+\infty}\sin t\,dt$ **diverge** : $1 - \cos x$ n'a pas de limite. Le critère « bornée ⟹ converge » ne vaut que pour une fonction **positive** (c'était le piège du Wooclap 9 du cours).
:::

:::theorem[Comparaison]
Si $0 \le f \le g$ au voisinage de $b$ :
- $\int_a^b g$ converge ⟹ $\int_a^b f$ converge (**le petit sous un grand convergent converge**) ;
- $\int_a^b f$ diverge ⟹ $\int_a^b g$ diverge (**le grand au-dessus d'un petit divergent diverge**).

Mais si $g$ diverge, on ne peut **rien** dire de $f$ ; si $f$ converge, rien de $g$.
:::

:::example[Majoration et minoration]
- $0 \le \frac{\sin^2 t}{t^2} \le \frac{1}{t^2}$ sur $[1, +\infty[$ et Riemann $\alpha = 2 > 1$ : $\int_1^{+\infty}\frac{\sin^2 t}{t^2}\,dt$ **converge**.
- $\frac{1 + \sin^2 t}{t} \ge \frac{1}{t} \ge 0$ et Riemann $\alpha = 1$ diverge : $\int_1^{+\infty}\frac{1 + \sin^2 t}{t}\,dt$ **diverge**.
:::

:::theorem[Comparaison asymptotique]
Soient $f, g \ge 0$ au voisinage de $b$.
- Si $f = O(g)$ (en particulier si $f = o(g)$) en $b$ : $\int_a^b g$ converge ⟹ $\int_a^b f$ converge.
- Si $f \underset{b}{\sim} g$ : $\int_a^b f$ et $\int_a^b g$ sont **de même nature**.
:::

:::definition[Rappels O, o, ∼ au voisinage de b]
- $f = O(g)$ : $\left|\frac{f}{g}\right|$ est **bornée** près de $b$. Exemple : $\frac{\sin x}{x^2} = O\left(\frac{1}{x^2}\right)$.
- $f = o(g)$ : $\frac{f}{g} \to 0$ ($f$ est **négligeable** devant $g$). Exemple : $\frac{1}{x^2} = o\left(\frac{1}{x}\right)$ en $+\infty$.
- $f \sim g$ : $\frac{f}{g} \to 1$. Exemple : $\frac{1}{x + 1} \sim \frac{1}{x}$ en $+\infty$.
:::

:::example[Nature de ∫₀¹ ln t dt par comparaison]
Par croissances comparées, $t^{1/2}\ln t \to 0$ en $0^+$, donc $|\ln t| = o\left(\frac{1}{t^{1/2}}\right)$. Comme $\int_0^1 \frac{dt}{t^{1/2}}$ converge (Riemann $\alpha = \frac{1}{2} < 1$), $\int_0^1 |\ln t|\,dt$ converge ($\ln t$ est de signe constant sur $]0, 1]$). Par calcul direct, elle vaut $\big[t\ln t - t\big]_0^1 = -1$.
:::

::item{id="ig-comparaison"}

## 6. Convergence absolue

:::theorem[Convergence absolue ⟹ convergence]
Si $\int_a^b |f(t)|\,dt$ converge, alors $\int_a^b f(t)\,dt$ converge. On dit que l'intégrale **converge absolument**. La réciproque est **fausse** (exemple : $\int_1^{+\infty}\frac{\sin t}{t}\,dt$ converge sans converger absolument).
:::

:::method[Quand f change de signe]
On ne peut pas appliquer les critères de comparaison à $f$ directement (ils exigent $f \ge 0$). On étudie $|f|$ : si on la majore par une fonction d'intégrale convergente, c'est gagné. Exemple : $\left|\frac{\sin t}{t^2}\right| \le \frac{1}{t^2}$, donc $\int_1^{+\infty}\frac{\sin t}{t^2}\,dt$ converge absolument, donc converge.
:::

## 7. Intégration par parties et changement de variable

:::theorem[IPP pour une intégrale généralisée]
Soient $u, v$ de classe $\mathcal{C}^1$ sur $[a, b[$. Si le **terme de bord** $\lim_{x \to b^-} u(x)v(x)$ existe et est **fini**, alors $\int_a^b u v'$ et $\int_a^b u' v$ sont **de même nature**, et en cas de convergence
$$\int_a^b u v' = \big[uv\big]_a^b - \int_a^b u' v, \qquad \big[uv\big]_a^b = \lim_{x \to b^-}u(x)v(x) - u(a)v(a).$$
**En pratique** : on fait l'IPP sur $[a, x]$ (intégrale ordinaire), **puis** on fait tendre $x$ vers $b$.
:::

:::example[∫₁^∞ sin t / t dt converge (sans converger absolument)]
Sur $[1, x]$, avec $u = \frac{1}{t}$, $v = -\cos t$ :
$$\int_1^x \frac{\sin t}{t}\,dt = \left[-\frac{\cos t}{t}\right]_1^x - \int_1^x \frac{\cos t}{t^2}\,dt.$$
Le terme de bord tend vers $\cos 1$ (car $\frac{\cos x}{x} \to 0$), et $\left|\frac{\cos t}{t^2}\right| \le \frac{1}{t^2}$ donne la convergence absolue du reste. Donc $\int_1^{+\infty}\frac{\sin t}{t}\,dt$ converge.
:::

:::example[∫₀^∞ x e^{-x} dx = 1]
$\int_0^x t e^{-t}\,dt = \big[-te^{-t}\big]_0^x + \int_0^x e^{-t}\,dt = -xe^{-x} + 1 - e^{-x} \to 1$.
:::

:::theorem[Changement de variable]
Si $\varphi : ]\alpha, \beta[ \to ]a, b[$ est une **bijection** de classe $\mathcal{C}^1$ avec $\varphi(\alpha^+) = a$ et $\varphi(\beta^-) = b$, alors $\int_a^b f(t)\,dt$ et $\int_\alpha^\beta f\big(\varphi(x)\big)\varphi'(x)\,dx$ sont **de même nature** et égales en cas de convergence. On transforme $t$, $dt$ **et les bornes**, et on vérifie le comportement aux bornes.
:::

:::example[Wooclap 13 du cours]
Avec $u = \sqrt{x}$, $x = u^2$, $dx = 2u\,du$ : $\frac{dx}{(1 + x)\sqrt{x}} = \frac{2\,du}{1 + u^2}$.
- $I_1 = \int_0^1 \frac{dx}{(1 + x)\sqrt{x}} = 2\int_0^1 \frac{du}{1 + u^2} = 2 \cdot \frac{\pi}{4} = \frac{\pi}{2}$.
- $I_2 = \int_1^{+\infty} \frac{dx}{(1 + x)\sqrt{x}} = 2\left(\frac{\pi}{2} - \frac{\pi}{4}\right) = \frac{\pi}{2}$.
:::

::item{id="ig-calculs"}

## 8. À retenir

:::key[Résumé]
- Intégrale généralisée = **limite** d'intégrales ordinaires. **Vérifier la convergence avant de calculer.**
- Plusieurs points problématiques ⟹ **découper** ; il faut que **chaque** morceau converge.
- Références : **Riemann** ($\alpha > 1$ en $+\infty$, $\alpha < 1$ en $0$), **exponentielle**, **Bertrand**.
- Fonctions **positives** : majoration, minoration, $O$, $o$, **équivalents**.
- Signe quelconque : **convergence absolue** ; sinon IPP (comme pour $\frac{\sin t}{t}$).
- IPP et changement de variable : sur $[a, x]$ d'abord, limite ensuite.
:::
