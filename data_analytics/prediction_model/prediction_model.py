#trying to make changes
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class PredictionModel:

    def __init__(self, input_file_path, output_path, output_file_name, y):
        self._file_path = input_file_path
        self._output_path = output_path
        self._output_file_name = output_file_name
        # Creates df upon instance initialization:
        self._df = pd.read_csv(self._file_path, header=0, delimiter=',')
	# Drop all columns that aren't required features for training:
        self.drop_attributes()
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

    # Target Feature (Duration), Features (Dayofweek, Timeofday, weather)

    def drop_attributes(self):
        features = ['duration','arrive_time','dayofweek','month','temp']
        self._df = self._df[features]

    # Split the data-frame into the train x, train y, test x and test y sets:
    def split_df(self):
        self._df_train_X, self._df_test_X, self._df_train_y, self._df_test_y = train_test_split(self._X, self._y, test_size=0.25, random_state=1)

    # Initialize the regression model:
    def initialize_model(self):

        self._regression_model = LinearRegression()
        self._regression_model.fit(self._df_train_X, self._df_train_y)
     
    #get the parameters of model		
    def getCoefficients(self):
        self._intercept = self._regression_model.intercept_[0]
        self._RSquared = self._regression_model.score(self._df_test_X, self._df_test_y)
        self._y_predict = self._regression_model.predict(self._df_test_X)
        self._regression_model_mse = mean_squared_error(self._y_predict, self._df_test_y)


# Define inputs for creation of instance
clean_file_path = '/home/student/data_analytics/bus_line_cleanse/result_of_66-dir1.csv'
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
instance.getCoefficients()
print("Intercept of Model ", instance._intercept)
print("R Squared Value ", instance._RSquared)
print("Mean Squared Error", instance._regression_model_mse)


