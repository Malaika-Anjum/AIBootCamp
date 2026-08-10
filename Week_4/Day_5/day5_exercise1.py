# Conduct T-Test

from scipy.stats import ttest_ind

# Scores of two groups
group1 = [85, 88, 90, 92, 87, 89, 94]
group2 = [78, 82, 85, 80, 84, 79, 83]

# Perform independent t-test
t_stat, p_value = ttest_ind(group1, group2)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Hypothesis testing
alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
    print("The means are significantly different.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is no significant difference between the means.")