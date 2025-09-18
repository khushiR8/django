from django.urls import path
from . import views

#connect views to urls
urlpatterns = [
    path("", views.index, name="index"), #starting point so it starts at root, hence ""
    path("about/", views.about, name="about"),
]


