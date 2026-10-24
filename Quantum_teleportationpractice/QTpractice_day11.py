#QTpractice_day11
import numpy as np

alice = np.array([1, 0], dtype=complex)
bob = np.array([1, 0], dtype=complex)
# Calculate the inner product <Alice|Bob>
overlap = np.vdot(alice, bob)
# Calculate fidelity
fidelity = abs(overlap) ** 2

print("Alice's state:", alice)
print("Bob's state:", bob)
print("Overlap:", overlap)
print("Fidelity:", fidelity)


# For input as |1>
alice = np.array([0, 1], dtype=complex)
bob = np.array([0, 1], dtype=complex)
# Calculate the inner product <Alice|Bob>
overlap = np.vdot(alice, bob)
# Calculate fidelity
fidelity = abs(overlap) ** 2

print("Alice's state:", alice)
print("Bob's state:", bob)
print("Overlap:", overlap)
print("Fidelity:", fidelity)

import numpy as np

# For original state |+>
alice = np.array([
    1/np.sqrt(2), 
    0,
    0,
    1/np.sqrt(2)
], 
    
    dtype=complex)
bob = np.array([
    1/np.sqrt(2),
    0,
    0,
    1/np.sqrt(2)
], 
    
    dtype=complex)

# Calculate the inner product <Alice|Bob>
overlap = np.vdot(alice, bob)

# Calculate fidelity
fidelity = abs(overlap) ** 2

print("Alice's state:", alice)
print("Bob's state:", bob)
print("Overlap:", overlap)
print("Fidelity:", fidelity)

