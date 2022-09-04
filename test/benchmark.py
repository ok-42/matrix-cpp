from __future__ import annotations

import time
from typing import Callable

import numpy as np

from mc.wrapper import (
    make_matrix_python,
    make_matrix_python_2,
    multiply,
    MatrixType
)


def random_matrix_numpy(rows: int, columns: int) -> np.ndarray:
    """Generates random numpy 2d-array"""
    return np.random.random((rows, columns))


def random_matrix_python(rows: int, columns: int) -> MatrixType:
    return random_matrix_numpy(rows, columns).tolist()


class MatrixPython:
    """Python implementation of a matrix which supports multiplication.

    Example:

    >>> a = MatrixPython([
    ...     [1, 2],
    ...     [3, 4],
    ... ])
    >>> b = MatrixPython([
    ...     [5],
    ...     [6],
    ... ])
    >>> c: MatrixPython = a @ b
    >>> print(*c.values, sep='\\n')
    """

    def __init__(self, values: MatrixType):
        self.rows = len(values)
        self.columns = len(values[0])
        self.values = values

    def __matmul__(self, other: MatrixPython) -> MatrixPython:
        result: MatrixType = [[0 for j in range(other.columns)] for i in range(self.rows)]
        matrix_1 = self.values
        matrix_2 = other.values
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    e_1 = matrix_1[i][k]
                    e_2 = matrix_2[k][j]
                    result[i][j] += e_1 * e_2
        return MatrixPython(result)


def measure_cpp_1():
    """Multiplies two random matrices using C++ code from this project.
    The matrices are built as arrays of vectors."""
    m_1 = make_matrix_python(np.random.random((90, 30)).tolist())
    m_2 = make_matrix_python(np.random.random((30, 40)).tolist())
    m = multiply(m_1, m_2)


def measure_cpp_2():
    """Multiplies two random matrices using C++ code from this project.
    The values are passed to matrix constructors as ``double**``."""
    m_1 = make_matrix_python_2(np.random.random((90, 30)).tolist())
    m_2 = make_matrix_python_2(np.random.random((30, 40)).tolist())
    m = multiply(m_1, m_2)


def measure_numpy():
    """Multiplies numpy arrays as matrices."""
    m_1 = random_matrix_numpy(90, 30)
    m_2 = random_matrix_numpy(30, 40)
    m = m_1 @ m_2


def measure_python():
    """Multiplies Python lists of lists, i.e. ``list[list[float]]``, as matrices."""
    m_1 = MatrixPython(random_matrix_python(90, 30))
    m_2 = MatrixPython(random_matrix_python(30, 40))
    m = m_1 @ m_2


def measure(func: Callable[[], None], text: str, iterations: int) -> None:
    """Execute a function a specified number of times.

    :param func: the function to be executed in a loop
    :param text: will be printed after the loop ends and elapsed time measured
    :param iterations: number of the function invocations
    :return: None; prints to stdout
    """
    start = time.time()
    for i in range(iterations):
        func()
    end = time.time()
    msec = (end - start) * 1_000
    print(f'{text:>8}: {msec:8.2f} msec')


ITER_NUMBER = 100
measure(measure_cpp_1, 'C++ 1st', ITER_NUMBER)
measure(measure_cpp_2, 'C++ 2nd', ITER_NUMBER)
measure(measure_numpy, 'Numpy', ITER_NUMBER)
measure(measure_python, 'Python', ITER_NUMBER)
