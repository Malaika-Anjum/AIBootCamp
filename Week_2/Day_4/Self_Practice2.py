#Merge three datasets and analyze relationship between them

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "City": ["New York", "London", "Tokyo", "Paris"]
})

df3 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Salary": [70000, 80000, 90000, 100000]
})

# Merge df1 and df2
merged_df = pd.merge(df1, df2, on="ID")

# Merge the result with df3
merged_df = pd.merge(merged_df, df3, on="ID")

print("Merged Dataset:\n")
print(merged_df)

print("Average Salary:", merged_df["Salary"].mean())
print("Oldest Person:", merged_df.loc[merged_df["Age"].idxmax()])