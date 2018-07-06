# Create your views here.

# Use django restful framework

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Routes, RoutesStopid, Stopsstatic
from .serializers import RouteSerializer, RoutesStopidSerializer


class RouteIdView(APIView):
	def get(self, request):
		route = Routes.objects.all()
		route_ser = RouteSerializer(route, many = True)
		return Response(route_ser.data)


class RoutesStopidView(APIView):
	def get(self, request):
		routeid = request.GET.get("route", "")
		if routeid:
			# stop = RoutesStopid.objects.filter(busroute=routeid)
			stop = Stopsstatic.objects.filter(routesstopid__busroute=routeid)
			stop_ser = RoutesStopidSerializer(stop, many=True)
			return Response(stop_ser.data)



# class StationView(View):
#     def get(self, request):
#         data = '{"station":[{"name":"Crofton Road Railway Station", "id":"100", "lat":"50", "lng": "100"}]}'
#         return HttpResponse(data, content_type='application/json')
#
#
#
# class WeatherView(View):
#     def get(self, request):
#         url = 'http://api.openweathermap.org/data/2.5/weather?id=2964574&APPID=66040549d2cc38abfa2a0be1019ad3b5'
#         response = requests.get(url)
#         return HttpResponse(response, content_type='application/json')
