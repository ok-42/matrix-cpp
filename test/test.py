import sys
import unittest

original_path = sys.path
sys.path = original_path[1:]
import mc  # noqa: E402
sys.path = original_path

values_1 = [
    [1, 2],
    [3, 4]]

values_2 = [
    [5, 6],
    [7, 8]]

# = values_1 + 1.5
values_1_plus_const = [
    [2.5, 3.5],
    [4.5, 5.5]]

# = values_1 + values_2
values_sum = [
    [6, 8],
    [10, 12]]

matrix_1 = mc.make_matrix_python(values_1)
matrix_2 = mc.make_matrix_python(values_2)


class TestMatrix(unittest.TestCase):

    def test_shape(self):
        self.assertEqual(matrix_1.shape, (2, 2))

    def test_tolist(self):
        self.assertEqual(matrix_1.tolist(), values_1)

    def test_add(self):
        self.assertEqual(
            matrix_1 + 1.5,
            mc.make_matrix_python(values_1_plus_const))
        self.assertEqual(
            matrix_1 + matrix_2,
            mc.make_matrix_python(values_sum))

    def test_matmul(self):
        self.assertEqual(
            matrix_1 @ matrix_2,
            mc.make_matrix_python([
                [19, 22],
                [43, 50]]))


if __name__ == '__main__':
    unittest.main()
