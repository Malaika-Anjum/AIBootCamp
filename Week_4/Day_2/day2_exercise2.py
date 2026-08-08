# Create and Analyze Random Variables

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform


# Discrete random variable: a fair six-sided die
outcomes = np.arange(1, 7)
probabilities = np.array([1/6]* 6)

plt.bar(outcomes, probabilities, color="steelblue", alpha=0.8)
plt.title("PMF of a Fair Dice Roll")
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.xticks(outcomes)
plt.ylim(0, 0.2)
plt.show()

# Continuous random variable: Uniform(0, 1)
x = np.linspace(0, 1, 100)
pdf = uniform.pdf(x, loc=0, scale=1)

plt.plot(x, pdf, color="crimson")
plt.title("PDF of Uniform(0, 1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(0, 1.2)
plt.show()
