# Visualize the loss function's surface and the SGD optimization path

import numpy as np
import matplotlib.pyplot as plt

# Define the loss function
def loss(x, y):
    return x**2 + y**2

# Define the gradients
def gradient(x, y):
    return 2 * x, 2 * y

# Assign values
learning_rate = 0.1
iterations = 20
x, y = 4, 4      # Random starting point

# Store optimization path
x_history = [x]
y_history = [y]

# Perform Stochastic Gradient Descent (SGD)
for _ in range(iterations):
    grad_x, grad_y = gradient(x, y)

    # Update x and y
    x = x - learning_rate * grad_x
    y = y - learning_rate * grad_y

    # We record the history of x and y for plotting
    x_history.append(x)
    y_history.append(y)

# Create values for plotting the loss surface
x_values = np.linspace(-5, 5, 100)
y_values = np.linspace(-5, 5, 100)

# Meshgrid for contour plot in (x, y)
X, Y = np.meshgrid(x_values, y_values)
Z = loss(X, Y)

# Plot the contour (loss surface)
plt.contour(X, Y, Z, levels=20)

# Plot the SGD optimization path
plt.plot(x_history, y_history, marker='o', color='red', label='SGD Path')

# Labels and title
plt.title("Loss Surface and SGD Optimization Path")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# Display the graph
plt.show()