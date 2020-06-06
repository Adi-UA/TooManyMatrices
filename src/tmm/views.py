from django.shortcuts import render
from tmm.mathsrc.matrix import *
from .utility import *

# def home(request):
# return render(request, 'blog/home.html')


def home(request):
    return render(request, 'tmm/home.html')


def handler404(request, exception):
    return render(request, 'tmm/404.html', status=404)


def handler500(request):
    return render(request, 'tmm/500.html', status=500)


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
        if operation == "Matrix Bitwise OR":
            return render(request, 'tmm/op_bitwise_OR.html')
        if operation == "Matrix Bitwise AND":
            return render(request, 'tmm/op_bitwise_AND.html')
        if operation == "Matrix Bitwise XOR":
            return render(request, 'tmm/op_bitwise_XOR.html')
        if operation == "Matrix Power":
            return render(request, 'tmm/op_power.html')
        if operation == "Matrix Right Shift":
            return render(request, 'tmm/op_right_shift.html')
        if operation == "Matrix Left Shift":
            return render(request, 'tmm/op_left_shift.html')
        if operation == "Matrix Scalar Multiplication":
            return render(request, 'tmm/op_scalar_multiplication.html')
        if operation == "Transpose":
            return render(request, 'tmm/op_transpose.html')
        if operation == "Boolean Product":
            return render(request, 'tmm/op_bool_product.html')
        if operation == "Boolean Power":
            return render(request, 'tmm/op_bool_power.html')
        if operation == "Matrix Determinant":
            return render(request, 'tmm/op_determinant.html')
        if operation == "Matrix Cofactor":
            return render(request, 'tmm/op_cofactor.html')
        if operation == "Matrix Adjoint":
            return render(request, 'tmm/op_adjoint.html')
        if operation == "Matrix Minor":
            return render(request, 'tmm/op_find_minor.html')
        if operation == "Matrix Inverse":
            return render(request, 'tmm/op_inverse.html')


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
        page = 'tmm/op_addition.html'
        m1, m1_entries = matrix_builder(request, "m", "m1")
        m2, m2_entries = matrix_builder(request, "m", "m2")

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})
        else:
            if order_checker(m1, m2, m1_entries, m2_entries):
                m1.insert_all(clean(m1_entries))
                m2.insert_all(clean(m2_entries))
                result_add = matrix_to_list(m1 + m2)
                return render(request,
                              page,
                              {'content': result_add})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


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
        page = 'tmm/op_subtraction.html'

        m1, m1_entries = matrix_builder(request, "m", "m1")
        m2, m2_entries = matrix_builder(request, "m", "m2")

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, m2, m1_entries, m2_entries):
                m1.insert_all(clean(m1_entries))
                m2.insert_all(clean(m2_entries))

                result_subtract = matrix_to_list(m1 - m2)
                return render(request,
                              page,
                              {'content': result_subtract})
            else:
                return render(request,
                              page,
                              {'error': [ERROR_DICT[0]]})


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
        page = 'tmm/op_multiplication.html'

        m1, m1_entries = matrix_builder(request, "m1", "m1")
        m2, m2_entries = matrix_builder(request, "m2", "m2")

        if m1 == False or m2 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})
        else:
            if order_checker(m1, m2, m1_entries, m2_entries):
                if m1.get_col_no() == m2.get_row_no():
                    m1.insert_all(clean(m1_entries))
                    m2.insert_all(clean(m2_entries))
                    result_multiply = matrix_to_list(m1 * m2)
                    return render(request, page, {'content': result_multiply})
                else:
                    return render(request,
                                  page,
                                  {'error': [ERROR_DICT[1],
                                             ERROR_DICT[2]]})

            else:
                return render(request,
                              page,
                              {'error': [ERROR_DICT[0]]})


