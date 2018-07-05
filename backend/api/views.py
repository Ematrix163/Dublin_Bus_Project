from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import requests
import json
# Create your views here.


class RouteId(View):
    def get(self, request):
        return HttpResponse('{"route":["46A","145","39A","63"]}', content_type='application/json')


class StationView(View):
    def get(self, request):
        data = '{"station":[{"name":"Crofton Road Railway Station", "id":"100", "lat":"50", "lng": "100"}]}'
        return HttpResponse(data, content_type='application/json')



class WeatherView(View):
    def get(self, request):
        url = 'http://api.openweathermap.org/data/2.5/weather?id=2964574&APPID=66040549d2cc38abfa2a0be1019ad3b5'
        response = requests.get(url)
        return HttpResponse(response, content_type='application/json')