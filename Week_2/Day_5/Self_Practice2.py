#Use pivot_table to Calculate Total Sales per Region and per Year

import pandas as pd

# Create a sample sales dataset
data = {
    "Region": ["North", "South", "North", "East", "South", "East", "North", "South"],
    "Year": [2023, 2023, 2024, 2023, 2024, 2024, 2023, 2024],
    "Sales": [50000, 30000, 60000, 45000, 35000, 55000, 40000, 38000]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Create a pivot table
pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Year",
    aggfunc="sum"
)

print("\nTotal Sales per Region and Year:\n")
print(pivot)