
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# True position
true_position = 50.0
num_measurements = 1000

# Sensor noise standard deviations (meters)
sigma_a = 0.5
sigma_b = 2.0

# Generate independent measurements from two unbiased sensors
sensor_a = true_position + rng.normal(0, sigma_a, num_measurements)
sensor_b = true_position + rng.normal(0, sigma_b, num_measurements)

# Simple fusion: equal weighting
equal_weight_estimate = (sensor_a + sensor_b) / 2

# Uncertainty-weighted fusion:
# More precise sensors receive greater weight.
weight_a = 1 / sigma_a**2
weight_b = 1 / sigma_b**2

weighted_estimate = (
    weight_a * sensor_a + weight_b * sensor_b
) / (weight_a + weight_b)

# Calculate statistics
def report_statistics(name, estimates):
    print(f"{name}:")
    print(f"  Mean: {np.mean(estimates):.4f} m")
    print(f"  Standard deviation: {np.std(estimates):.4f} m")
    print(f"  RMSE: {np.sqrt(np.mean((estimates - true_position)**2)):.4f} m")
    print()

report_statistics("Sensor A", sensor_a)
report_statistics("Sensor B", sensor_b)
report_statistics("Equal-weight estimate", equal_weight_estimate)
report_statistics("Uncertainty-weighted estimate", weighted_estimate)

print("Theoretical standard deviations:")
print(f"  Sensor A: {sigma_a:.4f} m")
print(f"  Sensor B: {sigma_b:.4f} m")
print(
    "  Equal-weight estimate: "
    f"{np.sqrt((sigma_a**2 + sigma_b**2) / 4):.4f} m"
)
print(
    "  Weighted estimate: "
    f"{np.sqrt(1 / (weight_a + weight_b)):.4f} m"
)

# Plot 1: Compare a short segment of sensor measurements
plt.figure()
sample_indices = np.arange(50)

plt.plot(sample_indices, sensor_a[:50], ".", label="Sensor A")
plt.plot(sample_indices, sensor_b[:50], ".", label="Sensor B")
plt.axhline(true_position, linestyle="--", label="True position")
plt.xlabel("Measurement index")
plt.ylabel("Position (m)")
plt.title("Two Sensors Measuring the Same Position")
plt.legend()
plt.grid(True)
plt.savefig("sensor_fusion_measurements.png")

# Plot 2: Compare error distributions
plt.figure()
plt.hist(sensor_a - true_position, bins=30, alpha=0.6, label="Sensor A")
plt.hist(sensor_b - true_position, bins=30, alpha=0.5, label="Sensor B")
plt.xlabel("Measurement error (m)")
plt.ylabel("Count")
plt.title("Sensor Error Distributions")
plt.legend()
plt.grid(True)
plt.savefig("sensor_fusion_errors.png")

# Plot 3: Compare estimation errors
plt.figure()
plt.hist(
    equal_weight_estimate - true_position,
    bins=30,
    alpha=0.6,
    label="Equal weighting"
)
plt.hist(
    weighted_estimate - true_position,
    bins=30,
    alpha=0.6,
    label="Uncertainty weighting"
)
plt.xlabel("Estimation error (m)")
plt.ylabel("Count")
plt.title("Fused Estimate Error Distributions")
plt.legend()
plt.grid(True)
plt.savefig("sensor_fusion_estimates.png")
