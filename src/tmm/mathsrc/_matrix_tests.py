import unittest
from matrix import *


def _check(ut, expected, result):
    """
    Uses the unittest object to check expected results against the actual
    result. The error message (if applicable) it prints is predefined.

    Arguments:
        ut  -- self from the unittest.TestCase subclass
        expected  -- Expected result can be any type
        result  -- Actual result can be any type
    """
    failure_message = "\nExpected: \n" + \
        str(expected) + "\n\n" + "But Got: \n" + str(result)
    ut.assertEqual(result, expected, failure_message)


class MatrixTests(unittest.TestCase):

    def test_add_1(self):
        """
        Tests addition on standard 3x3 matrices
        """
        m1 = Matrix(3, 3)
        m2 = Matrix(3, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m1 + m2
        expected = Matrix(3, 3)
        expected.insert_all([2, 4, 6, 8, 10, 12, 14, 16, 18])

        _check(self, expected, result)

    def test_add_2(self):
        """
        Tests addition on matrices with mismatched dimensions
        """
        m1 = Matrix(3, 4)
        m2 = Matrix(4, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 + m2
        expected = None

        _check(self, expected, result)

    def test_sub_1(self):
        """
        Tests subtraction on standard 3x3 matrices
        """
        m1 = Matrix(3, 3)
        m2 = Matrix(3, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m1 - m2
        expected = Matrix(3, 3)
        expected.insert_all([0, 0, 0, 0, 0, 0, 0, 0, 0])

        _check(self, expected, result)

    def test_sub_2(self):
        """
        Tests subtraction on matrices with mismatched dimensions
        """
        m1 = Matrix(3, 4)
        m2 = Matrix(4, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 - m2
        expected = None

        _check(self, expected, result)

    def test_mul_1(self):
        """
        Tests multiplication on standard 3x3 matrices
        """
        m1 = Matrix(3, 3)
        m2 = Matrix(3, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m1 * m2
        expected = Matrix(3, 3)
        expected.insert_all([30, 36, 42, 66, 81, 96, 102, 126, 150])

        _check(self, expected, result)

    def test_mul_2(self):
        """
        Tests multiplcation on matrices with mismatched dimensions
        """
        m1 = Matrix(4, 3)
        m2 = Matrix(4, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 * m2
        expected = None

        _check(self, expected, result)

    def test_mul_3(self):
        """
        Tests multiplcation on matrices with mismatched dimensions
        """
        m1 = Matrix(4, 3)
        m2 = Matrix(3, 4)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 * m2
        expected = Matrix(4,4)
        expected.insert_all([38, 44, 50, 56, 83, 98, 113, 128, 128, 152, 176, 200, 173, 206, 239, 272])

        _check(self, expected, result)

    def test_boolmul_1(self):
        """
        Tests boolean multiplication on standard 3x3 matrices
        """
        m1 = Matrix(3, 3)
        m2 = Matrix(3, 3)

        m1.insert_all([0, 0, 0, 1, 0, 1, 0, 0, 1])
        m2.insert_all([0, 0, 0, 1, 0, 1, 0, 0, 0])

        result = m1.boolean_product(m2)
        expected = Matrix(3, 3)
        expected.insert_all([0, 0, 0, 0, 0, 0, 0, 0, 0])

        _check(self, expected, result)

    def test_boolmul_2(self):
        """
        Tests boolean multiplcation on matrices with mismatched dimensions
        """
        m1 = Matrix(4, 3)
        m2 = Matrix(4, 3)

        m1.insert_all([0, 0, 0, 1, 0, 1, 0, 0, 1])
        m2.insert_all([0, 0, 0, 1, 0, 1, 0, 0, 0])

        result = m1.boolean_product(m2)
        expected = None

        _check(self, expected, result)

    def test_boolmul_3(self):
        """
        Tests boolean multiplcation on non boolean matrix
        """
        m1 = Matrix(4, 3)
        m2 = Matrix(4, 3)

        m1.insert_all([0, 0, 3, 1, 0, 1, 0, 0, 1])
        m2.insert_all([0, 0, 0, 1, 0, 1, 0, 0, 0])

        result = m1.boolean_product(m2)
        expected = None

        _check(self, expected, result)

    def test_boolmul_4(self):
        """
        Tests boolean multiplcation on non square matrices
        """
        m1 = Matrix(3, 4)
        m2 = Matrix(4, 3)

        m1.insert_all([0, 0, 0, 1, 0, 1, 0, 0, 1])
        m2.insert_all([0, 0, 0, 1, 0, 1, 0, 0, 0])

        result = m1.boolean_product(m2)
        expected = Matrix(3,3)
        expected.insert_all([0,0,0,0,0,0,0,0,0])

        _check(self, expected, result)

    def test_bitOR_1(self):
        """
        Tests OR on matrices
        """
        m1 = Matrix(4, 3)
        m2 = Matrix(4, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 | m2
        expected = Matrix(4, 3)
        expected.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        _check(self, expected, result)

    def test_bitOR_2(self):
        """
        Tests OR on matrices with mismatched dimensions
        """
        m1 = Matrix(3, 3)
        m2 = Matrix(4, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 | m2
        expected = None

        _check(self, expected, result)

    def test_bitAND_1(self):
        """
        Tests AND on matrices
        """
        m1 = Matrix(4, 3)
        m2 = Matrix(4, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 & m2
        expected = Matrix(4, 3)
        expected.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        _check(self, expected, result)

    def test_bitAND_2(self):
        """
        Tests AND on matrices with mismatched dimensions
        """
        m1 = Matrix(3, 3)
        m2 = Matrix(4, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 & m2
        expected = None

        _check(self, expected, result)

    def test_bitXOR_1(self):
        """
        Tests XOR on matrices
        """
        m1 = Matrix(4, 3)
        m2 = Matrix(4, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 ^ m2
        expected = Matrix(4, 3)
        expected.insert_all([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        _check(self, expected, result)

    def test_bitXOR_2(self):
        """
        Tests XOR on matrices with mismatched dimensions
        """
        m1 = Matrix(3, 3)
        m2 = Matrix(4, 3)

        m1.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])
        m2.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m1 ^ m2
        expected = None

        _check(self, expected, result)

    def test_lshift_1(self):
        """
        Tests left shift on standard 3x3 matrix
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m << 2
        expected = Matrix(3, 3)
        expected.insert_all([4, 8, 12, 16, 20, 24, 28, 32, 36])

        _check(self, expected, result)

    def test_lshift_2(self):
        """
        Tests left shift on non-square matrix
        """
        m = Matrix(2, 3)
        m.insert_all([1, 2, 3, 4, 5, 6])

        result = m << 2
        expected = Matrix(2, 3)
        expected.insert_all([4, 8, 12, 16, 20, 24])

        _check(self, expected, result)

    def test_lshift_3(self):
        """
        Tests left shift on matrix with non integer element
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4.0, 5, 6, 7, 8, 9])

        result = m << 2
        expected = None

        _check(self, expected, result)

    def test_rshift_1(self):
        """
        Tests right shift on standard 3x3 matrix
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m >> 2
        expected = Matrix(3, 3)
        expected.insert_all([0, 0, 0, 1, 1, 1, 1, 2, 2])

        _check(self, expected, result)

    def test_rshift_2(self):
        """
        Tests right shift on non-square matrix
        """
        m = Matrix(2, 3)
        m.insert_all([1, 2, 3, 4, 5, 6])

        result = m >> 2
        expected = Matrix(2, 3)
        expected.insert_all([0, 0, 0, 1, 1, 1])

        _check(self, expected, result)

    def test_rshift_3(self):
        """
        Tests right shift on matrix with non-integer element
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4.0, 5, 6, 7, 8, 9])

        result = m >> 2
        expected = None

        _check(self, expected, result)

    def test_pow_1(self):
        """
        tests matrix power on standard 3x3 matrix
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m**3
        expected = Matrix(3, 3)
        expected.insert_all(
            [468, 576, 684, 1062, 1305, 1548, 1656, 2034, 2412])

        _check(self, expected, result)

    def test_pow_2(self):
        """
        Tests matrix power on non square matrix
        """
        m = Matrix(3, 4)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m**3
        expected = None

        _check(self, expected, result)

    def test_pow_3(self):
        """
        Tests matrix power of 0
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m**0
        expected = Matrix(3, 3)
        expected.insert_all([1, 0, 0, 0, 1, 0, 0, 0, 1])

        _check(self, expected, result)

    def test_boolpow_1(self):
        """
        Tests boolean power on standard 3x3 zero-one matrix
        """
        m = Matrix(3, 3)
        m.insert_all([0, 0, 0, 1, 0, 1, 1, 1, 1])

        result = m.boolean_power(3)
        expected = Matrix(3, 3)
        expected.insert_all([0, 0, 0, 1, 1, 1, 1, 1, 1])

        _check(self, expected, result)

    def test_boolpow_2(self):
        """
        Tests boolean power on non-square zero-one matrix
        """
        m = Matrix(3, 4)
        m.insert_all([0, 0, 0, 1, 0, 1, 1, 1, 1])

        result = m.boolean_power(3)
        expected = None

        _check(self, expected, result)

    def test_boolpow_3(self):
        """
        Tests boolean power of 0 on zero-one 3x3 matrix
        """
        m = Matrix(3, 3)
        m.insert_all([0, 0, 0, 1, 0, 1, 1, 1, 1])

        result = m.boolean_power(0)
        expected = Matrix(3, 3)
        expected.insert_all([1, 0, 0, 0, 1, 0, 0, 0, 1])

        _check(self, expected, result)

    def test_boolpow_4(self):
        """
        Tests boolean power of 0 on non zero-one matrix.
        """
        m = Matrix(3, 3)
        m.insert_all([0, 0, 0, 10, 0, 1, 1, 1, 1])

        result = m.boolean_power(3)
        expected = None

        _check(self, expected, result)

    def test_tranpose_1(self):
        """
        Test transpose on standard 3x3 matrix
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m.transpose()
        expected = Matrix(3, 3)
        expected.insert_all([1, 4, 7, 2, 5, 8, 3, 6, 9])

        _check(self, expected, result)

    def test_tranpose_2(self):
        """
        Test transpose on non square matrix
        """
        m = Matrix(4, 3)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m.transpose()
        expected = Matrix(3, 4)
        expected.insert_all([1, 4, 7, 10, 2, 5, 8, 11, 3, 6, 9, 12])

        _check(self, expected, result)

    def test_tranpose_3(self):
        """
        Test transpose on matrix of size 1x1
        """
        m = Matrix(1, 1)
        m.insert_all([1])

        result = m.transpose()
        expected = Matrix(1, 1)
        expected.insert_all([1])

        _check(self, expected, result)

    def test_scalarmul_1(self):
        """
        Test scalar multiplication on a standard 2x3 matrix
        """
        m = Matrix(2, 3)
        m.insert_all([1, 2, 3, 4, 5, 6])

        result = m * 10
        expected = Matrix(2, 3)
        expected.insert_all([10, 20, 30, 40, 50, 60])

        _check(self, expected, result)

    def test_scalarmul_2(self):
        """
        Test scalar multiplication on a standard 2x3 matrix with float
        """
        m = Matrix(2, 3)
        m.insert_all([1, 2, 3, 4, 5, 6])

        result = m * 10.7

        expected = Matrix(2, 3)
        expected.insert_all([10.7, 21.4, 32.1, 42.8, 53.5, 64.2])

        _check(self, expected, result)

    def test_minor_1(self):
        """
        Test find minor for a 2x2 matrix
        """
        m = Matrix(2, 2)
        m.insert_all([1, 2, 3, 4])

        result = m.find_minor(1, 1)
        expected = Matrix(1, 1)
        expected.insert_all([4])

        _check(self, expected, result)

    def test_minor_2(self):
        """
        Test find minor for a 1x1 matrix
        """
        m = Matrix(1, 1)
        m.insert_all([1])

        result = m.find_minor(1, 1)
        expected = None

        _check(self, expected, result)

    def test_minor_3(self):
        """
        Test find minor on non-square matrix
        """
        m = Matrix(2, 3)
        m.insert_all([1, 2, 3, 4, 5, 6])

        result = m.find_minor(1, 1)
        expected = None

        _check(self, expected, result)

    def test_minor_4(self):
        """
        Test find minor on standard 3x3 matrix with i,j out of bounds
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m.find_minor(0, 0)
        expected = None

        _check(self, expected, result)

    def test_minor_5(self):
        """
        Test find minor on standard 3x3 matrix with i,j out of bounds
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m.find_minor(30, 42)
        expected = None

        _check(self, expected, result)

    def test_minor_6(self):
        """
        Test find minor on standard 3x3 matrix with a more complex i,j input
        where i!=j
        """
        m = Matrix(3, 3)
        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m.find_minor(3, 2)
        expected = Matrix(2, 2)
        expected.insert_all([1, 3, 4, 6])

        _check(self, expected, result)

    def test_det_1(self):
        """
        Checks determinant of a matrix with matching rows (checks det = 0)
        """
        m = Matrix(3, 3)

        m.insert_all([1, 2, 3, 1, 2, 3, 4, 5, 6])

        result = m.det()
        expected = 0

        _check(self, expected, result)

    def test_det_2(self):
        """
        Checks determinant of a matrix (checks det != 0)
        """
        m = Matrix(3, 3)

        m.insert_all([1, 2, 3, 4, 8, 6, 3, 1, -2])

        result = m.det()
        expected = -30

        _check(self, expected, result)

    def test_det_3(self):
        """
        Checks determinant of a non square matrix. Result should be undefined.
        """
        m = Matrix(4, 3)

        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        result = m.det()
        expected = None

        _check(self, expected, result)

    def test_adjoint_1(self):
        """
        Checks adjoint of a square matrix.
        """
        m = Matrix(3, 3)

        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = m.adjoint()
        expected = Matrix(3, 3)
        expected.insert_all([-3, 6, -3, 6, -12, 6, -3, 6, -3])

        _check(self, expected, result)

    def test_adjoint_2(self):
        """
        Checks adjoint of a non square matrix.
        """
        m = Matrix(3, 2)

        m.insert_all([1, 2, 3, 4, 5, 6])

        result = m.adjoint()
        expected = None

        _check(self, expected, result)

    def test_adjoint_3(self):
        """
        Checks adjoint of a matrix with float values.
        """
        m = Matrix(3, 3)

        m.insert_all([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])

        result = m.adjoint()
        expected = Matrix(3, 3)
        expected.insert_all(
            [-3.0, 6.0, -3.0, 6.0, -12.0, 6.0, -3.0, 6.0, -3.0])

        _check(self, expected, result)

    def test_adjoint_4(self):
        """
        Checks the adjoint of a 4*4 matrix.
        """
        m = Matrix(4, 4)

        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1])

        result = m.adjoint()
        expected = Matrix(4, 4)
        expected.insert_all([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        _check(self, expected, result)

    def test_cofactor_1(self):
        """
        Checks the cofactor of a square matrix.
        """
        m = Matrix(3, 3)

        m.insert_all([9, 8, 7, 6, 5, 4, 3, 2, 1])

        result = m.cofactor()
        expected = Matrix(3, 3)
        expected.insert_all([-3, 6, -3, 6, -12, 6, -3, 6, -3])

        _check(self, expected, result)

    def test_cofactor_2(self):
        """
        Checks the cofactor of a non square matrix.
        """
        m = Matrix(3, 2)

        m.insert_all([1, 2, 3, 4, 5, 6])

        result = m.cofactor()
        expected = None

        _check(self, expected, result)

    def test_cofactor_3(self):
        """
        Checks the cofactor of a matrix with float values.
        """
        m = Matrix(3, 3)

        m.insert_all([9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0])

        result = m.cofactor()
        expected = Matrix(3, 3)
        expected.insert_all(
            [-3.0, 6.0, -3.0, 6.0, -12.0, 6.0, -3.0, 6.0, -3.0])

        _check(self, expected, result)

    def test_cofactor_4(self):
        """
        Checks the cofactor of a 4*4 matrix.
        """
        m = Matrix(4, 4)

        m.insert_all([1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1])

        result = m.cofactor()
        expected = Matrix(4, 4)
        expected.insert_all([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        _check(self, expected, result)

    def test_inverse_1(self):
        """
        Checks the inverse of a square matrix.
        """
        m = Matrix(3, 3)

        m.insert_all([1, 2, 3, 4, 5, 6, 4, 2, 1])

        result = m.inv()
        expected = Matrix(3, 3)
        expected.insert_all([2.33, -1.33, 1, -6.67, 3.67, -2, 4, -2, 1])

        _check(self, expected, result)

    def test_inverse_2(self):
        """
        Checks the inverse of a non square matrix.
        """
        m = Matrix(3, 2)

        m.insert_all([1, 2, 3, 4, 5, 6])

        result = m.inv()
        expected = None
        _check(self, expected, result)

    def test_inverse_3(self):
        """
        Checks the inverse of an identity matrix.
        """
        m = Matrix(3, 3)

        m.insert_all([1, 0, 0, 0, 1, 0, 0, 0, 1])

        result = m.inv()
        expected = Matrix(3, 3)
        expected.insert_all([1, 0, 0, 0, 1, 0, 0, 0, 1])
        _check(self, expected, result)

    def test_inverse_4(self):
        """
        Checks the inverse of a matrix with determinant 0.
        """
        m = Matrix(3, 3)

        m.insert_all([1, 0, 0, 1, 0, 0, 3, 2, 1])

        result = m.inv()
        expected = None
        _check(self, expected, result)


if __name__ == "__main__":
    unittest.main()
