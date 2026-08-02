#Convert Categorical data to Numerical using One-Hot Encoding

import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "City": ["New York", "London", "Tokyo", "Paris"]
})

print("Original Dataset:\n", df)

# Convert Categorical data to Numerical using One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=["City"], dtype=int)

print("\nDataset After One-Hot Encoding:\n", df_encoded)