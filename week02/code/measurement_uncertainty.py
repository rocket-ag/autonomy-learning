
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Sensor model
true_position = 50.0
noise_limit = 1.0

# Generate 10,000 independent measurements
measurements = (
    true_position
    + rng.uniform(-noise_limit, noise_limit, size=10_000)
)

# Sample counts to investigate
sample_counts = np.array([1, 2, 5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000])

sample_means = []
sample_stds = []
standard_errors = []

for n in sample_counts:
    sample = measurements[:n]

    sample_means.append(np.mean(sample))
    sample_stds.append(np.std(sample))
    standard_errors.append(np.std(sample) / np.sqrt(n))

sample_means = np.array(sample_means)
sample_stds = np.array(sample_stds)
standard_errors = np.array(standard_errors)

# Print results
print(f"True position: {true_position:.3f} m")
print()
print(f"{'N':>7} {'Mean (m)':>12} {'Std Dev (m)':>14} {'Std Error (m)':>15}")

for i, n in enumerate(sample_counts):
    print(
            f"{n:7d} "
        f"{sample_means[i]:12.4f} "
        f"{sample_stds[i]:14.4f} "
        f"{standard_errors[i]:15.4f}"
    )

# Plot 1: Sample mean as the number of measurements increases
plt.figure()
plt.plot(sample_counts, sample_means, "o-", label="Sample mean")
plt.axhline(true_position, linestyle="--", label="True position")
plt.xscale("log")
plt.xlabel("Number of measurements")
plt.ylabel("Estimated position (m)")
plt.title("Position Estimate vs. Sample Count")
plt.legend()
plt.grid(True)
plt.savefig("measurement_uncertainty_mean.png")

# Plot 2: Standard error vs. sample count
plt.figure()
plt.plot(sample_counts, standard_errors, "o-", label="Estimated standard error")
plt.xscale("log")
plt.yscale("log")

# Theoretical standard error for uniform noise
theoretical_std = noise_limit / np.sqrt(3)
theoretical_error = theoretical_std / np.sqrt(sample_counts)

plt.plot(sample_counts, theoretical_error, "--", label="Theoretical standard error")
plt.xlabel("Number of measurements")
plt.ylabel("Standard error (m)")
plt.title("Uncertainty in the Mean vs. Sample Count")
plt.legend()
plt.grid(True, which="both")
plt.savefig("measurement_uncertainty_error.png")
