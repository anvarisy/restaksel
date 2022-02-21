"""restaksel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from api.views import CreateSantri, GetAllSantri, GetSantriById, UpdateSantri, DeleteSantri

urlpatterns = [
    path('admin/', admin.site.urls),
    path('santri/create/', CreateSantri.as_view()),
    path('santri/get/', GetAllSantri.as_view()),
    path('santri/update/<str:nis>/', UpdateSantri.as_view()),
    path('santri/get/<str:nis>/', GetSantriById.as_view()),
    path('santri/delete/<str:nis>/', DeleteSantri.as_view()),
]
