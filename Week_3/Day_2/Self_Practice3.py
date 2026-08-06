# Verify the property of eigenvalues: det (A - λI) = 0

import numpy as np

# Create a matrix
A = np.array([[3, 1],
              [1, 3]])

print("Matrix A:")
print(A)

# Compute eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

# Verify det(A - λI) = 0
for lam in eigenvalues:
    result = np.linalg.det(A - lam * np.eye(A.shape[0]))
    print(f"\nFor λ = {lam:.4f}")       #: tell Python howthis value to be displayed and .4 => display 4 digits after the decimal point.
    print("det(A - λI) =", result)