#Create a block diagonal matrix using NumPy

import numpy as np

# Define the blocks
A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# Create a block diagonal matrix
block_diag = np.block([[A, np.zeros((2, 2), dtype=int)],[np.zeros((2, 2), dtype=int), B]])

print("Block Diagonal Matrix :\n", block_diag)

#####################

# #Built-In 

# from scipy.linalg import block_diag
# import numpy as np

# A = np.array([[1, 2], [3, 4]])

# B = np.array([[5, 6], [7, 8]])

# result = block_diag(A, B)

# print("Result : \n", result)