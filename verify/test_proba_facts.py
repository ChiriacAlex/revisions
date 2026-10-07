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


# ---------- Lois continues ----------
I = counting.integrate
Phi = counting.Phi


def test_density_examples():
    assert abs(I(lambda x: 3 * x * x, 0, 1) - 1) < 1e-12
    assert abs(I(lambda x: 3 * x * x, 0.5, 1) - 7 / 8) < 1e-12
    assert abs(I(lambda x: 0.75 * (1 - x * x), -1, 1) - 1) < 1e-12
    assert abs(I(lambda x: 2 / x ** 3, 1, 4000, 800000) - 1) < 1e-6


def test_cdf_x3_median_and_central_interval():
    m = 2 ** (-1 / 3)
    assert abs(m ** 3 - 0.5) < 1e-12 and abs(m - 0.794) < 1e-3
    a, b = 0.025 ** (1 / 3), 0.975 ** (1 / 3)
    assert abs(a - 0.292) < 1e-3 and abs(b - 0.992) < 1e-3
    assert abs(I(lambda x: 3 * x * x, a, b) - 0.95) < 1e-9


def test_square_of_uniform_density():
    # Y = X², X ~ U([-1, 1]) : F_Y(t) = sqrt(t), f_Y(t) = 1/(2 sqrt t)
    for t in [0.01, 0.2, 0.5, 0.9]:
        mc = sum(1 for i in range(200001) if (-1 + 2 * i / 200000) ** 2 <= t) / 200001
        assert abs(mc - math.sqrt(t)) < 1e-3
    # f_Y = F_Y' : dérivée numérique de sqrt(t), et intégrale exacte 1 - sqrt(eps) -> 1
    for t in [0.01, 0.3, 0.8]:
        h = 1e-6
        assert abs((math.sqrt(t + h) - math.sqrt(t - h)) / (2 * h) - 1 / (2 * math.sqrt(t))) < 1e-5
    assert abs(I(lambda u: 1.0, 0, 1) - 1) < 1e-12  # changement de variable u = sqrt(t)


def test_uniform_moments():
    a, b = 2.0, 7.0
    f = lambda x: 1 / (b - a)
    m = I(lambda x: x * f(x), a, b)
    v = I(lambda x: x * x * f(x), a, b) - m * m
    assert abs(m - (a + b) / 2) < 1e-9 and abs(v - (b - a) ** 2 / 12) < 1e-9


def test_exponential_facts():
    lam = 0.5
    f = lambda t: lam * math.exp(-lam * t)
    assert abs(I(f, 0, 200) - 1) < 1e-9
    assert abs(I(lambda t: t * f(t), 0, 200) - 1 / lam) < 1e-6
    assert abs(I(lambda t: t * t * f(t), 0, 200) - 2 / lam ** 2 - 0) < 1e-5  # E[T²] = 2/λ²
    assert abs(math.exp(-lam * 3) - 0.2231) < 1e-4
    assert abs(1 - math.exp(-lam * (math.log(2) / lam)) - 0.5) < 1e-12
    for t0 in [0.5, 2, 5]:
        for dt in [0.1, 1, 3]:
            assert abs(math.exp(-lam * (t0 + dt)) / math.exp(-lam * t0) - math.exp(-lam * dt)) < 1e-12


def test_inverse_transform_sampling():
    lam = 1.7
    for i in range(1, 1000):
        u = i / 1000
        t = -math.log(1 - u) / lam
        assert abs((1 - math.exp(-lam * t)) - u) < 1e-12


def test_normal_table_and_rules():
    assert round(Phi(1), 4) == 0.8413 and round(Phi(1.96), 4) == 0.9750
    assert round(Phi(2), 4) == 0.9772 and round(Phi(3), 4) == 0.9987
    assert round(2 * Phi(1) - 1, 3) == 0.683 and round(2 * Phi(2) - 1, 3) == 0.954
    assert round(2 * Phi(3) - 1, 3) == 0.997 and abs(2 * Phi(1.96) - 1 - 0.95) < 1e-3
    phi = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
    assert abs(I(phi, -12, 12) - 1) < 1e-10
    for u in [0.3, 1, 2.5]:
        assert abs(Phi(-u) - (1 - Phi(u))) < 1e-12


def test_heights_example():
    m, s = 175, 7
    assert abs(Phi((182 - m) / s) - Phi((168 - m) / s) - 0.6827) < 1e-4
    lo, hi = m - 1.96 * s, m + 1.96 * s
    assert round(lo, 1) == 161.3 and round(hi, 1) == 188.7


