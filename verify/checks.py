"""Vérifications indépendantes des réponses écrites dans les fichiers *.items.yaml.

Chaque champ `verify` décrit un calcul (table de vérité, identité ensembliste sur toutes
les parties d'un petit univers, dénombrement par force brute…) dont le résultat doit
coïncider avec la réponse affichée à l'étudiant."""
from itertools import product, combinations
from math import comb, factorial

import counting
import importlib.util
from pathlib import Path

_SOLUTION = Path(__file__).resolve().parent.parent / "content" / "folo" / "python" / "folo_solution.py"
_spec = importlib.util.spec_from_file_location("folo_reference", _SOLUTION)
folo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(folo)


class B:
    """Booléen avec les connecteurs : ~ (non), & (et), | (ou), >> (implique)."""
    __slots__ = ("v",)

    def __init__(self, v):
        self.v = bool(v)

    def __invert__(self):
        return B(not self.v)

    def __and__(self, o):
        return B(self.v and o.v)

    def __or__(self, o):
        return B(self.v or o.v)

    def __rshift__(self, o):
        return B((not self.v) or o.v)

    def __bool__(self):
        return self.v


def iff(a, b):
    return B(a.v == b.v)


def xor(a, b):
    return B(a.v != b.v)


LETTERS = ["P", "Q", "R", "S"]


def _valuations(formulas):
    names = [n for n in LETTERS if any(n in f for f in formulas)]
    for values in product([False, True], repeat=len(names)):
        yield {n: B(v) for n, v in zip(names, values)}


def _eval_logic(formula, env):
    return eval(formula, {"iff": iff, "xor": xor, "__builtins__": {}, **env}).v


def is_tautology(formula):
    return all(_eval_logic(formula, env) for env in _valuations([formula]))


def are_equivalent(lhs, rhs):
    return all(_eval_logic(lhs, env) == _eval_logic(rhs, env) for env in _valuations([lhs, rhs]))


# ---------- Ensembles : A, B, C parcourent toutes les parties de E = {0, 1, 2} ----------
UNIVERSE = frozenset(range(3))


class S(frozenset):
    def __invert__(self):
        return S(UNIVERSE - self)

    def __or__(self, o):
        return S(frozenset.__or__(self, o))

    def __and__(self, o):
        return S(frozenset.__and__(self, o))

    def __sub__(self, o):
        return S(frozenset.__sub__(self, o))

    def __xor__(self, o):
        return S(frozenset.__xor__(self, o))


def _subsets(universe):
    items = sorted(universe)
    return [S(c) for r in range(len(items) + 1) for c in combinations(items, r)]


def _set_envs(expressions):
    names = [n for n in ["A", "B", "C", "D"] if any(n in e for e in expressions)]
    subsets = _subsets(UNIVERSE)
    for values in product(subsets, repeat=len(names)):
        env = dict(zip(names, values))
        env["E"] = S(UNIVERSE)
        env["empty"] = S()
        yield env


def _eval_set(expression, env):
    return eval(expression, {"__builtins__": {}, "len": len, "S": S, "all": all, "any": any, **env})


def set_identity_holds(lhs, rhs):
    return all(_eval_set(lhs, env) == _eval_set(rhs, env) for env in _set_envs([lhs, rhs]))


def set_statement_holds(statement):
    """`statement` est une expression Python booléenne sur A, B, C (ex. "(A <= B) == ((A & ~B) == empty)")."""
    return all(bool(_eval_set(statement, env)) for env in _set_envs([statement]))


# ---------- Quantificateurs : prédicats unaires arbitraires sur un petit domaine ----------
def _predicate_models(n, names):
    """Tous les modèles : un prédicat « P » est une partie de D, un prédicat « R/2 » une partie de D × D."""
    domain = list(range(n))
    pairs = [(x, y) for x in domain for y in domain]

    def extensions(name):
        base = domain if not name.endswith("/2") else pairs
        return [frozenset(c) for r in range(len(base) + 1) for c in combinations(base, r)]

    keys = [name.split("/")[0] for name in names]
    for values in product(*[extensions(name) for name in names]):
        yield domain, dict(zip(keys, values))


