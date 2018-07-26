"""
File uses classes in clean.py and randomForest_model.py to get pickle files for each route and direction
"""

from clean import CleanFile
from randomForest_model import RandomForestModel
from NN_model import NeuralNetworkModel
import os

extracted_files_dir = '/home/student/data_analytics/bus_lines/single_bus_line'
clean_files_dir = '/home/student/data_analytics/prediction_model/clean_files'
weather_file ='/home/student/data/weather/2017weatherClean.csv'
model_dir = '/home/student/data_analytics/prediction_model/pickle_files/'
y = 'duration'
'''
# creates a clean csv file for each route in direction 1 for model
for filename in os.listdir(extracted_files_dir):
    filepath = extracted_files_dir + '/' + filename
    output = clean_files_dir +'/'
    instance = CleanFile(filepath, output, weather_file, 1)
    instance.create_model_file()
    instance.save_result()
    print('finished a file')

print('finished creating direction 1 cleaned files')

# creates a clean csv file for each route in direction 2 for model
for filename in os.listdir(extracted_files_dir):
    filepath = extracted_files_dir + '/' + filename
    output = clean_files_dir + '/'
    instance = CleanFile(filepath, output, weather_file, 2)
    instance.create_model_file()
    instance.save_result()
    print('finished a file')

print('finished creating direction 2 cleaned files')


# making model pickle files for each route and direction
for filename in os.listdir(clean_files_dir):
    filepath = clean_files_dir + '/' + filename
    instance = RandomForestModel(filepath, model_dir, y)
    instance.split_df()
    instance.initialize_model()
    instance.get_results()
    print(filename, 'RESULTS:')
    print("train score" , instance._scoreTrain)
    print('test score', instance._scoreTest)
    print('mae', instance._mae)
    instance.save_model()
    instance.save_features()
    print('\n')
'''
for filename in os.listdir(clean_files_dir):
    filepath = clean_files_dir + '/' + filename
    instance = NeuralNetworkModel(filepath, model_dir, y)
    print('Finished:', filename)

print("finished making pickle files!")


