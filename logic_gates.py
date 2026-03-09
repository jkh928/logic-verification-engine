class LogicEngine:
    """
    A verification engine for formal logic and circuit integrity.
    Inspired by high-stakes systems management.
    """

    def __init__(self):
        self.domain = [1, 0]

    def verify_equivalence(self, name, func_a, func_b):
        """
        Implements the Tautology Test (P ↔ Q).
        Checks if two logical functions yield the same result for all inputs.
        """
        print(f"\n{'=' * 10} VERIFYING: {name} {'=' * 10}")
        print(f"{'P':<3} | {'Q':<3} | {'Side A':<8} | {'Side B':<8} | {'Match?'}")
        print("-" * 45)

        all_match = True
        for p in self.domain:
            for q in self.domain:
                # Execute the logic
                result_a = int(func_a(p, q))
                result_b = int(func_b(p, q))
                match = result_a == result_b

                if not match:
                    all_match = False

                print(f"{p:<3} | {q:<3} | {result_a:<8} | {result_b:<8} | {'YES' if match else 'NO'}")

        if all_match:
            print(f"\nRESULT: {name} IS A TAUTOLOGY (Verified Equivalent).")
        else:
            print(f"\nRESULT: {name} IS NOT EQUIVALENT.")
        return all_match

    def check_quantifiers(self, domain, predicate_func):
        """
        Demonstrates Universal (∀) and Existential (∃) verification.
        """
        forall = all(predicate_func(x) for x in domain)
        exists = any(predicate_func(x) for x in domain)
        print(f"\n--- Quantifier Results (Domain: {domain}) ---")
        print(f"Universal (∀x): {forall}")
        print(f"Existential (∃x): {exists}")


# --- Execution Block ---
if __name__ == "__main__":
    engine = LogicEngine()

    # 1. Conditional vs. Disjunction Proof: (P -> Q) ≡ (¬P ∨ Q)
    engine.verify_equivalence(
        "Conditional Implication",
        lambda p, q: (not p) or q,  # Standard definition
        lambda p, q: not (p and not q)  # Alternative logical form
    )

    # 2. De Morgan's Law Verification: ¬(P ∧ Q) ≡ (¬P ∨ ¬Q)
    engine.verify_equivalence(
        "De Morgan's (Corrected)",
        lambda p, q: not (p and q),
        lambda p, q: (not p) or (not q)
    )

    # 3. Distributive Law Expansion: p ∨ (q ∧ ¬p) ≡ (p ∨ q)
    engine.verify_equivalence(
        "Distributive Law",
        lambda p, q: p or (q and not p),
        lambda p, q: p or q
    )

    # 4. Quantifier Testing
    test_domain = [1, 2, 3, 4, 5]
    engine.check_quantifiers(test_domain, lambda x: x < 10)