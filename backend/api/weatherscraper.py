


from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Currentweather

import requests
import requests
import json
import sys
import dbconnect
from time import sleep





def connecting_method():
    """Creates an instance of class weather. Sends api key and city id """
    apikey='66040549d2cc38abfa2a0be1019ad3b5'
    cityid='2964574'
    return Weather(apikey,cityid)



class Weather:

    def __init__(self, apikey, cityid):
        self.key=apikey
        self.cityid=cityid
        self.dictionary=None


    def __init__(self, apikey, cityid):
        self.key = apikey
        self.cityid = cityid
        self.dictionary = None


    def api_request(self):
        # url = 'http://api.openweathermap.org/data/2.5/weather?id=2964574&APPID=66040549d2cc38abfa2a0be1019ad3b5'

        url = "http://api.openweathermap.org/data/2.5/weather?id=" + self.cityid + "&APPID=" + self.key
        response = requests.get(url)
        print("Status code: ", response.status_code)
        self.dictionary = response.json()
        return self.dictionary


    def read_api_response(self, dictionary):
        self.weather = self.dictionary['weather'][0]
        self.weather_main = self.weather['main']
        self.weather_description = self.weather['description']
        self.weather_id = self.weather['id']
        self.weather_icon = self.weather['icon']
        self.temp = self.dictionary['main']['temp']
        self.pressure = self.dictionary['main']['pressure']
        self.humidity = self.dictionary['main']['humidity']
        self.temp_min = self.dictionary['main']['temp_min']
        self.temp_max = self.dictionary['main']['temp_max']
        self.wind_speed = self.dictionary['wind']['speed']
        self.wind_deg = self.dictionary['wind']['deg']
        self.clouds_all = self.dictionary['clouds']['all']
        self.dt = self.dictionary['dt']
        self.city_id = self.dictionary['id']
        print("city id ", self.city_id)
        print("city id ", self.weather_description)
        w = Currentweather(weather_main=self.weather_main)
        w.save()


weather = connecting_method()
dict = weather.api_request()
weather.read_api_response(dict)


w = Currentweather(weather_main=weather_main)
w.save()

