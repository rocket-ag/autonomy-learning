# Estimation Uncertainty and Monte Carlo Simulation

## 1. Standard Error of the Mean

For N independent measurements with standard deviation sigma, the standard error of the sample mean is:

\[
\sigma_{\bar{x}}=\frac{\sigma}{\sqrt{N}}
\]

- Standard deviation describes the spread of individual measurements.
- Standard error describes the uncertainty in the estimated mean due to finite sampling.
- Increasing the number of independent measurements reduces standard error, but does not eliminate systematic bias.

## 2. Combining Sensor Measurements

For two independent, unbiased measurements of the same quantity, with known variances:

\[
w_i=\frac{1}{\sigma_i^2}
\]

\[
\hat{x}=\frac{w_1z_1+w_2z_2}{w_1+w_2}
\]

The lower-variance measurement receives more weight. A noisier sensor can still contribute useful information.

This result assumes the measurements are unbiased, their variances are known, and their errors are independent. Correlated errors and unknown biases require additional treatment.

## 3. Monte Carlo Simulation

Monte Carlo simulation evaluates a system across many realizations of uncertain inputs.

General workflow:
1. Define the system and its parameters.
2. Identify uncertain inputs and model their distributions.
3. Generate random inputs for one trial.
4. Run the system or algorithm.
5. Record a performance metric.
6. Repeat across many trials.
7. Analyze the distribution of outcomes.

Measurements per trial and number of trials serve different purposes:
- More measurements per trial can improve an estimate formed from those measurements.
- More trials characterize how the estimator performs across different realizations.

## 4. Performance Metrics

For trial errors \(e_i\):

Mean error:
\[
\bar{e}=\frac{1}{M}\sum_{i=1}^{M}e_i
\]

Root mean square error:
\[
RMSE=\sqrt{\frac{1}{M}\sum_{i=1}^{M}e_i^2}
\]

- Mean error reveals systematic overestimation or underestimation.
- Error standard deviation measures variability across trials.
- RMSE reflects both bias and random variability.

Monte Carlo results depend on the realism of the model, the scenarios tested, and the chosen performance metrics.
