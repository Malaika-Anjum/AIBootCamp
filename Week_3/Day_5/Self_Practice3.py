# Use Probability Distributions to Simulate and Analyze Real-World Datasets

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Simulate heights of 1000 people using a Gaussian (Normal) distribution
heights = np.random.normal(loc=170, scale=10, size=1000)

# Display basic statistics
print("Average Height:", np.mean(heights))
print("Minimum Height:", np.min(heights))
print("Maximum Height:", np.max(heights))

# Visualize the distribution
plt.hist(heights, bins=30, color="skyblue", edgecolor="black")

plt.title("Simulated Heights of People")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")

plt.show()