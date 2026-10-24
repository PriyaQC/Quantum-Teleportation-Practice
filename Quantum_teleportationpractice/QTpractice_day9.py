#QTpractice_day9
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Create three qubits
q = QuantumRegister(3, "q")

# Alice's two measurement bits
c = ClassicalRegister(2, "c")

# Bob's final measurement bit
out = ClassicalRegister(1, "out")

qc = QuantumCircuit(q, c, out)

# Step 1: Prepare Alice's input state |1>
qc.x(q[0])

# Step 2: Create the Bell pair
qc.h(q[1])
qc.cx(q[1], q[2])

# Step 3: Alice's teleportation operations
qc.cx(q[0], q[1])
qc.h(q[0])

# Step 4: Alice measures her two qubits
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

# Step 5: Bob applies conditional corrections

# Register value 1 means c[1]c[0] = 01.
# In our convention, Alice's result is 10: apply Z.
with qc.if_test((c, 1)):
    qc.z(q[2])

# Register value 2 means c[1]c[0] = 10.
# In our convention, Alice's result is 01: apply X.
with qc.if_test((c, 2)):
    qc.x(q[2])

# Register value 3 means both bits are 1: apply both gates.
with qc.if_test((c, 3)):
    qc.x(q[2])
    qc.z(q[2])

# Step 6: Measure Bob's corrected qubit
qc.measure(q[2], out[0])

# Display the circuit
print(qc.draw())