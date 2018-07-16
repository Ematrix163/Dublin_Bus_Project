import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.stats import zscore
import numpy as np
import math
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib


class RandomForestModel:
    """
    Class that initializes a random forest model on a csv file
    """

    def __init__(self, input_file_path, output_file_path, output_file, y):
        self._file_path = input_file_path
        self._output_file_path = output_file_path
        self._output_file = output_file
        # Creates df upon instance initialization:
        self._df = pd.read_csv(self._file_path, header=0, delimiter=',')
        # Drop all columns that aren't required features for training:
        self.set_features()
        # X are the independent variables (features)
        self._X = self._df.drop(y, axis=1)
        # y is the Dependent variable (Target Feature)
        self._y = self.df[[y]]
        # normalise data
        self._df = self._df.apply(zscore)
        # Creates train, test and cross validation data frames upon instance initialization
        self._df_train_X = None
        self._df_train_y = None
        self._df_test_X = None
        self._df_test_y = None
        self._rf = None

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

    def set_features(self):
        # numeric features chosen for model [see 46A notebook for feature selection]
        continuous = ['temp', 'clouds_all', 'wind_speed', 'wind_deg', 'pressure', 'humidity']
        df_continuous = self._df[continuous]

        # binary coding of start stops
        binary_start_stops = pd.get_dummies(self._df['start_point'])
        binary_end_stops = pd.get_dummies(self._df['end_point'])

        # binary coding of weather
        binary_weather = pd.get_dummies(self._df['weather_description'])

        # binary Coding of dayofweek
        binary_dayofweek = pd.get_dummies(self._df['dayofweek'])

        # Binary Coding of arrive time
        binary_arrive_time = pd.get_dummies(self._df['arrive_time'].divide(1800).round())

        self._df = pd.concat(
            [self._df['duration'], df_continuous, binary_weather,
             binary_start_stops, binary_end_stops, binary_dayofweek,
             binary_arrive_time], axis=1)

    def remove_outliers(self):
        self._df = self._df[self._df.duration < 3000]

    # Split the data-frame into the train x, train y, test x and test y sets:
    def split_df(self):
        self._df_train_X, self._df_test_X, self._df_train_y, self._df_test_y = train_test_split(self._X, self._y,
                                                                                                test_size=0.25,
                                                                                                random_state=1)

    # Initialize the random forest model:
    def initialize_model(self):
        self._rf = RandomForestRegressor(random_state=0, n_estimators=80, n_jobs=-1)
        self._rf.fit(self._df_train_X, self._df_train_y.values.ravel())

    # gets the results for the regression model
    def get_results(self):
        # Calculate Score
        self._scoreTrain = self._rf.score(self._df_train_X, self._df_train_y)
        self._scoreTest = self._rf.score(self._df_test_X, self._df_test_y)

    def save_model(self):
        joblib.dump(self._rf, self._output_file_path + self._output_file)


# Define inputs for creation of instance
clean_file_path = '/home/student/data_analytics/clean_files/result_of_25-dir1Model.csv'
output_file_path = '/home/student/data_analytics/prediction_model/pickle_files/'
output_file = '25-2.pkl'
y = 'duration'

# Create instance
instance = RandomForestModel(clean_file_path, output_file_path, output_file, y)
instance.split_df()
instance.initialize_model()
instance.get_results()
print(instance._scoreTrain)
print(instance._scoreTest)
instance.save_model()
print("finished")