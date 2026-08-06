#Compute the determinant and inverse of a 2x2 matrix using NumPy

import numpy as np

# Create a 2x2 matrix
A = np.array([[4, 7], [2, 6]])

# Compute determinant
det = np.linalg.det(A)

# Compute inverse
inv = np.linalg.inv(A)

print("Matrix A : ")
print(A)

print("\nDeterminant :")
print(det)

print("\nInverse : ")
print(inv)

