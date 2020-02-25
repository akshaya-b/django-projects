from django.shortcuts import render,redirect
from log.forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'account is created form the user {username} !!' )
            return redirect('login')
    else:
        form = UserForm()
    return render(request,'log/register.html',{'form':form})
@login_required
def home(request):
    return render(request,'log/home.html')

def index(request):
    return render(request,'log/index.html')
# Create your views here.
