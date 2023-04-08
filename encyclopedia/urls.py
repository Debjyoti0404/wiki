from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("srch", views.srch, name="search"),
    path("create", views.create_pg, name="pg_create"),
    path("wiki/<str:name>", views.default_route, name="entry_route")
    
]
