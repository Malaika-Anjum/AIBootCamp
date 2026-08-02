#Write a program to normalize an array (scale values between 0 and 1)

import numpy as np

arr = np.random.randint(1, 11, size=10)
print("Original Matrix : " , arr)

# Normalize the array
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print("Normalized Matrix : " , normalized_arr)