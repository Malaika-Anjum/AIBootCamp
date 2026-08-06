# Implement gradient descent with multiple learning rates and compare convergence speeds

import numpy as np

# Define Gradient Descent function
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    cost_history = []

    for _ in range(iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        gradients = (1/m) * X.T.dot(errors)

        # Update parameters
        theta -= learning_rate * gradients

        # Calculate Cost Function (Mean Squared Error)
        cost = (1/(2*m)) * np.sum(errors**2)
        cost_history.append(cost)

    return theta, cost_history

# Assign values for X, y, theta, and iterations
X = np.array([[1, 1],
              [1, 2],
              [1, 3],
              [1, 4]])

y = np.array([1, 2, 3, 4])

iterations = 100

# Different learning rates
learning_rates = [0.001, 0.01, 0.1]

# Perform Gradient Descent for each learning rate
for lr in learning_rates:

    theta = np.array([0.1, 0.1])   # Reset theta each time

    theta_final, cost_history = gradient_descent(
        X, y, theta, lr, iterations
    )

    print(f"\nLearning Rate: {lr}")
    print("Final Parameters (theta):", theta_final)
    print("Final Cost:", cost_history[-1])
    

# A smaller final cost means the algorithm converged better.

# A very small learning rate (e.g., 0.001) usually converges slowly.

# A moderate learning rate (e.g., 0.01) often converges efficiently.

# A larger learning rate (e.g., 0.1) may converge faster, but if it's 
# too large on other datasets, it can overshoot the minimum or fail to 
# converge.