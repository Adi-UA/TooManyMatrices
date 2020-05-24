import unittest
from matrix import *

def check(ut, expected, result):
    """
    Uses the unittest object to check expected results against the actual
    result. The error message (if applicable) it prints is predefined.

    Arguments:
        ut  -- self from the unittest.TestCase subclass
        expected  -- Expected result can be any type
        result  -- Actual result can be any type
    """
    failure_message = "\nExpected: \n" + str(expected) + "\n\n" +"But Got: \n" + str(result)
    ut.assertEqual(result,expected,failure_message)


class MatrixTests(unittest.TestCase):

    def test_add_1(self):
        """
        Tests addition on standard 3x3 matrices
        """
        m1 = Matrix(3,3)
        m2 = Matrix(3,3)

        m1.insert_all([1,2,3,4,5,6,7,8,9])
        m2.insert_all([1,2,3,4,5,6,7,8,9])

        result = m1+m2
        expected = Matrix(3,3)
        expected.insert_all([2 , 4,  6, 8, 10, 12, 14, 16, 18])

        check(self,expected, result)

    def test_add_2(self):
        """
        Tests addition on matrices with mismatched dimensions
        """
        m1 = Matrix(3,4)
        m2 = Matrix(4,3)

        m1.insert_all([1,2,3,4,5,6,7,8,9,10,11,12])
        m2.insert_all([1,2,3,4,5,6,7,8,9,10,11,12])

        result = m1+m2
        expected = None

        check(self,expected, result)

    def test_sub_1(self):
        """
        Tests subtraction on standard 3x3 matrices
        """
        m1 = Matrix(3,3)
        m2 = Matrix(3,3)

        m1.insert_all([1,2,3,4,5,6,7,8,9])
        m2.insert_all([1,2,3,4,5,6,7,8,9])

        result = m1-m2
        expected = Matrix(3,3)
        expected.insert_all([0,0,0,0,0,0,0,0,0])

        check(self,expected, result)

    def test_sub_2(self):
        """
        Tests subtraction on matrices with mismatched dimensions
        """
        m1 = Matrix(3,4)
        m2 = Matrix(4,3)

        m1.insert_all([1,2,3,4,5,6,7,8,9,10,11,12])
        m2.insert_all([1,2,3,4,5,6,7,8,9,10,11,12])

        result = m1-m2
        expected = None

        check(self,expected, result)


    def test_mul_1(self):
        """
        Tests multiplication on standard 3x3 matrices
        """
        m1 = Matrix(3,3)
        m2 = Matrix(3,3)

        m1.insert_all([1,2,3,4,5,6,7,8,9])
        m2.insert_all([1,2,3,4,5,6,7,8,9])

        result = m1*m2
        expected = Matrix(3,3)
        expected.insert_all([30, 36, 42, 66, 81, 96, 102, 126, 150])

        check(self,expected, result)

    def test_mul_2(self):
        """
        Tests multiplcation on matrices with mismatched dimensions
        """
        m1 = Matrix(4,3)
        m2 = Matrix(4,3)

        m1.insert_all([1,2,3,4,5,6,7,8,9,10,11,12])
        m2.insert_all([1,2,3,4,5,6,7,8,9,10,11,12])

        result = m1*m2
        expected = None

        check(self,expected, result)

    def test_det_1(self):
        """
        Checks determinant of a matrix with matching rows (checks det = 0)
        """
        m = Matrix(3,3)

        m.insert_all([1,2,3,1,2,3,4,5,6])

        result = m.det()
        expected = 0

        check(self,expected, result)

    def test_det_2(self):
        """
        Checks determinant of a matrix (checks det != 0)
        """
        m = Matrix(3,3)

        m.insert_all([1,2,3,4,8,6,3,1,-2])

        result = m.det()
        expected = -30

        check(self,expected, result)

    def test_det_3(self):
        """
        Checks determinant of a non square matrix. Result should be undefined.
        """
        m = Matrix(4,3)

        m.insert_all([1,2,3,4,5,6,7,8,9,10,11,12])

        result = m.det()
        expected = None

        check(self,expected, result)

if __name__ == "__main__":
    unittest.main()