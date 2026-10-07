"""Outils d'analyse pour vérifier les cours d'intégration : primitives, intégrales généralisées,
développements limités et limites. Les expressions sont des chaînes SymPy en la variable x."""
import mpmath
import sympy as sp

x = sp.Symbol("x", real=True)
_NS = {"x": x, "e": sp.E, "pi": sp.pi, "oo": sp.oo}


def parse(expr):
    return sp.sympify(expr, locals=_NS)


def antiderivative_ok(f, F, points=(0.3, 0.7, 1.3, 2.9), tol=1e-9):
    """F' = f aux points donnés (choisis dans le domaine) : le résultat d'un calcul de primitive est juste."""
    gap = sp.diff(parse(F), x) - parse(f)
    for p in points:
        point = sp.Float(str(p), 40)
        scale = max(1.0, abs(complex(parse(f).subs(x, point).evalf(40))))
        if abs(complex(gap.subs(x, point).evalf(40))) > tol * scale:
            return False
    return True


def _bound(b):
    if b in ("oo", "+oo"):
        return mpmath.inf
    if b == "-oo":
        return -mpmath.inf
    return mpmath.mpf(sp.N(parse(str(b)), 30)) if isinstance(b, str) else mpmath.mpf(b)


def integral(f, a, b, breakpoints=()):
    """Valeur numérique de ∫_a^b f (intégrale généralisée convergente), par quadrature adaptative."""
    func = sp.lambdify(x, parse(f), "mpmath")
    mpmath.mp.dps = 30
    nodes = [_bound(a), *[_bound(c) for c in breakpoints], _bound(b)]
    return float(mpmath.quad(func, nodes))


def series_coeff(f, n, at=0):
    """Coefficient de (x − at)^n dans le développement limité de f (exact, rendu en flottant)."""
    s = sp.series(parse(f), x, at, n + 1).removeO()
    return float(sp.N(s.coeff(x - at if at else x, n), 30))


def limit(f, at, direction=None):
    """Limite de f en `at` (nombre, "oo" ou "-oo") ; direction "+" ou "-" pour une limite latérale."""
    point = parse(str(at)) if isinstance(at, str) else at
    if point.is_infinite if hasattr(point, "is_infinite") else False:
        return float(sp.limit(parse(f), x, point))
    return float(sp.limit(parse(f), x, point, dir=direction or "+-"))


def identity(lhs, rhs, points=(0.3, 0.7, 1.3, 2.9), tol=1e-9):
    """lhs = rhs (identité, éventuellement complexe) aux points donnés."""
    gap = parse(lhs) - parse(rhs)
    return all(abs(complex(gap.subs(x, sp.Float(str(p), 40)).evalf(40))) < tol for p in points)


def value(expr):
    """Valeur numérique d'une expression constante (ex. "asin(1/2)", "exp(2*log(3))")."""
    return complex(parse(expr).evalf(30)).real
