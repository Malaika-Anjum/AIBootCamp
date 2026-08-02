#Create a DataFrame from a dictionary and add a new calculated column.

import pandas as pd

# Create a dictionary with sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Add a new calculated column (Salary with a 10% Bonus)
df["Bonus"] = df["Salary"] * 1.10

print(df)