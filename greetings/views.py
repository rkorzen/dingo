from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request, name="World!"):
    return HttpResponse(f"Hello {name}")


def about(request):
    return HttpResponse("About me")


def contact(request):
    return HttpResponse("Contact")


def welcome(request):
    return render(
        request=request,
        template_name="greetings/welcome.html",
        context={}
    )
