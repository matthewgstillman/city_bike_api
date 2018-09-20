from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    url = ("http://api.citybik.es/v2/networks")
    response = requests.get(url)
    networks = response.json()
    context = {
        'networks': networks
    }
    return render(request, 'city_bike_api/index.html', context)