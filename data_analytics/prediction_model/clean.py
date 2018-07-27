import pandas as pd
import numpy as np
from typing import Any


class CleanFile:

    """Class that takes merged trips and leave times file and finds duration from one stop to another and merges with  historic weather data
    """

    def __init__(self, input_file_path, output_path, weather_file, direction):
        self._file_path = input_file_path
        self._output_path = output_path
        self._weather = weather_file
        self._direction = direction
        # Creates data frame upon instance initialization:
        self._df = pd.read_csv(self._file_path, delimiter=',')
        # reads in weather file as a data frame
        self._weatherdf = pd.read_csv(weather_file, delimiter=',')
        self.drop_weather_attributes()
        self.isolate_direction()
        # saving the line ID and direction to name files
        self._lineID = self._df['LineID'].iloc[1]
        self._dir = self._df['Direction'].iloc[1]
        self._output_file_name = str(self._lineID) + "_" + str(self._dir)

        # defining variables involved in creating the file suitable for model
        self._u = None
        self._result = None

        self.create_model_file()
        self.save_result()

    # Getter methods to return protected variables.
    @property
    def input_file_path(self):
        return self._file_path

    @property
    def output_path(self):
        return self._output_path

    @property
    def weather_file(self):
        return self._weather

    @property
    def direction(self):
        return self._direction

    # keep only the weather features needed in model
    def drop_weather_attributes(self):

        features = ['dt', 'temp', 'pressure', 'humidity', 'wind_speed', 'weather_description', 'clouds_all', 'wind_deg']
        self._weatherdf = self._weatherdf[features]

    # only keep rows with the specified direction
    def isolate_direction(self):
        if self._direction ==1 or self._direction ==2:
            self._df = self._df.loc[(self._df['Direction'] == self._direction)]
        else:
            raise Exception('Direction must be either 1 or 2')

    # Creating target feature duration, creating features to be used in model (weather features, dayofweek, month etc)
    def create_model_file(self):

        # creating a new column which is a combination of the unique keys
        self._df['comb'] = self._df['DayOfService'].map(str) + self._df['TripID'].map(str)
        self._u = self._df['comb'].unique()

        self._result = pd.DataFrame(
            columns=['lineid', 'direction', 'dt', 'dayofweek', 'month', 'day', 'arrive_time', 'start_point', 'end_point', 'duration'])

        for date_trip in self._u:
            day_trip = self._df.loc[(self._df['comb'] == date_trip)].sort_values(by=['ProgrNumber'])

            day_trip.index = range(len(day_trip))

            # calculate the time between each pair stops
            time = day_trip['ActualTime_Arr'].shift(-1) - day_trip['ActualTime_Arr']
            time.drop(time.tail(1).index, inplace=True)

            # Get the month and the day, month and the day of week
            month = pd.to_datetime(day_trip['DayOfService']).dt.month
            day = pd.to_datetime(day_trip['DayOfService']).dt.day
            dayofweek = pd.to_datetime(day_trip['DayOfService']).dt.dayofweek

            # Add datetime and actual_arrive time as current unix time
            datetime = pd.DatetimeIndex(day_trip['DayOfService']).astype(np.int64) / 1000000000 + day_trip[
                'ActualTime_Arr']
            datetime = pd.DataFrame(data={'unixtime': datetime})

            # Convert float to int, this is for the following merge operation
            datetime['unixtime'] = datetime['unixtime'].astype(np.int64)

            # Set End point
            end_point = day_trip['StopPointID'].shift(-1)
            end_point.drop(end_point.tail(1).index, inplace=True)

            # merge columns
            merge = pd.concat(
                [day_trip['LineID'], day_trip['Direction'], datetime, dayofweek, month, day, day_trip['ActualTime_Arr'],
                 day_trip['StopPointID'],
                 end_point, time], axis=1)

            # Change the name of columns
            merge.columns = ['lineid', 'direction', 'dt', 'dayofweek', 'month', 'day', 'arrive_time', 'start_point',
                               'end_point', 'duration']
            merge.drop(merge.tail(1).index, inplace=True)

            self._weatherdf = self._weatherdf.sort_values(by=['dt'])
            merge = merge.sort_values(by=['dt'])

            # merge two tables
            r = pd.merge_asof(merge, self._weatherdf.sort_values('dt'), on="dt", direction='nearest')

            self._result = pd.concat([r, self._result], sort = True)

    # save result to a csv file
    def save_result(self):
        self._result.to_csv(self._output_path + self._output_file_name +'.csv')

"""
This was a testing instance before running on all routes
#Define inputs for creation of instance
input_file_path = '/home/student/data_analytics/bus_lines/single_bus_line/bus_66_merge.csv'
output_path = '/home/student/data_analytics/clean_files/'
weather_file ='/home/student/data/weather/2017weatherClean.csv'
direction = 1

instance = cleanFile(input_file_path, output_path, weather_file, direction)
#print(instance._df)
instance.create_model_file()
instance.save_result()
print('finished')
"""