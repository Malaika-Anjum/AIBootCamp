# Compute the expectation and varinace of a weighted die (Biases probabilites)

# Outcomes of the die
x = [1, 2, 3, 4, 5, 6]

# Biased probabilities
p = [0.10, 0.15, 0.20, 0.25, 0.20, 0.10]

# Check that probabilities sum to 1
if sum(p) != 1:
    print("Error: Probabilities must sum to 1")
else:
    # Expected value E(X)
    mean = sum(xi * pi for xi, pi in zip(x, p))

    # E(X^2)
    mean_square = sum((xi ** 2) * pi for xi, pi in zip(x, p))

    # Variance = E(X^2) - [E(X)]^2
    variance = mean_square - mean ** 2

    print("Expected Value =", mean)
    print("Variance =", variance)