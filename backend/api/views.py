# Create your views here.

# Use django restful framework
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Routes, Allstops, Forecastweather, ColumnSequence, RoutesStopid, Stopsstatic
from .serializers import RouteSerializer, RoutesStopidSerializer, StopInfoSerializer
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
        routeid = request.GET.get("route", "")
        allstops = Allstops.objects.filter(busroute=routeid)
        allstops_ser = RoutesStopidSerializer(allstops, many=True)
        return Response(allstops_ser.data)


class PredictTimeView(APIView):

    def getInfo(self, start_id, end_id, route):
        with open(settings.STATICFILES_DIRS[0]+'\\stopSeq\\46A.json', 'r') as f:
            data = json.load(f)

        allkeys = list(data.keys())
        start_index = allkeys.index(start_id)
        end_index = allkeys.index(end_id)
        # Calculate the direction and get all the stops between these twp stops
        if data[start_id] - data[end_id] < 0:
            direction = 1
            keys = allkeys[start_index:end_index+1]
        else:
            direction = 2
            keys = allkeys[start_index:end_index + 1]
            keys.reverse()
        result = {"direction":direction, "stops":keys}
        return result



    def get(self, request):
        routeid = request.GET.get("routeid", "")
        start_stop = request.GET.get("start_stop", "")
        end_stop = request.GET.get("end_stop", "")
        time = int(request.GET.get("datetime", ""))
        # Inilize the dataframe
        column_seq = ColumnSequence.objects.values_list('number_'+ routeid, flat=True)
        to_predict = pd.DataFrame(columns=column_seq, index=[0])
        to_predict.iloc[0] = [0] * len(column_seq)
        # Get the weather
        weather = Forecastweather.objects.all().order_by('dt').values('dt','temp','clouds_all', 'wind_speed', 'wind_deg', 'pressure', 'humidity')
        # All continuos features
        continuos_list = ['temp', 'clouds_all', 'wind_speed', 'wind_deg', 'pressure', 'humidity']
        # Find the nearest time
        for each in weather:
            if each['dt'] >= time:
                new_time = each['dt']
                for feature in continuos_list:
                    to_predict[feature][0] = each[feature]
                break
        else:
            new_time = each['dt']
            for feature in continuos_list:
                to_predict[feature][0] = each[feature]
        dayofweek = datetime.datetime.fromtimestamp(time).weekday()

        category_time = str(round((time % 86400)/1800))
        to_predict['arrivetime_'+category_time] = 1
        to_predict['dayofweek_'+str(dayofweek)] = 1

        # Load the pkl file
        clf = joblib.load(settings.MODEL_URL + '\\route46a.pkl')
        # Get All stops between these two stops
        info = self.getInfo(start_stop, end_stop, routeid)
        stops = info['stops']

        stopInfo = Stopsstatic.objects.filter(true_stop_id__in=stops)
        stopInfo_ser = StopInfoSerializer(stopInfo, many=True)


        length = len(stops)
        detail = []; total_time = 0
        for index in range(length-1):
            to_predict['start_stop_' + stops[index]][0] = 1
            to_predict['end_stop_' + stops[index+1]][0] = 1
            category_time = str(round((time % 86400)/1800))
            to_predict['arrivetime_'+category_time] = 1
            duration = clf.predict(to_predict)[0]
            total_time += duration
            detail.append(duration)

            to_predict['start_stop_' + stops[index]][0] = 0
            to_predict['end_stop_' + stops[index+1]][0] = 0


        result = {
            "status":"success",
            "data":{
                "detail": detail,
                "totalDuration": total_time,
                "stopsNum": length,
                "stopInfo": stopInfo_ser.data,
                "stopSeq": stops
        }}

        return Response(result)