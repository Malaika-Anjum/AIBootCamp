#Create a Dataset of Sales Data and Group it by Region or Product Category

import pandas as pd

# Create a Sales Dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
    "Region": ["North", "South", "North", "East", "South", "East"],
    "Sales": [50000, 30000, 20000, 45000, 35000, 25000]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Group by Region
region_sales = df.groupby("Region")["Sales"].sum()

print("\nTotal Sales by Region:\n")
print(region_sales)

# Group by Product
product_sales = df.groupby("Product")["Sales"].sum()

print("\nTotal Sales by Product:\n")
print(product_sales)