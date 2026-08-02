#Create a histogram with multiple datasets overlaid

import matplotlib.pyplot as plt

# Dataset 1
math_scores = [65, 70, 75, 80, 85, 90, 95, 88, 76, 84]

# Dataset 2
science_scores = [60, 68, 72, 78, 82, 85, 89, 91, 94, 97]

# Create overlaid histograms
plt.hist(math_scores, bins=5, alpha=0.6, label="Math Scores")
plt.hist(science_scores, bins=5, alpha=0.6, label="Science Scores")

# Add labels and title
plt.title("Math vs Science Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Number of Students")

# Show legend
plt.legend()

# Display the graph
plt.show()