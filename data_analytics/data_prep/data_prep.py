import pandas as pd
import os, sys
import datetime
import csv, itertools
import dask.dataframe as dd

class DataPrep:

    def __init__(self, file_path, dtypes, file_name):
        # Variables to store OWM connection data:
        self._file_path = file_path
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

    def df_info(self):
        # Print the number of rows in csv data-frame
        print()
        print('File name:', self._file_path)
        print('Rows (cardinality):', ("{:,}".format(len(self.df))),'and columns:', ("{:,}".format(len(self.df.columns))))
        print(self.df.head())


    def create_df_dask(self):
        self._df = dd.read_csv(self.file_path, delimiter=';')

    def save_csv(self):
        # Save data frame to a CSV file
        self.df.to_csv(self.file_name+'.csv', sep=';')

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

    @staticmethod
    def types_leavetimes():
        dtypes = {}

        return dtypes


file_dir = os.path.dirname(os.path.abspath("__file__"))
parent_dir = os.path.dirname(file_dir)
grandparent_dir = os.path.dirname(parent_dir)

data_path = 'data/db_historic/'

# print("Filename:", __file__)

lt_2017 = '/home/student/data/db_historic/rt_leavetimes_2017_I_DB.txt'
lt_2016 = '/home/student/data/db_historic/rt_leavetimes_2016_I_DB.txt'
trips_2017 = '/home/student/data/db_historic/rt_trips_2017_I_DB.txt'
trips_2016 = '/home/student/data/db_historic/rt_trips_2016_I_DB.txt'

# Call the types_trips() function to get data types
trips_dtypes = DataPrep.types_trips()
leavetimes_dtypes = DataPrep.types_trips()

# Create instances for each file
# summary_trips_2017 = DataPrep(trips_2017, trips_dtypes, 'samples/sample_trips_2017')
# summary_trips_2016 = DataPrep(trips_2016, trips_dtypes, 'samples/sample_trips_2016')

summary_leavetimes_2017 = DataPrep(lt_2017, leavetimes_dtypes, 'samples/sample_leavetimes_2017')
# summary_leavetimes_2016 = DataPrep(lt_2016, leavetimes_dtypes, 'samples/sample_leavetimes_2016')

summary_leavetimes_2017.create_df_dask()
print("tst")
summary_leavetimes_2017.df_info()

