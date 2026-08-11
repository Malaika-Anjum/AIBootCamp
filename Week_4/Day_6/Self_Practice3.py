# Use real-world datasets (e.g., Housing Prices) for Regression Analysis

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# Load the dataset
data = pd.read_csv(r"E:\AIBootCamp\Week_4\Day_6\House_price.csv")

# Display first five rows
print("First 5 Rows:")
print(data.head())

# Features and target
X = data.drop(["Price", "Address"], axis=1)
y = data["Price"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("\nModel Evaluation")
print("-" * 30)
print("R² Score:", round(r2_score(y_test, y_pred), 4))
print("Mean Absolute Error:", round(mean_absolute_error(y_test, y_pred), 2))
print("Mean Squared Error:", round(mean_squared_error(y_test, y_pred), 2))
print("Root Mean Squared Error:", round(mean_squared_error(y_test, y_pred) ** 0.5, 2))

# Display coefficients
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("\nFeature Coefficients")
print(coefficients.sort_values(by="Coefficient", ascending=False))