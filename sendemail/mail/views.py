from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hello from Akshaya',
    'body of the mail',
    'akshayabaskaran1996@gmail.com',
    ['todacil232@mailseo.net'],
    fail_silently=False
    )
    return render(request,'mail/index.html')
