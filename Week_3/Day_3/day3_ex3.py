#Implement Gradient Descent for Linear Regression

import numpy as np

#Define a Gradient Descent function
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        gradients = (1/m) * X.T.dot(errors)
        # gradients = (1/m) * X.T @ (X @ theta - y)     # or simplified method
        theta -= learning_rate * gradients
    return theta

#Assigning values for X, y, theta, learning_rate, and iterations
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])  # Add a bias term (intercept)
y = np.array([1, 2, 3, 4])  # Target
theta = np.array([0.1, 0.1])  # Initialize parameters
learning_rate = 0.01
iterations = 1000

#Perform Gradient Descent
theta_final = gradient_descent(X, y, theta, learning_rate, iterations)
print("Final parameters (theta): ", theta_final)
