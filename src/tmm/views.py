from django.shortcuts import render
from tmm.mathsrc.matrix import *
from .utility import *

__author__ = "Ved Shah"
__status__ = "Development"

# def home(request):
# return render(request, 'blog/home.html')


def home(request):
    return render(request, 'tmm/home.html')


def choose(request):
    """
    This function takes the choice of operation from home.html
    and redirects the user to the appropriate page to begin
    entering the values fro the discrete math calculation

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        operation = request.POST['choice']
        if operation == "0":
            return render(request, 'tmm/home.html')
        if operation == "Matrix Addition":
            return render(request, 'tmm/op_addition.html')
        if operation == "Matrix Subtraction":
            return render(request, 'tmm/op_subtraction.html')
        if operation == "Matrix Multiplication":
            return render(request, 'tmm/op_multiplication.html')


def add(request):
    """
    This function is called when the user chooses matrix addition as
    the desired operation and clicks the add button. It defines the
    matrices, initializes them with values and adds and displays the
    result.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        m1 = Matrix(int(request.POST['m_rows']),  # request.POST['m1_rows'] gives the value entered in the m1_rows field in the html input
                    int(request.POST['m_columns']))
        m1.insert_all(clean(request.POST['m1_entry']))
        m2 = Matrix(int(request.POST['m_rows']),
                    int(request.POST['m_columns']))
        m2.insert_all(clean(request.POST['m2_entry']))
        result_add = matrix_to_list(m1+m2)
        return render(request, 'tmm/op_addition.html', {'content': result_add})


def subtract(request):
    """
    This function is called when the user chooses matrix subtraction as
    the desired operation and clicks the subtract button. It defines the
    matrices, initializes them with values and subtracts and displays the
    result.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        m1 = Matrix(int(request.POST['m_rows']),  # request.POST['m1_rows'] gives the value entered in the m1_rows field in the html input
                    int(request.POST['m_columns']))
        m1.insert_all(clean(request.POST['m1_entry']))
        m2 = Matrix(int(request.POST['m_rows']),
                    int(request.POST['m_columns']))
        m2.insert_all(clean(request.POST['m2_entry']))
        result_subtract = matrix_to_list(m1-m2)
        return render(request, 'tmm/op_subtraction.html', {'content': result_subtract})


def multiply(request):
    """
    This function is called when the user chooses matrix multiplication as
    the desired operation and clicks the multiply button. It defines the
    matrices, initializes them with values and multiplies and displays the
    result.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        m1 = Matrix(int(request.POST['m1_rows']),  # request.POST['m1_rows'] gives the value entered in the m1_rows field in the html input
                    int(request.POST['m2_columns']))
        m1.insert_all(clean(request.POST['m1_entry']))
        m2 = Matrix(int(request.POST['m2_rows']),
                    int(request.POST['m2_columns']))
        m2.insert_all(clean(request.POST['m2_entry']))
        result_multiply = matrix_to_list(m1*m2)
        return render(request, 'tmm/op_multiplication.html', {'content': result_multiply})
