import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])
x2 = np.outer(x, y)

print("x:", x)
print("Shape:", x.shape)
print("Size:", x.size)
print("Data type:", x.dtype)

print("x2:", x2)
print("Shape:", x2.shape)
print("Size:", x2.size)
print("Data type:", x2.dtype)

print("Addition:", x + y)
print("Multiplication:", x * y)

print("Mean:", np.mean(x))
print("Standard deviation:", np.std(x))
