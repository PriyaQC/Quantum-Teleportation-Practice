#Quantumteleportation_day1
import numpy as np 
alpha = 1 / np.sqrt(3)
beta =  np.sqrt(2/3)
psi = np.array([alpha,beta],dtype = complex)
print("Quantum State:",psi)
probabilities = np.abs(psi)**2
print("Probability of 0 = ",probabilities[0])
print("Probability of 1 =" ,probabilities[1])
print("Total probability = ", np.sum(probabilities))











