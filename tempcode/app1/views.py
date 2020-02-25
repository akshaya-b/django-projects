from django.shortcuts import render


# Create your views here.
def index(request):


    return  render(request,"app1/index.html")

def base(request):
    context_dict = {'word': 'hello world', 'numeric': '57'}
    return  render(request,"app1/base.html",context_dict)

def other(request):
    return  render(request,"app1/other.html")
