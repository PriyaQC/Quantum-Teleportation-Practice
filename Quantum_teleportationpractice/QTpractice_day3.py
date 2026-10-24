#QTpractice_day3
import numpy as np
theta = np.pi/3
phi = np.pi/4

alpha = np.cos(theta/2)
beta = np.exp(1j*phi)*np.sin(theta/2)
psi = np.array([alpha,beta],dtype = complex)
probabilities = np.abs(psi)**2
print("Amplitude alpha:",alpha)
print("Amplitude beta:",beta)
print("Quantum State:",psi)
print("Probability of 0:", probabilities[0])
print("probability of 1:",probabilities[1])
print("Total probability:",np.sum(probabilities))
print("Normalized",np.isclose(np.sum(probabilities),1.0))