def test_gamma_function_factorial():
    for n in range(1, 10):
        assert abs(math.gamma(n) - math.factorial(n - 1)) < 1e-6


# ---------- TD lois continues ----------
def _bisect(g, lo, hi, it=200):
    for _ in range(it):
        mid = (lo + hi) / 2
        if (g(lo) > 0) == (g(mid) > 0):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def test_tdc_ex1_parameters_and_intervals():
    assert abs(I(lambda x: 2 / x ** 2, 2, 20000, 2_000_000) - 1) < 1e-3
    assert abs(2 / 0.975 - 2.051) < 1e-3 and 2 / 0.025 == 80
    assert abs(2 * I(lambda x: math.exp(-2 * x), 0, 60) - 1) < 1e-9
    b = math.log(20) / 2
    assert abs(b - 1.498) < 1e-3 and abs(1 - math.exp(-2 * b) / 2 - 0.975) < 1e-12
    assert abs(I(lambda x: 0.75 * x * (2 - x), 0, 2) - 1) < 1e-12
    F3 = lambda x: 0.75 * x * x - x ** 3 / 4
    a = _bisect(lambda x: F3(x) - 0.025, 0, 1)
    assert abs(F3(a) - 0.025) < 1e-12
    assert round(a, 3) == 0.189 and round(2 - a, 3) == 1.811 and abs(F3(2 - a) - 0.975) < 1e-9


def test_tdc_ex2_probabilities_and_cdf():
    f = lambda x: 0.75 * (1 - x * x)
    assert abs(I(f, -1, 0) - 0.5) < 1e-12
    assert abs(I(f, -0.5, 0.5) - 11 / 16) < 1e-12
    assert abs(I(f, 0.5, 1) - 5 / 32) < 1e-12
    F = lambda x: 0.5 + 0.75 * x - x ** 3 / 4
    for x in [-1, -0.3, 0, 0.4, 1]:
        assert abs(F(x) - I(f, -1, x)) < 1e-12


def test_tdc_ex3_uniform():
    assert (6 - 3) / 6 == 0.5
    lo, hi = -3 + 8 * 0.0, -3 + 8 * 0.999999
    assert lo == -3 and hi < 5


def test_tdc_ex4_exponential():
    lam = 1 / 4
    assert abs(math.exp(-2) - 0.135) < 1e-3
    a = 4 * math.log(10)
    assert abs(a - 9.21) < 1e-2 and abs(1 - math.exp(-lam * a) - 0.9) < 1e-12
    assert abs(math.exp(-0.5) - 0.607) < 1e-3


def test_tdc_ex5_normal():
    assert abs(1 - Phi(2) - 0.0228) < 1e-4
    assert abs(120 - 1.96 * 15 - 90.6) < 1e-9 and abs(120 + 1.96 * 15 - 149.4) < 1e-9


def test_tdc_extras():
    # |X| avec X ~ U([-2, 1])
    for t in [0.2, 0.7, 1.0, 1.3, 1.9]:
        direct = I(lambda x: 1 / 3, max(-t, -2), min(t, 1))
        formula = 2 * t / 3 if t <= 1 else (1 + t) / 3
        assert abs(direct - formula) < 1e-12
    # X ~ E(1) : X² et e^X
    for t in [0.5, 2, 7]:
        assert abs(1 - math.exp(-math.sqrt(t)) - I(lambda x: math.exp(-x), 0, math.sqrt(t))) < 1e-9
    for t in [1.5, 3, 10]:
        assert abs(1 - 1 / t - I(lambda x: math.exp(-x), 0, math.log(t))) < 1e-9
        assert abs(I(lambda w: 1 / w ** 2, 1, t) - (1 - 1 / t)) < 1e-9


# ---------- Ch2 Espérance et variance + TD 2 ----------
def test_archery_numbers_and_slide_errors():
    p = {x: Fr(21 - 2 * x, 100) for x in range(1, 11)}
    assert sum(p.values()) == 1
    assert counting.expectation(p) == Fr(385, 100)
    assert sum(x * x * q for x, q in p.items()) == Fr(2035, 100) != Fr(1827, 100)
    assert counting.variance(p) == Fr(55275, 10000)
    assert abs(math.sqrt(5.5275) - 2.35) < 1e-2
    f = lambda x: 8 * x
    assert abs(I(f, 0, 0.5) - 1) < 1e-12
    assert abs(I(lambda x: x * f(x), 0, 0.5) - 1 / 3) < 1e-12
    assert abs(I(lambda x: x * x * f(x), 0, 0.5) - 0.125) < 1e-12
    assert Fr(1, 8) - Fr(1, 9) == Fr(1, 72) and abs(math.sqrt(1 / 72) - 0.118) < 1e-3
    assert round(0.125 - 0.33 ** 2, 3) == 0.016  # l'arrondi prématuré des slides


