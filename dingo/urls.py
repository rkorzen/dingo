"""dingo URL Configuration

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
# dingo/urls.py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def math(request):
    return HttpResponse("Tu będzie matma")


def add(request, a, b):
    a, b = int(a), int(b)
    return HttpResponse(a + b)


def sub(request, a, b):
    a, b = int(a), int(b)
    return HttpResponse(a - b)


def mul(request, a, b):
    a, b = int(a), int(b)
    return HttpResponse(a * b)


def div(request, a, b):
    a, b = int(a), int(b)
    if b == 0:
        return HttpResponse("Nie dziel przez 0")
    return HttpResponse(a / b)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('maths/', math),
    path('maths/add/<int:a>/<int:b>', add),
    path('maths/sub/<int:a>/<int:b>', sub),
    path('maths/mul/<int:a>/<int:b>', mul),
    path('maths/div/<int:a>/<int:b>', div),
]
