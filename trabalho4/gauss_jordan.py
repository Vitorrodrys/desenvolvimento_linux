import numpy


class GaussJordanError(ValueError):
    pass


class GaussJordanSingularMatrixError(GaussJordanError):
    pass


class GaussJordanInvalidMatrixError(GaussJordanError):
    pass


def find_a_row_with_non_zero_element_in_pivo_column(
    augmented_matrix: numpy.ndarray[float], pivo_index: float
) -> float:
    """
    Find a row with a non-zero element in the pivo column
    """
    for index, row in enumerate(augmented_matrix):
        if row[pivo_index] != 0:
            return index
    raise RuntimeError("There is no row with a non-zero element in the pivo column")


def check_diagonal_elements_with_zeros(augmented_matrix: numpy.ndarray[float]) -> None:
    """
    Check if the diagonal elements are zero, if has, so will make
    a change of the line with diagonal element zero with another line
    that has a non-zero element in the same column
    """
    index = 0
    while index < augmented_matrix.shape[0]:
        if augmented_matrix[index][index] == 0:
            row_to_change = find_a_row_with_non_zero_element_in_pivo_column(
                augmented_matrix, index
            )
            augmented_matrix[[index, row_to_change]] = augmented_matrix[
                [row_to_change, index]
            ]
        index += 1


def fill_with_zero_by_pivo(
    augmented_matrix: numpy.ndarray[float],
) -> numpy.ndarray[float]:
    """
    Fill the augmented matrix with zeros below and above the main diagonal
    using the pivo element
    """

    def calculate_scalar_multiplication(pivo: float, original_element: float) -> int:
        return original_element / pivo

    check_diagonal_elements_with_zeros(augmented_matrix)
    pivo_index = 0
    for i, row in enumerate(augmented_matrix):
        for j, row_to_fill in enumerate(augmented_matrix):
            if i != j and row_to_fill[pivo_index] != 0:
                # calculate the scalar to multiply by pivo row and subtract from the row to fill
                scalar_multiplication = calculate_scalar_multiplication(
                    row[pivo_index], row_to_fill[pivo_index]
                )
                # subtract the row multiplied by the scalar from the row to fill
                # to make the element in the pivo column zero
                augmented_matrix[j] = row_to_fill - scalar_multiplication * row
        pivo_index += 1


def fill_main_diagonal_with_ones(augmented_matrix: numpy.ndarray[float]) -> None:
    """
    Fill the main diagonal with ones
    """
    for i, row in enumerate(augmented_matrix):
        if row[i] != 1:
            augmented_matrix[i] = row / row[i]


def gauss_jordan_equivalent(
    aumented_matrix: numpy.ndarray[float],
) -> numpy.ndarray[float]:
    """
    Calculate the equivalent matrix with zeros outside the main diagonal
    of the augmented matrix using the Gauss-Jordan method
    """
    fill_with_zero_by_pivo(aumented_matrix)
    fill_main_diagonal_with_ones(aumented_matrix)
    return aumented_matrix


def gauss_jordan(coefficients: list[list[float]], results: list[float]) -> list[float]:
    """
    Calculate the variable matrix that solve a system composed by the coefficients and results
    if the system doens't has solution, will be raise a ValueError exception
    if the len of coefficientes is different than the len of results, also will be raise
    a ValueError exception because this system doens't have a solution
    """

    if len(coefficients) != len(results):
        raise GaussJordanInvalidMatrixError(
            "The number of coefficients must be the same as the number of results"
        )
    mcf = numpy.array(coefficients, dtype=float)
    mr = numpy.array(results, dtype=float)
    augmented_matrix = numpy.column_stack((mcf, mr))

    if numpy.linalg.det(mcf) == 0:
        raise GaussJordanSingularMatrixError(
            "The determinant of the matrix must be different from 0"
        )
    augmented_matrix = gauss_jordan_equivalent(augmented_matrix)
    return [float(xvalue) for xvalue in augmented_matrix[:, -1]]
