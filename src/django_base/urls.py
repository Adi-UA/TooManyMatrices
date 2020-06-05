"""django_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

handler404 = 'tmm.views.handler404'
handler500 = 'tmm.views.handler500'

urlpatterns = [
    path('', include('tmm.urls')),
    # Redirects to tmm.url for the localhost:8000 without the /tmm part. Basically empty stuff redirects to tmm home
    path('tmm/', include('tmm.urls')),
    # Redirects to tmm.url for the localhost:8000/tmm/
]
