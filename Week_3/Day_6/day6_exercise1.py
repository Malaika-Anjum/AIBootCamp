# Calculate Mean, Variancen and Standard Deviation

import numpy as np

# Sample data
data = np.array([1, 2, 3, 4, 5])

# Calculate Mean
mean = np.mean(data)

# Calculate Variance
variance = np.var(data)

# Calculate Standard Deviation
std_dev = np.std(data)

print("Mean : ", mean)
print("Variance : ", variance)
print("Standard Deviation : ", std_dev)