from django.conf.urls import url
from app1 import views

#template tagging
app_name='app1'
urlpatterns=[

    url(r'^base2/$',views.base,name="ba"),
    url(r'^other2/$',views.other,name="ot"),

]