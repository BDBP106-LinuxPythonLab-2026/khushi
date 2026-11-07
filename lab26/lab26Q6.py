# (6) Explore the set_printoptions() function to print a 3x3 matrix containing random
# numbers up to 3 decimal places.
import numpy as np
arr = np.random.rand(3, 3)

np.set_printoptions(precision=3)

print(arr)
