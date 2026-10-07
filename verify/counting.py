"""Dénombrements par force brute (énumération explicite), indépendants des formules du cours."""
from itertools import combinations, product, permutations


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
