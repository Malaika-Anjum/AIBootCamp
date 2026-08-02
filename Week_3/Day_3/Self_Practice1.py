#Use sympy to compute second-order derivatives (Hessian matrix)

import sympy as sp

# Create symbolic variables
x, y = sp.symbols('x y')

# Define the function
f = x**2 + 3*x*y + y**2

print("Function:")
print(f)

# Compute the Hessian matrix
H = sp.hessian(f, (x, y))

print("\nHessian Matrix:")
print(H)