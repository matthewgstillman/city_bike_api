from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    company_id_href_dict = { "company":{
    },
    }
    network_list = []
    url_root = "http://api.citybik.es/v2/networks"
    url = ("http://api.citybik.es/v2/networks")
    response = requests.get(url)
    city_bikes = response.json()
    networks = city_bikes['networks']
    i = 0
    for i in range(0, len(networks)):
        company_id = networks[i]['id']
        print("ID: " + str(company_id))
        href = networks[i]['href']
        print("HREF: " + str(href))
        company_id_href_dict['company_id'] = company_id
        company_id_href_dict['href'] = href
        network_list.append(networks[i])
        i += 1
        company_url = str(url_root) + str(href)
        request.session['company_url'] = company_url
        session_company_url = request.session['company_url']
        request.session['href'] = href
        session_href = request.session['href']
    print("Company ID Href Dictionary: " + str(company_id_href_dict))
    context = {
        'company_id_href_dict': company_id_href_dict,
        'city_bikes': city_bikes,
        'network_list': network_list,
        'networks': networks,
        'session_company_url': session_company_url,
        'session_href': session_href,
    }
    return render(request, 'city_bike_api/index.html', context)

def company(request):
    url = ("http://api.citybik.es/v2/networks/edinburgh-cycle-hire")
    response = requests.get(url)
    company = response.json()
    print("Company: " + str(company))
    network = company['network']
    print("Network: " + str(network))
    name = network['name']
    print("Name: " + str(name))
    i = 0
    for i in range(0, len(network)):
        station = network['stations'][i]
        print("Station: " + str(station))
        i += 1
    context = {
        'company': company,
        'network': network,
        'name': name,
        'station': station,
    }
    return render(request, 'city_bike_api/company.html', context)

def company_name(request):
    url = ("http://api.citybik.es/v2/networks/v2/networks/edinburgh-cycle-hire")
    context = {
    }
    return render(request, 'city_bike_api/company.html', context)