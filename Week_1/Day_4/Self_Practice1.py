#Write a program to reverse a list and remove duplicates using a set
numbers = [1, 2, 3, 2, 4, 1, 5]

print("Original List:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed List:", numbers)

# Remove duplicates using a set
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)