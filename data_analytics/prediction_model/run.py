"""
File uses classes in clean.py and randomForest_model.py to get pickle files for each route and direction
"""

from clean.py import cleanFile
from randomForest_model.py import RandomForestModel
import os

output_path_clean = '/home/student/data_analytics/clean_files/'
weather_file ='/home/student/data/weather/2017weatherClean.csv'
output_path_model = '/home/student/data_analytics/prediction_model/pickle_files/'
y = 'duration'

#creates a clean csv file for each route in direction 1 for model
for filename in os.listdir('/home/student/data_analytics/bus_lines/single_bus_line'):
    filepath = '/home/student/data_analytics/bus_lines/single_bus_line/' + filename
    instance = cleanFile(filepath, output_file_path_clean, weather_file, 1)
    instance.create_model_file()
    instance.save_result()

print('finished creating direction 1 cleaned files')

#creates a clean csv file for each route in direction 2 for model
for filename in os.listdir('/home/student/data_analytics/bus_lines/single_bus_line'):
    filepath = '/home/student/data_analytics/bus_lines/single_bus_line/' + filename
    instance = cleanFile(filepath, output_file_path, weather_file, 2)
    instance.create_model_file()
    instance.save_result()

print('finished creating direction 2 cleaned files')


#making model pickle files for each route and direction
for filename in os.listdir('/home/student/data_analytics/clean_files'):
    filepath = '/home/student/data_analytics/clean_files/' + filename
    instance = RandomForestModel(filepath, output_path_model, y)
    instance.split_df()
    instance.initialize_model()
    instance.get_results()
    #print(instance._scoreTrain)
    #print(instance._scoreTest)
    instance.save_model()

print("finished making pickle files!")


