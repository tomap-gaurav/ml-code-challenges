# ------------------------------------------------------------------------------
# scaler matrix multiplication
# https://www.deep-ml.com/problem/Scalar%20Multiplication%20of%20a%20Matrix
# ------------------------------------------------------------------------------


def scalar_multiply(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:
    """funtion to multiply a matrix by a scaler and return the result

    Args:
        matrix (list[list[int  |  float]]): given matrix
        scalar (int | float): scaler to multiply the matrix with

    Returns:
        list[list[int | float]]: result of matrix-scaler multiplication
    """
    for row in matrix:
        for i in range(len(row)):
            row[i] = row[i] * scalar

    return matrix


# ------------------------------------------------------------------------------
# since matrix is a nested list we can use list comprehesion to multiply -
# - matrix and scaler
# ------------------------------------------------------------------------------


def scalar_multiply1(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:
    """funtion to multiply a matrix by a scaler and return the result

    Args:
        matrix (list[list[int  |  float]]): given matrix
        scalar (int | float): scaler to multiply the matrix with

    Returns:
        list[list[int | float]]: result of matrix-scaler multiplication
    """
    return [[i * scalar for i in row] for row in matrix]


if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    scalar = 2

    # print(scalar_multiply.__doc__)

    result = scalar_multiply(matrix=matrix, scalar=scalar)

    print(result)
