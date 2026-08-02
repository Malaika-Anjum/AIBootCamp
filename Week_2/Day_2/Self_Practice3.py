#Implement conditional replacement to create a binary mask for values
#above a threshold.

import numpy as np

# Create a random array
arr = np.random.randint(1, 11, size=10)

print("Original Array :", arr)

# Threshold
threshold = 5

# Create binary mask
binary_mask = np.where(arr > threshold, 1, 0)

print("Binary Mask :", binary_mask)