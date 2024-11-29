{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01cbeb27-5162-4493-b9dd-e131bd32835f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example usage for Geometric distribution\n",
    "try:\n",
    "    dist_name = \"Geometric\"\n",
    "    dist_params = (0.5,)  # p = 0.5\n",
    "    vals = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "    probability = get_probability_distribution(dist_name, dist_params, vals)\n",
    "    print(\"Geometric Probabilities:\", probability)\n",
    "except Exception as e:\n",
    "    print(\"Error while processing the distribution:\", e)\n",
    "\n",
    "\n",
    "# Example usage for Uniform distribution\n",
    "try:\n",
    "    dist_name = \"Uniform\"\n",
    "    dist_params = (0, 10)  # a = 0, b = 10\n",
    "    vals = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "    probability = get_probability_distribution(dist_name, dist_params, vals)\n",
    "    print(\"Uniform Probabilities:\", probability)\n",
    "except Exception as e:\n",
    "    print(\"Error while processing the distribution:\", e)\n",
    "    # Example usage for Poisson distribution\n",
    "try:\n",
    "    dist_name = \"Poisson\"\n",
    "    dist_params = (5)  # lambda = 5\n",
    "    vals = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "    probability = get_probability_distribution(dist_name, dist_params, vals)\n",
    "    print(\"Poisson Probabilities:\", probability)\n",
    "except Exception as e:\n",
    "    print(\"Error while processing the distribution:\", e)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
