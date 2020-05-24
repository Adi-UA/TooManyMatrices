from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('choose/', views.choose, name='choose'),
    path('add/', views.add, name='op_add')
]
