from django.shortcuts import render
import requests


# Create your views here.

def dash(request):
    response= requests.get('https://covid-api.com/api/regions').json()
    print(response)
    return render (request, 'dashboard.html',{'response':response})
