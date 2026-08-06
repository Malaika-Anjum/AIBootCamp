# Perform Hypothesis Testing on real-world Datasets (e.g. , comparing exam scores of two groups)


import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
df = pd.read_csv(r"E:\AIBootCamp\Week_3\Day_6\exam_score.csv")

# Separate Math Scores by Gender
male_scores = df[df["Gender"] == "male"]["MathScore"]
female_scores = df[df["Gender"] == "female"]["MathScore"]

# Perform Independent t-test
t_statistic, p_value = ttest_ind(male_scores, female_scores)

# Display results
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# Interpret the result
alpha = 0.05

if p_value < alpha:
    print("Reject the Null Hypothesis")
    print("There is a significant difference in the average Math scores.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("There is no significant difference in the average Math scores.")