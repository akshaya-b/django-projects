from django.conf.urls import url
from annan import views


urlpatterns=[
    url(r'^$', views.index, name='index'),
]