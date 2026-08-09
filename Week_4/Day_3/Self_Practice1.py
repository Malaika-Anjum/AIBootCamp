# Create Confidence Intervals for other Statistics

import numpy as np
from scipy.stats import chi2

# Sample data
data = [12, 15, 14, 10, 18, 20, 16, 13, 17, 19]

# Sample size
n = len(data)

# Sample variance
s2 = np.var(data, ddof=1)

# Confidence level
confidence = 0.95
alpha = 1 - confidence

# Confidence interval for variance
lower_var = (n - 1) * s2 / chi2.ppf(
    1 - alpha / 2,   # Probability (area under the curve)
    n - 1            # Degrees of freedom
)       #RIGHT critical value
upper_var = (n - 1) * s2 / chi2.ppf(
    alpha / 2,       # Probability (area under the curve)
    n - 1            # Degrees of freedom
)       #LEFT critical value   

# Confidence interval for standard deviation
lower_std = np.sqrt(lower_var)
upper_std = np.sqrt(upper_var)

print("95% CI for Variance:", (lower_var, upper_var))
print("95% CI for Standard Deviation:", (lower_std, upper_std))