"""Les vérificateurs eux-mêmes sont testés sur des résultats connus du cours."""
from checks import (are_equivalent, is_tautology, quantified_implication_holds,
                    set_identity_holds, set_statement_holds)


def test_excluded_middle_is_a_tautology():
    assert is_tautology("P | ~P")
    assert not is_tautology("P")


def test_de_morgan_and_contraposition():
    assert are_equivalent("~(P | Q)", "~P & ~Q")
    assert are_equivalent("P >> Q", "~Q >> ~P")
    assert not are_equivalent("P >> Q", "~P >> ~Q")


def test_set_identities():
    assert set_identity_holds("(A | B) | ~(A | B)", "E")
    assert set_identity_holds("A - B", "A & ~B")
    assert not set_identity_holds("(A - B) | B", "A")


def test_set_statements():
    assert set_statement_holds("(A <= B) == ((A & ~B) == empty)")
    assert not set_statement_holds("(A <= (B | C)) == ((A <= B) or (A <= C))")


def test_quantifier_swaps():
    # ∀x (P ∨ Q) n'implique pas (∀x P) ∨ (∀x Q)
    assert not quantified_implication_holds(
        "all(x in P or x in Q for x in D)", "all(x in P for x in D) or all(x in Q for x in D)", ["P", "Q"])
    assert quantified_implication_holds(
        "all(x in P for x in D) or all(x in Q for x in D)", "all(x in P or x in Q for x in D)", ["P", "Q"])


def test_binary_predicates_and_quantifier_order():
    from checks import evaluate_check
    # ¬(∀x ∃y R(x, y)) ⟺ ∃x ∀y ¬R(x, y)
    assert evaluate_check({"check": "quantified_equivalence", "predicates": ["R/2"],
                           "lhs": "not all(any((x, y) in R for y in D) for x in D)",
                           "rhs": "any(all((x, y) not in R for y in D) for x in D)"})
    # ∀x ∃y R(x, y) n'implique pas ∃y ∀x R(x, y)
    assert not evaluate_check({"check": "quantified_implication", "predicates": ["R/2"],
                               "hyp": "all(any((x, y) in R for y in D) for x in D)",
                               "concl": "any(all((x, y) in R for x in D) for y in D)"})
