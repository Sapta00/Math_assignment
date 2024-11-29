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