def bit_or(request):
    """
    This function is called when the user chooses matrix bitwise or as
    the desired operation and clicks the submit button. It defines the
    matrices, initializes them with values and computes and displays the
    result.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_bitwise_OR.html'

        m1, m1_entries = matrix_builder(request, "m", "m1")
        m2, m2_entries = matrix_builder(request, "m", "m2")

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, m2, m1_entries, m2_entries):
                m1.insert_all(clean(m1_entries, True))
                m2.insert_all(clean(m2_entries, True))
                result_bit_or = matrix_to_list(m1 | m2)
                return render(request,
                              page,
                              {'content': result_bit_or})
            else:
                return render(request,
                              page,
                              {'error': [ERROR_DICT[0]]})


def bit_and(request):
    """
    This function is called when the user chooses matrix bitwise and as
    the desired operation and clicks the submit button. It defines the
    matrices, initializes them with values and computes and displays the
    result.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_bitwise_AND.html'

        m1, m1_entries = matrix_builder(request, "m", "m1")
        m2, m2_entries = matrix_builder(request, "m", "m2")

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, m2, m1_entries, m2_entries):
                m1.insert_all(clean(m1_entries, True))
                m2.insert_all(clean(m2_entries, True))
                result_bit_and = matrix_to_list(m1 & m2)
                return render(request,
                              page,
                              {'content': result_bit_and})

            else:
                return render(request,
                              page,
                              {'error': [ERROR_DICT[0]]})


