# (9) Read the counts for 5 genes and store them in a numpy array. Without writing a loop,
# calculate the log2 of each element, rounded to 2 decimals. Also calculate without a loop,
# each gene’s percentage of the total count, rounded to 1 decimal.

import numpy as np

# Read counts for 5 genes
counts = np.array([int(input(f"Enter count for gene {i+1}: ")) for i in range(5)])

# Calculate log2 of each element, rounded to 2 decimals
log_values = np.round(np.log2(counts), 2)

# Calculate percentage of each gene's count, rounded to 1 decimal
percentages = np.round((counts / np.sum(counts)) * 100, 1)

# Display results
print("Gene Counts:", counts)
print("Log2 Values:", log_values)
print("Percentage of Total Counts:", percentages)
