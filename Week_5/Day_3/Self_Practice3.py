# Feature importance with Lasso :
    # Use Lasso Regression to perform feature selection and identify the most relevant predictors

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


# Load Dataset
data = pd.read_csv(r"E:\AIBootCamp\Week_4\Day_6\House_price.csv")


# Prepare Features and Target
X = data.drop(["Price", "Address"], axis=1)
y = data["Price"]


# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train Lasso Regression and Make Predictions
lasso = Lasso(alpha=10, max_iter=10000)
lasso.fit(X_train, y_train)
y_pred = lasso.predict(X_test)


# Evaluate Model
print("=" * 40)
print("LASSO REGRESSION RESULTS")
print("=" * 40)

print("R² Score :", round(r2_score(y_test, y_pred), 4))
print("MAE      :", round(mean_absolute_error(y_test, y_pred), 2))
print("MSE      :", round(mean_squared_error(y_test, y_pred), 2))
print("RMSE     :", round(mean_squared_error(y_test, y_pred) ** 0.5, 2))


# Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": lasso.coef_
})

importance["Absolute Coefficient"] = importance["Coefficient"].abs()

importance = importance.sort_values(
    by="Absolute Coefficient",
    ascending=False
)

print("\nFeature Importance")
print(importance)


# Selected Features
selected_features = importance[importance["Coefficient"] != 0]

print("\nSelected Features (Coefficient ≠ 0)")
print(selected_features[["Feature", "Coefficient"]])


# Removed Features
removed_features = importance[importance["Coefficient"] == 0]

print("\nRemoved Features (Coefficient = 0)")
print(removed_features[["Feature", "Coefficient"]])