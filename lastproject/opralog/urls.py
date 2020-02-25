from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('main/',views.weather, name='weather')
]
