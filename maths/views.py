# maths/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from maths.models import Math

def math(request):
    return HttpResponse("Tu będzie matma")


def add(request, a, b):
    wynik = a + b
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


def sub(request, a, b):
    wynik = a - b
    c = {"a": a, "b": b, "operacja": "-", "wynik": wynik, "title": "odejmowanie"}
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


def mul(request, a, b):
    wynik = a * b
    c = {"a": a, "b": b, "operacja": "*", "wynik": wynik, "title": "mnożenie"}
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


def div(request, a, b):
    if b == 0:
        wynik = "Error"
        messages.add_message(request, messages.ERROR, "Dzielenie przez zero!!")
    else:
        wynik = a / b
    c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


def maths_list(request):
    maths = Math.objects.all()
    return render(
        request=request,
        template_name="maths/list.html",
        context={"maths": maths}
    )


def math_details(request, id):
    math = Math.objects.get(id=id)
    return render(
        request=request,
        template_name="maths/details.html",
        context={"math": math}
    )
