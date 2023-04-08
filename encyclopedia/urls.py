from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("srch", views.srch, name="search"),
    path("wiki/<str:name>", views.default_route, name="main_route")
]
