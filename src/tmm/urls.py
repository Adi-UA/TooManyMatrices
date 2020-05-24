from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tmm-home'),  # redirects to home.html page
    path('choose/', views.choose, name='choose'),
    path('add/', views.add, name='op_add'),  # redirects to op_addition.html
]
