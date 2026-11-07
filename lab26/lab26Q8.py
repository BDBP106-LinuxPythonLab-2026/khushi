# (8) Create a numpy array with any 10 numbers, and print the average, highest and lowest
# score, how many numbers are above 20, and the scores that are below 20.
import numpy as np
scores = np.array([10, 25, 30, 15, 45, 50, 18, 22, 35, 12])

print("Scores:")
print(scores)

print("Average:", np.mean(scores))

print("Highest Score:", np.max(scores))

print("Lowest Score:", np.min(scores))

print("Numbers above 20:", np.sum(scores > 20))

print("Scores below 20:", scores[scores < 20])