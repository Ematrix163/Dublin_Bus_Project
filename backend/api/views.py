from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


class RouteId(View):
    def get(self, request):
        return HttpResponse('{"route":["46A","145","39A","63"]}', content_type='application/json')


class StationView(View):
    def get(self, request):
        data = '{"station":[{"name":"Crofton Road Railway Station", "id":"100", "lat":"50", "lng": "100"}]}'
        return HttpResponse(data, content_type='application/json')