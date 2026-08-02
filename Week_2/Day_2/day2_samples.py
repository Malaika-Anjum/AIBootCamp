import numpy as np

# #Array Broadcasting
# arr = np.array([1, 2, 3])
# print(arr + 10)

# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# vector = np.array([1, 0, 1])
# print(matrix + vector)

###################################

# #Aggregation Functions
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print("Sum : " , np.sum(arr))
# print("Mean : " , np.mean(arr))
# print("Max : " , np.max(arr))
# print("Min : " , np.min(arr))
# print("Standard Deviation : " , np.std(arr))
# print("Sum along Rows : " , np.sum(arr, axis=1))
# print("Sum along Rows : " , np.sum(arr, axis=0))

####################################

# #Boolean Indexing
# arr = np.array([1, 2, 3, 4, 5, 6])
# evens = arr[arr % 2 == 0]
# print("Evens : " , evens)

# arr[arr>3] = 0
# print("Modified Array : " , arr)

###################################

np.random.seed(62)

random_array = np.random.rand(3,3)   #Uniform distribution of 0s, 1s
print("Random Array : \n" , random_array)

random_integers = np.random.randint(0, 10, size=(2,3))
print("Random Integers : \n" , random_integers)
