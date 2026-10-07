"""Dénombrements par force brute (énumération explicite), indépendants des formules du cours."""
from itertools import combinations, product, permutations


def powerset(items):
    items = list(items)
    return [frozenset(c) for r in range(len(items) + 1) for c in combinations(items, r)]