def test_games_and_bulbs():
    A = {4: Fr(1, 2), 6: Fr(1, 2)}
    B = {1: Fr(1, 2), 9: Fr(1, 2)}
    assert counting.expectation(A) == counting.expectation(B) == 5
    assert counting.variance(A) == 1 and counting.variance(B) == 16
    bulbB = {1000: Fr(8, 10), 600: Fr(2, 10)}
    assert counting.expectation(bulbB) == 920 and counting.variance(bulbB) == 25600
    assert abs(200 ** 2 / 12 - 3333.33) < 0.01 and round(math.sqrt(200 ** 2 / 12)) == 58


def test_td2_exercise1_tail_densities():
    # intégrales partielles sur [1, M] comparées aux primitives exactes, puis limites M -> +inf
    M = 1000.0
    n = 2_000_000
    assert abs(I(lambda x: 3 / x ** 4, 1, M, n) - (1 - M ** -3)) < 1e-8          # -> 1 : densité
    assert abs(I(lambda x: 3 / x ** 3, 1, M, n) - 1.5 * (1 - M ** -2)) < 1e-8    # -> 3/2 = E[X]
    assert abs(I(lambda x: 3 / x ** 2, 1, M, n) - 3 * (1 - 1 / M)) < 1e-8        # -> 3 = E[X²]
    assert 3 - 1.5 ** 2 == 0.75 and abs(math.sqrt(0.75) - 0.866) < 1e-3
    # 1/x² : ∫ x·g = ln M diverge ; 2/x³ : E = 2(1 - 1/M) -> 2 mais E[X²] = 2 ln M diverge
    assert abs(I(lambda x: 1 / x, 1, M, n) - math.log(M)) < 1e-8
    assert abs(I(lambda x: 2 / x ** 2, 1, M, n) - 2 * (1 - 1 / M)) < 1e-8
    assert abs(I(lambda x: 2 / x, 1, M, n) - 2 * math.log(M)) < 1e-8


def test_td2_uniform_exponential_normal_moments():
    assert abs(I(lambda x: x, 0, 1) - 0.5) < 1e-12 and abs(I(lambda x: x * x, 0, 1) - 1 / 3) < 1e-12
    for a, b in [(2, 8), (-3, 5)]:
        m = I(lambda x: x / (b - a), a, b)
        v = I(lambda x: x * x / (b - a), a, b) - m * m
        assert abs(m - (a + b) / 2) < 1e-9 and abs(v - (b - a) ** 2 / 12) < 1e-9
    assert abs(I(lambda x: x * math.exp(-x), 0, 80) - 1) < 1e-9
    assert abs(I(lambda x: x * x * math.exp(-x), 0, 80) - 2) < 1e-8
    for lam in [0.5, 2, 3]:
        m = I(lambda x: x * lam * math.exp(-lam * x), 0, 200 / lam)
        v = I(lambda x: x * x * lam * math.exp(-lam * x), 0, 200 / lam) - m * m
        assert abs(m - 1 / lam) < 1e-7 and abs(v - 1 / lam ** 2) < 1e-6
    phi = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
    assert abs(I(lambda x: x * phi(x), -15, 15)) < 1e-12
    assert abs(I(lambda x: x * x * phi(x), -15, 15) - 1) < 1e-9


def test_td2_law_of_large_numbers_bound():
    assert 4 / (100 * 0.5 ** 2) == 0.16 and 25 / 20 ** 2 == 0.0625
    # V(moyenne) = σ²/n pour des dés indépendants (n = 2, calcul exact)
    die = {k: Fr(1, 6) for k in range(1, 7)}
    mean2 = {}
    for a in range(1, 7):
        for b in range(1, 7):
            mean2[Fr(a + b, 2)] = mean2.get(Fr(a + b, 2), 0) + Fr(1, 36)
    assert counting.expectation(mean2) == Fr(7, 2) and counting.variance(mean2) == counting.variance(die) / 2
