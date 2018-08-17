import MySQLdb
import mysql.connector
from mysql.connector import Error
from time import sleep
import logging



# create log file to register errors
logging.basicConfig(filename='dbconnect.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def establishConnection():
    """This function connects to the mysql database on the VM
    NB user must enter their own password details below"""
    while True:
        try:
            global connection
            connection = mysql.connector.connect(host='',
                                           database='',
                                           user='',
                                           password='')
            if connection.is_connected():
                print("This connection worked!")
                global cursor
                cursor = connection.cursor(buffered=True)  # create cursor object - this can execute sql statments

                return cursor
                break

            else:
                print("Connection not established")
                logging.info('Connection not established')

        except Error as error:
            print("ERRROR!!: ", error)
            logging.error('error at ' + str(error))
            print("will try to connect again in 25 seconds")
            sleep(25)



def weather_writer(dt, weather_main, weather_description, city_id, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_icon):
    """This function writes the current weather from openweathermap api call to the table currentWeather on our DB. If table has data, it will update it. If table is emtpy
    it will leave data there"""
    establishConnection()
    query = "SELECT COUNT(*) from dublinBus.currentWeather"
    cursor.execute(query)
    result = cursor.fetchone()
    rows = result[0]  # total rows
    print("number of rows", rows)
    if rows>0:
        cursor.execute('truncate table dublinBus.currentWeather')
    if rows==0:
        logging.info('Table is empty')
    cursor.execute('insert into dublinBus.currentWeather (dt, weather_main, weather_description, city_id, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_icon)' \
    'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (dt, weather_main, weather_description, city_id, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_icon))
    connection.commit()
    cursor.close()
    connection.close()



def forecast_writer(dt, weather_main, weather_description, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_icon, dt_txt):
    """This function writes the 5-day weather forecast from openweathermap api call to the table forecastWeather on our DB. If table has data, it will update it. If table is emtpy
    it will leave data there"""
    establishConnection()
    query = "SELECT COUNT(*) from dublinBus.forecastWeather"
    cursor.execute(query)
    cursor.execute('insert into dublinBus.forecastWeather (dt, weather_main, weather_description, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_icon, dt_txt)' \
    'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (dt, weather_main, weather_description, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_icon, dt_txt))
    connection.commit()
    cursor.close()
    connection.close()



def empty_table():
    """This function empties the forecastWeather table on our database if there is already info in it - if it is already empty, it does nothing"""
    establishConnection()
    query = "SELECT COUNT(*) from dublinBus.forecastWeather"
    cursor.execute(query)
    result = cursor.fetchone()
    rows = result[0]  # total rows
    print("number of rows in forecast table", rows)
    if rows>0:
        cursor.execute('truncate table dublinBus.forecastWeather')
    if rows==0:
        logging.info('Forecast Table is empty')
    connection.commit()
    cursor.close()
    connection.close()


