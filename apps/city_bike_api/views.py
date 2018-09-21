from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    network_list = []
    url = ("http://api.citybik.es/v2/networks")
    response = requests.get(url)
    city_bikes = response.json()
    networks = city_bikes['networks']
    i = 0
    for i in range(0, len(networks)):
        print(networks[i])
        network_list.append(networks[i])
        i += 1
    context = {
        # 'company': company,
        'city_bikes': city_bikes,
        'network_list': network_list,
        'networks': networks
    }
    return render(request, 'city_bike_api/index.html', context)