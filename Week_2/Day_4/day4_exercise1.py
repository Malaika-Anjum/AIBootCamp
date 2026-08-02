#Clean a Datasets by Handling Missing Values and Renaming Columns
import pandas as pd
import numpy as np

# Sample dataset with missing values
data = {
    "Name": ["Alice", np.nan ,  "Bob", "Charlie", "David"],
    "Age": [20, 25, 30, None, 35],
    "Salary": [55000, 50000, 60000, 70000, None]
}

df = pd.DataFrame(data)

print("Original Dataset : \n", df)

# Handle missing values
df = df.dropna(subset=["Name"])
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].interpolate()


# Rename columns
df = df.rename(columns={"Name": "Full Name", "Age": "Years Old"})

print(df)