# ------------------------------------------------------------------------------
# covariance matrix
# https://www.deep-ml.com/problem/Calculate%20Covariance%20Matrix
# ------------------------------------------------------------------------------

import sys
import time


def calculate_covariance(v: list[int | float], w: list[int | float]):
    """fucntion to calculate covariance of two vectors

    Args:
        v (list[int  |  float]): first vector
        w (list[int  |  float]): second vector

    Returns:
        int | float: covariance of vector v and vector w
    """

    # lenth of both vectors must be same for calculation of covariance
    try:
        assert len(v) == len(w)
    except AssertionError:
        sys.exit("Both vectors must be of same length")

    # average of vectors
    mu_v, mu_w = sum(v) / len(v), sum(w) / len(w)

    centered_v = [i - mu_v for i in v]
    centered_w = [i - mu_w for i in w]

    dot = sum([i * j for i, j in zip(centered_v, centered_w)])

    return f"{dot / len(v):.2f}"


def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    covariance_matrix = 0
    return covariance_matrix


if __name__ == "__main__":
    # vectors = [[1, 2, 3], [4, 5, 6]]

    time_now = time.perf_counter()
    for i in range(10_000_000):
        v, w = [1, 2, 3], [4, 5, 6]
    time_inline = time.perf_counter() - time_now
    print(f"Time for inline var creation: {time_inline}")
    time.sleep(3)

    time_now = time.perf_counter()
    for i in range(10_000_000):
        v = [1, 2, 3]
        w = [4, 5, 6]
    time_sep_line = time.perf_counter() - time_now
    print(f"Time for seperate line var creation: {time_sep_line}")

    # print(calculate_covariance(v=v, w=w))
    print()
