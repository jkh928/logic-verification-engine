import numpy as np


# --- Pure Logic Quantifier Functions ---

def universal_quantifier(domain, predicate):
    """
    Evaluates ∀x P(x).
    Returns: (Result: bool, Element: x)
    If False, Element is the counterexample. If True, Element is None.
    """
    for x in domain:
        if not predicate(x):
            return False, x
    return True, None


def existential_quantifier(domain, predicate):
    """
    Evaluates ∃x P(x).
    Returns: (Result: bool, Element: x)
    If True, Element is the supporting evidence. If False, Element is None.
    """
    for x in domain:
        if predicate(x):
            return True, x
    return False, None


# --- De Morgan Verification ---

def verify_de_morgan_laws(domain, predicate):
    """
    Verification of Negation Equivalence:
    1. ¬[∀x P(x)] ≡ ∃x ¬P(x)
    2. ¬[∃x P(x)] ≡ ∀x ¬P(x)
    """
    # Test Law 1: Negation of Universal
    all_p, _ = universal_quantifier(domain, predicate)
    not_all_p = not all_p
    exists_not_p, evidence_not_p = existential_quantifier(domain, lambda x: not predicate(x))
    law1_consistent = (not_all_p == exists_not_p)

    # Test Law 2: Negation of Existential
    exists_p, _ = existential_quantifier(domain, predicate)
    not_exists_p = not exists_p
    all_not_p, counter_not_p = universal_quantifier(domain, lambda x: not predicate(x))
    law2_consistent = (not_exists_p == all_not_p)

    return {
        "Universal Negation (Law 1)": (law1_consistent, evidence_not_p),
        "Existential Negation (Law 2)": (law2_consistent, counter_not_p)
    }


# --- Pure Logic Calculation Report ---

if __name__ == "__main__":
    # 1. Define Mathematical Domain and Predicate
    domain = np.array([2, 4, 6, 8, 11])
    is_even = lambda x: x % 2 == 0

    # 2. Execute Quantifier Checks
    univ_res, univ_val = universal_quantifier(domain, is_even)
    exis_res, exis_val = existential_quantifier(domain, is_even)
    dm_results = verify_de_morgan_laws(domain, is_even)

    # 3. Formal Logical Output
    print("-" * 60)
    print("LOGIC CALCULATION ENGINE: QUANTIFIER REPORT")
    print("-" * 60)

    # Universal Results (∀)
    print(f"Statement ∀x P(x) is: {univ_res}")
    if not univ_res:
        print(f" > Logical Status: Falsified")
        print(f" > Counterexample found: x = {univ_val}")
    else:
        print(f" > Logical Status: Verified for all x in domain.")

    print("-" * 60)

    # Existential Results (∃)
    print(f"Statement ∃x P(x) is: {exis_res}")
    if exis_res:
        print(f" > Logical Status: Verified")
        print(f" > Supporting evidence found: x = {exis_val}")
    else:
        print(f" > Logical Status: Falsified (No x satisfies P(x))")

    print("-" * 60)
    print("DE MORGAN'S LAW CONSISTENCY AUDIT")
    print("-" * 60)

    for law, (is_consistent, evidence) in dm_results.items():
        status = "CONSISTENT" if is_consistent else "ERROR"
        print(f" {law}: {status}")
        if evidence is not None:
            print(f"  > Validated via evidence/counterexample: x = {evidence}")

    print("-" * 60)