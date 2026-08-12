# Vary Regularization Parameters:
    # Experiment with different values of α (e.g., 0.1, 0, 10) for Ridge and Lasso Regression
    # Observe how the model's coefficients and performance change
    
# Compare Linear Regression, Ridge Regression, and Lasso Regression

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# Load Dataset
data = pd.read_csv(r"E:\AIBootCamp\Week_4\Day_6\House_price.csv")

print("First 5 Rows")
print(data.head())

# Prepare Data
X = data.drop("Price", axis=1)
y = data["Price"]

# Remove Address (every address is unique)
X = X.drop("Address", axis=1)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Linear Regression
print("\n==============================")
print("LINEAR REGRESSION")
print("==============================")

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred = linear_model.predict(X_test)

print("R² Score :", round(r2_score(y_test, y_pred),4))
print("MAE      :", round(mean_absolute_error(y_test, y_pred),2))
print("MSE      :", round(mean_squared_error(y_test, y_pred),2))
print("RMSE     :", round(mean_squared_error(y_test, y_pred)**0.5,2))

coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": linear_model.coef_
})

print("\nCoefficients")
print(coef_df)

# Ridge Regression
ridge_alphas = [0.1, 1, 10]
for alpha in ridge_alphas:

    print("\n==============================")
    print(f"RIDGE REGRESSION (alpha={alpha})")
    print("==============================")

    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    y_pred = ridge.predict(X_test)

    print("R² Score :", round(r2_score(y_test, y_pred),4))
    print("MAE      :", round(mean_absolute_error(y_test, y_pred),2))
    print("MSE      :", round(mean_squared_error(y_test, y_pred),2))
    print("RMSE     :", round(mean_squared_error(y_test, y_pred)**0.5,2))

    coef_df = pd.DataFrame({
        "Feature": X.columns,
        "Coefficient": ridge.coef_
    })

    print("\nCoefficients")
    print(coef_df)

# =====================================================
# Lasso Regression
# =====================================================

lasso_alphas = [0.1, 1, 10]

for alpha in lasso_alphas:

    print("\n==============================")
    print(f"LASSO REGRESSION (alpha={alpha})")
    print("==============================")

    lasso = Lasso(alpha=alpha, max_iter=10000)
    lasso.fit(X_train, y_train)
    y_pred = lasso.predict(X_test)

    print("R² Score :", round(r2_score(y_test, y_pred),4))
    print("MAE      :", round(mean_absolute_error(y_test, y_pred),2))
    print("MSE      :", round(mean_squared_error(y_test, y_pred),2))
    print("RMSE     :", round(mean_squared_error(y_test, y_pred)**0.5,2))

    coef_df = pd.DataFrame({
        "Feature": X.columns,
        "Coefficient": lasso.coef_
    })

    print("\nCoefficients")
    print(coef_df)
