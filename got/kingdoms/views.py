from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy
# Create your views here.
class Indexview(TemplateView):
    template_name='index.html'

class RegionListView(ListView):
    model=models.Region

class RegionDetailView(DetailView):
    context_object_name = 'regiondetail'
    model =models.Region
    template_name = 'kingdoms/region_detail.html'

class RegionCreateView(CreateView):
    fields = ('name','climate')
    model = models.Region

class RegionUpdateView(UpdateView):
    fields=('name','climate')
    model =models.Region

class RegionDeleteView(DeleteView):
    model =models.Region
    success_url= reverse_lazy("kingdoms:list")
