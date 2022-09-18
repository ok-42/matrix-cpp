import ctypes
from typing import Callable, List, Type


# noinspection PyProtectedMember
def import_function(
        func: ctypes.CDLL._FuncPtr,
        python_types: Type[Callable],
) -> Callable:
    """Set C data types for a C / C++ library function based on its corresponding Python callable data types.

    Let's consider a C++ function which takes two int and returns double.

    >>> from ctypes import c_double, c_int
    >>> lib = ctypes.CDLL('lib.so')

    The standard way which does not provide a developer with typing hints:

    >>> divide = lib.divide
    >>> divide.argtypes = [c_int, c_int]
    >>> divide.restype = c_double

    A confusing, unclear way which enables typing hints:

    >>> typ = Callable[[int, int], float]
    >>> divide: typ = import_function(lib.divide, typ)

    :param func: object (function) from a CDLL
    :param python_types: Python typing hint for that function (e.g., it contains int instead of c_int)
    :return: a callable object with correct data types (not a regular Python def)
    """

    result = func
    c_types: List[Type] = []

    conversion_dict = {
        bool: ctypes.c_bool,
        int: ctypes.c_int,
        float: ctypes.c_double}

    # typing.Callable stores arguments types and result type as a plain list in __args__
    # See typing._CallableGenericAlias.__repr__()
    for i in python_types.__args__:
        try:
            c_types.append(conversion_dict[i])
        except KeyError:
            c_types.append(i)

    result.argtypes = c_types[:-1]
    result.restype = c_types[-1]

    return result
