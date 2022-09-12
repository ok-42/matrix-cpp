from __future__ import annotations

import pathlib
from ctypes import (
    CDLL,
    POINTER,
    Structure,
    c_double,
    c_int,
    cast,
)
from typing import List, Tuple, Union, get_args

from ._utils import import_function
from .vector import make_vector_python, Vector

MatrixType = List[List[float]]
NumberType = Union[int, float]


class Matrix(Structure):
    _fields_ = [
        ('rows', c_int),
        ('columns', c_int),
        ('values', POINTER(POINTER(c_double))),
    ]

    @property
    def shape(self) -> Tuple[int, int]:
        return self.rows, self.columns

    @property
    def list(self) -> MatrixType:
        """Matrix representation as a Python list of lists of floats."""
        result: MatrixType = [[0 for i in range(self.columns)] for j in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                result[i][j] = self.values[i][j]
        return result

    def __add__(self, other: Union[Matrix, NumberType]) -> Matrix:
        """Add a number to all matrix elements or add two matrices of the same shape."""
        if isinstance(other, Matrix):
            if self.shape == other.shape:
                return add_matrix(self, other)
            else:
                raise Exception('Matrices should have the same shape')
        elif isinstance(other, get_args(NumberType)):
            return add_number(self, c_double(other))
        else:
            raise Exception('Invalid argument type. It should be a matrix or a number')

    def __matmul__(self, other: Matrix) -> Matrix:
        if self.column != other.rows:
            raise Exception('Wrong matrices dimensionality')
        return multiply(self, other)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        result = ''
        for row in self.list:
            result += '\t'.join(map(str, row)) + '\n'
        return result


lib = CDLL(str(pathlib.Path(__file__).parent.parent / 'ct.so'))

main = lib.main
main.restype = c_int

make_matrix = import_function(
    lib.make_matrix,
    [c_int, POINTER(Vector)],
    Matrix)

make_matrix_orig = lib.make_matrix_orig
lib.make_matrix_orig.argtypes = [c_int, c_int, POINTER(POINTER(c_double))]
lib.make_matrix_orig.restype = Matrix

print_matrix = lib.print_matrix
print_matrix.argtypes = [Matrix]
print_matrix.restype = None

multiply = lib.multiply
multiply.argtypes = [Matrix, Matrix]
multiply.restype = Matrix

add_number = lib.add_number
add_number.argtypes = [Matrix, c_double]
add_number.restype = Matrix

add_matrix = lib.add_matrix
add_matrix.argtypes = [Matrix, Matrix]
add_matrix.restype = Matrix


def make_matrix_python(values: MatrixType):
    vectors: List[Vector] = []
    for row in values:
        vectors.append(make_vector_python(row))
    n_rows = len(values)
    return make_matrix(n_rows, (Vector * n_rows)(*vectors))


# https://stackoverflow.com/a/58262388
def make_matrix_python_2(values: MatrixType):
    rows = len(values)
    cols = len(values[0])
    values = tuple(tuple(row) for row in values)

    double_ptr = POINTER(c_double)
    double_ptr_arr = double_ptr * rows
    double_array_array = (c_double * cols) * rows
    in_arr = double_array_array(*values)
    in_ptr = cast(
        double_ptr_arr(
            *(
                cast(row, double_ptr)
                for row in in_arr
            )
        ),
        POINTER(POINTER(c_double))
    )
    return make_matrix_orig(c_int(rows), c_int(cols), in_ptr)
