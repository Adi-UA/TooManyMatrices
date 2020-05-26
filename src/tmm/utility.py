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


def order_checker(request, m1, m2):
    """
    This Function takes the html request and two matrices and makes sure that that the 
    order of each of the matrix is consistent with the order of the entered values

    Arguments:
        request {HTML request} -- HTML POST/GET request
        m1 {matrix} -- The first Matrix for which you want to run the test
        m2 {matrix} -- The second Matrix for which you want to run the test

    Returns:
        boolean -- returns true if the order are consistent with the input data.
    """
    if m1.get_row_no() == get_string_rows(request.POST['m1_entry']) and m1.get_col_no() == get_string_columns(request.POST['m1_entry']) and m2.get_row_no() == get_string_rows(request.POST['m2_entry']) and m2.get_col_no() == get_string_columns(request.POST['m2_entry']):
        return True
    else:
        return False


def get_string_rows(s):
    """
    This function takes the HTML matrix value string and computes the number of rows.

    Arguments:
        s {string} -- Martrix input string for which the number of rows needs to be computed.
    
    Returns:
        int -- Number of rows
    """
    temp = s.split("\n")
    return(int(len(temp)))


def get_string_columns(s):
    """
    This function takes the HTML matrix value string and computes the number of columns.

    Arguments:
        s {string} -- Martrix input string for which the number of columns needs to be computed.
    
    Returns:
        int -- Number of columns
    """
    temp = s.split("\n")
    temp = temp[0].split()
    return(len(temp))
