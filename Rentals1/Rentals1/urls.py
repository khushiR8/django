"""
URL configuration for Rental1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

from django.urls import include

urlpatterns += [
    path('rentals/', include('rentals.urls', namespace='rentals')),
]

urlpatterns += [
    path('rentalsexternalcss/', include('rentalsexternalcss.urls', namespace='rentalsexternalcss')),
]

urlpatterns += [
    path('rentalstemplates/', include('rentalstemplates.urls', namespace='rentalstemplates')),
]


urlpatterns += [
    path('rentalsescaping/', include('rentalsescaping.urls', namespace='rentalsescaping')),
]

urlpatterns += [
    path('rentalsmodel/', include('rentalsmodel.urls', namespace='rentalsmodel')),
]