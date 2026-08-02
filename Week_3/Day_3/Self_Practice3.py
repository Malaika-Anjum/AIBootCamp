#Visualize the Gradient Descent Process on a Quadratic Function

import numpy as np
import matplotlib.pyplot as plt

# Define the quadratic function
def function(x):
    return x**2

# Define the gradient (derivative)
def gradient(x):
    return 2 * x

# Define Gradient Descent function
def gradient_descent(x, learning_rate, iterations):
    x_history = [x]
    y_history = [function(x)]

    for _ in range(iterations):
        grad = gradient(x)
        x -= learning_rate * grad

        x_history.append(x)
        y_history.append(function(x))

    return x_history, y_history

# Assign values for x, learning_rate, and iterations
x = 8
learning_rate = 0.1
iterations = 20

# Perform Gradient Descent
x_history, y_history = gradient_descent(x, learning_rate, iterations)

# Create values for plotting the quadratic function
x_values = np.linspace(-10, 10, 200)
y_values = function(x_values)

# Plot the quadratic function
plt.plot(x_values, y_values, label="f(x) = x²")

# Plot the Gradient Descent steps
plt.scatter(x_history, y_history, color="red", label="Gradient Descent Steps")
plt.plot(x_history, y_history)

# Labels and title
plt.title("Gradient Descent on a Quadratic Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Display the graph
plt.show()