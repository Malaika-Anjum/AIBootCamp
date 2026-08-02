#Create a 3*3 Matrix and Perform Operations

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix : \n", matrix)

#Transpose
transpose = matrix.T
print("Transpose : \n", transpose)

another_matrix = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Addition :\n", matrix + another_matrix)
print("Multiplications :\n", matrix * another_matrix)