#QTpractice_day4
import numpy as np
zero = np.array([1,0], dtype = complex)
one = np.array([0,1],dtype = complex)

state_00 = np.kron(zero,zero)
state_01 = np.kron(zero,one)
state_10 = np.kron(one,zero)
state_11 = np.kron(one,one)

print("|00> =", state_00)
print("|01> =", state_01)
print("|10> =", state_10)
print("|11> =", state_11)
print("Number of amplitudes:",len(state_00))
