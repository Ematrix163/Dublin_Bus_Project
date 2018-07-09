# Create your views here.

# Use django restful framework
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Routes, RoutesStopid, Stopsstatic
from .serializers import RouteSerializer, RoutesStopidSerializer


class RouteIdView(APIView):
    def get(self, request):
        route = Routes.objects.all()
        route_ser = RouteSerializer(route, many=True)
        return Response(route_ser.data)


class RoutesStopidView(APIView):
    def get(self, request):
        routeid = request.GET.get("route", "")
        allstops = RoutesStopid.objects.all()
        # for stop in allstops:
        #     print(stop)