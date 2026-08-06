# Compare Gaussian and Uniform distributions for continuous data

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate samples from Gaussian distribution
gaussian_samples = np.random.normal(loc=0, scale=1, size=1000)

# Generate samples from Uniform distribution
uniform_samples = np.random.uniform(low=-3, high=3, size=1000)

# Visualize the distributions
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(gaussian_samples, bins=30, color='blue', alpha=0.7, edgecolor='black')
plt.title('Gaussian Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(uniform_samples, bins=30, color='red', alpha=0.7, edgecolor='black')
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()