import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.stats import zscore
import numpy as np
import math
from sklearn.neural_network import MLPRegressor
from sklearn.externals import joblib
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
import csv

class NeuralNetworkModel:

    def __init__(self, input_file_path, output_path, y):
        self._file_path = input_file_path
        self._output_path = output_path
        # Creates df upon instance initialization:
        self._df = pd.read_csv(self._file_path, header=0, delimiter=',')
        self._lineID = self._df['lineid'].iloc[1]
        self._dir = self._df['direction'].iloc[1]
        self._output_file_name = str(self._lineID) + "_" + str(self._dir)
        # remove outliers
        # self.remove_outliers()
        # keep only features for model
        self._df_columns = None
        self.set_features()
        # X are the independent variables (features)
        self._X = self._df.drop(y, axis=1)
        # y is the Dependent variable (Target Feature)
        self._y = self.df[y]
        # normalise data
        # self._df = self._df.apply(zscore)
        # Creates train, test and cross validation data frames upon instance initialization:
        self._df_train_X = None
        self._df_train_y = None
        self._df_test_X = None
        self._df_test_y = None
        self._scaler = None
        self._clf = None
        self._predictions = None
        self._scoreTest = None
        self._scoreTrain = None
        self._mae = None
        self._results = None
        self._file = None
        self.split_df()
        self.scaler()
        self.initialize_model()
        self.get_results()
        self.save_features()
        self.save_model()
        self.save_results()

    @property
    def input_file_path(self):
        return self._input_file_path

    @property
    def input_file_path(self):
        return self._output_path

    @property
    def df(self):
        return self._df

    @property
    def y(self):
        return self._y

    @property
    def X(self):
        return self._X

    def set_features(self):
        # numeric features chosen for model [see 46A notebook for feature selection]
        continuous = ['temp', 'clouds_all', 'wind_speed', 'wind_deg', 'pressure', 'humidity']
        df_continuous = self._df[continuous]

        # binary coding of start stops
        binary_start_stops = pd.get_dummies(self._df['start_point'], prefix='start_stop')
        self._df['end_point'] = self._df['end_point'].astype('int')
        binary_end_stops = pd.get_dummies(self._df['end_point'], prefix='end_stop')

        # binary coding of weather
        binary_weather = pd.get_dummies(self._df['weather_description'])

        # binary Coding of dayofweek and month
        binary_dayofweek = pd.get_dummies(self._df['dayofweek'], prefix='dayofweek')

        # Binary Coding of arrive time
        self._df['arrive_time'] = self._df['arrive_time'].divide(1800).round()
        self._df['arrive_time'] = self._df['arrive_time'].astype('int')
        binary_arrive_time = pd.get_dummies(self._df['arrive_time'], prefix='arrive_time')

        self._df = pd.concat(
            [self._df['duration'], df_continuous,
             binary_start_stops, binary_end_stops, binary_dayofweek,
             binary_arrive_time], axis=1)

        self._df_columns = pd.concat([df_continuous,
                                      binary_start_stops, binary_end_stops, binary_dayofweek,
                                      binary_arrive_time], axis=1)

    # Split the data-frame into the train x, train y, test x and test y sets:
    def split_df(self):
        self._df_train_X, self._df_test_X, self._df_train_y, self._df_test_y = train_test_split(self._X, self._y,
                                                                                                test_size=0.25,
                                                                                                random_state=1)

    # scaling data for normalisation
    def scaler(self):
        self._scaler = StandardScaler()
        self._scaler.fit(self._df_train_X)
        self._df_train_X = self._scaler.transform(self._df_train_X)
        self._df_test_X = self._scaler.transform(self._df_test_X)
        joblib.dump(self._scaler, self._output_path+'scaler_'+self._output_file_name+'.pkl')

    # initialize model

    def initialize_model(self):
        self._clf = MLPRegressor(solver='lbfgs', alpha=1000, hidden_layer_sizes=(20,), max_iter = 50000, activation = 'logistic', learning_rate = 'adaptive', random_state=1)
        self._clf.fit(self._df_train_X, self._df_train_y.values.ravel())

    def get_results(self):
        results = [self._output_file_name]
        self._predictions = self._clf.predict(self._df_test_X)
        self._mae = mean_absolute_error(self._df_test_y, self._predictions)
        self._scoreTrain = self._clf.score(self._df_train_X, self._df_train_y)
        self._scoreTest = self._clf.score(self._df_test_X, self._df_test_y)
        results.append(self._mae)
        results.append(self._scoreTrain)
        results.append(self._scoreTest)
        return results

    def save_results(self):
        output = self.get_results()
        with open('/home/student/data_analytics/prediction_model/model_results.csv', 'a') as self._file:
            wr = csv.writer(self._file, dialect = 'excel')
            wr.writerow(output)

    def save_model(self):
        joblib.dump(self._clf, self._output_path+'model_'+self._output_file_name + ".pkl")

    def save_features(self):
        pd.DataFrame({"ColumnName": self._df_columns.columns}).to_csv(
            "/home/student/data_analytics/prediction_model/model_headers/headers_" + self._output_file_name + ".csv",
            index=False)

''' 
This was a testing instance before running on all routes
'''
filepath = '/home/student/data_analytics/prediction_model/clean_files/66_1.csv'
model_dir = '/home/student/data_analytics/prediction_model/pickle_files/'
y = 'duration'

instance = NeuralNetworkModel(filepath, model_dir, y)
#print('finished')

print('RESULTS for 66-1:')
print("train score", instance._scoreTrain)
print('test score', instance._scoreTest)
print('mae', instance._mae)

