from prediction_model.clean.py import cleanFile
#from randomForest_model.py import RandomForestModel
import os

output_path = '/home/student/data_analytics/clean_files/'
weather_file ='/home/student/data/weather/2017weatherClean.csv'

for filename in os.listdir('/home/student/data_analytics/bus_lines/single_bus_line'):
    instance = cleanFile(filename, output_file_path, weather_file, 1)
    instance.create_model_file()
    instance.save_result()
    print('finished')


