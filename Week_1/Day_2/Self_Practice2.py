#Find a largest number in a list using a for loop

numbers = [3, 5, 2, 8, 1, 4]
largest = numbers[0]  # Assume the first number is the largest
for number in numbers:
    if number > largest:
        largest = number  # Update largest if a larger number is found

print("The largest number is:", largest)

######################################

#Using a function to find the largest number in a list

# numbers = [3, 5, 2, 8, 1, 4]
# def find_largest_number(numbers):
#     largest = numbers[0]  # Assume the first number is the largest
#     for number in numbers:
#         if number > largest:
#             largest = number  # Update largest if a larger number is found
#     return largest

# # Call the function and print the result
# largest_number = find_largest_number(numbers)
# print("The largest number is:", largest_number)