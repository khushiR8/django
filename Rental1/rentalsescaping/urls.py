from django.urls import path
from . import views
app_name = "rentalsescaping"
urlpatterns = [
    path('', views.index3, name='index'),
    path('review/', views.review3, name='review'),
    ]