# ------------------------------------------------------------------------------
# vector matrix multiplication
# https://www.deep-ml.com/problem/Matrix%20times%20Vector
# ------------------------------------------------------------------------------


def dot_product_of_vectors(v: list[int | float], w: list[int | float]):
    """function to calculate dot product(element-wise product) of two vectors

    Args:
        v (list[int  |  float]): vector
        w (list[int  |  float]): vector

    Returns:
        list[int | floar]: fot product of two given vectors v and w
    """

    # both vectors v and w have to be of same len for dot product
    try:
        assert len(v) == len(w)
    except AssertionError:
        print("both vectors have to be of same length for dot products")
        return

    product = []

    for i, j in zip(v, w):
        product.append(i * j)

    # dot product of two vectors is sum of elementwise product
    return sum(product)


def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:
    """function to calculate dot product of given matrix a and vector b

    Args:
        a (list[list[int  |  float]]): given matrix
        b (list[int  |  float]): given vector

    Returns:
        list[int | float]: dot product of a and b
    """

    return [dot_product_of_vectors(row, b) for row in a]


if __name__ == "__main__":
    a = [[1, 2], [2, 4]]
    b = [1, 2]

    result = matrix_dot_vector(a=a, b=b)
    print(result)  # [5,10]

    # values from https://mathinsight.org/matrix_vector_multiplication_examples
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    B = [-2, 1, 0]

    result1 = matrix_dot_vector(a=A, b=B)
    print(result1)  # [0, -3, -6, -9]
