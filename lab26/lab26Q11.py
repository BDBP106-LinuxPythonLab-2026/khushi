# (11) One-Hot Encoding DNA Sequences: Machine learning models cannot ”read” strings like
# ”GATTACA”. We convert them into a matrix where each base is represented by a vector
#
# (e.g., A = [1,0,0,0], C = [0,1,0,0], etc.). The Task: Create a NumPy array for a DNA
# sequence where each row represents a base and each column represents A, C, G, or T.
import numpy as np
seq="GATTACA"
encoding={'A':[1,0,0,0],'C':[0,1,0,0],'G':[0,0,1,0],'T':[0,0,0,1]}
arr=[]
for base in seq:
    arr.append(encoding[base])
result=np.array(arr)
print("DNA Sequence:",seq)
print("One hot encoding:")
print(result)