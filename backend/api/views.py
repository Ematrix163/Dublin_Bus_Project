
# Use django restful framework
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Routes, Forecastweather, Stopsstatic, DublinbusScheduleCurrent, CoreUsersettings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import RouteSerializer, RoutesStopidSerializer, CoreUsersettingsSerializer
from django.conf import settings
from sklearn.externals import joblib
from django.contrib.auth.hashers import make_password
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
    @staticmethod
    def getInfo(start_id, end_id, route, direction):
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
        result = PredictTimeView.predict(routeid, direction, start_stop, end_stop,  time)
        return Response({"status":"success","data":[result]})

    @staticmethod
    def predict(routeid, direction, start_stop, end_stop, time):
        # Inilize the dataframe
        path = settings.STATICFILES_DIRS[0] + '/headers/' + routeid.upper() + '_' + direction + '.csv'
        with open(path, 'r') as f:
            temp = f.read().strip('\n')
            column_seq = temp.split('\n')
        to_predict = pd.DataFrame(columns=column_seq, index=[0])
        to_predict.iloc[0] = [0] * len(column_seq)
        # Get the weather from the database
        weather = Forecastweather.objects.all().order_by('dt').values('dt', 'temp', 'clouds_all', 'wind_speed','wind_deg','pressure', 'humidity')
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


        # Get the arrive bus time
        format_start_stop = '0' + str(start_stop)
        bus_time = DublinbusScheduleCurrent.objects.filter(stop_id=format_start_stop[-4:], line_id=routeid).values_list('arrival_time').order_by('arrival_time')
        dep_seconds = time % 86400
        # bus_seconds = dep_seconds
        # bus_readble_hour = int(bus_seconds / 3600)
        # bus_readble_min = int((bus_seconds - bus_readble_hour * 3600) / 60)
        # bus_readble_sec = bus_seconds - bus_readble_hour * 3600 - bus_readble_min * 60
        # bus_readble = str(bus_readble_hour) + ':' + str(bus_readble_min) + ':' + str(bus_readble_sec)

        # Try to find the next coming bus after user's input time
        for t in bus_time:
            bus_seconds = int(t[0][0:2]) * 3600 + int(t[0][3:5]) * 60
            if bus_seconds > dep_seconds:
                bus_readble = t[0]
                flag = True
                break
        else:
            # If there is no bus after that time, use the tomorrow's first bus
            flag = False
            bus_seconds = int(bus_time[0][0][0:2]) * 3600 + int(bus_time[0][0][3:5]) * 60
            bus_readble = bus_time[0][0]

        dayofweek = datetime.datetime.fromtimestamp(time).weekday()
        category_time = 'arrive_time_'  + str(int((bus_seconds % 86400) / 1800))

        # if category_time not in to_predict:
        to_predict[category_time] = 1
        to_predict['dayofweek_' + str(dayofweek)] = 1
        # Load the model pkl file
        model_path = settings.MODEL_URL + '/model_' + routeid.upper() + '_' + direction + '.pkl'
        clf = joblib.load(model_path)
        # Load the scaler file
        scaler_path = settings.MODEL_URL + '/scaler_' + routeid.upper() + '_' + direction + '.pkl'
        sca = joblib.load(scaler_path)
        # Get All stops between these two stops
        stops = PredictTimeView.getInfo(str(start_stop), str(end_stop), routeid, direction=direction)
        stopInfo = Stopsstatic.objects.filter(true_stop_id__in=stops)
        stopInfo_ser = RoutesStopidSerializer(stopInfo, many=True)
        stopInfo_data = stopInfo_ser.data
        length = len(stopInfo_data)
        # Sort the stop
        path = settings.STATICFILES_DIRS[0] + '/stopSeq/' + routeid + '_' + direction + '.json'
        with open(path, 'r') as f:
            data = json.load(f)
        for i in range(length):
            for j in range(i, length):
                if data[str(stopInfo_data[i]['true_stop_id'])] > data[str(stopInfo_data[j]['true_stop_id'])]:
                    stopInfo_data[i], stopInfo_data[j] = stopInfo_data[j], stopInfo_data[i]

        length = len(stops)
        detail = [];
        total_time = 0
        # pd.set_option('display.max_columns', 500)
        average_time = {}
        with open(settings.MODEL_URL + '/averages.csv') as f:
            temp = f.read().strip('\n').split('\n')
            for each in temp:
                x = each.split(',')
                average_time[x[0]] = x[1]

        for index in range(length - 1):
            current_start = 'start_stop_' + stops[index]
            current_end = 'end_stop_' + stops[index + 1]
            # If our model has these two stops
            if (current_start in to_predict and current_end in to_predict):
                to_predict['start_stop_' + stops[index]][0] = 1
                to_predict['end_stop_' + stops[index + 1]][0] = 1
                temp = sca.transform(to_predict)
                to_predict.iloc[0] = temp[0]
                duration = clf.predict(to_predict)[0]
                total_time += duration
                detail.append(duration)
                temp = sca.inverse_transform(to_predict)
                to_predict.iloc[0] = temp[0]
                to_predict['start_stop_' + stops[index]][0] = 0
                to_predict['end_stop_' + stops[index + 1]][0] = 0
            else:
                detail.append(average_time[routeid.upper() + '_'+direction])
                total_time += float(average_time[routeid.upper()+'_'+direction])
        total_time = int(total_time / 60)

        result = {
            "detail": detail,
            "totalDuration": total_time,
            "stopsNum": length,
            "stopInfo": stopInfo_data,
            "bustime": [bus_seconds, bus_readble],
            "flag": flag
         }
        return result


