# Example usage for Binomial distribution
try:
    dist_name = "Binomial"
    dist_params = (10, 0.5)  # Use a tuple for parameters
    vals = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    probability = get_probability_distribution(dist_name, dist_params, vals)
    print("Probabilities:", probability)
except Exception as e:
    print("Error while processing the distribution:", e)


# Example usage for Geometric distribution
try:
    dist_name = "Geometric"
    dist_params = (0.5,)  # p = 0.5
    vals = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    probability = get_probability_distribution(dist_name, dist_params, vals)
    print("Geometric Probabilities:", probability)
except Exception as e:
    print("Error while processing the distribution:", e)


# Example usage for Uniform distribution
try:
    dist_name = "Uniform"
    dist_params = (0, 10)  # a = 0, b = 10
    vals = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    probability = get_probability_distribution(dist_name, dist_params, vals)
    print("Uniform Probabilities:", probability)
except Exception as e:
    print("Error while processing the distribution:", e)

# Example usage for Poisson distribution
try:
    dist_name = "Poisson"
    dist_params = (5,)  # lambda = 5
    vals = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    probability = get_probability_distribution(dist_name, dist_params, vals)
    print("Poisson Probabilities:", probability)
except Exception as e:
    print("Error while processing the distribution:", e)