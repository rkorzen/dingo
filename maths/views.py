# maths/views.py
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from maths.forms import ResultForm
from maths.models import Math, Result


def math(request):
    return render(
        request=request,
        template_name="maths/../templates/main.html",
        context={}
    )


def add(request, a, b):
    wynik = a + b
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='add', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


def sub(request, a, b):
    wynik = a - b
    c = {"a": a, "b": b, "operacja": "-", "wynik": wynik, "title": "odejmowanie"}
    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='sub', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


def mul(request, a, b):
    wynik = a * b
    c = {"a": a, "b": b, "operacja": "*", "wynik": wynik, "title": "mnożenie"}
    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='mul', a=a, b=b, result=result)
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
    if wynik == "Error":
        result = Result.objects.get_or_create(error=wynik)[0]
    else:
        result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='add', a=a, b=b, result=result)
    Math.objects.create(operation='add', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )

@login_required
def maths_list(request):
    operation = request.GET.get('operation')
    if operation:
        maths = Math.objects.filter(operation=operation)
    else:
        maths = Math.objects.all()
    paginator = Paginator(maths, 5)
    page_number = request.GET.get('page')
    maths = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="maths/list.html",
        context={"maths": maths, 'active': "maths"}
    )


def math_details(request, id):
    math = Math.objects.get(id=id)
    return render(
        request=request,
        template_name="maths/details.html",
        context={"math": math, 'active': "maths"}
    )


def results_list(request):
    if request.method == "POST":
        form = ResultForm(data=request.POST)

        if form.is_valid():
            Result.objects.get_or_create(**form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy Result!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = ResultForm()
    results = Result.objects.all()
    return render(
        request=request,
        template_name="maths/results.html",
        context={
            "results": results,
            "form": form
        }
    )
