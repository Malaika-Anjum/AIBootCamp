# Simulate random variables from custom distributions

import numpy as np

# Possible values
values = [1, 2, 3, 4, 5, 6]

# Custom probabilities
probabilities = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]

# Simulate 1000 random values
random_values = np.random.choice(
    values,
    size=1000,
    p=probabilities
)

# Show first 20 results
print(random_values[:20])

# Count how often each value occurred
for value in values:
    print(value, ":", np.sum(random_values == value))