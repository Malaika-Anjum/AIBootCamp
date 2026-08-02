# Create a module for string operations, including functions to 
# reverse a string, count vowels, and check for palindromes.

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

def check_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False