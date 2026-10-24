#QTpractice_day6
import numpy as np
state_00 = np.array([1, 0, 0, 0], dtype=complex)
H = np.array([
    [1, 1],
    [1, -1]
], dtype=complex) / np.sqrt(2)

H_first = np.kron(H, np.eye(2))
state_after_H = H_first @ state_00

print("After Hadamard:")
print(state_after_H)

CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], dtype=complex)

bell_state = CNOT @ state_after_H

print("\nBell state:")
print(bell_state)

print("\nMeasurement probabilities:")
print(np.abs(bell_state) ** 2)