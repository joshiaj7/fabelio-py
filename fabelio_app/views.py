from django.http import HttpResponse
from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, "home.html", {})


# def index(request):
#     return HttpResponse("<h1>WELCOME TO MY APP</h1>")
