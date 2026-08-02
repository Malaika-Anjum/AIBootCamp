#Create a 4*4 matrix and calculate the sum of its rows and columns
import numpy as np

# Create a 4x4 matrix with random integers
matrix = np.random.randint(1, 10, size=(4, 4))
print("Original Matrix : \n", matrix)

# Calculate the sum of rows
row_sums = np.sum(matrix, axis=1)
print("Sum of Rows : \n", row_sums)

# Calculate the sum of columns
column_sums = np.sum(matrix, axis=0)
print("Sum of Columns : \n", column_sums)