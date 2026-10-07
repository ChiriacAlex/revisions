"""IGAF : chaque primitive, valeur ou développement écrit dans les cours est recalculé.

Une primitive est validée en dérivant le résultat (F' = f en plusieurs points du domaine) ;
une intégrale généralisée par quadrature numérique ; un DL par SymPy."""
import math

import pytest

from calculus import antiderivative_ok, identity, integral, limit, series_coeff

# ---------- Ch1 — Primitives : exercices de changement de variable et d'IPP (poly p. 4 et 7) ----------
PRIMITIVES_EXERCISES = [
    ("(x**3+x)**5*(3*x**2+1)", "(x**3+x)**6/6"),
    ("(3*x+2)*(3*x**2+4*x)**4", "(3*x**2+4*x)**5/10"),
    ("sqrt(2*x+1)", "(2*x+1)**Rational(3,2)/3"),
    ("x*sqrt(2*x+1)", "(2*x+1)**Rational(5,2)/10 - (2*x+1)**Rational(3,2)/6"),
    ("2*x/(x**2+1)**Rational(1,3)", "Rational(3,2)*(x**2+1)**Rational(2,3)"),
    ("2*(2*x+4)**5", "(2*x+4)**6/6"),
    ("7*sqrt(7*x-1)", "Rational(2,3)*(7*x-1)**Rational(3,2)"),
    ("2*x*(x**2+5)**(-4)", "-1/(3*(x**2+5)**3)"),
    ("4*x**3/(x**4+1)**2", "-1/(x**4+1)"),
    ("x**2*sin(x**3)", "-cos(x**3)/3"),
    ("(1+sqrt(x))**Rational(1,3)/sqrt(x)", "Rational(3,2)*(1+sqrt(x))**Rational(4,3)"),
    ("x*sin(2*x**2)", "-cos(2*x**2)/4"),
    ("(1-cos(x/2))**2*sin(x/2)", "Rational(2,3)*(1-cos(x/2))**3"),
    ("9*x**2/sqrt(1-x**3)", "-6*sqrt(1-x**3)"),
    ("cos(1/x)**2/x**2", "-1/(2*x) - sin(2/x)/4"),
    ("sqrt(x)*sin(x**Rational(3,2)-1)**2", "(x**Rational(3,2)-1)/3 - sin(2*x**Rational(3,2)-2)/6"),
    ("1/sqrt(5*x+8)", "Rational(2,5)*sqrt(5*x+8)"),
    ("x*(1-x**2)**Rational(1,4)", "-Rational(2,5)*(1-x**2)**Rational(5,4)"),
    ("1/(sqrt(x)*(1+sqrt(x))**2)", "-2/(1+sqrt(x))"),
    ("sin(x/3)**5*cos(x/3)", "sin(x/3)**6/2"),
    ("sin(2*x+1)/cos(2*x+1)**2", "1/(2*cos(2*x+1))"),
    ("cos(1/x-1)/x**2", "-sin(1/x-1)"),
    ("cos(sqrt(x)+3)/sqrt(x)", "2*sin(sqrt(x)+3)"),
    ("sqrt(2-1/x)/x**2", "Rational(2,3)*(2-1/x)**Rational(3,2)"),
    ("sin(1/x)*cos(1/x)/x**2", "-sin(1/x)**2/2"),
    ("sqrt((x**2-1)/x**2)/x**3", "(1-1/x**2)**Rational(3,2)/3"),
    ("x*sqrt(4-x)", "Rational(2,5)*(4-x)**Rational(5,2) - Rational(8,3)*(4-x)**Rational(3,2)"),
    ("(x+1)**2*(1-x)**5", "-Rational(2,3)*(1-x)**6 + Rational(4,7)*(1-x)**7 - (1-x)**8/8"),
    ("(x+5)*(x-5)**Rational(1,3)", "Rational(3,7)*(x-5)**Rational(7,3) + Rational(15,2)*(x-5)**Rational(4,3)"),
    ("x**3*sqrt(x**2+1)", "(x**2+1)**Rational(5,2)/5 - (x**2+1)**Rational(3,2)/3"),
    ("3*x**5*sqrt(x**3+1)", "Rational(2,5)*(x**3+1)**Rational(5,2) - Rational(2,3)*(x**3+1)**Rational(3,2)"),
    ("x/(x**2-4)**3", "-1/(4*(x**2-4)**2)"),
    ("x/(x-4)**3", "-1/(x-4) - 2/(x-4)**2"),
    # IPP
    ("x*log(x)", "x**2*log(x)/2 - x**2/4"),
    ("x*sin(x)", "-x*cos(x) + sin(x)"),
    ("x**2*sin(x)", "-x**2*cos(x) + 2*x*sin(x) + 2*cos(x)"),
    ("x*cos(x)", "x*sin(x) + cos(x)"),
    ("x**2*cos(x)", "x**2*sin(x) + 2*x*cos(x) - 2*sin(x)"),
    ("x*exp(x)", "(x-1)*exp(x)"),
    ("x*atan(x)", "(x**2+1)*atan(x)/2 - x/2"),
    ("x**3*sin(x)", "-x**3*cos(x) + 3*x**2*sin(x) + 6*x*cos(x) - 6*sin(x)"),
    ("x**3*cos(x)", "x**3*sin(x) + 3*x**2*cos(x) - 6*x*sin(x) - 6*cos(x)"),
    ("x*sin(x)*cos(x)", "-x*cos(2*x)/4 + sin(2*x)/8"),
    ("x*sin(x)**2", "x**2/4 - x*sin(2*x)/4 - cos(2*x)/8"),
]

