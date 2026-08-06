# Create and Visualize a Multinomial Distribution for Multi-Class Data

import numpy as np
import matplotlib.pyplot as plt

# Define class labels
classes = ["Class A", "Class B", "Class C"]

# Probability of each class
probabilities = [0.5, 0.3, 0.2]

# Number of observations
n = 100

# Generate multinomial distribution
Sample = np.random.multinomial(n, probabilities)

# Display generated counts
print("Class Counts:", Sample)

# Visualize the distribution
plt.bar(classes, Sample, color=["skyblue", "orange", "green"])

plt.title("Multinomial Distribution")
plt.xlabel("Classes")
plt.ylabel("Number of Samples")

plt.show()