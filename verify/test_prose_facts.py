"""Affirmations calculables écrites dans le texte des chapitres (tableaux, corrections) :
chacune est recalculée ici, indépendamment de la rédaction."""
from itertools import combinations, product

import pytest

from checks import folo


# ---------- Ch5, exercice 1 : tableau des propriétés de R1…R5 sur {1, 2, 3} ----------
E = {1, 2, 3}
RELATIONS = {
    "R1": {(1, 1), (2, 2), (3, 3)},
    "R2": {(1, 2), (2, 1)},
    "R3": {(1, 2), (2, 3)},
    "R4": set(),
    "R5": {(x, y) for x in E for y in E},
}
# (réflexive, symétrique, antisymétrique, transitive) tels qu'écrits dans le tableau
TABLE = {
    "R1": (True, True, True, True),
    "R2": (False, True, False, False),
    "R3": (False, False, True, False),
    "R4": (False, True, True, True),
    "R5": (True, True, False, True),
}


@pytest.mark.parametrize("name", TABLE)
def test_ch5_exercise1_table(name):
    r = RELATIONS[name]
    computed = (folo.is_reflexive(E, r), folo.is_symmetric(E, r), folo.is_antisymmetric(E, r), folo.is_transitive(E, r))
    assert computed == TABLE[name]


def test_ch5_r1_is_equivalence_and_order_r5_equivalence():
    assert folo.is_equivalence(E, RELATIONS["R1"]) and folo.is_partial_order(E, RELATIONS["R1"])
    assert folo.is_equivalence(E, RELATIONS["R5"])


def test_ch5_symmetric_transitive_not_reflexive_counterexample():
    es, r = {1, 2}, {(1, 1)}
    assert folo.is_symmetric(es, r) and folo.is_transitive(es, r) and not folo.is_reflexive(es, r)


def test_ch5_close_relation_not_transitive():
    assert abs(0 - 1) <= 1 and abs(1 - 2) <= 1 and not abs(0 - 2) <= 1


def test_ch5_mod3_classes():
    es = set(range(9))
    r = {(x, y) for x in es for y in es if (x - y) % 3 == 0}
    assert folo.gen_equiv_class(es, 4, r) == {1, 4, 7} == folo.gen_equiv_class(es, 1, r)
    assert folo.gen_equiv_class(es, 0, r) == {0, 3, 6}
    assert folo.gen_equiv_class(es, 2, r) == {2, 5, 8}


def test_ch5_divisors_of_12_hasse_edges():
    divisors = [1, 2, 3, 4, 6, 12]
    covers = {(a, b) for a in divisors for b in divisors
              if a != b and b % a == 0 and not any(c not in (a, b) and c % a == 0 and b % c == 0 for c in divisors)}
    assert covers == {(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 12), (6, 12)}
