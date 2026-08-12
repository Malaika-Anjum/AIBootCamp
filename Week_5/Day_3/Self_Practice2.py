# Use Multiple Features :
    # Include more features (e.g., HouseAge, AveRooms) and observe the impact on model performance.
    
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# Load dataset
data = pd.read_csv(r"E:\AIBootCamp\Week_4\Day_6\House_price.csv")

# Target
y = data["Price"]

# Model 1 : Using Only Two Features
print("="*50)
print("MODEL 1 : TWO FEATURES")
print("="*50)

X1 = data[["Avg. Area Income", "House Age"]]

X_train, X_test, y_train, y_test = train_test_split(
    X1,
    y,
    test_size=0.2,
    random_state=42
)

model1 = LinearRegression()
model1.fit(X_train, y_train)

y_pred = model1.predict(X_test)

print("Features Used:")
print(list(X1.columns))

print("\nR² Score :", round(r2_score(y_test, y_pred),4))
print("MAE      :", round(mean_absolute_error(y_test, y_pred),2))
print("MSE      :", round(mean_squared_error(y_test, y_pred),2))
print("RMSE     :", round(mean_squared_error(y_test, y_pred,)**0.5,2))

# Model 2 : Using All Numerical Features
print("\n")
print("="*50)
print("MODEL 2 : ALL NUMERICAL FEATURES")
print("="*50)

X2 = data.drop(["Price", "Address"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X2,
    y,
    test_size=0.2,
    random_state=42
)

model2 = LinearRegression()
model2.fit(X_train, y_train)

y_pred = model2.predict(X_test)

print("Features Used:")
print(list(X2.columns))

print("\nR² Score :", round(r2_score(y_test, y_pred),4))
print("MAE      :", round(mean_absolute_error(y_test, y_pred),2))
print("MSE      :", round(mean_squared_error(y_test, y_pred),2))
print("RMSE     :", round(mean_squared_error(y_test, y_pred)**0.5,2))


# Coefficients
coef = pd.DataFrame({
    "Feature": X2.columns,
    "Coefficient": model2.coef_
})

print("\nFeature Coefficients")
print(coef)