# Points pris dans tous les domaines (x > 1 évite les racines de 1 − x², x² − 4, etc. — sauf exceptions ci-dessous).
DOMAIN = {
    "9*x**2/sqrt(1-x**3)": (0.2, 0.5, 0.9),
    "x*(1-x**2)**Rational(1,4)": (0.2, 0.5, 0.9),
    "x*sqrt(4-x)": (0.5, 1.5, 3.5),
    "x/(x**2-4)**3": (2.5, 3.0, 5.0),
    "x/(x-4)**3": (4.5, 6.0, 9.0),
    "(x+5)*(x-5)**Rational(1,3)": (5.5, 7.0, 9.0),
    "sqrt((x**2-1)/x**2)/x**3": (1.2, 2.0, 3.0),
    "sqrt(2-1/x)/x**2": (0.8, 1.5, 3.0),
    "7*sqrt(7*x-1)": (0.5, 1.5, 3.0),
}


@pytest.mark.parametrize("f,F", PRIMITIVES_EXERCISES, ids=[f for f, _ in PRIMITIVES_EXERCISES])
def test_primitives_exercise_answers(f, F):
    assert antiderivative_ok(f, F, points=DOMAIN.get(f, (1.2, 1.7, 2.6)))


# ---------- Ch1 — Primitives : exemples du cours ----------
COURSE_PRIMITIVES = [
    ("tan(x)", "-log(cos(x))", (0.3, 0.9, 1.2)),
    ("x/sqrt(1-x**2)", "-sqrt(1-x**2)", (-0.5, 0.2, 0.8)),
    ("asin(x)", "x*asin(x)+sqrt(1-x**2)", (-0.5, 0.2, 0.8)),
    ("x*exp(x)", "(x-1)*exp(x)", (0.3, 1.0, 2.0)),
    ("x*sin(2*x)", "-x*cos(2*x)/2+sin(2*x)/4", (0.3, 1.0, 2.0)),
    ("x**2*exp(3*x)", "(x**2/3-2*x/9+Rational(2,27))*exp(3*x)", (0.3, 1.0, 2.0)),
    ("exp(x)*sin(x)", "exp(x)*(sin(x)-cos(x))/2", (0.3, 1.0, 2.0)),
    ("(x**2+7*x-5)*cos(2*x)", "(x**2+7*x-Rational(11,2))*sin(2*x)/2+(x+Rational(7,2))*cos(2*x)/2", (0.3, 1.0, 2.0)),
    ("1/sqrt(x**2-4)", "log(x/2+sqrt(x**2/4-1))", (2.5, 3.0, 5.0)),
    ("2*x/(x**2+1)**Rational(1,3)", "Rational(3,2)*(x**2+1)**Rational(2,3)", (0.3, 1.0, 2.0)),
]


@pytest.mark.parametrize("f,F,pts", COURSE_PRIMITIVES, ids=[c[0] for c in COURSE_PRIMITIVES])
def test_course_primitives(f, F, pts):
    assert antiderivative_ok(f, F, points=pts)


def test_poly_primitive_errors_are_really_errors():
    assert not antiderivative_ok("1/sqrt(x**2-4)", "log(x/2-sqrt(x**2/4-1))", points=(2.5, 3.0))
    assert not antiderivative_ok("asin(x)", "x*asin(x)+sqrt(1+x**2)", points=(0.2, 0.8))
    assert not antiderivative_ok("2*x*cos(x**2)", "-sin(x**2)")
    assert integral("x**2", -1, 1) == pytest.approx(2 * integral("x**2", 0, 1))
    assert integral("sin(x)", 0, "pi") / math.pi == pytest.approx(2 / math.pi)


