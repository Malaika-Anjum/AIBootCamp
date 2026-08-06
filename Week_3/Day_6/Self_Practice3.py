# Calculate Confidence Intervals for Proportions in Datasets

import numpy as np
from scipy.stats import norm

# Sample data
sample_size = 200
successes = 120

# Calculate sample proportion
p = successes / sample_size

# Confidence level
confidence_level = 0.95

# Calculate Z-score
z = norm.ppf((1 + confidence_level) / 2)

# Calculate Standard Error
standard_error = np.sqrt((p * (1 - p)) / sample_size)

# Calculate Margin of Error
margin_of_error = z * standard_error

# Calculate Confidence Interval
lower = p - margin_of_error
upper = p + margin_of_error

# Display results
print("Sample Proportion:", p)
print("95% Confidence Interval:")
print("Lower Limit:", lower)
print("Upper Limit:", upper)