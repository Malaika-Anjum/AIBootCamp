# Visualize the Distribution of Data and Highlight Mean, Median, and Mode using Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Sample dataset
data = [12, 15, 18, 18, 20, 22, 22, 22, 25, 28, 30, 32, 35]

# Calculate Mean
mean = np.mean(data)

# Calculate Median
median = np.median(data)

# Calculate Mode
values, counts = np.unique(data, return_counts=True)
mode = values[np.argmax(counts)]

# Plot histogram
plt.hist(data, bins=8, color="skyblue", edgecolor="black")

# Draw Mean, Median, and Mode
plt.axvline(mean, color="red", linestyle="--", label=f"Mean = {mean:.2f}")
plt.axvline(median, color="green", linestyle="--", label=f"Median = {median}")
plt.axvline(mode, color="purple", linestyle="--", label=f"Mode = {mode}")

# Add title and labels
plt.title("Distribution of Data")
plt.xlabel("Values")
plt.ylabel("Frequency")

# Display legend
plt.legend()

plt.show()