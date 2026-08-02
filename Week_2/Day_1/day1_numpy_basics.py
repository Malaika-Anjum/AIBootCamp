import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])
# #print(arr)

# ones = np.ones((3,3))
# #print(ones)

# range_array = np.arange(1, 10, 2)  
# #it returns an evenly spaced values within a given intervals i.e. gap between numbers
# #print(range_array)

# linspace_array = np.linspace(0, 1, 5)  
# #creates a specified number of evenly spaced values between a start and an end point i.e. number of values.  
# #print (linspace_array)


##############################

# arr = np.array([1, 2, 3, 4, 5, 6])
# reshaped = arr.reshape((2,3))
# print(reshaped)

# arr = np.array([1,2,3])
# expanded = arr[:, np.newaxis]
# print(expanded)

############################

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a + b)
# print(a*b)
# print(a/b)

# arr = np.array([4, 9, 16])
# print(np.sqrt(arr))
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))

###############################

arr = np.array([10, 20, 30, 40, 50, 60])

# print(arr[2])

# print(arr[-1])

# print(arr[1:4])

# print(arr[3:])

reshaped = arr.reshape(2,3)
print(reshaped)

