#Write a program to generate a dataset of random 
#floats and normalize the values between 0 and 1

import numpy as np

# Generate a dataset of random floats
dataset = np.random.rand(5, 5)
print("Original Dataset:\n", dataset)

# Normalize values between 0 and 1
normalized_dataset = (dataset - np.min(dataset)) / (np.max(dataset) - np.min(dataset))
print("Normalized Dataset:\n", normalized_dataset)
