import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.stats import zscore
import numpy as np
import math
from sklearn.neural_network import MLPRegressor


class NeuralNetworkModel:

    def __init__(self, input_file_path, output_path, output_file_name, y):
        self._file_path = input_file_path
        self._output_path = output_path
        self._output_file_name = output_file_name
        # Creates df upon instance initialization:
        self._df = pd.read_csv(self._file_path, header=0, delimiter=',')
        # Drop all columns that aren't required features for training:
        #self.drop_attributes()
        # X are the independent variables (features)
        self._X = self._df.drop(y, axis=1)
        #y is the Dependent variable (Target Feature)
        self._y = self.df[y]
        #normalise data
        self._df = self._df.apply(zscore)
         # Creates train, test and cross validation data frames upon instance initialization:
        self._df_train_X = None
        self._df_train_y = None
        self._df_test_X = None
        self._df_test_y = None
        self._df_cross = self.df

    @property
    def input_file_path(self):
        return self._input_file_path

    @property
    def input_file_path(self):
        return self._output_path

    @property
    def output_file_name(self):
        return self._output_file_name

    @property
    def df(self):
        return self._df

    @property
    def y(self):
        return self._y

    @property
    def X(self):
        return self._X


    # Split the data-frame into the train x, train y, test x and test y sets:
    def split_df(self):
        self._df_train_X, self._df_test_X, self._df_train_y, self._df_test_y = train_test_split(self._X, self._y, test_size=0.25, random_state=1)


    #initialize model
    def initialize_model(self):

        self._clf = MLPRegressor(hidden_layer_sizes=(300,300,300), activation='relu',solver='adam', alpha=0.0001, random_state=1, learning_rate='adaptive', max_iter=300)
        self._clf.fit(self._df_train_X, self._df_train_y.values.ravel())


    def getResults(self):
        self._trainScore = self._clf.score(self._df_train_X, self._df_train_y)
        self._testScore = self._clf.score(self._df_test_X, self._df_test_y)

clean_file_path = '/home/student/data_analytics/bus_lines/result_of_66-dir1Model.csv'
output_path = '/data_analytics/prediction_model/'
output_file_name = 'bus66.csv'
y = 'duration'

# Create instance
instance = NeuralNetworkModel(clean_file_path, output_path, output_file_name, y)

instance.split_df()
#print(instance._df_train_y)
instance.initialize_model()
instance.getResults()
print("Train Score ", instance._trainScore)
print("Test Score ", instance._testScore)
