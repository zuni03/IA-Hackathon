import random
import matplotlib.pyplot as plt

gain = 5.6       
num_points = 5    


Vin_plus = [random.uniform(0.0, 0.1) for _ in range(num_points)]
Vin_minus = [random.uniform(0.0, 0.1) for _ in range(num_points)]


noise = [random.uniform(0.02, 0.05) for _ in range(num_points)]
Vin_plus_noise = [v + n for v, n in zip(Vin_plus, noise)]
Vin_minus_noise = [v + n for v, n in zip(Vin_minus, noise)]


diff_signal = [vp - vm for vp, vm in zip(Vin_plus_noise, Vin_minus_noise)]
output_signal = [gain * d for d in diff_signal]


print("Sample\tVin+\tVin-\tAmplified Output")
for i, (vp, vm, out) in enumerate(zip(Vin_plus_noise, Vin_minus_noise, output_signal)):
    print(f"{i+1}\t{vp:.3f}\t{vm:.3f}\t{out:.3f}")

plt.figure(figsize=(10,6))
plt.plot(Vin_plus_noise, label='Vin+ (with noise)')
plt.plot(Vin_minus_noise, label='Vin- (with noise)')
plt.plot(output_signal, label='Amplified Output')
plt.title("Instrumentation Amplifier Simulation")
plt.xlabel("Sample Number")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid(True)
plt.show()

