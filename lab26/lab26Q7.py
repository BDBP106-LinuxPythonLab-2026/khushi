# (7) Explore the set_printoptions() function to pretty-print a numpy array by suppressing
# the scientific notation (like 1e10).
import numpy as np
arr = np.array([1e10, 2e10, 3e10, 4e10])

np.set_printoptions(suppress=True)

print(arr)
