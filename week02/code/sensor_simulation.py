# Simulated vehicle position sensor
import random


def calculate_position(initial_position, velocity, time):
    position = velocity * time + initial_position
    return position


def measure_position(true_position):
    measurement = true_position + random.uniform(-1, 1)
    return measurement


if __name__ == "__main__":
    initial_position = 0
    velocity = 10

    for time in range(11):
        true_position = calculate_position(initial_position, velocity, time)
        measurement = measure_position(true_position)
        error = measurement - true_position

        print(time, true_position, measurement, error)
