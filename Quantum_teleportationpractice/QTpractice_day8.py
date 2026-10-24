#QTpractice_day8
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Three qubits: input, Alice's entangled qubit, Bob's qubit
q = QuantumRegister(3, "q")
c = ClassicalRegister(2, "c")

qc = QuantumCircuit(q, c)

# Prepare the input state |1> for our first test
qc.x(q[0])

# Create a Bell pair between Alice's q[1] and Bob's q[2]
qc.h(q[1])
qc.cx(q[1], q[2])

# Alice's teleportation operations
qc.cx(q[0], q[1])
qc.h(q[0])

# Alice measures her two qubits
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

print(qc.draw())