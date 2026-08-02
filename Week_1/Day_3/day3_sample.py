# def function_name (parameters)   #it can be empty too if we don't need result or return value
#     #Code Block here
#     return result

#############################

# Function with parameters and return value
# def add_function (a , b):
#     return a+b

# result = add_function(5,41)
# print ("Result : " , result)

#############################

# #Local Scope
# def greet():
#     message = "Hello World"
#     print(message)
    
# greet()
# #print(message)

############################

# #Global Scope
# greeting = "Hi"

# def say_hello():
#     print(greeting + " from inside the function")
    
# say_hello()
# print(greeting + " from outside the function")

#############################

# #Importing an entire Modele
# import math as m
# print(m.sqrt(25))

#Importing an particular Modele
from math import sqrt 
print(sqrt(25))