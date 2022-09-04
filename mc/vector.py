from ctypes import (
    CDLL,
    POINTER,
    Structure,
    c_double,
    c_int,
)
from typing import List


class Vector(Structure):
    _fields_ = [
        ('length', c_int),
        ('values', POINTER(c_double))
    ]


lib = CDLL('./lib.so')

make_vector = lib.make_vector
make_vector.argtypes = [c_int, POINTER(c_double)]
make_vector.restype = Vector

print_vector = lib.print_vector
print_vector.argtypes = [Vector]
print_vector.restype = None


def make_vector_python(values: List[float]) -> Vector:
    length = len(values)
    return make_vector(length, (c_double * length)(*values))


values_1 = [10, 20, 30]
values_2 = [40, 50, 60]

v_1 = make_vector_python(values_1)
v_2 = make_vector_python(values_2)

print('Vector 1:')
print_vector(v_1)

print('Vector 2:')
print_vector(v_2)
