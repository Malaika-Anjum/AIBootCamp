# def bayes_theorem(prior, likelihood, evidence):
#     return (likelihood * prior) / evidence

##########################

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson

# Gausian Distribution
# x = np.linspace(-4, 4, 100)
# y = norm.pdf(x, loc=0, scale=1)
# plt.plot(x, y, label="Gaussian")
# plt.title("Gaussian Distribution")
# plt.show()

#########################

# p = 0.6
# plt.bar([0, 1], [1-p, p], color="blue")
# plt.title("Bernoulli Distribution")
# plt.xticks([0, 1], labels=["0 (Failure)", "1 (Success)"])
# plt.show()

################################

# n, p = 10, 0.5
# x = np.arange(0, n+1)
# y = binom.pmf(x, n, p)
# plt.bar(x, y, color="green")
# plt.title("Binomial Distribution")
# plt.show()

##############################

lam = 3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)
plt.bar(x, y, color="orange")
plt.title("Poisson Distribution")
plt.show()
        