import numpy as np

if __name__ == "__main__":
    true_position = 50
    rng = np.random.default_rng(42)
    measurements = true_position + rng.uniform(-1, 1, size=100)

    meas_mean = np.mean(measurements)
    meas_std = np.std(measurements)
    meas_min = np.min(measurements)
    meas_max = np.max(measurements)
    errors = measurements - true_position
    error_mean = np.mean(errors)
    error_std = np.std(errors)
    print("Measurement Mean:", meas_mean)
    print("Measurement STD:", meas_std)
    print("Measurement Min:", meas_min)
    print("Measurement Max:", meas_max)
    print("Error Mean:", error_mean)
    print("Error STD:", error_std)
