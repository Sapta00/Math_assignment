# Main function
def get_probability_distribution(dist_name, dist_params, vals):
    if dist_name.lower() not in ["geometric", "binomial", "poisson", "uniform"]:
        return "Error: Invalid distribution name."

    vals = np.array(vals)
    if np.any(vals < 0):
        vals = vals[vals >= 0]
        if len(vals) == 0:
            return "Error: All values in 'vals' are negative. No valid values to process."
        print("Warning: Negative values were removed from 'vals'.")

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

    # Plot the distribution
    plt.bar(vals, probs, color="blue", alpha=0.7, label=dist_name.capitalize())
    plt.xlabel("Values")
    plt.ylabel("Probability")
    plt.title(f"{dist_name.capitalize()} Distribution")
    plt.legend()
    plt.show()
    
    return probs