import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

true_position = 50.0
measurements = true_position + rng.uniform(-5, 5, size=100)
errors = measurements - true_position

# Calculate statistics
measurement_mean = np.mean(measurements)
measurement_std = np.std(measurements)
error_mean = np.mean(errors)
error_std = np.std(errors)

print("Measurement Mean:", measurement_mean)
print("Measurement STD:", measurement_std)
print("Error Mean:", error_mean)
print("Error STD:", error_std)

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
plt.title("Simulated Sensor Measurements")
plt.legend()
plt.grid(True)
plt.savefig("sensor_measurements.png")

# Plot 2: Error distribution
plt.figure()
plt.hist(errors, bins=10, edgecolor="black")
plt.axvline(
    0,
    linestyle="--",
    label="Zero Error"
)
plt.xlabel("Measurement Error (m)")
plt.ylabel("Count")
plt.title("Distribution of Sensor Errors")
plt.legend()
plt.grid(True)
plt.savefig("sensor_errors.png")
