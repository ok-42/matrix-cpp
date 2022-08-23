from ctypes import (
    CDLL,
    POINTER,
    Structure,
    c_double,
    c_int,
)
from typing import List

from vector import make_vector_python, Vector


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

print_matrix = lib.print_matrix
print_matrix.argtypes = [Matrix]
print_matrix.restype = None

multiply = lib.multiply
multiply.argtypes = [Matrix, Matrix]
multiply.restype = Matrix


def make_matrix_python(values: List[List[float]]):
    vectors: List[Vector] = []
    for row in values:
        vectors.append(make_vector_python(row))
    n_rows = len(values)
    return make_matrix(n_rows, (Vector * n_rows)(*vectors))


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
