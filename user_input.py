

# Function to get the range of values from the user
def get_vals_from_user():
    start = int(input("Enter the start of the range (inclusive): "))
    end = int(input("Enter the end of the range (inclusive): "))
    if start > end:
        raise ValueError("Start of the range must be less than or equal to the end.")
    return range(start, end + 1)

# Switch function for selecting a distribution
def run_selected_distribution():
    print("Choose a distribution from the following:")
    print("1. Geometric")
    print("2. Binomial")
    print("3. Poisson")
    print("4. Uniform")
    
    choice = input("Enter the number corresponding to your choice (1-4): ").strip()
    distribution_map = {
        "1": "geometric",
        "2": "binomial",
        "3": "poisson",
        "4": "uniform"
    }
    
    if choice not in distribution_map:
        print("Invalid choice. Exiting.")
        return

    dist_name = distribution_map[choice]
    
    # Get values range from the user
    vals = get_vals_from_user()

    # Gather parameters based on the distribution
    if dist_name == "geometric":
        p = float(input("Enter the probability of success (p): "))
        params = [p]
    elif dist_name == "binomial":
        n = int(input("Enter the number of trials (n): "))
        p = float(input("Enter the probability of success (p): "))
        params = [n, p]
    elif dist_name == "poisson":
        lam = float(input("Enter the rate parameter (lambda): "))
        params = [lam]
    elif dist_name == "uniform":
        a = float(input("Enter the lower bound (a): "))
        b = float(input("Enter the upper bound (b): "))
        params = [a, b]
        vals = np.linspace(a, b, 100)

    # Run the chosen distribution
    print(f"Running {dist_name.capitalize()} Distribution...")
    probs = get_probability_distribution(dist_name, params, vals)
    print("Probabilities:", probs)

# Execute the program
if __name__ == "__main__":
    run_selected_distribution()
