# Problem
# - A disease affects 1% of a population
# - A test is 95% accurate for diseased individuals
# - A test is 90% accurate for non-diseased individuals
# - Find the probability of having the disease given a positive test result

def bayes_theorem(prior, sensitivity, specificity):

    # Law of Total Probability
    # P(B) = P(B|A) * P(A) + P(B|¬A) * P(¬A)

    # Probability of getting a positive test result
    evidence = (sensitivity * prior) + ((1 - specificity) * (1 - prior))

    # Probability of having the disease given a positive test
    # Bayes' Theorem
    # P(A|B) = (P(B|A) * P(A)) / P(B)
    posterior = (sensitivity * prior) / evidence

    return posterior

# Given values
prior = 0.01          # Disease prevalence (1%)
sensitivity = 0.95    # True Positive Rate
specificity = 0.90    # True Negative Rate

# Calculate posterior probability
posterior = bayes_theorem(prior, sensitivity, specificity)

print("Probability of Disease Given Positive Test:", posterior)