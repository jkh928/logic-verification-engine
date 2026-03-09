# Logic Verification Engine

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active%20Development-green" alt="Status">
  <img src="https://img.shields.io/badge/Language-Python%203.x-blue" alt="Language">
  <img src="https://img.shields.io/badge/Focus-Discrete%20Mathematics-orange" alt="Focus">
</p>

## 📖 Overview
The **Logic Verification Engine** is a modular Python package designed to simulate, analyze, and mathematically audit logical systems. Moving beyond simple calculations, this engine prioritizes **System Integrity** by providing automated tools to verify tautologies and programmatically prove logical equivalences.

This toolkit serves as a foundation for transitioning abstract discrete mathematics into verifiable software constraints, essential for Safety-Critical Systems and Natural Language Processing (NLP).

## 📂 Repository Structure
```text
logic-verification-engine/
├── engine/                # Core Logic Package
│   ├── __init__.py        # Package Initializer
│   ├── logic_gates.py     # Boolean operations and Truth Table generation
│   └── quantifiers.py     # Universal (∀) and Existential (∃) verification
├── README.md
└── .gitignore
```
## 🛠 Core Modules

### 1. Boolean Logic & Tautology Testing (logic_gates.py)
* **Gate Simulation**: Full support for AND, OR, NOT, NAND, NOR, XOR, and XNOR operations.
* **Equivalence Verification**: Implements the **Tautology Test** to confirm if two compound statements are logically identical by evaluating the biconditional: P ↔ Q.

### 2. Predicate Logic & Quantifiers (quantifiers.py)
* **Universal (∀) & Existential (∃) Engines**: Evaluates predicates across variable domains to identify global constraints or specific supporting evidence.
* **Traceable Verification**: Unlike standard boolean returns, the engine identifies and returns the specific **Counterexample** (for ∀) or **Supporting Evidence** (for ∃) that triggered the result.
* **De Morgan Consistency Audit**: An internal verification layer that programmatically proves the mathematical consistency of negations (e.g., ¬[∀x P(x)] ≡ ∃x ¬P(x)).

## 🚀 Interview Highlight: The "Audit" Mindset
In engineering, "it works" is insufficient; "it is provable" is the standard. This engine is built with an **Audit Layer** that ensures software operations strictly follow the laws of discrete mathematics. By returning the specific data point that falsifies a universal statement, the engine provides the **Transparency** required for debugging complex automated decision-making systems.

---
*Author: Josh Hasam*