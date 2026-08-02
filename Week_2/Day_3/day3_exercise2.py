#Select Specific Columns and Filter Rows from a Dataset

import pandas as pd

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#Specific Columns
selected_columns = df[["species", "petal_length"]]
print("Selected Columns: \n", selected_columns)

#Filter Rows
filtered_rows = df[(df["petal_length"] > 4) & (df["species"] == "versicolor")]
print("Filtered Rows: \n", filtered_rows)