# ---------- Ch1 bis — Fractions rationnelles ----------
DECOMPOSITIONS = [
    ("(5*x-1)/(x**2-x-2)", "2/(x+1)+3/(x-2)"),
    ("(x**2-3)/((x-1)**2*(x+1))", "-1/(x-1)**2+Rational(3,2)/(x-1)-Rational(1,2)/(x+1)"),
    ("x**2/((x-1)*(x+2)*(x+3))", "Rational(1,12)/(x-1)-Rational(4,3)/(x+2)+Rational(9,4)/(x+3)"),
    ("(4*x**3+16*x**2+23*x+13)/((x+1)**3*(x+2))", "2/(x+1)**3+1/(x+1)**2+3/(x+1)+1/(x+2)"),
    ("1/((x-1)**3*(x**2+2*x+5))", "1/(8*(x-1)**3)-1/(16*(x-1)**2)+1/(64*(x-1))+(-x+1)/(64*(x**2+2*x+5))"),
    ("(x**9+x)/((x-1)**3*(x**2+1)**2*(x+2))", "x+1+1/(6*(x-1)**3)+4/(9*(x-1)**2)+41/(27*(x-1))+514/(675*(x+2))+(x+3)/(10*(x**2+1)**2)-(7*x+11)/(25*(x**2+1))"),
    ("(x**6+2)/((x**2+1)*(x**2-16))", "x**2+15-1/(17*(x**2+1))+2049/(68*(x-4))-2049/(68*(x+4))"),
    ("(x**5+2*x-1)/((x-1)**3*(x+1))", "x+2+1/(x-1)**3+3/(x-1)**2+7/(2*(x-1))+1/(2*(x+1))"),
    ("(x+1)/((x**2+1)**2*(x**2+x+1)**2)", "-(x+1)/(x**2+1)**2-(3*x-1)/(x**2+1)-1/(x**2+x+1)**2+(3*x+2)/(x**2+x+1)"),
    ("(x+1)/(x*(x**2+1)**2)", "1/x-(x-1)/(x**2+1)**2-x/(x**2+1)"),
    ("(5*x**3-17*x**2+19*x-13)/((x+1)*(x-2)**3)", "-1/(x-2)**3+4/(x-2)**2+3/(x-2)+2/(x+1)"),
    ("(x**2+x-5)/(x**2-1)", "1+Rational(5,2)/(x+1)-Rational(3,2)/(x-1)"),
    ("(2*x**3+4*x**2-3*x+5)/(x**2-2*x+1)", "2*x+8+8/(x-1)**2+11/(x-1)"),
    ("1/(x*(x**2+2*x+5))", "1/(5*x)-(x+2)/(5*(x**2+2*x+5))"),
    ("1/(x**2*(x**2+2*x+5))", "1/(5*x**2)-2/(25*x)+(2*x-1)/(25*(x**2+2*x+5))"),
    ("(4*x**3-7*x**2+31*x-38)/((x**2+4)*(x**2+9))", "(3*x-2)/(x**2+4)+(x-5)/(x**2+9)"),
    ("(12*x**4+190*x**2+13*x-6)/((2*x-1)*(x**2+16))", "6*x+3+3/(2*x-1)-(x-6)/(x**2+16)"),
]


@pytest.mark.parametrize("f,decomposition", DECOMPOSITIONS, ids=[d[0] for d in DECOMPOSITIONS])
def test_partial_fractions(f, decomposition):
    assert identity(f, decomposition, points=(0.37, 1.61, 2.71, -3.3))


FRACTION_PRIMITIVES = [
    ("(5*x-1)/(x**2-x-2)", "2*log(x+1)+3*log(x-2)", (2.5, 3.0, 5.0)),
    ("(5*x**3-17*x**2+19*x-13)/((x+1)*(x-2)**3)", "1/(2*(x-2)**2)-4/(x-2)+3*log(x-2)+2*log(x+1)", (2.5, 3.0, 5.0)),
    ("x/(x**2+2*x+5)", "log(x**2+2*x+5)/2-atan((x+1)/2)/2", (0.3, 1.0, 2.0)),
    ("1/(x*(x**2+2*x+5))", "log(x)/5-log(x**2+2*x+5)/10-atan((x+1)/2)/10", (0.3, 1.0, 2.0)),
    ("1/(x**2*(x**2+2*x+5))", "-1/(5*x)-Rational(2,25)*log(x)+log(x**2+2*x+5)/25-Rational(3,50)*atan((x+1)/2)", (0.3, 1.0, 2.0)),
    ("(4*x**3-7*x**2+31*x-38)/((x**2+4)*(x**2+9))", "Rational(3,2)*log(x**2+4)-atan(x/2)+log(x**2+9)/2-Rational(5,3)*atan(x/3)", (0.3, 1.0, 2.0)),
    ("(12*x**4+190*x**2+13*x-6)/((2*x-1)*(x**2+16))", "3*x**2+3*x+Rational(3,2)*log(2*x-1)-log(x**2+16)/2+Rational(3,2)*atan(x/4)", (0.8, 1.0, 2.0)),
    ("x/(x**2+2*x+5)**2", "-(x+5)/(8*(x**2+2*x+5))-atan((x+1)/2)/16", (0.3, 1.0, 2.0)),
    ("1/(1+x**2)**2", "(x/(1+x**2)+atan(x))/2", (0.3, 1.0, 2.0)),
    ("1/(1+x**2)**3", "Rational(3,8)*atan(x)+Rational(3,8)*x/(1+x**2)+x/(4*(1+x**2)**2)", (0.3, 1.0, 2.0)),
]


@pytest.mark.parametrize("f,F,pts", FRACTION_PRIMITIVES, ids=[c[0] for c in FRACTION_PRIMITIVES])
def test_fraction_primitives(f, F, pts):
    assert antiderivative_ok(f, F, points=pts)


def test_fraction_definite_integrals_and_poly_errors():
    assert integral("(x**2+x-5)/(x**2-1)", 2, 3) == pytest.approx(1 + 3.5 * math.log(2) - 2.5 * math.log(3))
    assert integral("(2*x**3+4*x**2-3*x+5)/(x**2-2*x+1)", 2, 3) == pytest.approx(17 + 11 * math.log(2))
    # Erreurs du poly : exemple 27 (A1 = −2/5…) et exemple 31 (oubli de dx = 2 dt)
    assert not antiderivative_ok("1/(x**2*(x**2+2*x+5))", "-1/(5*x)-Rational(2,5)*log(x)+log(x**2+2*x+5)/10-Rational(3,10)*atan((x+1)/2)")
    assert not antiderivative_ok("x/(x**2+2*x+5)**2", "-1/(2*x**2+4*x+10)-Rational(1,64)*(1+x)/(1+((1+x)/2)**2)-atan((1+x)/2)/32")
    assert not identity("(4*x**3+16*x**2+23*x+13)/((x+1)**3*(x+2))", "2/(x+1)**3+1/(x+1)**2+6/(x+1)+1/(x+2)")


