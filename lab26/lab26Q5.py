# (5) You are given two 1D arrays. Write a function to create a new array that contains the
# maximum of the respective elements in the two arrays. For example, if a=[1,2] and
# b=[0,5] then the new array will be c=[1,5].

a=[1,2]
b=[0,5]
print(a.max,b.max)

import numpy as np

def maximum_array(a, b):
    c = np.maximum(a, b)
    return c

a = np.array([1, 2])
b = np.array([0, 5])

c = maximum_array(a, b)

print("Array a:", a)
print("Array b:", b)
print("Maximum Array:", c)