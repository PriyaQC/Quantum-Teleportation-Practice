# Quantum-Teleportation-Practice
Daily Python and quantum computing practice from Day 1–11, covering Python fundamentals, NumPy, complex numbers, quantum states, normalization, quantum gates, Bell states, quantum teleportation, and fidelity using Python and Qiskit.
# Quantum Teleportation Using Python and Qiskit

## 1. Project Overview

This project explores the fundamental concepts behind quantum teleportation using Python, mathematical calculations, and quantum computing simulations.

Quantum teleportation is a protocol that transfers an unknown quantum state using shared entanglement, quantum operations, measurements, and classical communication.

The project follows a beginner-friendly learning journey, starting with Python programming and gradually introducing the mathematical and quantum-mechanical concepts required to understand teleportation.

**Field:** Quantum Mechanics and Quantum Computing
**Level:** Beginner undergraduate project
**Tools:** Python, NumPy, Qiskit, VS Code

---

## 2. Project Objectives

* Learn Python fundamentals for scientific computing.
* Understand complex numbers and quantum amplitudes.
* Represent qubits mathematically.
* Study normalization, superposition, and entanglement.
* Understand tensor products and multi-qubit systems.
* Explore fundamental quantum gates.
* Construct and understand Bell states.
* Implement the quantum teleportation protocol.
* Explore quantum-state fidelity using NumPy.

---

## 3. Learning Journey: Day 1–Day 11

### Day 1 — Introduction to Python

Learned basic Python syntax, variables, data types, and simple calculations.

**Application:** Building a programming foundation for quantum computing.

### Day 2 — Conditions and Logical Operations

Practised conditional statements and logical expressions.

**Application:** Understanding how program execution can depend on measurement outcomes.

### Day 3 — Functions and Reusable Code

Explored functions, arguments, and return values.

**Application:** Organizing mathematical calculations into reusable blocks of code.

### Day 4 — Lists, Arrays, and Numerical Calculations

Practised storing and manipulating numerical data.

**Application:** Preparing for the representation of quantum states as vectors.

### Day 5 — Introduction to NumPy

Learned basic NumPy arrays and numerical operations.

**Application:** Performing vector and matrix calculations relevant to quantum mechanics.

### Day 6 — Complex Numbers and Quantum Amplitudes

Explored complex numbers, magnitudes, and their mathematical properties.

A single-qubit state can be represented as

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle
$$

where \(\alpha\) and \(\beta\) can be complex amplitudes.

**Application:** Understanding the mathematical representation of qubits.

### Day 7 — Quantum-State Normalization

Studied the normalization condition for a single-qubit state:

$$
|\alpha|^2+|\beta|^2=1
$$

**Application:** Ensuring that the probabilities of all possible measurement outcomes sum to one.

### Day 8 — Multi-Qubit States and Quantum Gates

Explored tensor products, multi-qubit state representations, and basic quantum gates.

**Application:** Understanding how multiple qubits form a composite quantum system and how quantum gates transform its state.

### Day 9 — Bell-State Entanglement

Studied how a Hadamard gate and a controlled-NOT gate can create an entangled Bell state:

$$
|\Phi^+\rangle=
\frac{|00\rangle+|11\rangle}{\sqrt{2}}
$$

**Application:** Understanding entanglement as a fundamental resource for quantum teleportation.

### Day 10 — Quantum Teleportation Circuit

Studied the three-qubit teleportation protocol, including:

* Preparation of a shared Bell pair.
* Alice's CNOT and Hadamard operations.
* Measurement of Alice's two qubits.
* Conditional correction gates applied by Bob.
* Testing different input states.

The input states considered were:

$$
|0\rangle,\quad |1\rangle,\quad
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt{2}}
$$

**Application:** Understanding how the original quantum state can be recovered at Bob's end through the teleportation protocol.

### Day 11 — Quantum-State Fidelity

Introduced quantum-state fidelity as a measure of similarity between two pure quantum states:

$$
F=|\langle\psi|\phi\rangle|^2
$$

where \(|\psi\rangle\) is the reference state and \(|\phi\rangle\) is the comparison state.

Used NumPy to calculate fidelity for simple examples:

* Identical normalized states have fidelity \(F=1\).
* Orthogonal states have fidelity \(F=0\).

**Application:** Learning a mathematical method for evaluating the accuracy of quantum-state recovery.

---

## 4. Mathematical Foundations

The project introduces several important concepts from quantum mechanics.

### Qubit representation

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle
$$

### Normalization

$$
|\alpha|^2+|\beta|^2=1
$$

### Bell state

$$
|\Phi^+\rangle=
\frac{|00\rangle+|11\rangle}{\sqrt{2}}
$$

### Quantum-state fidelity

$$
F=|\langle\psi|\phi\rangle|^2
$$

These concepts form the mathematical foundation for understanding quantum teleportation.

---

## 5. Technologies Used

* **Python:** Programming and numerical calculations.
* **NumPy:** Complex arrays, vectors, and mathematical operations.
* **Qiskit:** Quantum-circuit construction and simulation.
* **Qiskit Aer:** Quantum-circuit simulation, where installed and used.
* **Visual Studio Code:** Development environment.
* **GitHub:** Version control and project documentation.


---

## 6. Testing and Observations

The project explores three possible input states:

| Input state | Expected recovered state in an ideal simulation |   |           |
| ----------- | ----------------------------------------------- | - | --------- |
| (           | 0\rangle)                                       | ( | 0\rangle) |
| (           | 1\rangle)                                       | ( | 1\rangle) |
| (           | +\rangle)                                       | ( | +\rangle) |

The fidelity exercises provide an introduction to comparing quantum states mathematically.


---

## 7. Limitations

* This project focuses on learning and simulation.
* It does not demonstrate teleportation using physical quantum hardware.
* Ideal simulations do not automatically include realistic hardware noise.
* Measurement counts alone cannot verify every property of a quantum state.

---

## 8. Learning Outcomes

Through this learning journey, I explored the relationship between applied mathematics, programming, and quantum computing.

The concepts studied include complex amplitudes, normalization, superposition, entanglement, tensor products, quantum gates, measurement, conditional corrections, and quantum-state fidelity.

This project represents an ongoing effort to build a strong foundation for further study in quantum mechanics and quantum information.

---

## 9. Conclusion

This project provides a beginner-level introduction to quantum teleportation through mathematical reasoning, Python programming, and quantum-circuit simulation.

The first eleven days establish the programming and conceptual foundations needed to understand the teleportation protocol and evaluate quantum-state similarity.

The project is intended as a foundation for further exploration of quantum information and quantum computing.

**Project type:** Self-directed educational project
**Academic level:** Undergraduate beginner
