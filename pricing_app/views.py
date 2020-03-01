from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .utils import parse_and_insert


def index(request, *args, **kwargs):
    url = request.POST.get("url")
    resp = ""

    if url and "fabelio.com" in url:
        # url = 'https://fabelio.com/ip/kubos-2020-frame.html'
        resp = parse_and_insert(url)

    return render(request, "home.html", {"resp": resp})


def product_list_page(request, *args, **kwargs):
    # list = Product.objects.all()
    return render(request, "product_list.html", {})


def product_detail_page(request, *args, **kwargs):
    return render(request, "product_detail.html", {})
