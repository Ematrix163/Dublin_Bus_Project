# Create your views here.

# Use django restful framework
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Routes, Forecastweather, Stopsstatic, DublinbusScheduleCurrent
from .serializers import RouteSerializer, RoutesStopidSerializer
from django.conf import settings
from sklearn.externals import joblib
import pandas as pd
import datetime
import requests
import json


class RouteIdView(APIView):
    def get(self, request):
        route = Routes.objects.all()
        route_ser = RouteSerializer(route, many=True)
        return Response(route_ser.data)


class RoutesStopidView(APIView):
    def get(self, request):
        routeid = request.GET.get("route", "").lower()
        direction = request.GET.get("direction", "")
        path = settings.STATICFILES_DIRS[0] + '/stopSeq/' + routeid + '_' + direction + '.json'

        with open(path, 'r') as f:
            data = json.load(f)
        allkeys = list(data.keys())
        allstops = Stopsstatic.objects.filter(true_stop_id__in=allkeys)
        allstops_ser = RoutesStopidSerializer(allstops, many=True)
        result = allstops_ser.data
        # Sort the result by program number
        length = len(result)
        for i in range(length):
            for j in range(i, length):
                if data[str(result[i]['true_stop_id'])] > data[str(result[j]['true_stop_id'])]:
                    result[i], result[j] = result[j], result[i]
        return Response({"status":"success","data": result})


class DirectionView(APIView):
    # Return the direction of a bus route
    def get(self, request):
        routeid = request.GET.get("routeid", "").lower()
        with open(settings.STATICFILES_DIRS[0]+'/stopSeq/directions.json', 'r') as f:
            data = json.load(f)
        result = data[str(routeid)]
        return Response(result)


class PredictTimeView(APIView):
    def getInfo(self, start_id, end_id, route, direction='1'):
        # Read local JSON File to get all stops sequence of one bus route
        path = settings.STATICFILES_DIRS[0]+'/stopSeq/' + route + '_' + direction +'.json'
        with open(path, 'r') as f:
            data = json.load(f)
        allkeys = list(data.keys())
        start_index = allkeys.index(start_id)
        end_index = allkeys.index(end_id)
        keys = allkeys[start_index:end_index + 1]
        return keys


    def get(self, request):
        # Get the request paramaters
        routeid = request.GET.get("routeid", "").lower()
        start_stop = request.GET.get("start_stop", "")
        end_stop = request.GET.get("end_stop", "")
        time = int(request.GET.get("datetime", "")) + 3600
        direction = str(request.GET.get("direction", ""))


        if not (routeid and start_stop and end_stop and time and direction):
            return Response({"Status":"Fail", "msg":"Missing paramaters!"})

        # Inilize the dataframe
        path = settings.STATICFILES_DIRS[0] + '\\headers\\headers_' + routeid + '_' + direction + '.csv'
        with open(path, 'r') as f:
            temp = f.read().strip('\n')
            column_seq = temp.split('\n')

        to_predict = pd.DataFrame(columns=column_seq, index=[0])
        to_predict.iloc[0] = [0] * len(column_seq)
        # Get the weather from the database
        weather = Forecastweather.objects.all().order_by('dt').values('dt','temp','clouds_all', 'wind_speed', 'wind_deg', 'pressure', 'humidity')
        # Select all continuos features
        continuous_list = ['temp', 'clouds_all', 'wind_speed', 'wind_deg', 'pressure', 'humidity']
        # Find the nearest time
        for each in weather:
            if each['dt'] >= time:
                for feature in continuous_list:
                    to_predict[feature][0] = each[feature]
                break
        else:
            for feature in continuous_list:
                to_predict[feature][0] = each[feature]
        dayofweek = datetime.datetime.fromtimestamp(time).weekday()
        category_time = str(round((time % 86400)/1800))
        to_predict['arrive_time_'+category_time] = 1
        to_predict['dayofweek_'+str(dayofweek)] = 1
        # Load the pkl file
        model_path = settings.MODEL_URL + '\\model_' + routeid + '_' + direction + '.pkl'
        clf = joblib.load(model_path)
        #Load the scaler file
        scaler_path = settings.MODEL_URL + '\\scaler_' + routeid + '_' + direction + '.pkl'
        sca = joblib.load(scaler_path)
        # Get All stops between these two stops
        stops = self.getInfo(start_stop, end_stop, routeid, direction=direction)
        stopInfo = Stopsstatic.objects.filter(true_stop_id__in=stops)
        stopInfo_ser = RoutesStopidSerializer(stopInfo, many=True)
        length = len(stops)
        detail = []; total_time = 0
        # pd.set_option('display.max_columns', 500)
        try:
            for index in range(length-1):
                to_predict['start_stop_' + stops[index]][0] = 1
                to_predict['end_stop_' + stops[index+1]][0] = 1
                temp = sca.transform(to_predict)
                to_predict.iloc[0] = temp[0]
                duration = clf.predict(to_predict)[0]
                total_time += duration
                detail.append(duration)
                temp = sca.inverse_transform(to_predict)
                to_predict.iloc[0] = temp[0]
                to_predict['start_stop_' + stops[index]][0] = 0
                to_predict['end_stop_' + stops[index+1]][0] = 0
        except ValueError:
            # If the bus is not in running time
            return Response({"status":"fail", "message":"Sorry, the bus is not in service at that time!"})
        total_time = int(total_time/60)


        # Get the arrive bus time
        bus_time = DublinbusScheduleCurrent.objects.filter(stop_id=start_stop, line_id=routeid).values_list('arrival_time').order_by('arrival_time')
        dep_seconds = time % 86400
        bus_seconds = 0; bus_readble = 0
        for t in bus_time:
            bus_seconds = int(t[0][0:2]) * 3600 + int(t[0][3:5]) * 60
            if bus_seconds > dep_seconds:
                bus_readble = t[0]
                break



        result = {
            "status":"success",
            "data":{
                "detail": detail,
                "totalDuration": total_time,
                "stopsNum": length + 1,
                "stopInfo": stopInfo_ser.data,
                "bustime": [bus_seconds, bus_readble]
        }}
        return Response(result)


class LocationView(APIView):
    def get(self, request):
        origin_lat = request.GET.get("origin_lat", "")
        origin_lng = request.GET.get("origin_lat", "")
        dest_lat = request.GET.get("dest_lat", "")
        dest_lng = request.GET.get("dest_lng", "")
        time = request.GET.get("time", "")

        r = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=53.3083,-6.2236&destination=53.3498,-6.2603&mode=transit&key=AIzaSyDjRsP2Z4JM86ag3hkbRMmfS1a72YBlD8w')
        return Response(r.json())