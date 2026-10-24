#QTpractice_7
import numpy as np 
import matplotlib.pyplot as plt 
bell_state = np.array([
    1/np.sqrt(2),
    0,
    0,
    1/np.sqrt(2)
],dtype = complex)
probabilities = np.abs(bell_state)**2
print("Bell state Amplitudes:")
print(bell_state)
print("\nTheoretical probabilities:")
print("|00>:",probabilities[0])
print("|01>:",probabilities[1])
print("|10>:",probabilities[2])
print("|11>:",probabilities[3])

outcomes = ["00","01","10","11"]

shots = 1000
measurements = np.random.choice(
    outcomes,
    size=shots,
    p=probabilities
)

counts = {
    outcome: int(np.sum(measurements == outcome))
    for outcome in outcomes
}

print("\nMeasurement counts:")
for outcome in outcomes:
    print(outcome,":",counts[outcome])

print("\nTotal Measurement:",sum(counts.values()))    

plt.bar(counts.keys(),counts.values())
plt.xlabel("Measurement outcome")
plt.ylabel("Number of Measurements")
plt.title("Bell-state measurement Simulation")
plt.tight_layout()
plt.savefig("day_7_bell_measurement.png",dpi=300)
plt.show()