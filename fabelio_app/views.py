from django.http import HttpResponse
from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, "home.html", {})


def product_list_page(request, *args, **kwargs):
    return render(request, "product_list.html", {})


def product_detail_page(request, *args, **kwargs):
    return render(request, "product_detail.html", {})
