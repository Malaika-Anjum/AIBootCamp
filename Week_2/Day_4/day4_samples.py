import pandas as pd

data1 = {
    "ID": [1, 7, 4],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

data2 = {
    "ID": [1, 7, 4],
    "Performance": ["66%", "87%", "75%"]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# combined = pd.concat([df1, df2], axis=0)
# combined = pd.concat([df1, df2], axis=1)
#print(combined)

# merged = pd.merge(df1, df2, on="ID")
# merged = pd.merge(df1, df2, how="left", on="ID")
merged = pd.merge(df1, df2, how="inner", on="ID")
print("Merged Dataset : \n", merged)


joined = df1.join(df2, how="inner", lsuffix="_df1", rsuffix="_df2")
#print(joined)