# ---------- Ch1 ter — Trigonométrie, Bioche, abéliennes ----------
TRIG_PRIMITIVES = [
    ("sin(x)**3*cos(x)**2", "cos(x)**5/5-cos(x)**3/3", (0.3, 1.0, 2.0)),
    ("cos(x)**5", "sin(x)-2*sin(x)**3/3+sin(x)**5/5", (0.3, 1.0, 2.0)),
    ("sin(x)**2*cos(x)**2", "x/8-sin(4*x)/32", (0.3, 1.0, 2.0)),
    ("sin(x)**2*cos(x)**4", "x/16-sin(4*x)/64+sin(2*x)**3/48", (0.3, 1.0, 2.0)),
    ("tan(x)**2", "tan(x)-x", (0.3, 0.9, 1.2)),
    ("cos(5*x)*sin(3*x)", "cos(2*x)/4-cos(8*x)/16", (0.3, 1.0, 2.0)),
    ("sin(x)/(1+cos(x)**2)", "-atan(cos(x))", (0.3, 1.0, 2.0)),
    ("cos(x)/(sin(x)**2-cos(x)**2)", "log(abs((sin(x)-1/sqrt(2))/(sin(x)+1/sqrt(2))))/(2*sqrt(2))", (0.2, 1.2, 2.5)),
    ("1/(cos(x)**2*(1+tan(x)))", "log(abs(1+tan(x)))", (0.2, 0.6, 1.0)),
    ("1/(1+cos(x))", "tan(x/2)", (0.3, 1.0, 2.0)),
    ("1/(-5+13*cosh(x))", "atan(3*tanh(x/2)/2)/6", (0.3, 1.0, 2.0)),
    ("1/(x+sqrt(x-1))", "log(x+sqrt(x-1))-2/sqrt(3)*atan((2*sqrt(x-1)+1)/sqrt(3))", (1.5, 3.0, 7.0)),
    ("1/(x*sqrt(x-1))", "2*atan(sqrt(x-1))", (1.5, 3.0, 7.0)),
    ("1/(x*sqrt(x**2+6*x+10))", "(log(abs(sqrt(x**2+6*x+10)-x-sqrt(10)))-log(abs(sqrt(x**2+6*x+10)-x+sqrt(10))))/sqrt(10)", (0.5, 2.0, 7.0)),
    ("x**2/sqrt(9-x**2)", "Rational(9,2)*asin(x/3)-x*sqrt(9-x**2)/2", (0.5, 1.5, 2.5)),
    ("sqrt(x**2+2*x+5)", "2*asinh((x+1)/2)+(x+1)*sqrt(x**2+2*x+5)/2", (0.3, 1.0, 2.0)),
    ("sqrt(-x**2+4*x-3)", "asin(x-2)/2+(x-2)*sqrt(-x**2+4*x-3)/2", (1.3, 2.2, 2.8)),
]


@pytest.mark.parametrize("f,F,pts", TRIG_PRIMITIVES, ids=[c[0] for c in TRIG_PRIMITIVES])
def test_trig_and_abelian_primitives(f, F, pts):
    assert antiderivative_ok(f, F, points=pts)


