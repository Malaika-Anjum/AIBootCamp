#Generate a random array and find the minium and maximum values

import numpy as np

arr = np.random.randint(1, 10, size=10)
print ("Original Array is : ", arr)

min_value = np.min(arr)
max_value = np.max(arr)

print("Minimum Value is : ", min_value)
print("Maximum Value is : ", max_value)