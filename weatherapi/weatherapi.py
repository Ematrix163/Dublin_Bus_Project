# This module uses an api request to get the current weather information  from openweather map. It is scheduled to run
# every hour. It writes this information to the database table currentWeather by calling the weather_writer function
# in the module dbconnect.py. 

import requests
import dbconnect
from time import sleep
import logging


print("this has started....")

# create log file to register errors
logging.basicConfig(filename='weatherApi.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')




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

    def api_request(self):
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
        print("weather description ", self.weather_description)
        dbconnect.weather_writer(self.dt, self.weather_main, self.weather_description, self.city_id, self.temp, self.temp_min, self.temp_max, self.pressure,
                                 self.humidity, self.wind_speed, self.wind_deg, self.clouds_all, self.weather_id, self.weather_icon)

    def timer(self):
        """ get weather data from openweather map at hourly intervals"""

        while True:
            try:
                sleep(120) # 2 min pause so it won't keep sending repeat requests if error has occurred
                dict = weather.api_request()
                weather.read_api_response(dict)
                sleep(3600)

            except Exception as ex:
                logging.error('error at ' + str(ex))
                print("Error!!!!: ", ex)


weather = connecting_method()
weather.timer()


