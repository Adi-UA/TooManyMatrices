from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tmm-home'),  # redirects to home.html page
    path('choose/', views.choose, name='choose'),
    path('add/', views.add, name='op_add'),  # redirects to op_addition.html
    # redirects to op_addition.html
    path('subtract/', views.subtract, name='op_subtract'),
    path('multiply/', views.multiply, name='op_multiply'),
]
