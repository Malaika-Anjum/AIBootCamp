# Perform Singular Value Decomposition

import numpy as np

A = np.array([[3, 1, 1], [-1, 3, 1], [1, 1, 3]])
U, S, Vt = np.linalg.svd(A)

print("U:\n", U)
print("Singular Values:\n", S)
print("V Transpose:\n", Vt)

# Reconstruct.... A=UΣVT
Sigma = np.zeros((3, 3))
np.fill_diagonal(Sigma, S)
reconstructed = U @ Sigma @ Vt
print("Reconstructed Matrix \n", reconstructed)