#Load a Local Excel File and Explore its Structure

import pandas as pd

df = pd.read_excel("Tokyo-Olympic-Sample-Data.xlsx", header=0)

#Exploring Datasheet

print("First 5 Columns : \n", df.head())

print("Last 5 Columns : \n", df.tail())

print("Information of Datasheet : \n", df.info())

print("Statistical Summary of Datasheet : \n", df.describe())

selected_columns=df[["Team","Rank by Total"]]
print(selected_columns)

filtered_rows= df[(df["Gold"]>10) & (df["Total"]>10)]
print("Filtered Rows : \n", filtered_rows)