# ---------- TD 1 — Intégration simple ----------
TD1_PRIMITIVES = [
    ("sin(x)**2", "x/2-sin(2*x)/4", (0.3, 1.0, 2.0)),
    ("cosh(x)**2", "x/2+sinh(2*x)/4", (0.3, 1.0, 2.0)),
    ("(acos(x)-x)/sqrt(1-x**2)", "-acos(x)**2/2+sqrt(1-x**2)", (-0.5, 0.2, 0.7)),
    ("sin(2*x)*exp(sin(x)**2)", "exp(sin(x)**2)", (0.3, 1.0, 2.0)),
    ("x/(2-x**2+2*x)", "-log(abs(-x**2+2*x+2))/2+log(abs((sqrt(3)+x-1)/(sqrt(3)-x+1)))/(2*sqrt(3))", (0.5, 1.5, 3.5)),
    ("1/(1+x+2*sqrt(1-x))", "log(abs(-(1-x)+2*sqrt(1-x)+2))-log(abs((sqrt(3)+sqrt(1-x)-1)/(sqrt(3)-sqrt(1-x)+1)))/sqrt(3)", (0.5, -1.5, -5.0)),
    ("x**2*log(x)", "x**3*log(x)/3-x**3/9", (0.3, 1.0, 2.0)),
    ("x*asin(x)/sqrt(1-x**2)", "-sqrt(1-x**2)*asin(x)+x", (-0.5, 0.2, 0.7)),
    ("asin(x/2)**2/sqrt(4-x**2)", "asin(x/2)**3/3", (-1.5, 0.5, 1.5)),
    ("x*log((1+x)/(1-x))", "(x**2-1)/2*log((1+x)/(1-x))+x", (-0.5, 0.2, 0.7)),
    ("exp(-x)*cos(x)", "exp(-x)*(sin(x)-cos(x))/2", (0.3, 1.0, 2.0)),
    ("1/(2*x+1)", "log(2*x+1)/2", (0.3, 1.0, 2.0)),
    ("x**3/(x+1)", "x**3/3-x**2/2+x-log(x+1)", (0.3, 1.0, 2.0)),
    ("(2*x-1)/(x-1)**2", "2*log(abs(x-1))-1/(x-1)", (0.3, 1.5, 3.0)),
    ("2*x**2/(x**4-1)", "log(abs(x-1))/2-log(abs(x+1))/2+atan(x)", (0.3, 1.5, 3.0)),
    ("1/(x**2*(x-1)**3)", "-3*log(abs(x))+1/x+3*log(abs(x-1))+2/(x-1)-1/(2*(x-1)**2)", (0.3, 1.5, 3.0)),
    ("1/(x**2+1)**2", "atan(x)/2+x/(2*(1+x**2))", (0.3, 1.0, 2.0)),
    ("1/(x*(x**2+1)**2)", "1/(2*(1+x**2))+log(abs(x))-log(1+x**2)/2", (0.3, 1.0, 2.0)),
    ("1/(x*(x**5+1)**2)", "log(abs(x))-log(abs(x**5+1))/5+1/(5*(x**5+1))", (0.3, 1.0, 2.0)),
    ("x**3/(1+x**2)**3", "1/(4*(1+x**2)**2)-1/(2*(1+x**2))", (0.3, 1.0, 2.0)),
    ("x**3/(1+x**2)**3", "(x**2/(1+x**2))**2/4", (0.3, 1.0, 2.0)),
    ("tan(x)/(1+sin(x)**2)", "-log(abs(cos(x)))/2+log(1+sin(x)**2)/4", (0.3, 1.2, 2.5)),
    ("1/cos(x)**4", "tan(x)+tan(x)**3/3", (0.2, 0.5, 1.2)),
    ("1/(sin(x)**2-cos(x)**2)", "-log(abs((1+tan(x))/(1-tan(x))))/2", (0.2, 0.5, 1.2)),
    ("1/(1-x)*sqrt(x/(1-x))", "2*sqrt(x/(1-x))-2*atan(sqrt(x/(1-x)))", (0.2, 0.5, 0.8)),
    ("1/(x-2+sqrt(x**2-2*x+2))", "(sqrt(x**2-2*x+2)-x)/2+log(abs(sqrt(x**2-2*x+2)-x))-log(abs(1+sqrt(x**2-2*x+2)-x))/2", (0.3, 3.0, 5.0)),
    ("sqrt((1-x)/(1+x))/x", "log(abs((sqrt((1-x)/(1+x))-1)/(sqrt((1-x)/(1+x))+1)))+2*atan(sqrt((1-x)/(1+x)))", (0.3, 0.8, -0.5)),
    ("sqrt(1+(x+2)**2)", "asinh(x+2)/2+(x+2)*sqrt(1+(x+2)**2)/2", (0.3, 1.0, 2.0)),
    ("1/sqrt(x**2+2*x)", "acosh(x+1)", (0.3, 1.0, 2.0)),
    ("1/sqrt(-9*x**2-6*x+3)", "asin((3*x+1)/2)/3", (-0.5, 0.1, 0.25)),
    ("(2*x-3)/sqrt(4*x-4*x**2)", "-sqrt(x-x**2)-asin(2*x-1)", (0.2, 0.5, 0.8)),
    ("(8*x-3)/sqrt(-4*x**2+12*x-5)", "-2*sqrt(-4*x**2+12*x-5)+Rational(9,2)*asin(x-Rational(3,2))", (0.7, 1.2, 2.3)),
    ("1/((1+x)*(2+x))", "log(1+x)-log(2+x)", (0.3, 1.0, 2.0)),
    ("log(1+x)/(2+x)**2", "-log(1+x)/(2+x)+log(1+x)-log(2+x)", (0.3, 1.0, 2.0)),
    ("exp(-x)*log(1+exp(x))/(1+2*exp(-x))**2", "-log(1+exp(x))/(2+exp(x))+log(1+exp(x))-log(2+exp(x))", (0.3, 1.0, 2.0)),
    ("1/((cos(x)+sin(x))*(2*cos(x)+sin(x)))", "log(abs((1+tan(x))/(2+tan(x))))", (0.2, 0.6, 1.0)),
    ("1/(x*(x**2-1))", "-log(x)+log(x+1)/2+log(x-1)/2", (1.5, 2.0, 3.0)),
    ("2*x/(x**2-1)**2", "-1/(x**2-1)", (1.5, 2.0, 3.0)),
]


@pytest.mark.parametrize("f,F,pts", TD1_PRIMITIVES, ids=[f"{c[0]}->{c[1]}" for c in TD1_PRIMITIVES])
def test_td1_primitives(f, F, pts):
    assert antiderivative_ok(f, F, points=pts)


def test_td1_definite_integrals_and_wallis():
    assert integral("(x**2-1)/(2*x-1)", -1, 0) == pytest.approx(3 / 8 * math.log(3))
    assert integral("cos(x)**3/(1-2*sin(x))", "-pi/2", 0) == pytest.approx(3 / 8 * math.log(3))
    assert integral("2*x*log(x)/(x**2-1)**2", 2, 3) == pytest.approx(-13 / 8 * math.log(3) + 17 / 6 * math.log(2))
    wallis = [integral(f"sin(x)**{n}", 0, "pi/2") for n in range(12)]
    assert wallis[0] == pytest.approx(math.pi / 2) and wallis[1] == pytest.approx(1)
    for n in range(10):
        assert wallis[n + 2] == pytest.approx((n + 1) / (n + 2) * wallis[n])
        assert (n + 1) * wallis[n] * wallis[n + 1] == pytest.approx(math.pi / 2)


