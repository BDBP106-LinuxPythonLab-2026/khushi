# (12) Analyzing Gene Expression ”Heatmaps”: You have a matrix representing the expression
# of 5 genes across 10 different tissue samples. Create a 5 x 10 array of random floats
# between 0 and 100 using np.random.rand. Subtract the mean of each gene (row) from
# its values so the average expression for every gene is 0. Identify which samples (columns)
# have a total expression (sum) greater than a specific threshold.

import numpy as np
arr=np.random.rand(5,10)*100
print("Original gene expression:")
print(arr)
mean=np.mean(arr,axis=1,keepdims=True)
normalized=arr-mean
print("Normalized expression:")
print(normalized)
sample_sum=np.sum(normalized,axis=0)
print("Sample sums:")
print(sample_sum)
threshold=50
print("Samples above threshold:")
print(np.where(sample_sum>threshold)[0]+1)