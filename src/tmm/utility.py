from tmm.mathsrc.matrix import *


def clean(s):
    """
    This function takes the string input from the HTML text area
    field and converts those entries into a list of floating-point numbers which
    will be used to intialize the matrices.

    This function assumes the string only has number values separated by space.

    Arguments:
        s [str] -- The string to be convereted into a list of floating-point numbers
        must be space separated and can be on newlines.

    Returns:
        list -- Python list of floating-point numbers from the string
    """
    temp = s.split()
    for i in range(0, len(temp)):
        temp[i] = float(temp[i])
    return temp


def matrix_to_list(m):
    matrix_string = []
    for i in range(1, m.get_row_no()+1):
        s = ""
        for j in range(1, m.get_col_no()+1):
            s += str(m.get_value(i, j)) + " "
        matrix_string.append(s)
    return matrix_string
