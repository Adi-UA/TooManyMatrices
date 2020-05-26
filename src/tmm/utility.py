from tmm.mathsrc.matrix import *

__author__ = "Ved Shah"
__status__ = "Development"


def matrix_builder(request, mindex, entry_index, isSquare=False):
    m_row_no = int(request.POST[mindex + '_rows'])

    if isSquare:
        m_col_no = int(request.POST[mindex + '_rows'])
    else:
        m_col_no = int(request.POST[mindex + '_columns'])

    m = Matrix(m_row_no, m_col_no)
    m_entries = request.POST[entry_index + '_entry'].strip()

    return m, m_entries


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
    for i in range(1, m.get_row_no() + 1):
        s = ""
        for j in range(1, m.get_col_no() + 1):
            s += str(m.get_value(i, j)) + " "
        matrix_string.append(s)
    return matrix_string


def order_checker(m1, m2, m1_entries, m2_entries):
    """
     This Function takes the html request and two matrices and makes sure that that the
    order of each of the matrix is consistent with the order of the entered values

    Arguments:
        m1 {Matrix} -- Matrix 1
        m2 {Matrix} -- Matrix 2 or None for one matrix
        m1_entries {str} -- The string of characters to input into m1
        m2_entries {str} -- The string of characters to input into m2 or None
        for one matrix

    Returns:
        boolean -- True if everything is consistent and False
    """

    # Sanity chcek for input and actual dimensions of m1
    m1_new_line_split = m1_entries.split("\n")
    m1_row_no = len(m1_new_line_split)
    m1_col_no = len(m1_new_line_split[0].split())

    if m2 is not None:
        # Sanity chcek for input and actual dimensions of m2
        m2_new_line_split = m2_entries.split("\n")
        m2_row_no = len(m2_new_line_split)
        m2_col_no = len(m2_new_line_split[0].split())

        return (m1.get_row_no() == m1_row_no
                and m1.get_col_no() == m1_col_no
                and m2.get_row_no() == m2_row_no
                and m2.get_col_no() == m2_col_no)
    else:
        return (m1.get_row_no() == m1_row_no
                and m1.get_col_no() == m1_col_no)
