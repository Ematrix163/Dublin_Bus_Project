# Create your views here.

# Use django restful framework
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Routes, Allstops, Forecastweather, ColumnSequence, RoutesStopid, Stopsstatic
from .serializers import RouteSerializer, RoutesStopidSerializer
from django.conf import settings
from sklearn.externals import joblib

import pandas as pd
import datetime
import json


class RouteIdView(APIView):
    def get(self, request):
        route = Routes.objects.all()
        route_ser = RouteSerializer(route, many=True)
        return Response(route_ser.data)


class RoutesStopidView(APIView):
    def get(self, request):
        routeid = request.GET.get("route", "").lower()
        print(routeid)
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
            for j in range(i, length-1):
                if data[str(result[i]['true_stop_id'])] > data[str(result[j]['true_stop_id'])]:
                    result[i], result[j] = result[j], result[i]
        return Response({"status":"success","data": result})


class DirectionView(APIView):
    # Return the direction of a bus route
    def get(self, request):
        routeid = request.GET.get("routeid", "").lower()
        with open(settings.STATICFILES_DIRS[0]+'/stopSeq/directions.json', 'r') as f:
            data = json.load(f)
        print(data)
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
        time = int(request.GET.get("datetime", ""))
        direction = str(request.GET.get("direction", ""))

        # Inilize the dataframe
        column_seq = ColumnSequence.objects.values_list('number_'+ routeid, flat=True)
        to_predict = pd.DataFrame(columns=column_seq, index=[0])
        to_predict.iloc[0] = [0] * len(column_seq)

        # Get the weather from the database
        weather = Forecastweather.objects.all().order_by('dt').values('dt','temp','clouds_all', 'wind_speed', 'wind_deg', 'pressure', 'humidity')

        # Select all continuos features
        continuous_list = ['temp', 'clouds_all', 'wind_speed', 'wind_deg', 'pressure', 'humidity']
        # Find the nearest time
        for each in weather:
            if each['dt'] >= time:
                new_time = each['dt']
                for feature in continuous_list:
                    to_predict[feature][0] = each[feature]
                break
        else:
            new_time = each['dt']
            for feature in continuous_list:
                to_predict[feature][0] = each[feature]
        dayofweek = datetime.datetime.fromtimestamp(time).weekday()
        pd.set_option('display.max_columns', 500)
        category_time = str(round((time % 86400)/1800))
        to_predict['arrivetime_'+category_time] = 1
        to_predict['dayofweek_'+str(dayofweek)] = 1
        # Load the pkl file
        path = settings.MODEL_URL + '/' + routeid + '_' + direction + '.pkl'
        clf = joblib.load(path)
        # Get All stops between these two stops
        stops = self.getInfo(start_stop, end_stop, routeid, direction=direction)
        stopInfo = Stopsstatic.objects.filter(true_stop_id__in=stops)
        stopInfo_ser = RoutesStopidSerializer(stopInfo, many=True)
        length = len(stops)
        detail = []; total_time = 0
        category_time = str(round((time % 86400) / 1800))
        to_predict['arrivetime_' + category_time] = 1
        try:
            for index in range(length-1):
                to_predict['start_stop_' + stops[index]][0] = 1
                to_predict['end_stop_' + stops[index+1]][0] = 1
                duration = clf.predict(to_predict)[0]
                total_time += duration
                detail.append(duration)
                to_predict['start_stop_' + stops[index]][0] = 0
                to_predict['end_stop_' + stops[index+1]][0] = 0
        except ValueError:
            # If the bus is not in running time
            return Response({"status":"fail", "message":"Sorry, the bus is not in service at that time!"})

        total_time = int(total_time/60)
        result = {
            "status":"success",
            "data":{
                "detail": detail,
                "totalDuration": total_time,
                "stopsNum": length + 1,
                "stopInfo": stopInfo_ser.data
        }}
        return Response(result)