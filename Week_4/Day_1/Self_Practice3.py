# Explore other distributions (e.g., normal, binomial) using Python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

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


################################

# Binomial Distribution

# Parameters
n = 10       # Number of trials
p = 0.5      # Probability of success

# Possible number of successes
x = np.arange(0, n + 1)

# Probability for each value
y = binom.pmf(x, n, p)

# Plot
plt.bar(x, y)
plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show()

# Probability of exactly 5 successes
probability = binom.pmf(5, n, p)

print("P(X = 5) =", probability)