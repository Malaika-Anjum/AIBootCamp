# Compare the effects of Skewness and Kurtosis on different datasets

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

np.random.seed(42)

# Create datasets
normal_data = np.random.normal(0, 1, 1000)
right_skewed = np.random.exponential(1, 1000)
left_skewed = -np.random.exponential(1, 1000)
outliers = np.append(np.random.normal(0, 1, 950), np.random.normal(0, 8, 50))

# Store datasets
datasets = [
    ("Normal", normal_data),
    ("Right Skewed", right_skewed),
    ("Left Skewed", left_skewed),
    ("With Outliers", outliers)
]

# Calculate skewness and kurtosis
for name, data in datasets:
    print(name)
    print("Skewness:", round(skew(data), 2))
    print("Kurtosis:", round(kurtosis(data), 2))
    print()

# Plot datasets
fig, axes = plt.subplots(2, 2, figsize=(10, 7))

for ax, (name, data) in zip(axes.flat, datasets):
    sns.histplot(data, kde=True, ax=ax)
    ax.set_title(name)

plt.tight_layout()
plt.show()