# Simulate flipping a coin 10000 times and calculate probabilties of heads/tails

import numpy as np

# Simulate flipping a coin 10000 times
flips = np.random.choice(["Heads", "Tails"], size=10000)

# Count heads and tails
heads = np.sum(flips == "Heads")
tails = np.sum(flips == "Tails")

# Calculate probabilities
prob_heads = heads / 10000
prob_tails = tails / 10000

print("Number of Heads:", heads)
print("Number of Tails:", tails)

print("Probability of Heads:", prob_heads)
print("Probability of Tails:", prob_tails)