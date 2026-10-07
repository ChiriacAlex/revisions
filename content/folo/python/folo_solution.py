from typing import TypeVar, Callable, Tuple, Optional, Set

E = TypeVar('E')
F = TypeVar('F')


def is_relation(es: Set[E], fs: Set[F], pairs: Set[Tuple[E, F]]) -> bool:
    """Given 'es', a set of objects, and 'fs', a set of objects,
    determine whether the set 'pairs' of pairs in es × fs designates
    a *binary relation* on es × fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    # pairs ⊆ es × fs  ⟺  ∀(x, y) ∈ pairs, x ∈ es ∧ y ∈ fs
    return all(x in es and y in fs for (x, y) in pairs)


def is_partial_function(es: Set[E], fs: Set[F], pairs: Set[Tuple[E, F]]) -> bool:
    """Given 'es', a set of objects, and 'fs', a set of objects,
    determine whether the set 'pairs' of pairs in es × fs designates
    a *partial function* relation es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    if not is_relation(es, fs, pairs):
        return False
    # (x ∼ y1) ∧ (x ∼ y2) ⟹ y1 = y2 : on retient la première image vue de chaque x.
    image = {}
    for (x, y) in pairs:
        if x in image and image[x] != y:
            return False
        image[x] = y
    return True


def is_function(es: Set[E], fs: Set[F], pairs: Set[Tuple[E, F]]) -> bool:
    """Given 'es', a set of objects, and 'fs', a set of objects,
    determine whether the set 'pairs' of pairs in es × fs designates
    a *function* relation es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    if not is_partial_function(es, fs, pairs):
        return False
    # Unicité déjà garantie ; il reste l'existence : ∀x ∈ es, ∃y, (x, y) ∈ pairs.
    antecedents = {x for (x, _) in pairs}
    return all(x in antecedents for x in es)


def is_injection(g: Callable[[E], F], es: Set[E], fs: Set[F]) -> bool:
    """Given 'es', a set of objects, 'fs', a set of objects,
    determine whether the function 'g' is an *injection* es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert callable(g), type(g)
    assert all(g(x) in fs for x in es), f"internal testing error, {fs=} {es=} image={[g(x) for x in es]}"
    # Injective ⟺ deux antécédents distincts n'ont jamais la même image
    # ⟺ l'image a autant d'éléments que es (aucune « collision »).
    return len({g(x) for x in es}) == len(es)


def is_surjection(g: Callable[[E], F], es: Set[E], fs: Set[F]) -> bool:
    """Given 'es', a set of objects, 'fs', a set of objects,
    determine whether the function 'g' is a *surjection* es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert callable(g), type(g)
    assert all(g(x) in fs for x in es), f"internal testing error, {fs=} {es=} image={[g(x) for x in es]}"
    # ∀y ∈ fs, ∃x ∈ es, g(x) = y  ⟺  fs ⊆ Im(g)
    image = {g(x) for x in es}
    return all(y in image for y in fs)


def is_bijection(g: Callable[[E], F], es: Set[E], fs: Set[F]) -> bool:
    """Given 'es', a set of objects, 'fs', a set of objects,
    determine whether the function 'g' is a *bijection* es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert callable(g), type(g)
    assert all(g(x) in fs for x in es), f"internal testing error, {fs=} {es=} image={[g(x) for x in es]}"
    return is_injection(g, es, fs) and is_surjection(g, es, fs)


def find_inverse(g: Callable[[E], F], es: Set[E], fs: Set[F]) -> Optional[Callable[[F], E]]:
    """Given 'es', a set of objects, 'fs', a set of objects, and a function 'g',
    if g is a bijection es → fs return its *inverse*, otherwise return None."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert callable(g), type(g)
    assert all(g(x) in fs for x in es), f"internal testing error, {fs=} {es=} image={[g(x) for x in es]}"

    if not is_bijection(g, es, fs):
        return None

    # g bijective : chaque y de fs a exactement un antécédent, qu'on mémorise.
    antecedent = {g(x): x for x in es}

    def h(f: F) -> E:
        return antecedent[f]

    return h


def is_symmetric(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    a *symmetric, binary* relation on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    # ∀x, y ∈ es, x ∼ y ⟹ y ∼ x : il suffit de parcourir les paires présentes.
    return is_relation(es, es, pairs) and all((y, x) in pairs for (x, y) in pairs)


def is_antisymmetric(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    an *antisymmetric, binary* relation on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    # ∀x, y ∈ es, (x ∼ y) ∧ (y ∼ x) ⟹ x = y
    return is_relation(es, es, pairs) and all(x == y for (x, y) in pairs if (y, x) in pairs)


def is_reflexive(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects, and 'fs', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    an *reflexive, binary* relation on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    # ∀x ∈ es, x ∼ x
    return is_relation(es, es, pairs) and all((x, x) in pairs for x in es)


def is_transitive(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    a *transitive, binary* relation on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    if not is_relation(es, es, pairs):
        return False
    # ∀x, y, z, (x ∼ y) ∧ (y ∼ z) ⟹ (x ∼ z).
    # On ne parcourt que les z effectivement reliés à y (successeurs), au lieu de tout es.
    successors = {}
    for (x, y) in pairs:
        successors.setdefault(x, set()).add(y)
    return all((x, z) in pairs
               for (x, y) in pairs
               for z in successors.get(y, ()))


def is_equivalence(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    an *equivalence* relation on es × fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    return is_reflexive(es, pairs) and is_symmetric(es, pairs) and is_transitive(es, pairs)


def gen_equiv_class(es: Set[E], e: E, equiv_pairs:Set[Tuple[E, E]]) -> Set[E]:
    """Given 'es', a set of objects, an element 'e' of 'es',
    and a set 'equiv_pairs' of pairs in es × es designating an equivalence relation,
    return as a set the equivalence class of e according to equiv_pairs."""
    assert is_equivalence(es, equiv_pairs)
    assert e in es
    # [e] = {y ∈ es | e ∼ y}
    return {y for y in es if (e, y) in equiv_pairs}


def is_partial_order(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    a *partial order relation* on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    return is_reflexive(es, pairs) and is_antisymmetric(es, pairs) and is_transitive(es, pairs)


def is_total_order(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    a *total order relation* on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    # Ordre + ∀x, y ∈ es, x ∼ y ∨ y ∼ x
    return is_partial_order(es, pairs) and all((x, y) in pairs or (y, x) in pairs
                                               for x in es for y in es)
