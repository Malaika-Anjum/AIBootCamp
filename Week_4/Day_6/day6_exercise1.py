# Calculate Correlation between Features

import pandas as pd

# Load dataset
data = pd.read_csv(r"E:\AIBootCamp\Week_4\Day_6\students_data.csv")

# Select numerical columns
numeric_data = data.select_dtypes(include="number")

# Calculate correlation
correlation = numeric_data.corr()

print("Correlation Matrix:")
print(correlation)