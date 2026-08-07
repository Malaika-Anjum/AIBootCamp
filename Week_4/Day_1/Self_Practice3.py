# Explore other distributions (e.g., normal, binomial) using Python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Normal Distribution

# Parameters
mean = 50
std = 10

# Generate values
x = np.linspace(mean - 4*std, mean + 4*std, 1000)

# Probability density
y = norm.pdf(x, mean, std)

# Plot
plt.plot(x, y)
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.show()

# Probability that X is less than 60
probability = norm.cdf(60, mean, std)

print("P(X < 60) =", probability)
