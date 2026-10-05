# Engineering Principles

## 1. Understand the fundamentals before relying on abstractions

I should understand the mathematical and engineering principles behind an algorithm before relying on a library implementation. Libraries are useful tools, but I should be able to explain what the algorithm is doing, what assumptions it makes, and what its important parameters represent.

## 2. Validate algorithms against known results

Whenever possible, I should test an implementation against an analytically known solution, a simplified case, or another trusted reference. A program producing an output without errors does not mean that the output is correct.

## 3. Make experiments reproducible

When performing an experiment or simulation, I should record the relevant code, parameters, datasets, initial conditions, random seeds, and software dependencies so that I can reproduce the result later.

## 4. Question assumptions

I should explicitly identify the assumptions behind an algorithm or model and understand how violations of those assumptions could affect the result. This is particularly important for autonomous systems because real-world sensors and environments rarely behave exactly like idealized models.

## 5. Use simulation to understand behavior, not to prove reality

Simulation is useful for testing algorithms and understanding system behavior, but a successful simulation does not prove that a system will work in the real world. I should understand the limitations of the simulation and eventually consider how the algorithm would behave with real sensor noise, imperfect models, delays, and unexpected conditions.

## 6. Prefer quantitative evaluation over visual inspection

I should use measurable performance metrics whenever possible rather than relying solely on whether a plot or animation looks correct. Examples include estimation error, position error, detection accuracy, computational time, probability of failure, and robustness to noise.

## 7. Build incrementally

I should start with simple problems that I can understand completely before adding complexity. When an algorithm fails, simplifying the problem should be one of my first debugging tools.

## 8. Understand why a result occurs

I should not be satisfied with obtaining the correct answer without understanding why the system produced it. The goal of this curriculum is not simply to make code work, but to develop the ability to reason about autonomous systems and predict how they will behave under different conditions.
