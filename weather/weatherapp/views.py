from django.shortcuts import render, redirect
import requests

from weatherapp.models import City
from .forms import CityForm
# Create your views here.
def index(request):
    #url='https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    err_msg=''
    message=''
    message_class=''
    if request.method=='POST':
        form=CityForm(request.POST)

        if form.is_valid():
            new_city=form.cleaned_data['name']
            existing_city_count=City.objects.filter(name=new_city).count()
            if existing_city_count==0:
                r=requests.get(url.format(new_city)).json()
                if r['cod']==200:
                    form.save()
                else:
                    err_msg='invalid city'

            else:
                err_msg='city already exist'
        if err_msg:
            message=err_msg
            message_class='danger'
        else:
            message= 'city added successfully'
            message_class='success'

    print(err_msg)
    form=CityForm()

    cities=City.objects.all()
    weather_data=[]
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={
        'city':city,
        'temperature': r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
        }
        weather_data.append(city_weather)
    context={'weather_data':weather_data,'form':form,'message':message,'message_class':message_class}
    return render(request,'weatherapp/index.html',context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