def bit_xor(request):
    """
    This function is called when the user chooses matrix bitwise xor as
    the desired operation and clicks the submit button. It defines the
    matrices, initializes them with values and computes and displays the
    result.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_bitwise_XOR.html'

        m1, m1_entries = matrix_builder(request, "m", "m1")
        m2, m2_entries = matrix_builder(request, "m", "m2")

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, m2, m1_entries, m2_entries):
                m1.insert_all(clean(m1_entries, True))
                m2.insert_all(clean(m2_entries, True))
                result_bit_xor = matrix_to_list(m1 ^ m2)
                return render(request,
                              page,
                              {'content': result_bit_xor})
            else:
                return render(request,
                              page,
                              {'error': [ERROR_DICT[0]]})


def power(request):
    """
    This function is called when the user chooses matrix power as
    the desired operation and clicks the submit button. It defines the
    matrices, initializes them with values and computes and displays the
    matrix raised to the power.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_power.html'

        m1, m1_entries = matrix_builder(request, "m", "m1", True)
        power = request.POST['pow']

        if m1 == False or input_checker(power) == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries))
                power = int(power)

                result_power = matrix_to_list(m1 ** power)
                return render(request, page,
                              {'content': result_power})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def right_shift(request):
    """
    This function is called when the user chooses matrix right shift as
    the desired operation and clicks the submit button. It defines the
    matrices, initializes them with values and computes and displays the
    right shifted matrix.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_right_shift.html'

        m1, m1_entries = matrix_builder(request, "m", "m1")
        shift = request.POST['shift']

        if m1 == False or input_checker(shift) == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries, True))
                shift = int(shift)

                result_right_shift = matrix_to_list(m1 >> shift)
                return render(request, page,
                              {'content': result_right_shift})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def left_shift(request):
    """
    This function is called when the user chooses matrix left shift as
    the desired operation and clicks the submit button. It defines the
    matrices, initializes them with values and computes and displays the
    left shifted matrix.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_left_shift.html'

        m1, m1_entries = matrix_builder(request, "m", "m1")
        shift = request.POST['shift']

        if m1 == False or input_checker(shift) == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries, True))
                shift = int(shift)

                result_left_shift = matrix_to_list(m1 << shift)
                return render(request, page,
                              {'content': result_left_shift})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def scalar_multiply(request):
    """
    This function is called when the user chooses matrix scalar multiplication as
    the desired operation and clicks the submit button. It defines the
    matrices, initializes them with values and computes and displays the
    right shifted matrix.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_scalar_multiplication.html'

        m1, m1_entries = matrix_builder(request, "m", "m1")
        multiplier = request.POST['multiplier']

        if m1 == False or input_checker(multiplier) == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries))
                multiplier = int(multiplier)

                result_scalar_multiply = matrix_to_list(m1 * multiplier)
                return render(request, page,
                              {'content': result_scalar_multiply})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def transpose(request):
    """
    This function is called when the user chooses matrix transpose as
    the desired operation and clicks the submit button. It defines the
    matrices, initializes them with values and computes and displays the
    transpose of the matrix.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_transpose.html'

        m1, m1_entries = matrix_builder(request, "m", "m1")

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries))
                result_transpose = matrix_to_list(m1.transpose())
                return render(request, page,
                              {'content': result_transpose})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def boolean_multiply(request):
    """
    This function is called when the user chooses boolean produuct as
    the desired operation and clicks the multiply button. It defines the
    matrices, initializes them with values and multiplies and displays the
    result.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_bool_product.html'

        m1, m1_entries = matrix_builder(request, "m1", "m1")
        m2, m2_entries = matrix_builder(request, "m2", "m2")

        if m1 == False or m2 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, m2, m1_entries, m2_entries):
                if m1.get_col_no() == m2.get_row_no():
                    m1.insert_all(clean(m1_entries, True))
                    m2.insert_all(clean(m2_entries, True))
                    result = m1.boolean_product(m2)
                    if result is None:
                        return render(request, page,
                                      {'error': [ERROR_DICT[3]]})
                    else:
                        result_bool_product = matrix_to_list(result)
                        return render(request,
                                      page,
                                      {'content': result_bool_product})
                else:
                    return render(request,
                                  page,
                                  {'error': [ERROR_DICT[1],
                                             ERROR_DICT[2]]})
            else:
                return render(request,
                              page,
                              {'error': [ERROR_DICT[0]]})


def boolean_power(request):
    """
    This function is called when the user chooses matrix power as
    the desired operation and clicks the submit button. It defines the
    matrices, initializes them with values and computes and displays the
    matrix raised to the power.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_bool_power.html'

        m1, m1_entries = matrix_builder(request, "m", "m1", True)
        power = request.POST['pow']

        if m1 == False or input_checker(power) == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries, True))
                power = int(power)

                result = m1.boolean_power(power)
                if result is None:
                    return render(request, page,
                                  {'error': [ERROR_DICT[3]]})
                else:
                    result_power = matrix_to_list(result)
                    return render(request, page,
                                  {'content': result_power})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def determinant(request):
    """
    This function handles the matrix determinant request from the user.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_determinant.html'

        m1, m1_entries = matrix_builder(request, "m", "m1", True)

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries))
                result = m1.det()
                return render(request, page,
                              {'content': [result]})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def cofactor(request):
    """
    This function handles the matrix cofactor request from the user.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_cofactor.html'

        m1, m1_entries = matrix_builder(request, "m", "m1", True)

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries))
                result = matrix_to_list(m1.cofactor())
                return render(request, page,
                              {'content': result})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def adjoint(request):
    """
    This function handles the matrix adjoint request from the user.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_adjoint.html'

        m1, m1_entries = matrix_builder(request, "m", "m1", True)

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries))
                result = matrix_to_list(m1.adjoint())
                return render(request, page,
                              {'content': result})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def inverse(request):
    """
    This function handles the matrix inverse request from the user.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_inverse.html'

        m1, m1_entries = matrix_builder(request, "m", "m1", True)

        if m1 == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries))
                result = m1.inv()

                if result is not None:
                    return render(request, page,
                                  {'content': matrix_to_list(result)})
                else:
                    return render(request, page,
                                  {'error': [ERROR_DICT[4]]})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})


def find_minor(request):
    """
    This function handles the matrix minor request from the user at the
    specified row and column.

    Returns:
        The rendered page view
    """
    if request.method == "POST":
        page = 'tmm/op_find_minor.html'

        m1, m1_entries = matrix_builder(request, "m", "m1", True)
        r = request.POST['row']
        c = request.POST['col']

        if m1 == False or input_checker(r) == False or input_checker(c) == False:
            return render(request, page,
                          {'error': [ERROR_DICT[5]]})

        else:
            if order_checker(m1, None, m1_entries, None):
                m1.insert_all(clean(m1_entries))
                r = int(r)
                c = int(c)
                result = m1.find_minor(r, c)

                if result is not None:
                    return render(request, page,
                                  {'content': matrix_to_list(result)})
                else:
                    return render(request, page,
                                  {'error': ['Your row or column was invalid']})
            else:
                return render(request, page,
                              {'error': [ERROR_DICT[0]]})
