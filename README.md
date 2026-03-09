# Logic Verification Engine (`logic_gates.py`)

### Overview
A Python-based toolkit designed to simulate, analyze, and verify complex digital logic circuits. This engine prioritizes **system integrity** by providing automated tools to generate truth tables and mathematically prove logical equivalence between different circuit architectures.

### Core Features
* **Gate Simulation**: Full support for AND, OR, NOT, NAND, NOR, XOR, and XNOR operations.
* **Truth Table Generation**: Automates the mapping of all possible input combinations ($2^n$) to determine output states.
* **Equivalence Verification**: Implements the **Tautology Test** to programmatically confirm if two compound statements or circuits are logically identical.

---

### Mathematical Foundation: The Tautology Test
In safety-critical systems, visual comparison of truth tables is insufficient for formal verification. This engine verifies the logical equivalence ($P \equiv Q$) by evaluating the biconditional statement:

$$P \leftrightarrow Q$$

The system identifies the two circuits as **Equivalent** if and only if the resulting column is a **Tautology** (all True). This ensures that no "algorithmic error" or edge-case mismatch exists between a simplified circuit and its original logic.

---

### Usage Example
```python
from logic_gates import LogicEngine

# Define two different logical expressions
circuit_a = "(P and Q) or (not P)"
circuit_b = "not P or Q"

# Verify Equivalence using the Tautology Test
verifier = LogicEngine()
is_equivalent = verifier.check_equivalence(circuit_a, circuit_b)

print(f"Logic Verified: {is_equivalent}")
