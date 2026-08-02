#Create a Custom Aggregation Function to Calculate the Variance for each Group

import pandas as pd

# Create sample dataset
data = {
    "Region": ["North", "North", "South", "South", "East", "East"],
    "Sales": [50000, 60000, 30000, 35000, 45000, 55000]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Custom function to calculate variance
def calculate_variance(x):
    return x.var()

# Apply the custom function
variance = df.groupby("Region")["Sales"].agg(calculate_variance)

print("\nVariance of Sales by Region:\n")
print(variance)