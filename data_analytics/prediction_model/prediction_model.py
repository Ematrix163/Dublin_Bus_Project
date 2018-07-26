import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.stats import zscore
import numpy as np
import math
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

class PredictionModel:

    def __init__(self, input_file_path, output_path, y):
        self._file_path = input_file_path
        self._output_path = output_path
        #self._output_file_name = output_file_name
        # Creates df upon instance initialization:
        self._df = pd.read_csv(self._file_path, header=0, delimiter=',')
        self._lineID = self._df['lineid'].iloc[1]
        self._dir = self._df['direction'].iloc[1]
        self._output_file = str(self._lineID) + "_" + str(self._dir)
        self.remove_outliers()
        self.set_features()
        # normalise data
        #self._df = self._df.apply(zscore)
        # X are the independent variables (features)
        self._X = self._df.drop(y, axis=1)
	    #y is the Dependent variable (Target Feature)
        self._y = self.df[[y]]
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
        self._df_train_X, self._df_test_X, self._df_train_y, self._df_test_y = train_test_split(self._X, self._y, test_size=0.25, random_state=1)

    # Initialize the Linear regression model:
    def initialize_model(self):

        self._regression_model = LinearRegression()
        self._regression_model.fit(self._df_train_X, self._df_train_y)
          
    #get the Coefficients of Linear model		
    def getCoefficientsLR(self):
        for idx, col_name in enumerate(self._df_train_X.columns):
            print("The coefficient for {} is {}".format(col_name, self._regression_model.coef_[0][idx]))

    #gets the accuracy scores of Linear model
    def getResultsLR(self):
        self._intercept = self._regression_model.intercept_[0]
        self._RSquaredTest = self._regression_model.score(self._df_test_X, self._df_test_y)
        self._RSquaredTrain = self._regression_model.score(self._df_train_X, self._df_train_y)
        self._y_predict = self._regression_model.predict(self._df_test_X)
        self._regression_model_mse = mean_squared_error(self._y_predict, self._df_test_y)


    def save_model(self):
        joblib.dump(self._regression_model, self._output_path + self._output_file + ".pkl")

    
# Define inputs for creation of instance
clean_file_path = '/home/student/data_analytics/prediction_model/clean_files/66_1.csv'
output_path = '/home/student/data_analytics/prediction_model/'
y = 'duration'


# Create instance
instance = PredictionModel(clean_file_path, output_path, y)

#print(instance.df.shape)
#print(instance.df.dtypes)
#print(instance.y)
#print(instance.X)
instance.split_df()
#print(instance.initialize_model())
instance.initialize_model()
instance.getResultsLR()
#print("Intercept of Model ", instance._intercept)
print("R Squared Value Test ", instance._RSquaredTest)
print("R Squared Value Train ", instance._RSquaredTrain)
print("Mean Squared Error", instance._regression_model_mse)
#instance.getCoefficients()
instance.save_model()

