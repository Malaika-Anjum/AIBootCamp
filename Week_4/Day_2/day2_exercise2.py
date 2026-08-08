# Analyze Dataset's Distribution

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Load Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Select a numerical column
feature = df["sepal_length"]

# Calculate distribution statistics
print("Mean:", feature.mean())
print("Median:", feature.median())
print("Standard Deviation:", feature.std())
print("Skewness:", skew(feature))
print("Kurtosis:", kurtosis(feature))

# Visualize the distribution
sns.histplot(feature, kde=True, bins=15, color="skyblue")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()