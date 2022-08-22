from ctypes import (
    CDLL,
    POINTER,
    Structure,
    c_double,
    c_int,
)


class Matrix(Structure):
    _fields_ = [
        ('rows', c_int),
        ('columns', c_int),
        ('data', POINTER(POINTER(c_double))),
    ]


lib = CDLL('./lib.so')

main = lib.main
main.restype = c_int

multiply = lib.multiply
multiply.argtypes = [c_int, c_int]
multiply.restype = Matrix

a = Matrix(c_int(2), c_int(4))
b = Matrix(c_int(4), c_int(1))
c = multiply(a, b)

print('Start')
main()
print('End')