def test_td1_errors_of_the_handout_are_errors():
    wrong = [
        ("cosh(x)**2", "x/2-sinh(2*x)/4"), ("(acos(x)-x)/sqrt(1-x**2)", "-acos(x)/2+sqrt(1-x**2)"),
        ("asin(x/2)**2/sqrt(4-x**2)", "Rational(2,5)*asin(x/2)**3"),
        ("x*log((1+x)/(1-x))", "x**2/2*log((1+x)/(1-x))-x+log((1+x)/(1-x))/2"),
        ("1/(x**2*(x-1)**3)", "-3*log(abs(x))+1/x-3*log(abs(x-1))+2/(x-1)-1/(2*(x-1)**2)"),
        ("1/(x*(x**5+1)**2)", "log(abs(x**5))/5+log(abs(x**5+1))/5+1/(5*(x**5+1))"),
        ("(2*x-3)/sqrt(4*x-4*x**2)", "-sqrt(x-x**2)/2-asin(2*x-1)/4"),
        ("1/(2*x+1)", "log(2*x+1)"),
    ]
    for f, F in wrong:
        assert not antiderivative_ok(f, F, points=(0.2, 0.4)), f


# ---------- Ch2 — Développements limités ----------
def _dl(f, order):
    return [series_coeff(f, k) for k in range(order + 1)]


@pytest.mark.parametrize("f,coeffs", [
    ("1/(1-x)-exp(x)", [0, 0, 1 / 2, 5 / 6]),
    ("sqrt(1+x)+sqrt(1-x)", [2, 0, -1 / 4, 0, -5 / 64]),
    ("sqrt(1+x)", [1, 1 / 2, -1 / 8, 1 / 16, -5 / 128]),
    ("1/sqrt(1+x)", [1, -1 / 2, 3 / 8, -5 / 16]),
    ("sin(x)*cos(x)", [0, 1, 0, -2 / 3, 0, 2 / 15]),
    ("(1+x**3)*sqrt(1-x)", [1, -1 / 2, -1 / 8, 15 / 16]),
    ("exp(x)/(1+x)", [1, 0, 1 / 2, -1 / 3]),
    ("sin(2*x)", [0, 2, 0, -4 / 3, 0, 4 / 15]),
    ("1/(1+x**2)", [1, 0, -1, 0, 1, 0, -1]),
    ("1/(1+cos(x))", [1 / 2, 0, 1 / 8]),
    ("tan(x)", [0, 1, 0, 1 / 3, 0, 2 / 15, 0, 17 / 315]),
    ("tanh(x)", [0, 1, 0, -1 / 3, 0, 2 / 15, 0, -17 / 315]),
    ("atan(x)", [0, 1, 0, -1 / 3, 0, 1 / 5]),
    ("atanh(x)", [0, 1, 0, 1 / 3, 0, 1 / 5]),
    ("asin(x)", [0, 1, 0, 1 / 6, 0, 3 / 40]),
    ("asinh(x)", [0, 1, 0, -1 / 6, 0, 3 / 40]),
    ("log(1-x)", [0, -1, -1 / 2, -1 / 3, -1 / 4]),
    ("log(1+x)/sin(x)", [1, -1 / 2, 1 / 2, -1 / 3]),
])
def test_taylor_expansions(f, coeffs):
    assert _dl(f, len(coeffs) - 1) == pytest.approx(coeffs)


def test_dl_limits_and_equivalents():
    assert series_coeff("exp(cos(x))", 0) == pytest.approx(math.e)
    assert series_coeff("exp(cos(x))", 2) == pytest.approx(-math.e / 2)
    assert limit("x**2*sqrt(cosh(x)-1)/(sin(tan(x)**2)*log(1+x))", 0, "-") == pytest.approx(-math.sqrt(2) / 2)
    for f, g in [("sin(x)", "x"), ("log(1+x)", "x"), ("1-cos(x)", "x**2/2"), ("cosh(x)-1", "x**2/2"),
                 ("exp(x)-1-x", "x**2/2"), ("sin(x)-x", "-x**3/6"), ("(1+x)**Rational(1,3)-1", "x/3")]:
        assert limit(f"({f})/({g})", 0) == pytest.approx(1)


# ---------- Ch3 — Intégrales généralisées et méthodes ----------
@pytest.mark.parametrize("f,a,b,value", [
    ("exp(-x)", 0, "oo", 1),
    ("1/(4-x)**Rational(1,2)", 0, 4, 4),
    ("1/x**Rational(3,2)", 1, "oo", 2),
    ("1/(1+x**2)", 0, "oo", math.pi / 2),
    ("1/x**2", 1, "oo", 1),  # ∫ₑ^∞ dx/(x ln²x) après u = ln x (la quadrature directe converge trop lentement)
    ("log(x)/x**2", 1, "oo", 1),
    ("x*exp(-x)", 0, "oo", 1),
    ("x*exp(-2*x)", 0, "oo", 1 / 4),
    ("log(x)", 0, 1, -1),
    ("log(x)/(1+x)**2", 0, 1, -math.log(2)),
    ("log(x)/sqrt(1-x)", 0, 1, 4 * math.log(2) - 4),
    ("exp(-x)*sin(x)", 0, "oo", 1 / 2),
    ("(1+x+x**2)*exp(-x)", 0, "oo", 4),
    ("exp(-x**2)", 0, "oo", math.sqrt(math.pi) / 2),
    ("x*log(x)/(1+x**2)**2", 0, "oo", 0),
    ("log(sin(x))", 0, "pi/2", -math.pi / 2 * math.log(2)),
    ("1/sqrt((x-1)*(2-x))", 1, 2, math.pi),
    ("1/((1+x)*sqrt(x))", 0, 1, math.pi / 2),
    ("1/((1+x)*sqrt(x))", 1, "oo", math.pi / 2),
    ("1/sqrt(x)", 0, 4, 4),
    ("x**(-Rational(1,3))", 0, 1, 1.5),
])
def test_improper_integral_values(f, a, b, value):
    assert integral(f, a, b) == pytest.approx(value, abs=1e-9)


