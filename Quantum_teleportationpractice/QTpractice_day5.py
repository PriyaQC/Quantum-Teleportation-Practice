#QTpractice_day5
import numpy as np 
plus = np.array([1,1],dtype=complex)/np.sqrt(2)
two_qubit_state = np.kron(plus,plus)
probabilities = np.abs(two_qubit_state)**2
print("Two-qubit state:",two_qubit_state)
print("Measurement probabilities",probabilities)
print("Total Probabbility:",np.sum(probabilities))
