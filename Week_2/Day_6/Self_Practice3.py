#Combine multiple plots in a single figure using Matplotlib's subplot.

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]
y3 = [5, 7, 6, 8, 7]
y4 = [10, 8, 6, 4, 2]

# Create a figure
plt.figure(figsize=(10, 8))

# Plot 1 - Line Plot
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("Line Plot")

# Plot 2 - Bar Plot
plt.subplot(2, 2, 2)
plt.bar(x, y2)
plt.title("Bar Plot")

# Plot 3 - Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(x, y3)
plt.title("Scatter Plot")

# Plot 4 - Histogram
plt.subplot(2, 2, 4)
plt.hist(y4, bins=5)
plt.title("Histogram")

# Adjust spacing
plt.tight_layout()

# Show all plots
plt.show()