@pytest.mark.parametrize("f,g,at,side", [
    ("(x+1)/(x**3+2)", "1/x**2", "oo", None),
    ("(1-cos(x))/x**3", "1/(2*x)", 0, "+"),
    ("(exp(1/x)-cos(1/x))/x", "1/x**2", "oo", None),
    ("1/(1-cos(x))**Rational(1,3)", "2**Rational(1,3)/x**Rational(2,3)", 0, "+"),
    ("1/(x**2*(x**3-8)**Rational(2,3))", "1/(4*12**Rational(2,3)*(x-2)**Rational(2,3))", 2, "+"),
    ("sqrt(x)/log(1+x)*sin(1/x**2)", "1/(x**Rational(3,2)*log(x))", "oo", None),
    ("(cbrt(x+1)-cbrt(x+2))/sqrt(x)", "-1/(3*x**Rational(7,6))", "oo", None),
    ("1/(cbrt(x)*sqrt(1-x**3)*log(1+x))", "1/x**Rational(4,3)", 0, "+"),
    ("1/sqrt(x*tan(x))", "1/x", 0, "+"),
    ("1/sqrt(x**3-1)", "1/(sqrt(3)*sqrt(x-1))", 1, "+"),
    ("log(x+1)/sin(x-1)**2", "log(2)/(x-1)**2", 1, "+"),
    ("1/sqrt(x**3+x**2)", "1/x", 0, "+"),
])
def test_equivalents_used_in_convergence_proofs(f, g, at, side):
    assert limit(f"({f})/({g})", at, side) == pytest.approx(1)


def test_slowly_convergent_bertrand_integral_by_primitive():
    # primitive −1/ln x : vaut −1 en x = e et tend vers 0 en +∞, donc ∫ₑ^∞ = 1
    assert antiderivative_ok("1/(x*log(x)**2)", "-1/log(x)", points=(2.9, 5, 30))
    assert limit("-1/log(x)", "oo") == 0


def test_divergent_bertrand_integral():
    assert antiderivative_ok("1/(x*log(x))", "log(log(x))", points=(2.5, 4, 9))
    assert limit("log(log(x))", "oo") == math.inf


# ---------- TD 2 — Intégrales généralisées ----------
def test_td_improper_integrals():
    for alpha in (0.5, 2.0):
        assert integral(f"exp(-{alpha}*x)", 0, "oo") == pytest.approx(1 / alpha)
        assert integral(f"exp({alpha}*x)", "-oo", 0) == pytest.approx(1 / alpha)  # et non −1/α
    assert integral("x**(-Rational(5,4))", 1, "oo") == pytest.approx(4)
    assert integral("log(x)*exp(-x)", 0, "oo", breakpoints=(1,)) == pytest.approx(-0.5772156649015329)
    assert integral("log(1+x**2)/x**2", 0, "oo", breakpoints=(1,)) == pytest.approx(math.pi)
    assert integral("1/(2+x**2)", 0, "oo") == pytest.approx(math.pi / (2 * math.sqrt(2)))
    assert identity("(3+2*x**2)/((1+x**2)*(2+x**2))", "1/(1+x**2)+1/(2+x**2)")
    assert integral("(3+2*x**2)/((1+x**2)*(2+x**2))", 0, "oo") == pytest.approx(math.pi * (2 + math.sqrt(2)) / 4)
    for lam in (0.5, 2.0):
        assert integral(f"{lam}*exp(-{lam}*x)", 0, "oo") == pytest.approx(1)
        assert integral(f"x*{lam}*exp(-{lam}*x)", 0, "oo") == pytest.approx(1 / lam)
        assert integral(f"x**2*{lam}*exp(-{lam}*x)", 0, "oo") - lam ** -2 == pytest.approx(1 / lam ** 2)
    A, a, w = 1.3, 0.7, 2.1
    energy = integral(f"({A}*exp(-{a}*x)*cos({w}*x))**2", 0, "oo")
    assert energy == pytest.approx(A ** 2 / (4 * a) + A ** 2 * a / (4 * (a * a + w * w)))


def test_fresnel_value():
    import mpmath
    mpmath.mp.dps = 20
    value = mpmath.quadosc(lambda t: mpmath.cos(t * t), [0, mpmath.inf], zeros=lambda n: mpmath.sqrt(mpmath.pi * (n - 0.5)))
    assert float(value) == pytest.approx(0.5 * math.sqrt(math.pi / 2), rel=1e-8)


