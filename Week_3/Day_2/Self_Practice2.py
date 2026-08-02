#Use SVD to reduce the dimensionality of a dataset

import numpy as np

# Original dataset (5 samples, 3 features)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [2, 3, 4],
              [5, 6, 7]])

print("Original Dataset:")
print(A)

# Perform Singular Value Decomposition
U, S, Vt = np.linalg.svd(A, full_matrices=False)

# Number of dimensions to keep
k = 2

# Keep only the first k singular values and vectors
U_k = U[:, :k]
S_k = np.diag(S[:k])
Vt_k = Vt[:k, :]

# Reduced dataset
A_reduced = U_k @ S_k

print("\nReduced Dataset:")
print(A_reduced)