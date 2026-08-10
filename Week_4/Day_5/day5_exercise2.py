# Perform a Chi-Square Test

from scipy.stats import chi2_contingency

# Observed frequencies
data = [
    [50, 30],   # Group 1
    [20, 40]    # Group 2
]

# Perform Chi-Square test
chi2, p, dof, expected = chi2_contingency(data)

print("Chi-Square Statistic:", chi2)
print("P-Value:", p)
print("Degrees of Freedom:", dof)
print("Expected Frequencies:", expected)

# Hypothesis testing
alpha = 0.05

if p < alpha:
    print("Reject the null hypothesis.")
    print("There is a significant relationship between the variables.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is no significant relationship between the variables.")