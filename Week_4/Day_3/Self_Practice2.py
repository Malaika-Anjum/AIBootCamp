# Perform Stratified Sampling and Compare Intervals across Strata

import numpy as np
from scipy.stats import t

# Marks of each department (stratum)
cs = [85, 80, 82, 88, 90, 84, 81, 83]
se = [72, 75, 78, 74, 76, 73, 77, 75]
ai = [90, 92, 88, 91, 89, 93, 94, 90]

# Function to calculate Confidence Interval
def confidence_interval(data):
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    n = len(data)

    t_value = t.ppf(0.975, df=n-1)

    margin_error = t_value * (std / np.sqrt(n))

    lower = mean - margin_error
    upper = mean + margin_error

    return mean, lower, upper

# Calculate CI for each stratum
for name, marks in zip(["CS", "SE", "AI"], [cs, se, ai]):
    mean, lower, upper = confidence_interval(marks)

    print(f"{name}")
    print("Mean:", round(mean,2))
    print("95% CI:", (round(lower,2), round(upper,2)))
    print()