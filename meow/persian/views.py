from django.shortcuts import render
from persian.forms import Familyform
from persian.models import Family
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    return render(request,"persian/Persian.html")

def form(request):
    form=Familyform()

    if request.method=='POST':
        form=Familyform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:

            print("Error Form invalid")

    return render(request,'persian/register.html',{'form':form})


def details(request):
    famlist= Family.objects.order_by('husky')
    print(famlist)
    famdict={'fam':famlist}
    return render(request,'persian/familydetails.html',famdict)











# Create your views here.
