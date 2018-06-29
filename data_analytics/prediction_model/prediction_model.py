import pandas as pd
import os, sys
import datetime
import csv, itertools
import subprocess

class DataPrep:

    def __init__(self, file_path, dtypes, file_name, sample_file_path):
        self._file_path = file_path
        self._dtypes = dtypes
        self._sample_file_path = sample_file_path
        self._file_name = file_name
        self._df = None

    @property
    def file_name(self):
        return self._file_name

    @property
    def file_path(self):
        return self._file_path

    @property
    def df(self):
        return self._df

    @staticmethod
    def types_trips():
        dtypes = {'datasource': str,
                 'dayofservice': object,
                 'tripid': int, 'lineid': object,
                 'routeid': object,
                 'direction': object,
                 'plannedtime_arr': object,
                 'plannedtime_dep': object,
                 'actualtime_arr': object,
                 'actualtime_dep': object,
                 'basin': object,
                 'tenderlot': object,
                 'suppressed': str,
                 'justificationid': object,
                 'lastupdate': str,
                 'note': str}

        return dtypes

    def create_df(self):
        self._df = pd.read_csv(self._file_path, header=0, delimiter=';', nrows= 500)

    def save_csv(self):
        # Save data frame to a CSV file
        self._df.to_csv(self._sample_file_path, index = False)

    def df_stats(self):
        # Print the number of rows in csv data-frame
        print('Rows (cardinality):', ("{:,}".format(len(self.df))),'and columns:', ("{:,}".format(len(self.df.columns))))



    def extract_route_sample(self):
        os.system('/home/student/data_analytics/sample_files/./bus66.sh')
        # bashCommand = ['awk -F', '{ if ($4 == "+"66"+") print $0 }' '/home/student/data_analytics/sample_files/sample_trips.csv >> test.csv']
        # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()
        print('Done')

    def extract_route(self):
        print("executing shell script")
        os.system('/home/student/data_analytics/./bus66.sh')
        # bashCommand = ['awk -F', '{ if ($4 == "+"66"+") print $0 }' '/home/student/data_analytics/sample_files/sample_trips.csv >> test.csv']
        # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()
        print('extracted from full file')




class PredictionModel:

    def __init__(self, data_file_path, dtypes, file_name):
        # Variables to store OWM connection data:
        self._data_file_path = file_path
        self._dtypes = dtypes
        self._file_name = file_name
        self._df = None
        #self.save_csv()
        # self.df_info()

    # Python Class Encapsulation - Properties (getter), setters
    @property
    def file_path(self):
        return self._file_path

    @property
    def dtypes(self):
        return self._dtypes

    @property
    def file_name(self):
        return self._file_name

    @property
    def df(self):
        return self._df

    @staticmethod
    def types_leavetimes():
        dtypes = {}

        return dtypes



data_file_lt_2017 = '/home/student/data/db_historic/rt_leavetimes_2017_I_DB.txt'
data_file_lt_2016 = '/home/student/data/db_historic/rt_leavetimes_2016_I_DB.txt'
data_file_trips_2017 = '/home/student/data/db_historic/rt_trips_2017_I_DB.txt'
data_file_trips_2016 = '/home/student/data/db_historic/rt_trips_2016_I_DB.txt'

# Call the types_trips() function to get data types
trips_dtypes = DataPrep.types_trips()


# Routes to create
route66_trips = '/home/student/data_analytics/individual_bus_lines/route66_trips.csv'
sample_trips = '/home/student/data_analytics/sample_files/sample_trips.csv'

# Route names:
route_name = '66'

# Create instances for each file
summary_trips_2017 = DataPrep(data_file_trips_2017, trips_dtypes, route66_trips, sample_trips)
# summary_trips_2016 = DataPrep(trips_2016, trips_dtypes, 'samples/sample_trips_2016')
# summary_leavetimes_2017 = DataPrep(lt_2017, leavetimes_dtypes, 'samples/sample_leavetimes_2017')
# summary_leavetimes_2016 = DataPrep(lt_2016, leavetimes_dtypes, 'samples/sample_leavetimes_2016')

route66_trips_2017 = DataPrep(data_file_trips_2017, trips_dtypes, route66_trips, sample_trips)

print(route66_trips_2017.file_path)
print(route66_trips_2017.file_name)

# route66_trips_2017.create_df()
# route66_trips_2017.df_stats()
# route66_trips_2017.save_csv()
route66_trips_2017.extract_route()
#route66_trips_2017.extract_route()