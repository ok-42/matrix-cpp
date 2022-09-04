from ctypes import (
    CDLL,
    POINTER,
    Structure,
    c_double,
    c_int,
    cast,
)
from typing import List

from .vector import make_vector_python, Vector

MatrixType = List[List[float]]


class Matrix(Structure):
    _fields_ = [
        ('rows', c_int),
        ('columns', c_int),
        ('data', POINTER(POINTER(c_double))),
    ]


lib = CDLL('./lib.so')

main = lib.main
main.restype = c_int

make_matrix = lib.make_matrix
lib.make_matrix.argtypes = [c_int, POINTER(Vector)]
lib.make_matrix.restype = Matrix

make_matrix_orig = lib.make_matrix_orig
lib.make_matrix_orig.argtypes = [c_int, c_int, POINTER(POINTER(c_double))]
lib.make_matrix_orig.restype = Matrix

print_matrix = lib.print_matrix
print_matrix.argtypes = [Matrix]
print_matrix.restype = None

multiply = lib.multiply
multiply.argtypes = [Matrix, Matrix]
multiply.restype = Matrix


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


a = make_matrix_python([
    [1, 2, 3],
    [5, 3, 1]])

b = make_matrix_python([
    [8, 2],
    [5, 3],
    [6, 2]])

c = multiply(a, b)

print('Matrix A:')
print_matrix(a)
print('Matrix B:')
print_matrix(b)
print('Result:')
print_matrix(c)

print('Start')
main()
print('End')
