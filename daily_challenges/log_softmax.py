# ==============================================================================
# Daily challenge 39: log soft-max
# https://www.deep-ml.com/problems/39
# ==============================================================================

"""
In machine learning and statistics, the softmax function is a generalization of
the logistic function that converts a vector of scores into probabilities.
The log-softmax function is the logarithm of the softmax function, and it is often
used for numerical stability when computing the softmax of large numbers.

Given a 1D numpy array of scores, implement a Python function to compute the
log-softmax of the array.
"""

import numpy as np

# setting precision for np arr values
np.set_printoptions(precision=4)


def log_softmax(scores: list) -> np.ndarray:
    # convert scores into numpy array
    scores = np.array(scores)

    # incorporating the shift in scores arr by subtracting max value
    scores_max_diff = scores - scores.max()

    # log part of log soft-max expression
    log_vals = np.log(np.sum(np.exp(scores_max_diff)))

    log_softmax = scores_max_diff - log_vals

    return log_softmax


def main():
    A = np.array([1, 2, 3])
    print(log_softmax(A))


if __name__ == "__main__":
    main()
