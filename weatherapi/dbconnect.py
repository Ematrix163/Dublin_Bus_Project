import MySQLdb
import mysql.connector
from mysql.connector import Error
from time import sleep
import logging



# create log file to register errors
logging.basicConfig(filename='dbconnect.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



def establishConnection():
    """This function connects to the mysql database on the VM"""
    while True:
        try:
            global connection
            connection = mysql.connector.connect(host='localhost',
                                           database='dublinBus',
                                           user='front_end',
                                           password='12345')
            if connection.is_connected():
                print("This connection worked!")
                global cursor
                cursor = connection.cursor()  # create cursor object - this can execute sql statments
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




