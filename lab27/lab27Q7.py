import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-8, 8, 1000)

# Standard deviations
sigmas = [1, 1.5, 2]

plt.figure(figsize=(9, 6))

for sigma in sigmas:

    # Gaussian function
    g = (1 / (sigma * np.sqrt(2 * np.pi))) * \
        np.exp(-(x**2) / (2 * sigma**2))

    # Plot
    plt.plot(x, g, label=f'σ = {sigma}')

plt.xlabel("x")
plt.ylabel("g(x)")

plt.title("Normalized Gaussian Distributions")

plt.legend()
plt.grid()

plt.show()