#Create a DataFrame from a dictionary and add a new calculated column.
#Save filtered data to a new CSV file

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

filtered_rows = df[(df["Age"] > 28) & (df["Salary"] > 55000)]
print("Filtered Rows: \n", filtered_rows)

filtered_rows.to_csv("filtered_data.csv", index=False)