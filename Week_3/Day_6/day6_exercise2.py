# Perform a T-Test

import numpy as np
from scipy.stats import ttest_ind

# Sample data
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([2, 3, 4, 5, 6])

# Perform T-Test
t_statistic, p_value = ttest_ind(data1, data2)

print("T-Statistic : ", t_statistic)
print("P-Value : ", p_value)