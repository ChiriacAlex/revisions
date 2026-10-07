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


# ---------- Ch7 : annale 2022 (fonction d'ordre supérieur g = image directe) ----------
def _direct_image(f, X):
    return frozenset(f[x] for x in X)


def test_ch7_exam2022_injective_iff_disjoint_images():
    for E, F in [({0, 1, 2}, {0, 1, 2}), ({0, 1, 2}, {0, 1}), ({0, 1}, {0, 1, 2, 3})]:
        PE = _powerset(E)
        for f in _all_functions(E, F):
            injective = folo.is_injection(lambda x: f[x], set(E), set(F))
            h = all(not (A & B == frozenset()) or (_direct_image(f, A) & _direct_image(f, B) == frozenset())
                    for A in PE for B in PE)
            assert injective == h


def test_ch7_converse_holds_for_every_function():
    E, F = {0, 1, 2}, {0, 1}
    PE = _powerset(E)
    for f in _all_functions(E, F):
        assert all(not (_direct_image(f, A) & _direct_image(f, B) == frozenset()) or (A & B == frozenset())
                   for A in PE for B in PE)


def test_ch7_properties_of_direct_image():
    E, F = {0, 1, 2}, {0, 1}
    PE = _powerset(E)
    for f in _all_functions(E, F):
        assert _direct_image(f, frozenset()) == frozenset()
        for x in E:
            assert _direct_image(f, {x}) == {f[x]}
        for A in PE:
            for B in PE:
                assert _direct_image(f, A | B) == _direct_image(f, A) | _direct_image(f, B)
                assert _direct_image(f, A & B) <= _direct_image(f, A) & _direct_image(f, B)
                if A <= B:
                    assert _direct_image(f, A) <= _direct_image(f, B)


def test_ch7_intersection_equality_iff_injective():
    for E, F in [({0, 1, 2}, {0, 1, 2}), ({0, 1, 2}, {0, 1})]:
        PE = _powerset(E)
        for f in _all_functions(E, F):
            injective = folo.is_injection(lambda x: f[x], set(E), set(F))
            equality = all(_direct_image(f, A & B) == _direct_image(f, A) & _direct_image(f, B) for A in PE for B in PE)
            assert injective == equality


# ---------- Ch8 : formules et contre-exemples de récurrence ----------
import math


def test_ch8_sum_formulas():
    for n in range(1, 500):
        assert sum(range(1, n + 1)) == n * (n + 1) // 2
        assert sum(k * k for k in range(1, n + 1)) * 6 == n * (n + 1) * (2 * n + 1)
        assert sum(2 * k - 1 for k in range(1, n + 1)) == n * n
        assert 2 * n * n + 7 * n + 6 == (n + 2) * (2 * n + 3)


def test_ch8_sin_inequality_numerically():
    for n in range(1, 30):
        for i in range(-300, 301):
            x = i / 37
            assert abs(math.sin(n * x)) <= n * abs(math.sin(x)) + 1e-9


def test_ch8_nine_divides_ten_power_plus_one_never():
    assert all((10 ** n + 1) % 9 == 2 for n in range(1, 200))
    # l'hérédité était juste : 10^(n+1) + 1 = 10 (10^n + 1) - 9
    assert all(10 ** (n + 1) + 1 == 10 * (10 ** n + 1) - 9 for n in range(50))


def test_ch8_divisibility_and_powers():
    assert all((n ** 3 - n) % 3 == 0 for n in range(1000))
    assert all(2 ** n >= n * n for n in range(4, 500)) and 2 ** 3 < 9


# ---------- Ch9 ----------
from fractions import Fraction


def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def test_ch9_fibonacci_bound_exact():
    for n in range(300):
        assert Fraction(_fib(n)) <= Fraction(5, 3) ** n
    assert Fraction(5, 3) + 1 == Fraction(24, 9) and Fraction(5, 3) ** 2 == Fraction(25, 9)


