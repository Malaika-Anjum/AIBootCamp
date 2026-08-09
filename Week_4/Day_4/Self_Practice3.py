# Perform hyposthesis testing on proportions using the binomial distribution

from scipy.stats import binomtest

# Number of trials
n = 100

# Observed number of successes
successes = 68

# Claimed population proportion
p0 = 0.60

# Perform exact binomial hypothesis test
result = binomtest(successes, n=n, p=p0, alternative="two-sided")

print("Observed proportion:", successes / n)
print("P-value:", result.pvalue)

# Decision
alpha = 0.05

if result.pvalue < alpha:
    print("Reject the null hypothesis.")
    print("There is a significant difference from the claimed proportion.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is not enough evidence to reject the claimed proportion.")