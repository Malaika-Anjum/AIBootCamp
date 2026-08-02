# # # [expression for item in iterable if condition]

# # #Create a list of squares
# # squares = [x**2 for x in range(10)]
# # #print(squares)

# # # Filter Even Numbers
# # evens = [x for x in range(10) if x % 2 == 0]
# # #print(evens) 

# # # Lambda Arguments : Expression

# # add = lambda x, y: x + y
# # print (add(3,5))

# ##################

# numbers = [1,2,3,4]

# # squares = map(lambda x: x**2, numbers)
# # print(list(squares))

# # evenlist = filter(lambda x: x % 2 == 0 , numbers)
# # print(list(evenlist))

# from functools import reduce

# product = reduce(lambda x,y: x * y , numbers)
# print(product)

############################

# import os

# print (os.getcwd())
# os.mkdir("test_dir")
# #os.rmdir("test_dir")

# os.remove("file.txt")

############################

# import sys

# print(sys.argv)
# print(sys.version)