# ---------- Ch4 — Suites d'intégrales ----------
def test_dominated_convergence_examples():
    seq = [integral(f"1/(x**{n}+exp(x))", 0, "oo", breakpoints=(1,)) for n in (5, 20, 80)]
    assert abs(seq[-1] - (1 - math.exp(-1))) < abs(seq[0] - (1 - math.exp(-1)))
    assert seq[-1] == pytest.approx(1 - math.exp(-1), abs=1e-2)
    assert integral("sin(x)**200", 0, "pi/2") == pytest.approx(math.sqrt(math.pi / 400), rel=1e-2)
    for n in (1, 5, 20):  # la bosse qui s'échappe garde une aire proche de √π
        assert integral(f"exp(-(x-{n})**2)", 0, "oo", breakpoints=(n,)) == pytest.approx(
            math.sqrt(math.pi) * (1 + math.erf(n)) / 2)
    for n in (1, 4, 10):  # densité normale N(0, 1/n²) : aire 1
        assert integral(f"{n}/sqrt(2*pi)*exp(-{n}**2*x**2/2)", "-oo", "oo", breakpoints=(0,)) == pytest.approx(1)
    for n in (1, 3, 10):
        assert integral(f"(sin(x)+sin(10*x)/{n})**2", 0, "2*pi") == pytest.approx(math.pi + math.pi / n ** 2)


# ---------- TD 3 — Suites d'intégrales ----------
def test_td_sequences_of_integrals():
    n = 10 ** 4
    assert integral(f"{n}*log(1+x/{n})/(1+x**2)**2", 0, "oo") == pytest.approx(0.5, abs=1e-3)
    assert integral("x/(1+x**2)**2", 0, "oo") == pytest.approx(0.5)
    assert integral("sin(x)/(10**4+x**2)", 0, "oo", breakpoints=(100,)) == pytest.approx(0, abs=1e-3)
    assert integral("1/(1+x**2)**400", 0, "oo") == pytest.approx(0, abs=0.05)
    m = 2000
    assert m * integral(f"sin(x/{m})/(x*(1+x**2))", 0, "oo", breakpoints=(1,)) == pytest.approx(math.pi / 2, rel=1e-3)
    for k in (5, 20):  # approximation de Gauss
        assert integral(f"(1-x**2/{k}**2)**({k}**2)", 0, k) == pytest.approx(math.sqrt(math.pi) / 2, abs=5e-2)
    assert integral("(1-x**2/40**2)**(40**2)", 0, 40) == pytest.approx(math.sqrt(math.pi) / 2, abs=1e-3)
    for k in (2, 7):
        assert integral(f"({k}+1)*x**{k}", 0, 1) == pytest.approx(1)


# ---------- Ch5 / TD 4 — Intégrales à paramètre ----------
def test_gamma_function():
    for n in range(1, 7):
        assert integral(f"exp(-x)*x**{n - 1}", 0, "oo") == pytest.approx(math.factorial(n - 1))
    assert integral("exp(-x)*x**(-Rational(1,2))", 0, "oo") == pytest.approx(math.sqrt(math.pi))
    for x0 in (0.5, 1.7, 3.2):  # Γ(x + 1) = x Γ(x)
        assert integral(f"exp(-x)*x**{x0}", 0, "oo") == pytest.approx(x0 * integral(f"exp(-x)*x**({x0}-1)", 0, "oo"))
    for n, s in [(1, 2.0), (3, 1.5)]:
        assert integral(f"x**{n}*exp(-{s}*x)", 0, "oo") == pytest.approx(math.factorial(n) / s ** (n + 1))


def test_parameter_integral_exercises():
    def F(xv):  # F(x) = ∫ sin(xt) e^{-t²} dt vérifie F' + x F / 2 = 1/2
        return integral(f"sin({xv}*x)*exp(-x**2)", 0, "oo")
    for xv in (0.5, 1.3):
        h = 1e-4
        derivative = (F(xv + h) - F(xv - h)) / (2 * h)
        assert derivative + xv / 2 * F(xv) == pytest.approx(0.5, abs=1e-6)
        dawson = 0.5 * math.exp(-xv ** 2 / 4) * integral("exp(x**2/4)", 0, xv)
        assert F(xv) == pytest.approx(dawson)
    assert integral("x**2", 0, 1) == pytest.approx(1 / 3)
    eps = 1e-4  # taux d'accroissement de ∫₀^π sin(x sin t) dt
    assert integral(f"sin({eps}*sin(x))", 0, "pi") / eps == pytest.approx(2, abs=1e-6)
    for xv in (0.5, 1, 3):
        assert integral(f"sin(x)/x*exp(-{xv}*x)", 0, "oo") == pytest.approx(math.pi / 2 - math.atan(xv))
        assert integral(f"exp(-{xv}*x)*sin(x)", 0, "oo") == pytest.approx(1 / (1 + xv ** 2))
        assert integral(f"(exp(-{xv}*x)-exp(-x))/x", 0, "oo") == pytest.approx(-math.log(xv))
    assert integral("(exp(-x)-exp(-3*x))/x", 0, "oo") == pytest.approx(math.log(3))


def test_gauss_by_the_auxiliary_function():
    for xv in (0.3, 1.0, 2.0):
        g = integral(f"exp(-(x**2+1)*{xv}**2)/(1+x**2)", 0, 1)
        f = integral("exp(-x**2)", 0, xv)
        assert g + f ** 2 == pytest.approx(math.pi / 4)
        assert 0 <= g <= math.pi / 4 * math.exp(-xv ** 2)
    assert integral("exp(-x**2)", 0, "oo") == pytest.approx(math.sqrt(math.pi) / 2)
    assert integral("exp(-4*x**2)", "-oo", "oo") == pytest.approx(math.sqrt(math.pi / 4))
