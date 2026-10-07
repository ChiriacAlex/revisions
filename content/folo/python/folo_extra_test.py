"""Tests supplémentaires (plus stricts que le test public) : cas limites,
relations « mal typées », performance. Ils suivent exactement l'énoncé du projet."""
import time
from itertools import combinations
from unittest import TestCase

from folo import *


def relation(es, fs, predicate):
    return {(x, y) for x in es for y in fs if predicate(x, y)}


def powerset(s):
    s = list(s)
    return {frozenset(c) for r in range(len(s) + 1) for c in combinations(s, r)}


class ExtraRelations(TestCase):
    # Q1 — is_relation
    def test_is_relation_empty_pairs(self):
        self.assertTrue(is_relation({1, 2}, {3}, set()))
        self.assertTrue(is_relation(set(), set(), set()))

    def test_is_relation_rejects_bad_first_component(self):
        self.assertFalse(is_relation({1, 2}, {3, 4}, {(1, 3), (5, 3)}))

    def test_is_relation_rejects_bad_second_component(self):
        self.assertFalse(is_relation({1, 2}, {3, 4}, {(1, 3), (2, 5)}))

    # Q2 — is_partial_function
    def test_is_partial_function_two_images(self):
        self.assertFalse(is_partial_function({1, 2}, {3, 4}, {(1, 3), (1, 4)}))

    def test_is_partial_function_missing_images_are_fine(self):
        self.assertTrue(is_partial_function({1, 2, 3}, {3, 4}, {(1, 3)}))
        self.assertTrue(is_partial_function({1, 2}, {3}, set()))

    def test_is_partial_function_requires_a_relation(self):
        self.assertFalse(is_partial_function({1}, {3}, {(1, 3), (2, 3)}))

    # Q3 — is_function
    def test_is_function_every_element_has_one_image(self):
        self.assertTrue(is_function({1, 2}, {3}, {(1, 3), (2, 3)}))

    def test_is_function_rejects_missing_image(self):
        self.assertFalse(is_function({1, 2}, {3}, {(1, 3)}))

    def test_is_function_rejects_two_images(self):
        self.assertFalse(is_function({1}, {3, 4}, {(1, 3), (1, 4)}))

    def test_is_function_requires_a_relation(self):
        self.assertFalse(is_function({1}, {3}, {(1, 3), (1, 9)}))

    def test_is_function_on_empty_domain(self):
        self.assertTrue(is_function(set(), {3}, set()))

    # Q8 — is_symmetric
    def test_is_symmetric_requires_a_relation(self):
        self.assertFalse(is_symmetric({1}, {(1, 2), (2, 1)}))

    def test_is_symmetric_examples(self):
        es = set(range(6))
        self.assertTrue(is_symmetric(es, relation(es, es, lambda x, y: (x + y) % 2 == 0)))
        self.assertFalse(is_symmetric(es, relation(es, es, lambda x, y: x <= y)))

    # Q9 — is_antisymmetric
    def test_is_antisymmetric_examples(self):
        self.assertFalse(is_antisymmetric({1, 2}, {(1, 2), (2, 1)}))
        self.assertTrue(is_antisymmetric({1, 2}, {(1, 1), (1, 2)}))
        self.assertTrue(is_antisymmetric({1, 2}, set()))

    def test_is_antisymmetric_requires_a_relation(self):
        self.assertFalse(is_antisymmetric({1}, {(1, 2)}))

    # Q10 — is_reflexive
    def test_is_reflexive_missing_loop(self):
        self.assertFalse(is_reflexive({1, 2}, {(1, 1)}))

    def test_is_reflexive_empty_set(self):
        self.assertTrue(is_reflexive(set(), set()))

    def test_is_reflexive_requires_a_relation(self):
        self.assertFalse(is_reflexive({1}, {(1, 1), (1, 2)}))

    # Q11 — is_transitive
    def test_is_transitive_missing_shortcut(self):
        self.assertFalse(is_transitive({1, 2, 3}, {(1, 2), (2, 3)}))
        self.assertTrue(is_transitive({1, 2, 3}, {(1, 2), (2, 3), (1, 3)}))

    def test_is_transitive_cycle_needs_loops(self):
        self.assertFalse(is_transitive({1, 2}, {(1, 2), (2, 1)}))
        self.assertTrue(is_transitive({1, 2}, {(1, 2), (2, 1), (1, 1), (2, 2)}))

    def test_is_transitive_requires_a_relation(self):
        self.assertFalse(is_transitive({1}, {(1, 1), (2, 2)}))

    def test_is_transitive_fast_enough(self):
        es = set(range(300))
        pairs = relation(es, es, lambda x, y: x <= y)
        start = time.perf_counter()
        self.assertTrue(is_transitive(es, pairs))
        self.assertFalse(is_transitive(es, pairs | {(299, 0)}))
        self.assertLess(time.perf_counter() - start, 10, "algorithme trop lent : évite les boucles sur toutes les paires de paires")

    # Q12 — is_equivalence
    def test_is_equivalence_congruence_modulo_3(self):
        es = set(range(12))
        self.assertTrue(is_equivalence(es, relation(es, es, lambda x, y: (x - y) % 3 == 0)))

    def test_is_equivalence_rejects_order(self):
        es = set(range(5))
        self.assertFalse(is_equivalence(es, relation(es, es, lambda x, y: x <= y)))

    def test_is_equivalence_requires_a_relation(self):
        self.assertFalse(is_equivalence({1}, {(1, 1), (2, 2)}))

    # Q13 — gen_equiv_class
    def test_gen_equiv_class_modulo_3(self):
        es = set(range(9))
        pairs = relation(es, es, lambda x, y: (x - y) % 3 == 0)
        self.assertEqual(gen_equiv_class(es, 4, pairs), {1, 4, 7})
        self.assertEqual(gen_equiv_class(es, 0, pairs), {0, 3, 6})

    def test_gen_equiv_class_singletons(self):
        es = {"a", "b"}
        self.assertEqual(gen_equiv_class(es, "a", {("a", "a"), ("b", "b")}), {"a"})

    def test_gen_equiv_class_checks_its_inputs(self):
        es = {1, 2}
        with self.assertRaises(AssertionError):
            gen_equiv_class(es, 3, {(1, 1), (2, 2)})
        with self.assertRaises(AssertionError):
            gen_equiv_class(es, 1, {(1, 1)})

    # Q14 — is_partial_order
    def test_is_partial_order_inclusion(self):
        subsets = powerset({1, 2, 3})
        self.assertTrue(is_partial_order(subsets, relation(subsets, subsets, lambda a, b: a <= b)))

    def test_is_partial_order_divisibility(self):
        es = set(range(1, 13))
        self.assertTrue(is_partial_order(es, relation(es, es, lambda a, b: b % a == 0)))

    def test_is_partial_order_rejects_equivalence(self):
        es = set(range(6))
        self.assertFalse(is_partial_order(es, relation(es, es, lambda x, y: (x - y) % 3 == 0)))

    def test_is_partial_order_requires_a_relation(self):
        self.assertFalse(is_partial_order({1}, {(1, 1), (2, 2)}))

    # Q15 — is_total_order
    def test_is_total_order_divisibility_is_not_total(self):
        es = set(range(1, 13))
        self.assertFalse(is_total_order(es, relation(es, es, lambda a, b: b % a == 0)))

    def test_is_total_order_inclusion_is_not_total(self):
        subsets = powerset({1, 2})
        self.assertFalse(is_total_order(subsets, relation(subsets, subsets, lambda a, b: a <= b)))

    def test_is_total_order_single_element(self):
        self.assertTrue(is_total_order({1}, {(1, 1)}))


