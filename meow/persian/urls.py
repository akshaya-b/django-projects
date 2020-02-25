from django.urls import path
from persian import views

app_name='persian'
urlpatterns = [
    path("",views.index,name='index'),
    path("register/",views.form ,name='register'),
    path("familydetails/",views.details,name='famdet'),




]
