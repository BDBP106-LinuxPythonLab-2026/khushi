import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)

organisms = ["E. coli", "S. cerevisiae",
             "P. falciparum", "S. coelicolor"]

mean_gc = [51, 38, 19, 72]

# Create 2x2 subplot grid
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

# Flatten axes
axes = axes.flatten()

# Common histogram bins
bins = np.arange(0, 101, 2)

for ax, organism, gc in zip(axes, organisms, mean_gc):

    # Generate GC values
    values = rng.normal(gc, 4, size=1000)

    # Histogram
    ax.hist(values, bins=bins, color='skyblue',
            edgecolor='black')

    # Mark mean
    ax.axvline(gc, color='red', linestyle='--')

    # Title
    ax.set_title(f"{organism} (Mean GC = {gc}%)")

# Label only outer axes
axes[0].set_ylabel("Frequency")
axes[2].set_ylabel("Frequency")

axes[2].set_xlabel("GC content (%)")
axes[3].set_xlabel("GC content (%)")

# Overall title
fig.suptitle("GC Content Distribution in Different Organisms")

plt.tight_layout()
plt.show()