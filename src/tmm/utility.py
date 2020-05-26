from tmm.mathsrc.matrix import *

__author__ = "Ved Shah"
__status__ = "Development"


def clean(s, isInt=False):
    """
    This function takes the string input from the HTML text area
    field and converts those entries into a list of floating-point numbers or integers 
    (for bitwise operations) which will be used to intialize the matrices.

    This function assumes the string only has number values separated by space.

    Arguments:
        s [str] -- The string to be convereted into a list of floating-point numbers
        must be space separated and can be on newlines.

        isInt [boolean] -- It tells the function if the values returned need to be
        integers or not

    Returns:
        list -- Python list of floating-point numbers from the string
    """
    temp = s.split()
    for i in range(0, len(temp)):
        if isInt:
            temp[i] = int(temp[i])
        else:
            temp[i] = float(temp[i])
    return temp


def matrix_to_list(m):
    """
    This function takes a matrix argument and reformats it to a list of string.
    Its purpose is to make it possible for the matrix to be displayed appropriately
    on a html webpage

    Arguments:
        m [matrix] -- The matrix that needs to be reformated into a list of strings

    Returns:
        list -- Python list of strings from floating-point numbers
    """
    matrix_string = []
    for i in range(1, m.get_row_no()+1):
        s = ""
        for j in range(1, m.get_col_no()+1):
            s += str(m.get_value(i, j)) + " "
        matrix_string.append(s)
    return matrix_string
