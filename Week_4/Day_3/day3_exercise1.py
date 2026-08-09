# Calculate Confidence Intervals for Sample Data

import numpy as np
from scipy.stats import t

# Sample data
data = [12, 15, 14, 10, 13, 16, 18, 11, 14, 15]

# Sample statistics
mean = np.mean(data)
std = np.std(data, ddof=1)
n = len(data)

# 95% Confidence Interval
confidence = 0.95
t_value = t.ppf((1 + confidence) / 2, df=n - 1)
margin_error = t_value * (std / np.sqrt(n))

lower = mean - margin_error
upper = mean + margin_error

print("Sample Mean:", mean)
print("95% Confidence Interval: ({:.2f}, {:.2f})".format(lower, upper))