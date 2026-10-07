"""Probabilités : chaque nombre écrit dans les cours est recalculé (fractions exactes ou numérique)."""
import math
from fractions import Fraction as Fr
from itertools import combinations, product
from math import comb

import counting


def law(values):
    out = {}
    for v, p in values:
        out[v] = out.get(v, 0) + p
    return out


# ---------- Variables discrètes ----------
def test_two_dice():
    L = counting.law_of_two_dice_sum()
    assert all(L[k] == Fr(6 - abs(k - 7), 36) for k in range(2, 13)) and sum(L.values()) == 1
    assert counting.expectation(L) == 7 and counting.variance(L) == Fr(35, 6)
    assert sum(p for k, p in L.items() if k <= 4) == Fr(1, 6)


def test_one_die():
    L = {k: Fr(1, 6) for k in range(1, 7)}
    assert counting.expectation(L) == Fr(7, 2)
    assert sum(k * k * p for k, p in L.items()) == Fr(91, 6)
    assert counting.variance(L) == Fr(35, 12) == Fr(6 * 6 - 1, 12)


def test_couple_example():
    J = {(0, 0): Fr(1, 10), (0, 1): Fr(3, 10), (1, 0): Fr(2, 10), (1, 1): Fr(4, 10)}
    px = {x: sum(p for (a, b), p in J.items() if a == x) for x in (0, 1)}
    py = {y: sum(p for (a, b), p in J.items() if b == y) for y in (0, 1)}
    assert px == {0: Fr(4, 10), 1: Fr(6, 10)} and py == {0: Fr(3, 10), 1: Fr(7, 10)}
    exy = sum(a * b * p for (a, b), p in J.items())
    assert exy == Fr(4, 10) and exy - Fr(6, 10) * Fr(7, 10) == Fr(-2, 100)
    assert J[(1, 0)] / px[1] == Fr(1, 3)


def test_zero_covariance_not_independent():
    X = {-1: Fr(1, 3), 0: Fr(1, 3), 1: Fr(1, 3)}
    exy = sum(x * x * x * p for x, p in X.items())
    assert exy - counting.expectation(X) * sum(x * x * p for x, p in X.items()) == 0
    assert Fr(1, 3) != Fr(1, 3) * Fr(1, 3)


def test_usual_laws_moments():
    n, p = 12, Fr(3, 10)
    B = {k: comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)}
    assert sum(B.values()) == 1 and counting.expectation(B) == n * p and counting.variance(B) == n * p * (1 - p)
    U = {k: Fr(1, n) for k in range(1, n + 1)}
    assert counting.expectation(U) == Fr(n + 1, 2) and counting.variance(U) == Fr(n * n - 1, 12)
    # géométrique, Poisson, binomiale négative : séries tronquées (numérique)
    q = 0.3
    G = {k: (1 - q) ** (k - 1) * q for k in range(1, 400)}
    assert abs(sum(k * v for k, v in G.items()) - 1 / q) < 1e-9
    assert abs(sum(k * k * v for k, v in G.items()) - (1 / q) ** 2 - (1 - q) / q ** 2) < 1e-8
    lam = 3.7
    P = {k: math.exp(-lam) * lam ** k / math.factorial(k) for k in range(120)}
    m = sum(k * v for k, v in P.items())
    assert abs(m - lam) < 1e-9 and abs(sum(k * k * v for k, v in P.items()) - m * m - lam) < 1e-9
    r, pp = 3, 0.4
    NB = {k: comb(k - 1, r - 1) * pp ** r * (1 - pp) ** (k - r) for k in range(r, 600)}
    mnb = sum(k * v for k, v in NB.items())
    assert abs(mnb - r / pp) < 1e-9 and abs(sum(k * k * v for k, v in NB.items()) - mnb ** 2 - r * (1 - pp) / pp ** 2) < 1e-7


def test_poisson_sum_stability():
    lam, mu = 1.5, 2.5
    for s in range(15):
        conv = sum(math.exp(-lam) * lam ** k / math.factorial(k) * math.exp(-mu) * mu ** (s - k) / math.factorial(s - k)
                   for k in range(s + 1))
        assert abs(conv - math.exp(-(lam + mu)) * (lam + mu) ** s / math.factorial(s)) < 1e-12


def test_hypergeometric_moments():
    N, K, n = 10, 4, 3
    H = {k: Fr(comb(K, k) * comb(N - K, n - k), comb(N, n)) for k in range(n + 1)}
    p = Fr(K, N)
    assert sum(H.values()) == 1 and counting.expectation(H) == n * p
    assert counting.variance(H) == n * p * (1 - p) * Fr(N - n, N - 1)


# ---------- Exercices du chapitre discret ----------
def test_ex1_urn():
    balls = ["R"] * 3 + ["B"] * 2
    draws = list(combinations(range(5), 2))
    L = law((sum(balls[i] == "R" for i in d), Fr(1, len(draws))) for d in draws)
    assert L == {0: Fr(1, 10), 1: Fr(6, 10), 2: Fr(3, 10)}
    assert counting.expectation(L) == Fr(12, 10) and counting.variance(L) == Fr(36, 100)


def test_ex2_temperature():
    assert 1.8 * 20 + 32 == 68 and abs(1.8 ** 2 * 25 - 81) < 1e-9


def test_ex3_lottery():
    E_L = 100 * Fr(1, 100) + 10 * Fr(1, 20)
    assert E_L == Fr(3, 2) and E_L - 2 == Fr(-1, 2)


def test_ex4_with_and_without_replacement():
    tokens = [1] * 4 + [0] * 6
    draws = list(combinations(range(10), 3))
    H = law((sum(tokens[i] for i in d), Fr(1, len(draws))) for d in draws)
    assert H == {0: Fr(1, 6), 1: Fr(1, 2), 2: Fr(3, 10), 3: Fr(1, 30)}
    assert counting.expectation(H) == Fr(6, 5) and counting.variance(H) == Fr(56, 100)
    B = law((sum(tokens[i] for i in d), Fr(1, 1000)) for d in product(range(10), repeat=3))
    assert B == {0: Fr(216, 1000), 1: Fr(432, 1000), 2: Fr(288, 1000), 3: Fr(64, 1000)}
    assert counting.variance(B) == Fr(72, 100)
    assert 1 - H[0] == Fr(5, 6)


def test_ex5_poisson_approximation():
    exact0 = 0.998 ** 1000
    assert abs(exact0 - 0.1351) < 1e-4 and abs(math.exp(-2) - 0.1353) < 1e-4
    exact_le2 = sum(comb(1000, k) * 0.002 ** k * 0.998 ** (1000 - k) for k in range(3))
    assert abs(5 * math.exp(-2) - 0.677) < 1e-3 and abs(exact_le2 - 0.677) < 1e-3


def test_ex6_geometric():
    assert abs(0.7 ** 3 - 0.343) < 1e-12 and abs(0.7 ** 5 / 0.7 ** 2 - 0.343) < 1e-12
