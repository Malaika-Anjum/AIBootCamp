# Use the Iris dataset a test if the mean sepal length differs between two species

import pandas as pd
from statsmodels.stats.weightstats import ztest

# Load Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Select two species
setosa = iris[iris["species"] == "setosa"]["sepal_length"]
versicolor = iris[iris["species"] == "versicolor"]["sepal_length"]

# Perform two-sample z-test
z_stat, p_value = ztest(setosa, versicolor)

print("Setosa mean sepal length:", setosa.mean())
print("Versicolor mean sepal length:", versicolor.mean())
print("Z-statistic:", z_stat)
print("P-value:", p_value)

# Hypothesis test
alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
    print("The mean sepal lengths are significantly different.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is no significant difference in mean sepal length.")