class LocationView(APIView):
    def get(self, request):
        origin_lat = request.GET.get("origin_lat", "")
        origin_lng = request.GET.get("origin_lng", "")
        dest_lat = request.GET.get("dest_lat", "")
        dest_lng = request.GET.get("dest_lng", "")
        time = request.GET.get("time", "")
        url = 'https://maps.googleapis.com/maps/api/directions/json?origin=' + origin_lat + ',' + origin_lng + '&departure_time='+ time + '&destination='+ dest_lat + ',' +dest_lng + '&mode=transit&transit_mode=bus&key=AIzaSyDjRsP2Z4JM86ag3hkbRMmfS1a72YBlD8w'
        r = requests.get(url)
        r = r.json()
        steps = r['routes'][0]["legs"][0]["steps"]
        predict_result = []
        for eachstep in steps:
            if eachstep['travel_mode'] == "TRANSIT":
                # Get the line id of the route
                lineid = eachstep["transit_details"]["line"]["short_name"]
                # Get the direction of the bus
                headsign =  eachstep["transit_details"]["headsign"].split(' ')[0]
                with open(settings.STATICFILES_DIRS[0] + '/stopSeq/directions.json', 'r') as f:
                    data_dir = json.load(f)
                try:
                    dir1 = data_dir[lineid]["dir1"]
                except KeyError:
                    return Response({"status":"fail", "msg":"Sorry, this is not Dublin Bus Company's route."})
                if dir1.find(headsign) > dir1.find('To'):
                    direction = '1'
                else:
                    direction = '2'
                # Get all stops of that direction and line ID
                path = settings.STATICFILES_DIRS[0] + '/stopSeq/' + lineid + '_' + direction + '.json'
                with open(path) as f:
                    data_stop = json.load(f)
                allkeys = list(data_stop.keys())
                allstops = Stopsstatic.objects.filter(true_stop_id__in=allkeys)
                allstops_ser = RoutesStopidSerializer(allstops, many=True)
                allstops_data = allstops_ser.data
                # Get the latitude and longitude of the stop
                start_stop_lat = eachstep["transit_details"]["departure_stop"]["location"]["lat"]
                start_stop_lng = eachstep["transit_details"]["departure_stop"]["location"]["lng"]
                end_stop_lat = eachstep["transit_details"]["arrival_stop"]["location"]["lat"]
                end_stop_lng = eachstep["transit_details"]["arrival_stop"]["location"]["lng"]
                min_start = 100; min_end = 100;
                #This is to find the match stop to get the stop id to predict
                for eachstop in allstops_data:
                    temp_start = abs((float(eachstop["stop_lat"]) - start_stop_lat)) + abs((float(eachstop["stop_long"]) - start_stop_lng))
                    temp_end = abs((float(eachstop["stop_lat"]) - end_stop_lat)) + abs((float(eachstop["stop_long"]) - end_stop_lng))
                    if temp_start < min_start:
                        min_start = temp_start
                        start_stop_id = eachstop['true_stop_id']
                    if temp_end < min_end:
                        min_end = temp_end
                        end_stop_id = eachstop["true_stop_id"]
                predict_result.append(PredictTimeView.predict(lineid, direction, start_stop_id, end_stop_id, int(time)))

        # result["data"]["google"] = r
        result = {
            "status": "success",
            "data": predict_result,
            "google": r
        }
        return Response(result)


def error_404(request):
    return render(request, 'error_404.html')


def error_500(request):
    return render(request, 'error_500.html')


class StaticFileView(APIView):
    def get(self, request):
        path = settings.STATICFILES_DIRS[0]+'/APIOutline.md'
        with open(path, encoding='utf-8') as f:
            result = f.read()
        return Response(result)


class UserPlaceView(APIView):
    # This class is to return use's data, needs to be authenticated
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        userid = request.user.id
        result = CoreUsersettings.objects.filter(userid=userid)
        result_ser = CoreUsersettingsSerializer(result, many=True)
        return Response({"data": result_ser.data})


class SavePlaceView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        userid = request.user
        routeid = request.data['routeid']
        dir_name = request.data['dir_name']
        dir_id = request.data['dir_id']
        origin_id = request.data['origin_id']
        origin_name = request.data['origin_name']
        dest_id = request.data['dest_id']
        dest_name = request.data['dest_name']
        jour = request.data['jour']

        CoreUsersettings.objects.create(
            routeid=routeid,
            direction_id=dir_id,
            direction_name=dir_name,
            originstop_id=origin_id,
            originstop_name=origin_name,
            destinationstop_id=dest_id,
            destinationstop_name=dest_name,
            journeyname=jour,
            userid=userid,
        )

        return Response({"status": "success"})


class SignUpView(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        if User.objects.filter(username=username):
            return Response({"status":"fail","msg":"Your username has been registered!"})

        user = User()
        user.username = username
        user.password = make_password(password)
        user.save()

        return Response({"status":"success"})


class DeleteView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        userid = request.user
        id = request.data['journey_id']
        CoreUsersettings.objects.filter(userid=userid, id=id).delete()
        return Response({"status": "success"})
