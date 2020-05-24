from django.shortcuts import render
from blog.mathsrc.matrix import *
from .clean_up import *
# Create your views here.


# def home(request):
# return render(request, 'blog/home.html')


def home(request):
    return render(request, 'blog/home.html')


def choose(request):
    """
    This function takes the choice of operation from home.html
    and redirects the user to the appropriate page to begin 
    entering the values fro the discrete math calculation
    """
    if request.method == "POST":
        operation = request.POST['choice']
        if operation == "0":
            return render(request, 'blog/home.html')
        if operation == "Matrix Addition":
            return render(request, 'blog/op_addition.html')


def add(request):
    """
    This function is called when the user chooses matrix addition as
    the desired operation and clicks the add button. It defines the 
    matrices, initializes them with values and adds and displays the
    result.
    """
    if request.method == "POST":
        m1 = Matrix(int(request.POST['m1_rows']),  # request.POST['m1_rows'] gives the value entered in the m1_rows field in the html input
                    int(request.POST['m1_columns']))
        m1.insert_all(clean(request.POST['m1_entry']))
        m2 = Matrix(int(request.POST['m2_rows']),
                    int(request.POST['m2_columns']))
        m2.insert_all(clean(request.POST['m2_entry']))
        print(m1+m2)
        return render(request, 'blog/home.html')
