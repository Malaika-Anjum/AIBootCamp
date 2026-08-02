#Create a 3D random array and compute statistics specific axes

import numpy as np


# Create a 3D random array (2 × 3 × 4)
arr = np.random.randint(1, 11, size=(2, 3, 4))

print("Original 3D Array:\n", arr)

# Mean
print("\nMean along axis 0:\n", np.mean(arr, axis=0))
print("\nMean along axis 1:\n", np.mean(arr, axis=1))
print("\nMean along axis 2:\n", np.mean(arr, axis=2))

# Minimum
print("\nMinimum along axis 0:\n", np.min(arr, axis=0))
print("\nMinimum along axis 1:\n", np.min(arr, axis=1))
print("\nMinimum along axis 2:\n", np.min(arr, axis=2))

# Maximum
print("\nMaximum along axis 0:\n", np.max(arr, axis=0))
print("\nMaximum along axis 1:\n", np.max(arr, axis=1))
print("\nMaximum along axis 2:\n", np.max(arr, axis=2))

