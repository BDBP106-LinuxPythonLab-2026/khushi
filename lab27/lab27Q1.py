# (1) Use the following data to
# temps = np.arange(20, 71, 5)
# activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5]) #relative activity
# 1. Plot activity against temperature as a line with circle markers.
# 2. Find the optimum temperature with temps[np.argmax(activity)], not by reading
# it off the data.
# 3. Mark it with a dashed vertical line (ax.axvline) and a text label pointing to the
# peak using ax.annotate(). Your plot should show: a rise and fall with the peak, and
# the label, at 50oC.

import numpy as np
import matplotlib.pyplot as plt

temps = np.arange(20, 71, 5)

activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])

# Find optimum temperature
opt_temp = temps[np.argmax(activity)]

print("Optimum temperature:", opt_temp, "°C")

# Plot
fig, ax = plt.subplots()

ax.plot(temps, activity, marker='o', color='blue',linestyle='-', label='Enzyme activity')

# Mark optimum temperature
ax.axvline(opt_temp, color='red', linestyle='--')

# Annotate peak
ax.annotate(f'Peak at {opt_temp}°C',xy=(opt_temp, max(activity)),xytext=(opt_temp + 5, max(activity) - 10),arrowprops=dict(arrowstyle='->', color='red'))
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Relative activity")
ax.set_title("Effect of Temperature on Enzyme Activity")
ax.legend()
ax.grid()

plt.show()