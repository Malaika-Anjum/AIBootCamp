# Explore datasets with real-world applications of distributions

import numpy as np
import matplotlib.pyplot as plt

# Create real-world style datasets
height = np.random.normal(170, 10, 1000)       # Heights in cm
success = np.random.binomial(10, 0.5, 1000)    # Successes in 10 trials
customers = np.random.poisson(5, 1000)         # Customers per hour

# Plot the datasets
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(height, bins=20)
plt.title("Human Heights")
plt.xlabel("Height (cm)")

plt.subplot(1, 3, 2)
plt.hist(success, bins=11)
plt.title("Successes in 10 Trials")
plt.xlabel("Number of Successes")

plt.subplot(1, 3, 3)
plt.hist(customers, bins=15)
plt.title("Customers per Hour")
plt.xlabel("Customers")

plt.tight_layout()
plt.show()