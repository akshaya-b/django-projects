from django.shortcuts import render
from django.core.mail import send_mail
from .models import Opratable, Oprajsn
import datetime


# Create your views here.
# def index(request):
#     send_mail('sub:Hello from Akshaya',
#     'todays report',
#     'akshayabaskaran1996@gmail.com',
#     ['dapacap827@iwebtm.com'],
#     fail_silently=False
#     )
#     return render(request,'opralog/index.html')

def index(request):
    x = datetime.datetime.now()
    y=(x.strftime("%d/%m/%y"))
    filelist= Opratable.objects.filter(date=y)
    print(filelist)
    filedict={'fam':filelist}
    return render(request,'opralog/index.html',filedict)

def weather(request):
    mainlist= Oprajsn.objects.filter(main='Clouds')
    maindict={'main':mainlist}
    return render(request,'opralog/main.html',maindict)
