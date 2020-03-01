from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request, *args, **kwargs):
    print("request POST: {}".format(request.POST))
    print("request POST: {}".format(request.POST.get("url")))

    return render(request, "home.html", {})


def product_list_page(request, *args, **kwargs):
    # list = Product.objects.all()
    return render(request, "product_list.html", {})


def product_detail_page(request, *args, **kwargs):
    return render(request, "product_detail.html", {})
