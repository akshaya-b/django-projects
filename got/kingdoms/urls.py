from django.conf.urls import url
from kingdoms import views

app_name='kingdoms'
urlpatterns=[
    url(r'^$',views.RegionListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.RegionDetailView.as_view(),name='detail'),
    url(r'^create/$',views.RegionCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.RegionUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.RegionDeleteView.as_view(),name='delete'),
    ]
