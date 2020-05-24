"""
matrix.py: This module defines a Matrix class to represent and perform
operations on matrices. It also provides a couple additional functions to
quickly generate identity matrices and compare matrix orders. Refer to the HTML
documentation for an indepth explanation.
"""
import numpy as np

__author__ = "Aditya Banerjee"
__status__ = "Development"


class Matrix:
    """
    This class represents a Matrix. Refer to the HTML documentation for method
    details.
    """

    def __init__(self, row_no, col_no):
        """
        Creates an object that represents a matrix. During initialization the
        number of rows and columns needs to be given.

        Arguments: row_no {int} -- The number of rows in the matrix col_no {int}
            -- The number of columns in the matrix
        """
        self._row_no = row_no
        self._col_no = col_no
        self._matrix = np.array([[0] * col_no] * row_no)

    def __eq__(self, other):
        """
        This method checks the equality of two Matrix instances. Two matrices
        are said to be equal if they are of the same size and have the same
        elements at corresponding positions

        Arguments: other {Matrix} -- The Matrix object that the calling matrix
            is compared to

        Returns: boolean -- true if equal and false otherwise
        """
        if isinstance(other, Matrix):
            comparison = self._matrix == other._matrix
            return comparison.all()
        else:
            return False

    def get_row_no(self):
        """
        Returns the number of rows in the calling matrix.

        Returns: int -- The number of rows
        """
        return self._row_no

    def get_col_no(self):
        """
        Returns the number of columns in the calling matrix.

        Returns: int -- The number of columns
        """
        return self._col_no

    def get_value(self, row, col):
        """
        Returns the matrix value at the given position. Index starts at (1,1)

        Arguments: row {int} -- The row position of the element col {int} -- The
            column position of the element

        Returns: The value stored at (row, col) or None if the position is
            invalid
        """
        if row > 0 and col > 0 and row <= self._row_no and col <= self._col_no:
            return self._matrix[row - 1][col - 1]
        else:
            return None

    def set_value(self, row, col, value):
        """
        Sets the matrix value at the given position. Index starts at (1,1)

        Arguments: row {int} -- The row position of the element col {int} -- The
            column position of the element
        """
        if row > 0 and col > 0 and row <= self._row_no and col <= self._col_no:
            self._matrix[row - 1][col - 1] = value
        else:
            return None

    def _set_matrix_array(self, array):
        """
        This private method is used to modify the Matrix objects internal array
        and update its row and column size accordingly. DO NOT USE THIS
        EXTERNALLY.

        Arguments: array {numpy array} -- The 2D numpy array representin a valid
            matrix
        """
        self._matrix = array
        self._row_no = len(array)
        self._col_no = len(array[0])

    def insert_all(self, elements):
        """
        This method accepts a list of elements and initializes the matrix with
        them. Make sure to pass as many elements in the list as there are spaces
        in the matrix you defined. The Matrix object is modified in place.

        Arguments: elements {list} -- List of elements to put in the matrix

        Returns: boolean -- True if elements were added and False otherwise.
        """
        if len(elements) == self._row_no * self._col_no:
            self._matrix = np.reshape(elements, (self._row_no, self._col_no))
            return True
        else:
            return False

    def transpose(self):
        """
        This method finds and returns the transpose of the calling object. The
        calling object is NOT modified in place.

        Returns: Matrix -- A reference to the new transposed Matrix object
        """
        retval = Matrix(self._col_no, self._row_no)
        retval._matrix = np.transpose(self._matrix)
        return retval

    def det(self):
        """
        This method finds the determinant of the calling object.

        Returns: float -- The determinant value rounded up to two places or None
            if the request was invalid
        """
        if self._row_no == self._col_no:
            return round(np.linalg.det(self._matrix), 2)
        else:
            return None

    def multiply_scalar(self, scalar):
        """
        This method multiplies a scalar coefficient into the matrix.The calling
        object is NOT modified in place.

        Arguments: scalar -- The coefficient to multiply by

        Returns: Matrix -- A reference to the Matrix object with scalar
            multiplication applied
        """
        retval = Matrix(self._col_no, self._row_no)
        retval._matrix = self._matrix * scalar
        return retval

    def inv(self):
        """
        This method finds the inverse matrix of the calling object.The calling
        object is NOT modified in place.

        Returns: Matrix -- A reference to the inverse matix or None if the
            request was invalid
        """
        if self.det() != 0 and self._row_no == self._col_no:
            retval = Matrix(self._row_no, self._col_no)
            inverse_array = np.matrix.round(np.linalg.inv(self._matrix), 2)
            retval._set_matrix_array(inverse_array)
            return retval
        else:
            return None

    def cofactor(self):
        """
        This method finds the cofactor matrix of the calling object.The calling
        object is NOT modified in place.

        Returns: Matrix -- A reference to the cofactor matrix or None if the
            request was invalid
        """
        if self._row_no == self._col_no:
            retval = Matrix(self._row_no, self._col_no)

            values = []
            for i in range(1, self._row_no + 1):
                for j in range(1, self._col_no + 1):
                    sign_factor = (-1)**(i + j)
                    remaining = self.find_minor(i, j)
                    cofactor = sign_factor * remaining.det()
                    values.append(cofactor)

            retval.insert_all(values)
            return retval
        else:
            return None

    def adjoint(self):
        """
        This method finds the adjoint matrix of the calling object.The calling
        object is NOT modified in place.

        Returns: Matrix -- A reference to the adjoint matrix or None if the
            request was invalid
        """
        return self.cofactor().transpose()

    def find_minor(self, row, column):
        """
        This method finds the minor of the calling object at the given
        position.The calling object is NOT modified in place.

        Arguments: row -- The minor row column -- The minor column

        Returns: Matrix -- A reference to the minor matrix or None if the
            request was invalid
        """
        if self._row_no == self._col_no:
            retval = Matrix(self._row_no - 1, self._col_no - 1)
            values = []

            for i in range(1, self._row_no + 1):
                for j in range(1, self._col_no + 1):
                    if i == row or j == column:
                        pass
                    else:
                        values.append(self._matrix[i - 1][j - 1])

            retval.insert_all(values)
            return retval
        else:
            return None

    def is_boolean(self):
        """
        This method checks to see if a matrix is a zero-one matrix. That is, it
        checks to see if all the elements in the matrix are either 0 or one.

        Returns: boolean -- True or False depending on wheter or not it is a
            zero-one matrix or not
        """
        for i in range(1, self._row_no + 1):
            for j in range(1, self._col_no + 1):
                value = self._matrix[i - 1][j - 1]
                if value != 1 and value != 0:
                    return False

        return True

    def boolean_power(self, pow):
        """
        This method finds the boolean power of the given matrix raised to the
        pow parameter.The calling object is NOT modified in place.

        Arguments: pow -- The power

        Returns: Matrix -- A reference to the resulting matrix or None if the
            request was invalid.For a power of 0 the identity matrix of input
            matrix row size will be returned.
        """
        if pow == 0:
            return get_identity_matrix(self._row_no)
        if pow > 0:
            retval = self
            for i in range(pow - 1):
                retval = retval.boolean_product(self)
                if retval is None:
                    return None
            return retval
        else:
            return None

    def boolean_product(self, other):
        """
        This method finds the boolean product of the given matries.The calling
        object is NOT modified in place.

        Arguments: other -- The matrix object with which a boolean product is to
            be computed

        Returns: Matrix -- A reference to the resulting matrix or None if the
            request was invalid.
        """
        if isinstance(other, Matrix):
            if self._col_no == other._row_no:
                values = []
                for i in range(1, self._row_no + 1):
                    for j in range(1, self._col_no + 1):
                        res_val = 0
                        for k in range(1, self._col_no + 1):
                            value1 = self._matrix[i - 1][k - 1]
                            value2 = other._matrix[k - 1][j - 1]
                            if (value1 == 0 or value1 == 1) and (
                                    value2 == 0 or value2 == 1):
                                res_val = res_val | (value1 & value2)
                            else:
                                return None
                        values.append(res_val)
                retval = Matrix(self._row_no, other._col_no)
                print(values)
                retval.insert_all(values)
                return retval
            else:
                return None
        else:
            return None

    def __add__(self, other):
        """
        This method finds the addition of the given matries.The calling object
        is NOT modified in place.

        Arguments: other -- The matrix object to be added

        Returns: Matrix -- A reference to the resulting matrix or None if the
            request was invalid.
        """
        if dimensions_match(self, other):
            retval = Matrix(self._row_no, self._col_no)
            retval._matrix = np.add(self._matrix, other._matrix)
            return retval
        else:
            return None

    def __sub__(self, other):
        """
        This method finds the subtraction of the given matries.The calling
        object is NOT modified in place.

        Arguments: other -- The matrix object to be subtracted

        Returns: Matrix -- A reference to the resulting matrix or None if the
            request was invalid.
        """
        if dimensions_match(self, other):
            retval = Matrix(self._row_no, self._col_no)
            retval._matrix = np.subtract(self._matrix, other._matrix)
            return retval
        else:
            return None

    def __mul__(self, other):
        """
        This method finds the multiplication of the given matries.The calling
        object is NOT modified in place.

        Arguments: other -- The matrix object to be multiplied

        Returns: Matrix -- A reference to the resulting matrix or None if the
            request was invalid.
        """
        if self._col_no == other._row_no:
            retval = Matrix(self._row_no, other._col_no)
            retval._matrix = np.dot(self._matrix, other._matrix)
            return retval
        else:
            return None

    def __pow__(self, pow):
        """
        This method finds the power of the given matrix raised to the pow
        parameter.The calling object is NOT modified in place.

        Arguments: pow -- The power

        Returns: Matrix -- A reference to the resulting matrix or None if the
            request was invalid. For a power of 0 the identity matrix of input
            matrix row size will be returned.
        """
        if pow == 0:
            return get_identity_matrix(self._row_no)
        if pow > 0:
            retval = self
            for i in range(pow - 1):
                retval = retval * self
            return retval
        else:
            return None

    def __ilshift__(self, shift_val):
        """
        This method left shifts each value in the matrix. The calling object is
        NOT modified in place.

        Arguments: shift_val -- The shift value

        Returns: Matrix -- A reference to the resulting matrix.
        """

        retval = Matrix(self._row_no, self._col_no)
        for i in range(self._row_no):
            for j in range(self._col_no):
                retval._matrix[i][j] = self._matrix[i][j] << shift_val
        return retval

    def __irshift__(self, shift_val):
        """
        This method right shifts each value in the matrix. The calling object is
        NOT modified in place.

        Arguments: shift_val -- The shift value

        Returns: Matrix -- A reference to the resulting matrix.
        """
        retval = Matrix(self._row_no, self._col_no)
        for i in range(self._row_no):
            for j in range(self._col_no):
                retval._matrix[i][j] = self._matrix[i][j] >> shift_val
        return retval

    def __and__(self, other):
        """
        This method finds the elementwise bitwise AND of the given matries.The
        calling object is NOT modified in place.

        Arguments: other -- The matrix object to be AND-ed with

        Returns: Matrix -- A reference to the resulting matrix or None if the
            request was invalid.
        """
        if dimensions_match(self, other):
            retval = Matrix(self._row_no, self._col_no)
            retval._matrix = np.bitwise_and(self._matrix, other._matrix)
            return retval
        else:
            return None

    def __or__(self, other):
        """
        This method finds the elementwise bitwise OR of the given matries.The
        calling object is NOT modified in place.

        Arguments: other -- The matrix object to be OR-ed with

        Returns: Matrix -- A reference to the resulting matrix or None if the
            request was invalid.
        """
        if dimensions_match(self, other):
            retval = Matrix(self._row_no, self._col_no)
            retval._matrix = np.bitwise_or(self._matrix, other._matrix)
            return retval
        else:
            return None

    def __xor__(self, other):
        """
        This method finds the elementwise bitwise XOR of the given matries.The
        calling object is NOT modified in place.

        Arguments: other -- The matrix object to be XOR-ed with

        Returns: Matrix -- A reference to the resulting matrix or None if the
            request was invalid.
        """
        if dimensions_match(self, other):
            retval = Matrix(self._row_no, self._col_no)
            retval._matrix = np.bitwise_xor(self._matrix, other._matrix)
            return retval
        else:
            return None

    def __str__(self):
        """
        This method retruns the string representation of the matrix.

        Returns: str -- The matrix's string representation
        """
        return str(self._matrix)


def dimensions_match(matrix1, matrix2):
    """
    This function checks if the orders of the given matrices match.

    Arguments: matrix1 {Matrix} - The first Matrix object matrix2 {Matrix} - The
        second Matrix object

    Returns: boolean-- True or False depending on if their orders match or not.
    """
    return matrix1.get_row_no() ==  matrix2.get_row_no() and matrix1.get_col_no() == matrix2.get_col_no()


def get_identity_matrix(size):
    """
    This method creates and returns an identity Matrix object of the requested
    size.

    Arguments: size {int} -- Size of identity matrix

    Returns: Matrix -- The identity matrix.
    """
    retval = Matrix(size, size)
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if i == j:
                retval.set_value(i, j, 1)
    return retval
