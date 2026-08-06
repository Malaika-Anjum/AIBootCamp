# Implement Mini-Batch SGD and Compare it with Vanilla SGD

import numpy as np

# Dataset
X = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 4, 6, 8, 10, 12])

# Initialize parameter
theta = 0.0

learning_rate = 0.01
epochs = 10
batch_size = 2
m=len(X)

# ------------------ Vanilla SGD ------------------

theta_sgd = theta

for epoch in range(epochs):
    for i in range(m):

        prediction = theta_sgd * X[i]
        error = prediction - y[i]
        gradient = error * X[i]

        theta_sgd -= learning_rate * gradient

print("Theta using Vanilla SGD : ", theta_sgd)

# ------------------ Mini-Batch SGD ------------------

theta_batch = theta

for epoch in range(epochs):

    for i in range(0, m, batch_size):

        X_batch = X[i:i + batch_size]
        y_batch = y[i:i + batch_size]

        predictions = theta_batch * X_batch
        errors = predictions - y_batch

        gradient = np.mean(errors * X_batch)

        theta_batch = theta_batch - learning_rate * gradient

print("Theta using Mini-Batch SGD : ", theta_batch)