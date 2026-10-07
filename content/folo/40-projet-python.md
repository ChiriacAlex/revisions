---
title: Projet Python — folo.py
summary: Le devoir de programmation (2 points) — consignes, rappels Python, labo qui lance les tests officiels dans le navigateur, et les 15 questions expliquées avec indices et solutions.
kind: project
tags: [projet, Python, relations, fonctions]
minutes: 180
---

## 1. Les consignes (à respecter à la lettre)

:::warning[Sinon : 0, sans contestation possible]
- Toutes tes réponses vont dans **un seul fichier** `folo.py`, construit à partir du modèle fourni.
- Le fichier doit s'exécuter **sans aucune erreur** : teste-le sous Linux avec `python3 folo.py`, dans un terminal, sans IDE. Une seule erreur de syntaxe et tout le devoir est ignoré.
- Garde **exactement** les noms et signatures des fonctions du modèle.
- Tu peux lancer le fichier de test fourni `folo_test.py` dans le même dossier : il affiche les assertions qui échouent (ou rien si tout va bien).
- Teste chaque fonction sur un ou plusieurs exemples.
- Attention aux **dépendances** : une erreur dans une fonction du début se propage aux suivantes (par exemple `is_function` utilise `is_partial_function`, qui utilise `is_relation`).
:::

## 2. Le labo

Le labo ci-dessous contient le **modèle officiel**. Écris tes fonctions, puis clique sur **Lancer les tests** : il exécute dans ton navigateur le **test public officiel** (`folo_test.py`) et une série de **tests supplémentaires** plus exigeants (cas limites, relations « mal typées », performance), et t'affiche le résultat question par question. Ton code est sauvegardé automatiquement sur cet appareil ; le bouton **Télécharger** te donne le fichier `folo.py` à rendre.

::pylab{id="folo-homework"}

