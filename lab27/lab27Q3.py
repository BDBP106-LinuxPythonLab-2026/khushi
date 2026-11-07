import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)

length = rng.integers(50, 800, size=100)

weight = length * 0.11 + rng.normal(0, 3, size=100)

membrane = rng.random(100) < 0.3

# Scatter plot
plt.figure(figsize=(8, 6))

# Membrane proteins
plt.scatter(
    length[membrane],
    weight[membrane],
    color='red',
    marker='^',
    alpha=0.6,
    label='Membrane proteins'
)

# Soluble proteins
plt.scatter(
    length[~membrane],
    weight[~membrane],
    color='blue',
    marker='o',
    alpha=0.6,
    label='Soluble proteins'
)

plt.xlabel("Protein length (amino acids)")
plt.ylabel("Molecular weight (kDa)")

plt.title("Protein Length vs Molecular Weight")

plt.legend()
plt.grid(alpha=0.3)

# Save figure
plt.savefig("protein_size.png", dpi=150)

plt.show()