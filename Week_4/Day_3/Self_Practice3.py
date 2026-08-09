# Visualize Confidence Intervals for multiple Samples Using Matplotlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Four different samples
samples = [
    [72, 75, 78, 74, 76],
    [80, 82, 85, 81, 83],
    [65, 68, 70, 69, 67],
    [88, 90, 91, 89, 87]
]

means = []
errors = []

# Calculate confidence interval for each sample
for sample in samples:

    mean = np.mean(sample)
    std = np.std(sample, ddof=1)
    n = len(sample)

    t_value = t.ppf(0.975, df=n-1)

    margin_error = t_value * (std / np.sqrt(n))

    means.append(mean)
    errors.append(margin_error)

# Plot
plt.errorbar(
    x=[1,2,3,4],
    y=means,
    yerr=errors,
    fmt='o',
    capsize=5
)

plt.xticks([1,2,3,4], ['Sample 1','Sample 2','Sample 3','Sample 4'])

plt.xlabel("Samples")
plt.ylabel("Mean")
plt.title("95% Confidence Intervals")

plt.grid(True)
plt.show()