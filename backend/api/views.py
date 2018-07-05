# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Routes, RoutesStopid, Stopsstatic
from .serializers import RouteSerializer


class RouteIdView(APIView):
	def get(self, request):
		route = Routes.objects.all()
		route_ser = RouteSerializer(route, many = True)
		print(route_ser.data)
		return Response(route_ser.data)


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
