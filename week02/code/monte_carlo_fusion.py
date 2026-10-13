
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Simulation parameters
true_position = 50.0
sigma_a = 0.5
sigma_b = 2.0
num_measurements = 1000
num_trials = 5000

# Store the estimation error from every trial
errors_a = np.empty(num_trials)
errors_equal = np.empty(num_trials)
errors_weighted = np.empty(num_trials)

# Inverse-variance weights
weight_a = 1 / sigma_a**2
weight_b = 1 / sigma_b**2

for trial in range(num_trials):
    sensor_a = true_position + rng.normal(0, sigma_a, num_measurements)
    sensor_b = true_position + rng.normal(0, sigma_b, num_measurements)

    # Estimate position by averaging each sensor's measurements
    estimate_a = np.mean(sensor_a)
    estimate_b = np.mean(sensor_b)

    # Three estimators
    estimate_equal = (estimate_a + estimate_b) / 2

    estimate_weighted = (
        weight_a * estimate_a + weight_b * estimate_b
    ) / (weight_a + weight_b)

    # Record errors
    errors_a[trial] = estimate_a - true_position
    errors_equal[trial] = estimate_equal - true_position
    errors_weighted[trial] = estimate_weighted - true_position

# Evaluate performance across trials
def report_results(name, errors):
    bias = np.mean(errors)
    rmse = np.sqrt(np.mean(errors**2))
    spread = np.std(errors)

    print(name)
    print(f"  Mean error (bias): {bias:.6f} m")
    print(f"  Error standard deviation: {spread:.6f} m")
    print(f"  RMSE: {rmse:.6f} m")
    print()

report_results("Sensor A average", errors_a)
report_results("Equal-weight fusion", errors_equal)
report_results("Weighted fusion", errors_weighted)

# Compare error distributions
plt.figure()
plt.hist(errors_a, bins=50, alpha=0.5, label="Sensor A")
plt.hist(errors_equal, bins=50, alpha=0.5, label="Equal-weight fusion")
plt.hist(errors_weighted, bins=50, alpha=0.5, label="Weighted fusion")
plt.axvline(0, linestyle="--", label="Zero error")
plt.xlabel("Estimation error (m)")
plt.ylabel("Number of trials")
plt.title("Monte Carlo Estimation Error")
plt.legend()
plt.grid(True)
plt.savefig("monte_carlo_fusion.png")

# Compare RMSE
names = ["Sensor A", "Equal weight", "Weighted"]
rmses = [
    np.sqrt(np.mean(errors_a**2)),
    np.sqrt(np.mean(errors_equal**2)),
    np.sqrt(np.mean(errors_weighted**2)),
]

plt.figure()
plt.bar(names, rmses)
plt.ylabel("RMSE (m)")
plt.title("Estimation Performance Across Trials")
plt.grid(axis="y")
plt.savefig("monte_carlo_rmse.png")
