from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy
from django.http import HttpResponse

"""
normal way
def index(request):
    return render(request,'index.html')
"""
"""
using View method
class Cbv(View):
    def get(self,request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")
"""

"""
#using TemplateView

class Indexview(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['injectme']='base injectiom'
        return context
        """

class Indexview(TemplateView):
    template_name='index.html'

class SchoolListView(ListView):
    context_oject_name='schools'
    model=models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model =models.School
    template_name = 'advpro/school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model =models.School

class SchoolDeleteView(DeleteView):
    model =models.School
    success_url= reverse_lazy("advpro:list")