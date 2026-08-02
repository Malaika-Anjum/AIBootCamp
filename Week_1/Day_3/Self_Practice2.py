#Importing String Operations here

import string_operations as so

text = input("Enter a string: ")

print("Reversed String:", so.reverse_string(text))
print("Number of Vowels:", so.count_vowels(text))

if so.check_palindrome(text):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")