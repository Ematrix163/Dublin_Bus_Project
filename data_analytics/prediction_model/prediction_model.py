import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.stats import zscore
import numpy as np
import math
from sklearn.linear_model import LinearRegression

class PredictionModel:

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
        self._y = self.df[[y]]
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

    # Target Feature (Duration), Features (Dayofweek, Timeofday, weather)
    #this needs to be tidied 
    def drop_attributes(self):
        
        features = ['delay','time','dayofweek','month','temp','Sky is Clear','broken clouds','few clouds','fog','drizzle','light intensity drizzle','light intensity drizzle rain','light intensity shower rain','light rain','light shower sleet','mist','moderate rain','overcast clouds','proximity shower rain','scattered clouds','shower rain', '312','317','346','400', '493', '494', '495', '1444','1445','1449','1450','1451','2191','2192', '2193','2194','2195','2196','2197','2198','2193','2200','2201','2213','2214','2215','2216','2217','2218','2219','3365','3366','3367','3886','3887','3888','3918','3954','3955','3956','3957','3958','3959','3960','3961','3962','3963','3964','3965','3966','3968','4401','4599','5113','5114','7078','7186','7187','7239','7391' ]
        self._df = self._df[features]

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

    
# Define inputs for creation of instance
clean_file_path = '/home/student/data_analytics/bus_lines/result_of_66-dir1Model.csv'
output_path = '/data_analytics/prediction_model/'
output_file_name = 'bus66.csv'
y = 'duration'


# Create instance
instance = PredictionModel(clean_file_path, output_path, output_file_name, y)

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

