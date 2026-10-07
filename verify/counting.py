"""Dénombrements par force brute (énumération explicite), indépendants des formules du cours."""
from itertools import combinations, product, permutations  # noqa: F401


def powerset(items):
    items = list(items)
    return [frozenset(c) for r in range(len(items) + 1) for c in combinations(items, r)]


# ---------- Ch11 : O'Zaman ----------
BREADS = ["pita", "wrap"]
MEATS = ["poulet", "boeuf", "agneau"]
SAUCES = ["algérienne", "ketchup", "yaourt", "mayonnaise"]


def kebab_full():
    return len(list(product(BREADS, MEATS, SAUCES)))


def kebab_partial():
    """Sandwichs (pain obligatoire) auxquels il manque la viande ou la sauce (ou les deux)."""
    all_options = product(BREADS, MEATS + [None], SAUCES + [None])
    return sum(1 for (_, m, s) in all_options if m is None or s is None)


def kebab_full_without_chicken_or_ketchup():
    return sum(1 for (_, m, s) in product(BREADS, MEATS, SAUCES) if m != "poulet" or s != "ketchup")


# ---------- Ch11 : mots binaires, chemins ----------
def binary_words(length):
    return len(list(product([0, 1], repeat=length)))


def binary_words_with_ones(length, ones):
    return sum(1 for w in product([0, 1], repeat=length) if sum(w) == ones)


def total_ones(length):
    return sum(sum(w) for w in product([0, 1], repeat=length))


def lattice_paths(right, up):
    """Nombre de chemins (pas : droite ou haut) d'un coin à l'autre, par programmation dynamique."""
    ways = [[0] * (up + 1) for _ in range(right + 1)]
    for i in range(right + 1):
        for j in range(up + 1):
            ways[i][j] = 1 if i == 0 or j == 0 else ways[i - 1][j] + ways[i][j - 1]
    return ways[right][up]


def folo_is_injection_on_empty():
    """Toute fonction ∅ → F est injective (vérifié avec la solution de référence du projet)."""
    from checks import folo
    return all(folo.is_injection(lambda x: x, set(), F) for F in [set(), {1}, {1, 2}])


# ---------- TD 2 : tournois (road trip) ----------
def _tournaments(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for orient in product([0, 1], repeat=len(pairs)):
        yield {(i, j) if o == 0 else (j, i) for (i, j), o in zip(pairs, orient)}


def _hamiltonian_paths(n, edges):
    return [p for p in permutations(range(n)) if all((p[k], p[k + 1]) in edges for k in range(n - 1))]


def every_tournament_has_hamiltonian_path(n):
    return all(_hamiltonian_paths(n, t) for t in _tournaments(n))


def every_tournament_has_unique_hamiltonian_path(n):
    return all(len(_hamiltonian_paths(n, t)) == 1 for t in _tournaments(n))


def every_tournament_has_hamiltonian_cycle(n):
    return all(any((p[-1], p[0]) in t for p in _hamiltonian_paths(n, t)) for t in _tournaments(n))


# ---------- Probabilités : outils exacts et numériques ----------
from fractions import Fraction
import math


def integrate(f, a, b, n=20000):
    """Intégrale numérique (méthode de Simpson), n pair."""
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def Phi(x):
    """Fonction de répartition de la loi normale centrée réduite."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def law_of_two_dice_sum():
    law = {}
    for a in range(1, 7):
        for b in range(1, 7):
            law[a + b] = law.get(a + b, 0) + Fraction(1, 36)
    return law


def expectation(law):
    return sum(x * p for x, p in law.items())


def variance(law):
    m = expectation(law)
    return sum((x - m) ** 2 * p for x, p in law.items())
