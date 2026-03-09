import itertools
import re


class LogicAuditor:
    """
    Advanced Logic Verification Engine.
    Automates formal verification for N-variable systems to ensure
    architectural integrity in safety-critical applications.
    """

    def __init__(self):
        self.states = [1, 0]

    def get_variables(self, *expressions):
        """Extracts unique variable names (p, q, r, etc.) using Regex."""
        combined = " ".join(expressions).lower()
        # Find all single letters that are NOT reserved keywords
        vars_found = set(re.findall(r'\b[a-z]\b', combined))
        return sorted(list(vars_found))

    def audit(self, expr_a, expr_b):
        """Performs a formal audit of two logical structures."""
        vars_list = self.get_variables(expr_a, expr_b)
        num_vars = len(vars_list)
        combinations = list(itertools.product(self.states, repeat=num_vars))

        print(f"\n{'=' * 25} SYSTEM AUDIT {'=' * 25}")
        print(f"Variables Detected: {', '.join(vars_list)}")
        print(f"Total States Verified: {len(combinations)} (2^{num_vars})")
        print("-" * 64)

        # Header for Truth Table
        header = " | ".join(vars_list) + " | Side A | Side B | Result"
        print(header)
        print("-" * len(header))

        all_match = True
        for combo in combinations:
            # Create the context for eval()
            context = dict(zip(vars_list, combo))

            # Evaluate expressions
            try:
                # Use a clean dictionary for globals to keep eval() safe
                res_a = int(eval(expr_a.lower(), {"__builtins__": None}, context))
                res_b = int(eval(expr_b.lower(), {"__builtins__": None}, context))
            except Exception as e:
                print(f"Evaluation Error: {e}")
                return

            match = res_a == res_b
            if not match:
                all_match = False

            # Format the row for the table
            row_values = [str(val) for val in combo]
            row_str = " | ".join(row_values)
            print(f"{row_str} |   {res_a}    |   {res_b}    | {'PASS' if match else 'FAIL'}")

        print("-" * len(header))
        if all_match:
            print(f"VERIFICATION SUCCESS: Logic is redundant and 100% equivalent.")
        else:
            print(f"VERIFICATION FAILURE: Logic mismatch detected in system architecture.")
        print(f"{'=' * 64}\n")


if __name__ == "__main__":
    inspector = LogicAuditor()

    print("Logic Verification Engine v2.0")
    print("Enter expressions using 'p', 'q', 'r', 's', 'and', 'or', 'not'")

    a = input("Enter Original Logic: ")
    b = input("Enter Optimized Logic: ")

    inspector.audit(a, b)