# /// script
# dependencies = ["numpy", "math"]
# ///
import numpy as np
import math


# Gives the inverse of a matrix in mod p
def modMatInv(A, p):
    """
    Returns the inverse of matrix A in mod p
    """
    if not isinstance(A, np.ndarray):
        raise Exception("The given `A` parameter is not an array")
    if not (len(A.shape) == 2 and A.shape[0] == A.shape[1]):
        raise Exception("The given `A` parameter is not the correct shape")
    determinant = det(A)
    if determinant % p == 0 or not math.gcd(determinant, p) == 1:
        raise Exception("The cannot take the inverse of this matrix in mod", p)
    out_mat = np.zeros(A.shape)
    for i in range(len(A)):
        for j in range(len(A[i])):
            out_mat[i][j] = (-1) ** (i + j) * det(minorMat(A, i, j)) % p
    return np.mod((pow(int(determinant), -1, p)) * out_mat.transpose(), p)


def det(A):
    """
    Returns the determinant of matrix A
    """
    if not isinstance(A, np.ndarray):
        raise Exception("The given `A` parameter is not an array")
    if not (len(A.shape) == 2 and A.shape[0] == A.shape[1]):
        raise Exception("The given `A` parameter is not the correct shape")
    det_calc = 0
    if A.shape == (1, 1):
        return A[0][0]
    for i in range(len(A)):
        det_calc += ((-1) ** i) * A[i][0] * det(minorMat(A, i, 0))

    return det_calc


def minorMat(A, row, column):
    """
    Returns the row,column-minor of a matrix A
    """
    if not isinstance(A, np.ndarray):
        raise Exception("The given `A` parameter is not an array")
    if not isinstance(row, int) or not isinstance(column, int):
        raise Exception("The given `row` or `column` paramters were not integers~")

    minus_row = np.append(A[:row], A[row + 1 :], axis=0)
    minor = np.array(
        list(map(lambda x: np.append(x[:column], x[column + 1 :]), minus_row))
    )

    return minor
