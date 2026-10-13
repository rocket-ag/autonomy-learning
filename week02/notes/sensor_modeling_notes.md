# Sensor Modeling and Measurement Uncertainty

## 1. Sensor Measurement Model

A basic sensor measurement can be modeled as:

\[
z = x + b + v
\]

Where:
- \(z\): measured value
- \(x\): true value
- \(b\): systematic sensor bias
- \(v\): random measurement noise

Random noise causes individual measurements to vary. Bias causes measurements to be consistently offset from the truth.

## 2. Accuracy and Precision

- **Accuracy:** How close a measurement or estimate is to the true value.
- **Precision:** How repeatable measurements are, or how tightly they cluster together.
- A sensor can be precise but inaccurate if it has a systematic bias.
- Averaging measurements can reduce the effect of independent random noise, but does not remove a constant bias.

## 3. Measurement Statistics

For measurements \(z_1,\ldots,z_N\), the sample mean is:

\[
\bar{z}=\frac{1}{N}\sum_{i=1}^{N}z_i
\]

The standard deviation describes the spread of individual measurements around their mean.

For uniform random noise between \(-a\) and \(+a\):

\[
\sigma_v=\frac{a}{\sqrt{3}}
\]

For noise uniformly distributed between -1 m and +1 m, the standard deviation is approximately 0.577 m.

The standard error of the mean for independent measurements is:

\[
\sigma_{\bar{z}}=\frac{\sigma_v}{\sqrt{N}}
\]

Increasing the number of measurements reduces uncertainty in the estimated mean, but does not eliminate systematic bias.

## 4. Error Analysis

Measurement error is:

\[
e=z-x
\]

For the sensor model above:

\[
e=b+v
\]

The mean error estimates the combined effect of bias and the average noise in the sample. The error standard deviation characterizes the spread of errors.

When the noise has zero expected value, the expected error is the bias.

## 5. Sensor Calibration

If the sensor bias \(b\) is known, a corrected measurement is:

\[
z_{\text{corrected}}=z-b
\]

Calibration can compensate for a known bias, but real sensor biases may change with temperature, time, operating conditions, or installation.

A single sensor generally cannot distinguish its own bias from an unknown change in the true state without additional information or assumptions.

## 6. Visualizing Sensor Data

- A measurement-versus-sample plot preserves the order of measurements and can reveal trends, drift, or sudden changes.
- A histogram shows the distribution of measurements or errors, including spread and approximate shape.
- A histogram discards the time ordering of observations.
- A fixed random seed makes simulations reproducible; it does not make them more accurate or representative.

## 7. NumPy and Python Lessons

- NumPy arrays support efficient numerical operations on collections of values.
- Operations such as `measurements - true_position` apply elementwise.
- `np.mean`, `np.std`, `np.min`, and `np.max` summarize arrays.
- `np.random.default_rng(seed)` creates a reproducible random-number generator when initialized with a fixed seed.
- Matplotlib can visualize measurements and error distributions. Saving figures with `plt.savefig()` is useful when an interactive display is unavailable.

## 8. Relevance to Autonomous Systems

Autonomous systems combine imperfect measurements from sources such as GPS, IMUs, wheel encoders, and cameras.

Understanding noise, uncertainty, bias, and calibration helps an estimator decide how much confidence to place in each measurement. Sensor fusion combines information from multiple sources, while state estimation uses measurements and system models to infer the vehicle's underlying state.
