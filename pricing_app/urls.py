from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.product_list_page),
    path("product/<product_id>/", views.product_detail_page),
]