:::note[Avant de rendre]
Le labo tourne dans le navigateur (Pyodide). Fais quand même la vérification officielle sur ta machine : `python3 folo.py` (aucune sortie d'erreur), puis `python3 -m unittest folo_test` dans le même dossier.
:::

## 3. Rappels Python utiles

```python
es = {0, 1, 2}        # un ensemble
es.add(3)
ems = set()           # ensemble vide — attention : {} est un dictionnaire, pas un ensemble !
for x in es:          # parcourir un ensemble
    print(x)
if 1 in es:           # appartenance
    print("one")
pairs = {(0, 1), (1, 2), (2, 0)}
for (x, y) in pairs:  # parcourir des couples
    print(x + y)
assert 1 + 1 == 2     # lève AssertionError si c'est faux

def f(k):             # une fonction qui renvoie une fonction
    def h(x):
        return x + k
    return h
g = f(3)
print(g(2))           # 5
```

**Les quantificateurs en Python** : $\forall$ s'écrit `all(...)`, $\exists$ s'écrit `any(...)`.

```python
def even(n):
    return n % 2 == 0

e = {2, 6, 10, 11}
print(all(even(n) for n in e))                 # ∀n ∈ e, pair(n)            → False
print(all(even(n) for n in e if n <= 10))      # ∀n ∈ e, n ≤ 10 ⇒ pair(n)   → True
f = {-2, -1, 3}
print(all(n + m > 0 for n in e for m in f))    # ∀n ∈ e, ∀m ∈ f, n + m > 0 → False
print(any(n % 5 == 0 for n in e))              # ∃n ∈ e, 5 | n              → True
print({x * x for x in range(0, 9) if even(x)}) # {x² | x ∈ E, pair(x)}      → {0, 4, 16, 36, 64}
```

:::warning[Une coquille dans l'énoncé]
L'énoncé écrit `all((n + m > 0) for n in e for n in f)` : la variable `n` y est utilisée deux fois et `m` n'est jamais définie (`NameError`). Il faut lire `for n in e for m in f`, comme ci-dessus. De même, `print g(2)` est de la syntaxe Python 2 : en Python 3, c'est `print(g(2))`.
:::

:::key[Deux pièges du projet]
- `all(...)` sur un ensemble **vide** vaut `True`, `any(...)` vaut `False` : c'est la vérité vide du chapitre 4, et c'est exactement ce qu'exigent les tests (une relation vide sur un ensemble vide est réflexive…).
- `if` dans une compréhension = **implication** : `all(Q(x) for x in E if P(x))` code $\forall x \in E,\ P(x) \Rightarrow Q(x)$.
:::

## 4. Les questions une par une

Pour chaque question : la définition mathématique, des indices, les pièges, puis une solution possible (repliée). Joue le jeu : n'ouvre la solution qu'après avoir fait passer les tests ou après un vrai blocage.

### Q1 — `is_relation(es, fs, pairs)`

`pairs` est une relation binaire sur $E \times F$ si $\text{pairs} \subseteq E \times F$, c'est-à-dire $\forall (x, y) \in \text{pairs},\ x \in E \wedge y \in F$.

:::hint[Indice]
Un seul `all(...)` sur les couples de `pairs`.
:::

:::solution
```python
return all(x in es and y in fs for (x, y) in pairs)
```
:::

### Q2 — `is_partial_function(es, fs, pairs)`

Fonction partielle : chaque $x$ a **au plus une** image : $(x \sim y_1) \wedge (x \sim y_2) \Rightarrow y_1 = y_2$. Commence par vérifier que c'est une relation (Q1).

:::hint[Indice]
Version directe : `all(y1 == y2 for (x1, y1) in pairs for (x2, y2) in pairs if x1 == x2)` — correcte mais en $O(|R|^2)$. Version efficace : parcourir les couples en mémorisant la première image vue de chaque $x$ dans un dictionnaire.
:::

:::solution
```python
if not is_relation(es, fs, pairs):
    return False
image = {}
for (x, y) in pairs:
    if x in image and image[x] != y:
        return False
    image[x] = y
return True
```
:::

### Q3 — `is_function(es, fs, pairs)`

Fonction : chaque $x \in E$ a **exactement une** image : fonction partielle + **existence** d'une image pour **chaque** $x$ de `es`.

:::hint[Piège]
Un élément de `es` sans image fait échouer `is_function` mais pas `is_partial_function` (test public : `is_function(es | {-1}, fs, pairs)` doit valoir `False`).
:::

:::solution
```python
if not is_partial_function(es, fs, pairs):
    return False
antecedents = {x for (x, _) in pairs}
return all(x in antecedents for x in es)
```
:::

### Q4 — `is_injection(g, es, fs)`

Cette fois `g` est une **fonction Python**. Injective : $g(x) = g(y) \Rightarrow x = y$.

:::hint[Indice]
Deux éléments distincts ne doivent jamais avoir la même image : il n'y a aucune « collision » si et seulement si l'ensemble des images a **autant d'éléments** que `es`.
:::

:::solution
```python
return len({g(x) for x in es}) == len(es)
```
(Version « définition », en $O(n^2)$ : `all(x == y for x in es for y in es if g(x) == g(y))`.)
:::

### Q5 — `is_surjection(g, es, fs)`

Surjective : $\forall y \in F,\ \exists x \in E,\ g(x) = y$.

:::hint[Indice]
Calcule d'abord l'ensemble des images, une seule fois, puis vérifie que chaque `y` de `fs` y est. (Faire `any(g(x) == y for x in es)` pour chaque `y` marche aussi, mais en $O(n \cdot m)$.)
:::

:::solution
```python
image = {g(x) for x in es}
return all(y in image for y in fs)
```
:::

### Q6 — `is_bijection(g, es, fs)`

:::solution
```python
return is_injection(g, es, fs) and is_surjection(g, es, fs)
```
:::

### Q7 — `find_inverse(g, es, fs)`

Si $g$ est bijective, renvoyer $h : F \to E$ telle que $h(g(x)) = x$ et $g(h(y)) = y$ ; sinon renvoyer `None`.

:::hint[Indice]
Le modèle contient déjà une fonction interne `h`. Puisque $g$ est bijective, chaque `y` a **un unique** antécédent : construis un dictionnaire `{g(x): x for x in es}` **avant** de définir `h`, et fais-lui renvoyer `antecedent[f]`.
:::

:::warning[Piège du modèle]
Le modèle contient `if not is_bijection(g, es, fs): raise NotImplementedError()` : il faut remplacer ce `raise` par `return None`.
:::

:::solution
```python
if not is_bijection(g, es, fs):
    return None
antecedent = {g(x): x for x in es}

def h(f):
    return antecedent[f]

return h
```
:::

### Q8 à Q11 — symétrie, antisymétrie, réflexivité, transitivité

À chaque fois, **commence par** `is_relation(es, es, pairs)` (l'énoncé insiste : « Don't forget to check that pairs defines a binary relation on es × es beforehand »).

| Question | Propriété | Indice |
|---|---|---|
| Q8 `is_symmetric` | $x \sim y \Rightarrow y \sim x$ | parcourir les couples présents, tester le couple retourné |
| Q9 `is_antisymmetric` | $x \sim y \wedge y \sim x \Rightarrow x = y$ | `all(... for (x, y) in pairs if (y, x) in pairs)` |
| Q10 `is_reflexive` | $\forall x \in E,\ x \sim x$ | quantifier sur `es`, pas sur `pairs` |
| Q11 `is_transitive` | $x \sim y \wedge y \sim z \Rightarrow x \sim z$ | ne parcourir que les $z$ **successeurs** de $y$ |

:::warning[Q11 et la performance]
L'énoncé prévient : trois boucles imbriquées peuvent provoquer des **dépassements de temps** au test. Pire encore, boucler sur les **paires de couples** (`for (x, y) in pairs for (y2, z) in pairs`) coûte $|R|^2$ : pour $\le$ sur 300 éléments, cela fait 2 milliards de comparaisons (environ 30 s). Le test supplémentaire `test_is_transitive_fast_enough` le détecte. Solution : un dictionnaire des successeurs `succ[y]` = ensemble des $z$ tels que $y \sim z$, puis `all((x, z) in pairs for (x, y) in pairs for z in succ.get(y, ()))`.
:::

:::solution[Voir les solutions Q8 à Q11]
```python
def is_symmetric(es, pairs):
    return is_relation(es, es, pairs) and all((y, x) in pairs for (x, y) in pairs)

def is_antisymmetric(es, pairs):
    return is_relation(es, es, pairs) and all(x == y for (x, y) in pairs if (y, x) in pairs)

def is_reflexive(es, pairs):
    return is_relation(es, es, pairs) and all((x, x) in pairs for x in es)

def is_transitive(es, pairs):
    if not is_relation(es, es, pairs):
        return False
    successors = {}
    for (x, y) in pairs:
        successors.setdefault(x, set()).add(y)
    return all((x, z) in pairs for (x, y) in pairs for z in successors.get(y, ()))
```
(Les `assert` du modèle sont à conserver en tête de chaque fonction.)
:::

### Q12 à Q15 — équivalences, classes, ordres

- **Q12** `is_equivalence` : réflexive **et** symétrique **et** transitive.
- **Q13** `gen_equiv_class(es, e, pairs)` : garder les deux `assert` du modèle (relation d'équivalence, $e \in E$), puis renvoyer $[e] = \{y \in E \mid e \sim y\}$.
- **Q14** `is_partial_order` : réflexive **et** antisymétrique **et** transitive.
- **Q15** `is_total_order` : ordre **et** $\forall x, y \in E,\ x \sim y \vee y \sim x$.

:::solution[Voir les solutions Q12 à Q15]
```python
def is_equivalence(es, pairs):
    return is_reflexive(es, pairs) and is_symmetric(es, pairs) and is_transitive(es, pairs)

def gen_equiv_class(es, e, equiv_pairs):
    assert is_equivalence(es, equiv_pairs)
    assert e in es
    return {y for y in es if (e, y) in equiv_pairs}

def is_partial_order(es, pairs):
    return is_reflexive(es, pairs) and is_antisymmetric(es, pairs) and is_transitive(es, pairs)

def is_total_order(es, pairs):
    return is_partial_order(es, pairs) and all((x, y) in pairs or (y, x) in pairs
                                               for x in es for y in es)
```
:::

## 5. Check-list avant de rendre

1. `python3 folo.py` ne produit **aucune** erreur.
2. `python3 -m unittest folo_test` : tous les tests passent.
3. Aucun `raise NotImplementedError()` restant (en particulier dans `find_inverse`).
4. Aucun `print` de débogage oublié, aucun `input()`.
5. Noms et signatures **identiques** au modèle ; les `assert` du modèle sont conservés.
6. Le fichier s'appelle exactement `folo.py`.
