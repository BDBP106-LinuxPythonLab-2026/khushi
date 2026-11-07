# (4) Thinking along the same lines of the above question, how will you swap two columns in
# a 2D array? Define a 3x3 matrix with random values, and swap first and second columns
# in this array.
import numpy as np

# Create a 3x3 matrix with random values
arr = np.random.randint(1, 100, size=(3, 3))

print("Original Matrix:")
print(arr)

# Swap the first and second columns
arr[:, [0, 1]] = arr[:, [1, 0]]

print("\nMatrix after swapping first and second columns:")
print(arr)
