from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tmm-home'),  # redirects to home.html page
    path('choose/', views.choose, name='choose'),
    path('add/', views.add, name='op_add'),  # redirects to op_addition.html
    # redirects to op_addition.html
    path('subtract/', views.subtract, name='op_subtract'),
    path('multiply/', views.multiply, name='op_multiply'),
    path('bitwiseor/', views.bit_or, name='op_bitwiseOR'),
    path('bitwiseand/', views.bit_and, name='op_bitwiseAND'),
    path('bitwisexor/', views.bit_xor, name='op_bitwiseXOR'),
    path('power/', views.power, name='op_power'),
    path('rightshift/', views.right_shift, name='op_right_shift'),

]
