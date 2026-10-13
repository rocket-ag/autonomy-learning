
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Sensor model
true_position = 50.0
bias = 2.0
noise = rng.uniform(-1, 1, size=100)

measurements = true_position + bias + noise
errors = measurements - true_position

# Calculate statistics
measurement_mean = np.mean(measurements)
measurement_std = np.std(measurements)
error_mean = np.mean(errors)
error_std = np.std(errors)

print("True Position:", true_position, "m")
print("Sensor Bias:", bias, "m")
print()
print("Measurement Mean:", measurement_mean, "m")
print("Measurement STD:", measurement_std, "m")
print("Error Mean:", error_mean, "m")
print("Error STD:", error_std, "m")

# Plot 1: Measurements
plt.figure()
plt.plot(measurements, "o", label="Measurements")
plt.axhline(
    true_position,
    linestyle="--",
    label="True Position"
)
plt.axhline(
    measurement_mean,
    linestyle="-.",
    label="Mean Measurement"
)
plt.xlabel("Sample Number")
plt.ylabel("Position (m)")
plt.title("Sensor Measurements with Bias")
plt.legend()
plt.grid(True)
plt.savefig("sensor_bias_measurements.png")

# Plot 2: Error distribution
plt.figure()
plt.hist(errors, bins=10, edgecolor="black")
plt.axvline(
    0,
    linestyle="--",
    label="Zero Error"
)
plt.axvline(
    bias,
    linestyle="-.",
    label="Expected Bias"
)
plt.xlabel("Measurement Error (m)")
plt.ylabel("Count")
plt.title("Distribution of Sensor Errors")
plt.legend()
plt.grid(True)
plt.savefig("sensor_bias_errors.png")
