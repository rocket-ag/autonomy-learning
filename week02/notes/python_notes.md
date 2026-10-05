# Python Notes

## 1. What is a Python variable?

A Python variable is a name that refers to a value or object. Variables allow data to be stored and referenced later in a program.

For example:

x = 10
velocity = 25.0
name = "vehicle"

Python is dynamically typed, meaning I do not have to explicitly declare the type of a variable. Python determines the type from the value assigned to it.

A variable can also be reassigned to a different type of object.

For example:

x = 10
x = "hello"

This is allowed in Python because the variable name is not permanently associated with one data type.


## 2. What is the difference between a list and a NumPy array?

A Python list is a general-purpose container that can hold multiple objects. Lists can contain different types of objects and are useful for general programming.

For example:

measurements = [1.2, 1.4, 1.1, 1.3]

A NumPy array is specifically designed for numerical and scientific computing. NumPy arrays generally contain elements of the same data type and support efficient vectorized mathematical operations.

For example:

import numpy as np

measurements = np.array([1.2, 1.4, 1.1, 1.3])

NumPy arrays make it possible to perform mathematical operations on entire arrays efficiently without explicitly writing a loop for every element.

For example:

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

x + y

produces:

[5, 7, 9]

NumPy arrays are therefore much more useful than standard Python lists for the vector and matrix calculations commonly encountered in engineering.


## 3. What is the purpose of a Python function?

A function is a reusable block of code that performs a particular task.

Functions allow a program to be divided into smaller, organized pieces and prevent the same code from having to be written repeatedly.

For example:

def calculate_position(initial_position, velocity, time):
    return initial_position + velocity * time

The function can then be called with different inputs:

position = calculate_position(0, 10, 5)

Functions can accept inputs called arguments and can return an output.

Functions are particularly useful in engineering because they allow individual pieces of a mathematical model or algorithm to be isolated and tested independently.


## 4. What is the purpose of a Python module?

A Python module is a file containing Python code that can be imported and used by another Python program.

For example:

import math

allows a program to use functionality provided by Python's math module.

Modules allow related functionality to be organized separately and reused across multiple programs.

Python also has many libraries made up of modules that provide functionality for engineering and scientific computing. Examples include NumPy, SciPy, and Matplotlib.

Modules allow me to avoid implementing common functionality from scratch and make larger programs easier to organize.


## 5. Why is NumPy useful for engineering and scientific computing?

NumPy is useful because it provides efficient data structures and mathematical operations for numerical computing.

The most important data structure is the NumPy array, which can represent vectors, matrices, and higher-dimensional numerical data.

NumPy supports operations such as:

- vector addition
- dot products
- matrix multiplication
- transposes
- statistical calculations
- array indexing and slicing
- mathematical functions

For example:

A @ x

performs matrix-vector multiplication.

This is especially important for autonomy because many algorithms are expressed mathematically using vectors and matrices.

For example, later in the curriculum I will encounter equations such as:

x_next = F @ x

and:

P_next = F @ P @ F.T + Q

NumPy allows these mathematical operations to be implemented directly and efficiently in Python.

NumPy therefore provides the foundation for much of the scientific computing I will be doing throughout the autonomy curriculum.


## Important Python concepts learned

Some of the most important concepts from this reading are:

- Variables store references to values or objects.
- Python is dynamically typed.
- Lists are general-purpose containers.
- NumPy arrays are designed for numerical computation.
- Functions allow code to be organized and reused.
- Modules allow functionality to be organized and imported.
- NumPy provides efficient vector and matrix operations.
- Python can be used as a high-level interface for implementing mathematical algorithms.
