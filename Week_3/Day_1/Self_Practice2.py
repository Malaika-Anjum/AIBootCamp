#Verify properties of matrix multiplication

import numpy as np

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

C = np.array([[2, 0], [1, 2]])

# Associative
print("Associative:", np.array_equal((A @ B) @ C, A @ (B @ C)))

# Distributive
print("Distributive:", np.array_equal(A @ (B + C), (A @ B) + (A @ C)))

# Identity
I = np.eye(2)
print("Left Identity:", np.array_equal(I @ A, A))
print("Right Identity:", np.array_equal(A @ I, A))

# Commutative
print("Commutative:", np.array_equal(A @ B, B @ A))