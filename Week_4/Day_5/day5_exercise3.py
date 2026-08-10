# Conduct ANOVA

from scipy.stats import f_oneway

# Data for three groups
group1 = [12, 14, 15, 16, 17]
group2 = [11, 13, 14, 15, 16]
group3 = [10, 12, 13, 14, 15]

# Perform one-way ANOVA
f_stat, p_value = f_oneway(group1, group2, group3)

print("F-Statistic:", f_stat)
print("P-Value:", p_value)

# Hypothesis testing
alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
    print("At least one group mean is significantly different.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is no significant difference between the group means.")