import requests
import json
import sys
import dbconnect
from time import sleep
import logging


print("this has started....")

# create log file to register errors
logging.basicConfig(filename='forecastApi.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')




def connecting_method():
    """Creates an instance of class forecast. Sends api key and city id """
    apikey='66040549d2cc38abfa2a0be1019ad3b5'
    cityid='2964574'
    return Forecast(apikey,cityid)

class Forecast:

    def __init__(self, apikey, cityid):
        self.key=apikey
        self.cityid=cityid
        self.dictionary=None

    def api_request(self):
        url = "http://api.openweathermap.org/data/2.5/forecast?id=" + self.cityid + "&APPID=" + self.key + "&units=metric"
        response = requests.get(url)
        print("Status code: ", response.status_code)
        print("Response: ", response.text)
        self.dictionary = response.json()
        return self.dictionary

    def read_api_response(self, dictionary):
        self.weatherlist = self.dictionary['list']
        print("List is a: ", type(self.weatherlist))
        print("lenght of list is ", len(self.weatherlist))
        dbconnect.empty_table()
        for i in self.weatherlist:
            self.dt = i['dt']
            self.weather = i['weather']
            self.weather_main = i['weather'][0]['main']
            self.weather_description = i['weather'][0]['description']
            self.weather_icon = i['weather'][0]['icon']
            self.weather_id = i['weather'][0]['id']
            self.main = i['main']
            self.temp = i['main']['temp']
            self.temp_min = i['main']['temp_min']
            self.temp_max = i['main']['temp_max']
            self.pressure = i['main']['pressure']
            self.humidity = i['main']['humidity']
            self.clouds_all = i['clouds']['all']
            self.wind_speed = i['wind']['speed']
            self.wind_degree = i['wind']['deg']
            self.dt_txt = i['dt_txt']
            dbconnect.forecast_writer(self.dt, self.weather_main, self.weather_description, self.temp, self.temp_min, self.temp_max, self.pressure,
                                self.humidity, self.wind_speed, self.wind_degree, self.clouds_all, self.weather_id, self.weather_icon, self.dt_txt)





    def timer(self):
        """ get forecast from openweather map every 3 hours"""

        while True:
            try:
                sleep(120) # 2 min pause so it won't keep sending repeat requests if error has occurred
                dict = forecast.api_request()
                forecast.read_api_response(dict)
                sleep(10800)

            except Exception as ex:
                logging.error('error at ' + str(ex))
                print("Error!!!!: ", ex)



forecast = connecting_method()
forecast.timer()


