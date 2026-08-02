n = int (input ("Enter a Number : "))
factorial = 1

if n == 0 or n == 1:
    factorial = 1
else:
    for i in range(1, n + 1):
        factorial = factorial * i

print(f"The factorial of {n} is {factorial}")
