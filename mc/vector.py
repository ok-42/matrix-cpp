import pathlib
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


lib = CDLL(str(pathlib.Path(__file__).parent.parent / 'ct.so'))

make_vector = lib.make_vector
make_vector.argtypes = [c_int, POINTER(c_double)]
make_vector.restype = Vector

print_vector = lib.print_vector
print_vector.argtypes = [Vector]
print_vector.restype = None


def make_vector_python(values: List[float]) -> Vector:
    length = len(values)
    return make_vector(length, (c_double * length)(*values))
