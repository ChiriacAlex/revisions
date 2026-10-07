"""Les outils d'analyse (primitives, intégrales, DL, limites) sont testés sur des résultats sûrs."""
import math

from calculus import antiderivative_ok, integral, limit, series_coeff
from checks import evaluate_check


def test_antiderivative_detects_right_and_wrong_primitives():
    assert antiderivative_ok("x*exp(x)", "x*exp(x) - exp(x)")
    assert not antiderivative_ok("x*exp(x)", "-x*exp(x) - exp(x)")
    # Le poly donne ∫ cosh² = x/2 − sinh(2x)/4 : faux.
    assert antiderivative_ok("cosh(x)**2", "x/2 + sinh(2*x)/4")
    assert not antiderivative_ok("cosh(x)**2", "x/2 - sinh(2*x)/4")


def test_antiderivative_respects_the_domain_points():
    assert antiderivative_ok("1/sqrt(1-x**2)", "asin(x)", points=(-0.5, 0.2, 0.7))


def test_improper_integrals():
    assert math.isclose(integral("exp(-x)", 0, "oo"), 1)
    assert math.isclose(integral("log(x)", 0, 1), -1)
    assert math.isclose(integral("exp(-x**2)", "-oo", "oo"), math.sqrt(math.pi))


def test_series_and_limits():
    assert series_coeff("tan(x)", 5) == 2 / 15
    assert series_coeff("log(1+x)/sin(x)", 3) == -1 / 3
    assert math.isclose(limit("sin(x)/x", 0), 1)
    assert math.isclose(limit("x**2*sqrt(cosh(x)-1)/(sin(tan(x)**2)*log(1+x))", 0, "-"), -math.sqrt(2) / 2)


def test_python_expr_exposes_calculus():
    value = evaluate_check({"check": "python_expr", "expr": "calc.integral('1/(1+x**2)', 0, 'oo') * 2"})
    assert math.isclose(value, math.pi)


def test_limits_at_infinity():
    assert math.isclose(limit("sqrt(x**2+x)-x", "oo"), 0.5)
    assert limit("exp(x)/x**100", "oo") == math.inf
    assert math.isclose(limit("x*log(x)", 0, "+"), 0, abs_tol=1e-12)


def test_identity_checks_formula_sheets():
    from calculus import identity
    assert identity("cos(x)/sin(x) - cos(2*x)/sin(2*x)", "sin(x)/(sin(x)*sin(2*x))")
    assert not identity("cos(x)/sin(x) - cos(2*x)/sin(2*x)", "sin(-x)/(sin(x)*sin(2*x))")
    assert identity("cot(x)", "-I*(1+exp(2*I*x))/(1-exp(2*I*x))")
    assert not identity("cot(x)", "I*(1+exp(2*I*x))/(1-exp(2*I*x))")
