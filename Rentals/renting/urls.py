from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #starting point so it starts at root, hence ""
    path("about/", views.about, name="about"),
]


