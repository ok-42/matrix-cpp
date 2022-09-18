import ctypes
from typing import Callable, List, Type


# noinspection PyProtectedMember
def import_function(
        func: ctypes.CDLL._FuncPtr,
        argtypes: List[Type],
        restype: Type
) -> Callable:
    # Its type in Python could be Callable[argtypes, restype]
    result = func
    result.argtypes = argtypes
    result.restype = restype
    return result
