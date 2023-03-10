# from typing import List, Union

from .matrix import Matrix, make_matrix_python as make_matrix, MatrixType
from .vector import Vector, make_vector_python as make_vector


# def make_mc(values: Union[MatrixType, List[float]]) -> Union[Matrix, Vector]:
def make_mc(values: MatrixType | list[float]) -> Matrix | Vector:
    """Creates a :class:`Matrix` or a :class:`Vector` object depending on input values type.

    Example:

    >>> a: Matrix = make_matrix([
    ...     [1, 2],
    ...     [3, 4]])
    >>> b: Vector = make_vector([1, 2])
    """

    if isinstance(values[0], list):
        return make_matrix(values)
    return make_vector(values)
