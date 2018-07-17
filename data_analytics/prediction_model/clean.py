import pandas as pd
import numpy as np
from typing import Any


class cleanFile:

    """Class that takes merged trips and leave times file and finds duration from one stop to another and merges with  historic weather data
    """

    def __init__(self, input_file_path, output_path, weather_file, direction):
        self._file_path = input_file_path
        self._output_path = output_path
        self._weather = weather_file
        self._direction = direction
        # Creates df upon instance initialization:
        self._df = pd.read_csv(self._file_path, delimiter=',')
        self._weatherdf = pd.read_csv(weather_file, delimiter=',')
        self.drop_attributes()
        self.isolate_direction()
        self._lineID = self._df['LineID'].iloc[1]
        self._dir = self._df['Direction'].iloc[1]
        self._output_file_name = str(self._lineID) + "_" + str(self._dir)

        self._u = None
        self._a = None
        self._r = None
        self._result = None

    # keep only the weather features needed in model
    def drop_attributes(self):

        features = ['dt', 'temp', 'pressure', 'humidity', 'wind_speed', 'weather_description', 'clouds_all', 'wind_deg']
        self._weatherdf = self._weatherdf[features]

    # only keep rows with the specified direction
    def isolate_direction(self):

        self._df = self._df.loc[(self._df['Direction'] == self._direction)]

    # Creating the target feature duration and merging in the weather file
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
            self._a = pd.concat(
                [day_trip['LineID'], day_trip['Direction'], datetime, dayofweek, month, day, day_trip['ActualTime_Arr'], day_trip['StopPointID'],
                 end_point, time], axis=1)
            # Change the name of columns
            self._a.columns = ['lineid', 'direction', 'dt', 'dayofweek', 'month', 'day', 'arrive_time', 'start_point', 'end_point',
                               'duration']
            self._a.drop(self._a.tail(1).index, inplace=True)

            self._weatherdf = self._weatherdf.sort_values(by=['dt'])
            self._a = self._a.sort_values(by=['dt'])

            # merge two tables
            self._r = pd.merge_asof(self._a, self._weatherdf.sort_values('dt'), on="dt", direction='nearest')

            self._result = pd.concat([self._r, self._result], sort = True)



    # save result to a csv file
    def save_result(self):
        self._result.to_csv(self._output_path + self._output_file_name +'.csv')

"""
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