def quantified_implication_holds(hyp, concl, predicates, max_domain=3):
    """hyp ⟹ concl dans tous les modèles finis (domaines de taille 1..max_domain)."""
    for n in range(1, max_domain + 1):
        for domain, preds in _predicate_models(n, predicates):
            # Variables passées en globales : visibles depuis les générateurs (all(... for x in D)).
            env = {"__builtins__": {}, "D": domain, "all": all, "any": any, **preds}
            if eval(hyp, env) and not eval(concl, env):
                return False
    return True


def witness_refutes(spec):
    """Le contre-exemple cité dans l'explication réfute-t-il vraiment l'énoncé ?"""
    w = spec["witness"]
    kind = spec["check"]
    if kind in ("tautology", "equivalent"):
        env = {k: B(v) for k, v in w.items()}
        if kind == "tautology":
            return not _eval_logic(spec["formula"], env)
        return _eval_logic(spec["lhs"], env) != _eval_logic(spec["rhs"], env)
    if kind in ("set_identity", "set_statement"):
        env = {k: S(v) for k, v in w.items()}
        env["E"] = S(UNIVERSE | frozenset().union(*[frozenset(v) for v in w.values()]))
        env["empty"] = S()
        if kind == "set_identity":
            return _eval_set(spec["lhs"], env) != _eval_set(spec["rhs"], env)
        return not bool(_eval_set(spec["statement"], env))
    if kind in ("quantified_implication", "quantified_equivalence"):
        env = {"__builtins__": {}, "all": all, "any": any, "D": list(w["D"])}
        for name in spec["predicates"]:
            key = name.split("/")[0]
            env[key] = frozenset(tuple(v) if isinstance(v, list) else v for v in w.get(key, []))
        if kind == "quantified_implication":
            return bool(eval(spec["hyp"], env)) and not bool(eval(spec["concl"], env))
        return bool(eval(spec["lhs"], env)) != bool(eval(spec["rhs"], env))
    raise ValueError(f"témoin non géré pour {kind}")


def evaluate_check(spec):
    """Renvoie la valeur de vérité (ou le nombre) calculée pour une spécification `verify`."""
    kind = spec["check"]
    if kind == "tautology":
        return is_tautology(spec["formula"])
    if kind == "equivalent":
        return are_equivalent(spec["lhs"], spec["rhs"])
    if kind == "set_identity":
        return set_identity_holds(spec["lhs"], spec["rhs"])
    if kind == "set_statement":
        return set_statement_holds(spec["statement"])
    if kind == "quantified_implication":
        return quantified_implication_holds(spec["hyp"], spec["concl"], spec["predicates"], spec.get("max_domain", 3))
    if kind == "quantified_equivalence":
        size = spec.get("max_domain", 3)
        return (quantified_implication_holds(spec["lhs"], spec["rhs"], spec["predicates"], size)
                and quantified_implication_holds(spec["rhs"], spec["lhs"], spec["predicates"], size))
    if kind == "python_expr":
        return eval(spec["expr"], {"comb": comb, "factorial": factorial, "counting": counting})
    if kind == "relation":
        # Propriété d'une relation finie, calculée avec la solution de référence du projet (elle-même testée).
        es = set(eval(spec["es"], {"range": range, "frozenset": frozenset}))
        if "pairs" in spec:
            pairs = {tuple(p) for p in spec["pairs"]}
        else:
            rel = eval(spec["rel"], {"abs": abs})
            pairs = {(x, y) for x in es for y in es if rel(x, y)}
        return getattr(folo, spec["property"])(es, pairs)
    if kind == "count":
        fn = getattr(counting, spec["fn"])
        return fn(**spec.get("args", {}))
    raise ValueError(f"check inconnu : {kind}")
