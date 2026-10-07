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


# ---------- Ch6, exercice 2 : g1, g2, h1, h2 sont-elles toujours des fonctions ? ----------
def _powerset(items):
    items = list(items)
    return {frozenset(c) for r in range(len(items) + 1) for c in combinations(items, r)}


def _all_functions(E, F):
    E = sorted(E)
    for images in product(sorted(F), repeat=len(E)):
        yield dict(zip(E, images))


def _relations_for(f, E, F):
    PE, PF = _powerset(E), _powerset(F)
    g1 = {(y, x) for x in E for y in F if f[x] == y}
    g2 = {(y, X) for y in F for X in PE if all((x in X) == (f[x] == y) for x in E)}
    h1 = {(X, Y) for X in PE for Y in PF if all((x not in X) or (f[x] in Y) for x in E)}
    h2 = {(X, Y) for X in PE for Y in PF if Y == frozenset(f[x] for x in X)}
    return {"g1": (set(F), set(E), g1), "g2": (set(F), PE, g2), "h1": (PE, PF, h1), "h2": (PE, PF, h2)}


def test_ch6_exercise2_g2_and_h2_always_functions_g1_h1_not():
    always = {"g1": True, "g2": True, "h1": True, "h2": True}
    for E, F in [({0, 1, 2}, {0, 1}), ({0, 1}, {0, 1, 2}), ({0, 1}, {0, 1})]:
        for f in _all_functions(E, F):
            for name, (dom, cod, rel) in _relations_for(f, E, F).items():
                always[name] &= folo.is_function(set(dom), set(cod), rel)
    assert always == {"g1": False, "g2": True, "h1": False, "h2": True}


def test_ch6_g1_function_iff_f_bijective():
    E = F = {0, 1, 2}
    for f in _all_functions(E, F):
        g1 = {(y, x) for x in E for y in F if f[x] == y}
        assert folo.is_function(F, E, g1) == folo.is_bijection(lambda x: f[x], E, F)


def test_ch6_complement_is_involution():
    PE = _powerset({0, 1, 2})
    comp = lambda X: frozenset({0, 1, 2}) - X
    assert folo.is_bijection(comp, set(PE), set(PE))
    assert all(comp(comp(X)) == X for X in PE)


def test_ch6_composition_counterexample_g_not_injective():
    f = {0: 0}
    g = {0: 0, 1: 0}
    gf = lambda x: g[f[x]]
    assert folo.is_injection(gf, {0}, {0}) and not folo.is_injection(lambda y: g[y], {0, 1}, {0})


def test_ch6_affine_inverse_formula():
    for a in [-3, -1, 2, 5]:
        for b in [-2, 0, 7]:
            for y in range(-20, 21):
                x = (y - b) / a
                assert abs(a * x + b - y) < 1e-12
