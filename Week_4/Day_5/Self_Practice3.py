# Visualize test results using boxplots or bar plots.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load student dataset
data = pd.read_csv(r"E:\AIBootCamp\Week_4\Day_5\students_data.csv")

# Rename 'class' because it is a Python reserved keyword
data = data.rename(columns={"class": "student_class"})


# Display relevant columns
print(data[["student_class", "gender", "GPA"]].head())

# Two-way ANOVA
model = ols(
    "GPA ~ C(student_class) * C(gender)",
    data=data
).fit()

# ANOVA table
anova_table = sm.stats.anova_lm(model, typ=2)

print("\nANOVA Table:")
print(anova_table)

# Test interaction effect
interaction_p = anova_table.loc[
    "C(student_class):C(gender)", "PR(>F)"
]

print("\nInteraction p-value:", interaction_p)

# Hypothesis testing
alpha = 0.05

if interaction_p < alpha:
    print("Reject the null hypothesis.")
    print("There is a significant interaction between class and gender.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is no significant interaction between class and gender.")

# Visualization using boxplots

sns.boxplot(
    data=data,
    x="student_class",
    y="GPA"
)

plt.title("GPA Distribution by Class")
plt.xlabel("Class")
plt.ylabel("GPA")

plt.show()

# Visualization using bar plots

sns.barplot(
    data=data,
    x="student_class",
    y="GPA",
    hue="gender"
)

plt.title("Mean GPA by Class and Gender")
plt.xlabel("Class")
plt.ylabel("Mean GPA")

plt.show()