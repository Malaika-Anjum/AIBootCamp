# Compare Correlation and Regression results for non-linear realtionships

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Create data
x = np.linspace(-10, 10, 100)
y = x**2

# Correlation
corr, p_value = pearsonr(x, y)

# Linear Regression
X = x.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

# Results
print("Correlation Coefficient:", corr)
print("P-value:", p_value)
print("R² Score:", r2_score(y, y_pred))

# Plot
plt.scatter(x, y, label="Actual Data")
plt.plot(x, y_pred, color="red", label="Linear Regression")

plt.title("Linear Regression on a Non-linear Relationship")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()