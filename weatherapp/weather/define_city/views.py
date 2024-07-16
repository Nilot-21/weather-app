from django.shortcuts import render
import json
import datetime
import requests
import urllib.request
def home(request):
    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=2992535bdcd3ee2561a344df029c9a09').read()
        list_of_data=json.loads(source)
        details={
            'country_code':str(list_of_data['sys']['country']),
            'description':list_of_data['weather'][0]['description'],
            'temp':str(int((list_of_data['main']['temp']-273.5)))+'°C',
            'icon':list_of_data['weather'][0]['icon'],
            'day':datetime.date.today(),
            'city':city,
            }
        print(details)
    else:
        details={}

    return render(request,'index.html',details)

    
    