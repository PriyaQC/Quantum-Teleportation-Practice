#QTpractice_day10
#For input |+>
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

# Create 3 qubits and 3 classical bits
q = QuantumRegister(3, "q")
c = ClassicalRegister(2, "c")
out = ClassicalRegister(1, "out")

qc = QuantumCircuit(q, c, out)

# Step 1: Prepare input state |+>
qc.h(q[0])

# Step 2: Create a Bell pair between Alice and Bob
qc.h(q[1])
qc.cx(q[1], q[2])

# Step 3: Alice's operations
qc.cx(q[0], q[1])
qc.h(q[0])

# Step 4: Alice measures her two qubits
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

# Step 5: Bob applies correction gates
with qc.if_test((c, 1)):
    qc.z(q[2])

with qc.if_test((c, 2)):
    qc.x(q[2])

with qc.if_test((c, 3)):
    qc.x(q[2])
    qc.z(q[2])

# Step 6: Bob measures his qubit
qc.measure(q[2], out[0])

# Step 7: Run the simulation
simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()

print("Input state: |+>")
print("Measurement results:", counts)
print(qc.draw())