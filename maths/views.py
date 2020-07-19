from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template


def math(request):
    return HttpResponse("Tu będzie matma")


def add(request, a, b):
    a, b = int(a), int(b)
    wynik = a + b
    t = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
Wynik operacji {{a}} + {{b}} wynosi {{wynik}}    
</body>
</html>
        """)
    c = Context({"a": a, "b": b, "wynik": wynik})
    return HttpResponse(t.render(c))


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
