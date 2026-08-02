#Write a function to check if a number is even or odd and call it within another function
def is_even(number):
    return number % 2 == 0

def check_number(number):
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Creating another function
def display_result():
    num = int(input("Enter a number: "))
    check_number(num)

# Call the function
display_result()