# Use Adam Optimizer for a More Complex Dataset

import numpy as np

# Dataset
X = np.array([1, 2, 3, 4, 5, 6])
y = np.array([3, 5, 7, 9, 11, 13])

# Initialize parameters
theta = 0.0

learning_rate = 0.1
iterations = 100

# Adam parameters
beta1 = 0.9
beta2 = 0.999
epsilon = 1e-8

# Initialize first and second moments
m = 0
v = 0

# Perform Adam Optimization
for t in range(1, iterations + 1):

    # Predictions
    predictions = theta * X

    # Errors
    errors = predictions - y

    # Gradient
    gradient = np.mean(errors * X)

    # Update first moment estimate
    m = beta1 * m + (1 - beta1) * gradient

    # Update second moment estimate
    v = beta2 * v + (1 - beta2) * (gradient ** 2)

    # Bias correction
    m_hat = m / (1 - beta1 ** t)
    v_hat = v / (1 - beta2 ** t)

    # Update parameter
    theta = theta - learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)

print("Final Theta:", theta)