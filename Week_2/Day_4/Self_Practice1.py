#Drop columns with more than 50% missing values

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Name" : ["Alice", "Bob", "Charlie", np.nan, "David"],
#     "Age" : [25, np.nan, 35, np.nan, 45],
#     "City" : [np.nan, "London", np.nan, "Paris", np.nan]
# })

# print("Original Dataset : \n", df)

# threshold = len(df) * 0.5
# df_cleaned = df.dropna(thresh=threshold, axis=1)

# print ("\nDataset After Dropping Columns with More Than 50% Missing Values : \n ", df_cleaned)

#But better practice is :

import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", np.nan, "David"],
    "Age": [25, np.nan, 35, np.nan, 45],
    "City": [np.nan, "London", np.nan, "Paris", np.nan]
})

print("Original Dataset:\n")
print(df)

# Calculate percentage of missing values in each column
missing_percentage = df.isnull().mean() * 100

print("\nMissing Percentage:\n")
print(missing_percentage)

# Keep only columns with 50% or less missing values
df = df.loc[:, missing_percentage <= 50]

print("\nDataset After Dropping Columns with More Than 50% Missing Values:\n")
print(df)
