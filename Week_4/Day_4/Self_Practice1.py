# Perform a z-test for large sample sizes

import numpy as np
from statsmodels.stats.weightstats import ztest

# Sample data
sample = np.array([52, 48, 51, 49, 53, 50, 47, 54, 52, 51,
                   49, 50, 48, 53, 52, 51, 50, 49, 54, 52])

# Hypothesized population mean
population_mean = 50

# Perform one-sample z-test
z_stat, p_value = ztest(sample, value=population_mean)

print("Z-statistic:", z_stat)
print("P-value:", p_value)

# Decision
alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")