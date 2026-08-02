#Compute eigenvalues and eigenvectors for larger matrices

import numpy as np

# Create a 3x3 matrix
A = np.array([[4, 2, 1],
              [2, 5, 3],
              [1, 3, 6]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix A:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)