from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .utils import parse_and_insert


def index(request):
    url = request.POST.get("url")
    resp = ""

    if url and "fabelio.com" in url:
        resp = parse_and_insert(url)

    return render(request, "home.html", {"resp": resp})


def product_list_page(request):
    product_list = Product.objects.all()
    return render(request, "product_list.html", {"product_list": product_list})


def product_detail_page(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "product_detail.html", {"product": product})
