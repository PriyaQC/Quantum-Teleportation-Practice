#QTpractice_day2
import numpy as np
alpha = 1/np.sqrt(2)
beta = 1j/np.sqrt(2)
psi = np.array([alpha,beta],dtype = complex)
probabilities = np.abs(psi)**2
print("Quantum State :",psi)
print("Probability of measuring 0:", probabilities[0])
print("Probability of measuring 1:", probabilities[1])
print("Total probability =",np.sum(probabilities))
print("Is the state normalized ?",
                  np.isclose(np.sum(probabilities),1.0))