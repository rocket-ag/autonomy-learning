# Python Exercise 1 — Answers

## 1. What is the difference between the true position and the measured position?

The true position is the actual position of the vehicle. In our simulation, we know the true position because we calculate it directly from the vehicle's initial position, velocity, and time.

The measured position is the value reported by the simulated sensor. It is the true position plus measurement noise.

In mathematical form:

measured position = true position + measurement noise

The measured position therefore may be slightly higher or lower than the true position.


## 2. Why can't we simply use the measured position as the true position?

A real sensor is not perfect. Its measurements contain noise and may also contain systematic errors such as bias.

Therefore, the measured position is only an estimate of the actual position. Treating every measurement as exactly correct would cause the system to believe that sensor errors are real changes in the vehicle's position.

Autonomous systems therefore need methods for estimating the actual state of the vehicle from imperfect sensor measurements.


## 3. What happens to the measurements if you change the sensor error range from ±1 m to ±5 m?

The measurements become less accurate because the possible measurement error is larger.

With an error range of ±1 m, a measurement of a true position of 50 m could range from 49 m to 51 m.

With an error range of ±5 m, the same true position could produce a measurement between 45 m and 55 m.

Therefore, increasing the noise range increases the uncertainty in the sensor measurements.


## 4. Why do you get different measurements each time you run the program?

The sensor noise is generated randomly using Python's random module.

Each measurement receives a new random error between -1 m and +1 m. Because the random values are different between runs, the simulated sensor measurements are also different.

This represents the fact that real sensors do not produce exactly the same measurement every time, even when the true physical quantity has not changed.


## 5. What would happen if the sensor had a constant +2 m bias in addition to random noise?

Every measurement would tend to be approximately 2 m higher than the true position, in addition to the random measurement noise.

For example, if the true position were 50 m, the sensor might produce measurements such as:

51.4 m
52.2 m
51.7 m
52.8 m

The random noise would cause the measurements to vary, but the entire set of measurements would be shifted upward by approximately 2 m.

This is different from random noise because a constant bias is a systematic error. Collecting more measurements would not necessarily eliminate the bias.

For example:

measured position = true position + 2 m bias + random noise


## 6. If the vehicle is traveling at 10 m/s, how much position error would a 0.1-second timing error introduce?

The position error would be:

position error = velocity × time error

position error = 10 m/s × 0.1 s

position error = 1 m

Therefore, a 0.1-second timing error could produce a 1 m position error for a vehicle traveling at 10 m/s.

This demonstrates why accurate timing is important in autonomous systems. A sensor measurement is associated with a particular point in time, so if the system assigns the measurement the wrong timestamp, the estimated position can be incorrect.

The problem becomes even more significant at higher vehicle speeds or with larger timing errors. In a real autonomous system, sensors operating at different rates also need to be properly time-synchronized so that measurements from different sensors can be correctly associated with the vehicle's state at the same point in time.
