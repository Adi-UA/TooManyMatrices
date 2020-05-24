from django.shortcuts import render
from blog.mathsrc.matrix import *
# Create your views here.


# def home(request):
# return render(request, 'blog/home.html')


def home(request):
    return render(request, 'blog/home.html')


def choose(request):
    if request.method == "POST":
        operation = request.POST['choice']
        if operation == "0":
            return render(request, 'blog/home.html')
        if operation == "Matrix Addition":
            return render(request, 'blog/op_addition.html')


def add(request):
    if request.method == "POST":
        m1_r = int(request.POST['m1_rows'])
        m1_c = int(request.POST['m1_columns'])
        m1_data = request.POST['m1_entry']
        temp_1 = m1_data.split()
        m2_r = int(request.POST['m2_rows'])
        m2_c = int(request.POST['m2_columns'])
        m2_data = request.POST['m2_entry']
        temp_2 = m2_data.split()
        print(temp_1)
        print(temp_2)
        for i in range(0, len(temp_1)):
            temp_1[i] = int(temp_1[i])
        for i in range(0, len(temp_2)):
            temp_2[i] = int(temp_2[i])
        m1 = Matrix(m1_r, m1_c)
        m1.insert_all(temp_1)
        m2 = Matrix(m2_r, m2_c)
        m2.insert_all(temp_2)
        print(m1)
        print(m2)
        print(m1+m2)
        return render(request, 'blog/home.html')
