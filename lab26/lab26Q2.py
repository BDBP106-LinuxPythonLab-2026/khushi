# (2) Array creation and manipulation exercises. Print all the arrays in each exercise.
# (i) Create a 1D array from 0 to 9.

import numpy as np
a=np.arange(10)
print(a)
# (ii) Create a boolean array of size 3x3.
arr= np.array([[True, False, True],
              [True, False,True],
              [False,True,True]])
print(arr)

# (iii) Using syntax from list comprehension, create an array that satisfies the condition.
# For example,
# arr = np.arange(10)
# arr = arr[ arr%2 == 1 ]
# Create an array of prime numbers from 1 to 50 using a similar approach.



arr = np.arange(1, 51)

prime = arr[np.array([
    all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    and n > 1 for n in arr
])]

print(prime)



# (iv) Create a 1D array with 20 random elements, and reshape it as a 4x5 array. Print
# the two arrays.
arr = np.random.randint(1, 100, 20)

print("Original 1D Array:")
print(arr)

new_arr = arr.reshape(4, 5)

print("Reshaped 4x5 Array:")
print(new_arr)





# (v) Create two 1D arrays a and b where a has numbers ranging from 0 to 9 and b has
# only 1s. Then stack the two arrays horizontally.
a = np.arange(10)
b = np.ones(10, dtype=int)

print("Array a:")
print(a)

print("Array b:")
print(b)

result = np.hstack((a, b))

print("Horizontally Stacked Array:")
print(result)



# (vi) Define two 1D arrays, where array a has list of first 100 numbers, and b has first
# 100 prime numbers. Obtain a new array that is the intersection of these two
# arrays (Hint: use np.intersect1d())
a = np.arange(1, 101)

b = np.array([
    n for n in range(2, 1000)
    if all(n % j != 0 for j in range(2, int(n**0.5) + 1))
])[:100]

result = np.intersect1d(a, b)

print("Array a:")
print(a)

print("Array b:")
print(b)

print("Intersection:")
print(result)


# (vii) Use the above two arrays with the aim this time to remove items from a that are
# in b. (We are doing a-b operation, use np.setdiff1d())

result = np.setdiff1d(a, b)

print("Elements in a but not in b:")
print(result)
# (viii) Use the above two arrays with the aim of getting the indices of common elements
# between the two arrays. (Hint: Use np.where(a==b))
common_indices = np.where(np.isin(a, b))

print("Indices of common elements:")
print(common_indices)


# (ix) Extract the elements of the array a above that are greater than 5 and less than
# 20.
result = a[(a > 5) & (a < 20)]

print("Elements greater than 5 and less than 20:")
print(result)