def test_ch9_three_five_both_methods():
    for n in range(8, 400):
        assert any(3 * a + 5 * b == n for a in range(n // 3 + 1) for b in range(n // 5 + 1))
    assert not any(3 * a + 5 * b == 7 for a in range(3) for b in range(2))
    # méthode 2 : les deux remplacements de pièces conservent la somme + 1
    for a in range(3, 30):
        assert 3 * a + 1 == 3 * (a - 3) + 5 * 2
    for a in range(0, 30):
        for b in range(1, 30):
            assert 3 * a + 5 * b + 1 == 3 * (a + 2) + 5 * (b - 1)


def test_ch9_mean_sequence_constant():
    u = [Fraction(1)]
    for n in range(100):
        u.append(sum(u) / (n + 1))
    assert all(x == 1 for x in u)


# ---------- Ch10 ----------
def test_ch10_encodings_of_57():
    assert int("57") == 57 and int("111001", 2) == 57 and int("2010", 3) == 57


def test_ch10_directed_graphs_on_3_vertices():
    cells = [(i, j) for i in range(3) for j in range(3)]
    graphs = {frozenset(c for c, bit in zip(cells, bits) if bit) for bits in product([0, 1], repeat=9)}
    assert len(graphs) == 512
    assert len({g for g in graphs if all(i != j for (i, j) in g)}) == 64


def test_ch10_powerset_bijection_with_bitstrings():
    E = ["a", "b", "c", "d"]
    code = lambda X: tuple(1 if e in X else 0 for e in E)
    subsets = _powerset(E)
    assert folo.is_bijection(code, set(subsets), set(product([0, 1], repeat=len(E))))


def test_ch10_zigzag_bijection_n_to_z():
    f = lambda n: n // 2 if n % 2 == 0 else -(n + 1) // 2
    g = lambda z: 2 * z if z >= 0 else -2 * z - 1
    assert all(g(f(n)) == n for n in range(5000))
    assert all(f(g(z)) == z for z in range(-2500, 2500))


# ---------- Ch11 ----------
import counting
from math import comb


def test_ch11_kebab_three_answers_and_breakdowns():
    assert counting.kebab_full() == 24
    assert counting.kebab_partial() == 16 == 6 + 8 + 2
    assert counting.kebab_full_without_chicken_or_ketchup() == 22 == 16 + 18 - 12


def test_ch11_binary_words_and_paths():
    assert counting.binary_words(4) == 16
    assert [counting.binary_words_with_ones(4, i) for i in range(5)] == [1, 4, 6, 4, 1]
    assert counting.total_ones(4) == 32
    assert counting.lattice_paths(5, 5) == 252 == comb(10, 5)
    assert counting.lattice_paths(4, 4) == 70


def test_ch11_sum_of_binomials_and_inclusion_exclusion():
    for n in range(15):
        assert sum(comb(n, k) for k in range(n + 1)) == 2 ** n
    U = range(5)
    for A in _powerset(U):
        for B in _powerset(U):
            assert len(A | B) == len(A) + len(B) - len(A & B)


def test_ch11_delegates():
    assert len([(d, s) for d in range(30) for s in range(30) if d != s]) == 870
    assert comb(30, 3) == 4060


# ---------- Ch12 ----------
from itertools import permutations


def test_ch12_equations():
    assert [x for x in (1, -2) if abs((2 - x) ** 0.5 - x) < 1e-12] == [1]
    assert [x for x in (1, -2) if (x + 3) >= 0 and abs((x + 3) ** 0.5 - (x + 1)) < 1e-12] == [1]
    f = lambda x: -x
    assert all(f(x) + 2 * f(-x) == x for x in range(-50, 51))


def test_ch12_subsets_containing_A_bijection():
    E = frozenset(range(6))
    A = frozenset({0, 2})
    P_A = {X for X in _powerset(E) if A <= X}
    P_rest = set(_powerset(E - A))
    phi = lambda X: X - A
    psi = lambda Y: Y | A
    assert all(phi(X) in P_rest for X in P_A) and all(psi(Y) in P_A for Y in P_rest)
    assert all(psi(phi(X)) == X for X in P_A) and all(phi(psi(Y)) == Y for Y in P_rest)
    assert len(P_A) == 2 ** (len(E) - len(A))


def test_ch12_bijections_count_n_factorial():
    for n in range(1, 7):
        assert len(list(permutations(range(n)))) == math.factorial(n)
