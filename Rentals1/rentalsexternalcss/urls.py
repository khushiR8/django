from django.urls import path
from . import views
app_name = "rentalsexternalcss"
urlpatterns = [
    path('', views.index, name='index'),
    path('review/', views.review, name='review'),
    ]