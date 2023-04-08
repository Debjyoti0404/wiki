from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_pg, name="pg_create"),
    path("edit/<str:name>", views.edit_pg, name="edit"),
    path("random", views.random_pg, name="random"),
    path("srch", views.srch, name="search"),
    path("wiki/<str:name>", views.default_route, name="entry_route")
    
]