class ExtraBijections(TestCase):
    # Q4 — is_injection
    def test_is_injection_constant(self):
        self.assertFalse(is_injection(lambda x: 0, {1, 2}, {0}))

    def test_is_injection_square_on_symmetric_set(self):
        self.assertFalse(is_injection(lambda x: x * x, {-2, -1, 0, 1, 2}, {0, 1, 4}))

    def test_is_injection_large(self):
        es = set(range(5000))
        self.assertTrue(is_injection(lambda x: x + 1, es, set(range(1, 5001))))

    # Q5 — is_surjection
    def test_is_surjection_missed_value(self):
        self.assertFalse(is_surjection(lambda x: 2 * x, {0, 1}, {0, 1, 2}))

    def test_is_surjection_empty_domain_non_empty_target(self):
        self.assertFalse(is_surjection(lambda x: x, set(), {1}))

    def test_is_surjection_large(self):
        es = set(range(5000))
        self.assertTrue(is_surjection(lambda x: x // 2, es, set(range(2500))))

    # Q6 — is_bijection
    def test_is_bijection_needs_both(self):
        self.assertFalse(is_bijection(lambda x: x, {1, 2}, {1, 2, 3}))
        self.assertFalse(is_bijection(lambda x: 1, {1, 2}, {1}))
        self.assertTrue(is_bijection(lambda x: -x, {1, 2}, {-1, -2}))

    # Q7 — find_inverse
    def test_find_inverse_none_when_not_bijective(self):
        self.assertIsNone(find_inverse(lambda x: 0, {1, 2}, {0}))
        self.assertIsNone(find_inverse(lambda x: x, {1}, {1, 2}))

    def test_find_inverse_on_tuples(self):
        es = {(a, b) for a in range(3) for b in range(3)}
        swap = lambda p: (p[1], p[0])
        h = find_inverse(swap, es, es)
        for p in es:
            self.assertEqual(h(swap(p)), p)
            self.assertEqual(swap(h(p)), p)
