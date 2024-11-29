import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Geometric distribution
def geometric(p, vals):
    if not (0 < p <= 1):
        raise ValueError("Parameter 'p' for geometric distribution must be in the range (0, 1].")
    return stats.geom.pmf(vals, p)

# Binomial distribution
def binomial(n, p, vals):
    if n <= 0 or not isinstance(n, int):
        raise ValueError("Parameter 'n' for binomial distribution must be a positive integer.")
    if not (0 <= p <= 1):
        raise ValueError("Parameter 'p' for binomial distribution must be in the range [0, 1].")
    return stats.binom.pmf(vals, n, p)

# Poisson distribution
def poisson(lam, vals):
    if lam <= 0:
        raise ValueError("Parameter 'lam' (lambda) for Poisson distribution must be a positive number.")
    return stats.poisson.pmf(vals, lam)

# Uniform distribution
def uniform(a, b, vals):
    if a >= b:
        raise ValueError("Parameter 'a' must be less than 'b' for uniform distribution.")
    return stats.uniform.pdf(vals, loc=a, scale=b - a)

# Main function
def get_probability_distribution(dist_name, dist_params, vals):
    if dist_name.lower() not in ["geometric", "binomial", "poisson", "uniform"]:
        return "Error: Invalid distribution name."
    if dist_name.lower() == "geometric":
        if len(dist_params) != 1:
            return "Error: Geometric distribution requires one parameter (p)."
        p = dist_params[0]
        probs = geometric(p, vals)
    elif dist_name.lower() == "binomial":
        if len(dist_params) != 2:
            return "Error: Binomial distribution requires two parameters (n, p)."
        n, p = dist_params
        probs = binomial(n, p, vals)
    elif dist_name.lower() == "poisson":
        if len(dist_params) != 1:
            return "Error: Poisson distribution requires one parameter (lam)."
        lam = dist_params[0]
        probs = poisson(lam, vals)
    elif dist_name.lower() == "uniform":
        if len(dist_params) != 2:
            return "Error: Uniform distribution requires two parameters (a, b)."
        a, b = dist_params
        probs = uniform(a, b, vals)
    vals = np.array(vals)
    if np.any(vals < 0):
        vals = vals[vals >= 0]
        if len(vals) == 0:
            return "Error: All values in 'vals' are negative. No valid values to process."
        print("Warning: Negative values were removed from 'vals'.")

    # Plot the distribution
    plt.bar(vals, probs, color="blue", alpha=0.7, label=dist_name.capitalize())
    plt.xlabel("Values")
    plt.ylabel("Probability")
    plt.title(f"{dist_name.capitalize()} Distribution")
    plt.legend()
    plt.show()
    
    return probs

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
