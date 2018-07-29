import pandas as pd
import os
import shutil
import string

import subprocess
import pexpect
import sys


# The current schedule class is for methods that relate to the current schedule data
class CurrentSchedule:

    _mysql_load_command = "bash /home/student/data_analytics/scripts/mysql_load_data.sh"
    _output_path = "/home/student/data_analytics/prediction_model/tmp/"
    _output_file = "dublinBus_schedule_current.csv"

    # This method automatically initializes the class variables when an class instance is created
    def __init__(self, input_path_one, input_path_two):
        self._input_path_one = input_path_one
        self._input_path_two = input_path_two
        self._df_one = None
        self._df_two = None
        self._df_merged = None
        self.password = None
        self.command = None

    # Python getter method
    @property
    def input_file_path(self):
        return self._input_file_path

    def create_data_frames(self):
        self._df_one = pd.read_csv(self._input_path_one)
        self._df_two = pd.read_csv(self._input_path_two)

    # Method to merge the path one and path two class variables
    def merge(self):
        # merge with the main df basedhttps://stackoverflow.com/questions/23441994/truncate-table-via-command-line-in-linux on year and country
        self._df_merged = pd.merge(self._df_one, self._df_two, how='left', left_on=['trip_id'], right_on=['trip_id'])



    # Creates line_id col in dataframe
    def create_line_id(self):
        self._df_merged['line_id'] = self._df_merged['route_id']
        self._df_merged['A'], self._df_merged['line_id'], self._df_merged['C'], self._df_merged['D'] = self._df_merged['line_id'].str.split('-', 3).str
        self._df_merged.drop('A', axis=1, inplace=True)
        self._df_merged.drop('C', axis=1, inplace=True)
        self._df_merged.drop('D', axis=1, inplace=True)

    def modify_stop_id(self):
        self._df_merged['stop_id'] = self._df_merged['stop_id'].astype(str).str[-4:]

    def clean_columns(self):
        self._df_merged['trip_headsign'] = self._df_merged['trip_headsign'].str.replace(',', ' ')

    def create_directory(self):
        try:
            os.mkdir(self._output_path)
        except OSError:
            print ("Creation of directory %s failed" % self._output_path)
        else:
            print ("Successfully created directory %s " % self._output_path)

    def delete_tmp(self):

        ## If file exists, delete it ##
        if os.path.isdir(self._output_path):
            shutil.rmtree(self._output_path)
            print("Removed files in folder %s" % self._output_path)
        else:  ## Show an error ##
            print("Note: %s Do not need to remove any temporary files" % self._output_path)

    def export(self):
        self._df_merged.index.name = 'pkey'
        self._df_merged.to_csv(self._output_path+self._output_file, index=True)
        print("Created merged csv file %s" % self._output_path+self._output_file)

    # Calls a shell script to get mysql to truncate table and load data in file
    def mysql_load_data(self):
        #    mysqlimport --ignore-lines=1 --fields-terminated-by=, --verbose --local -u [user] -p [database] /path/to/address.csv
        subprocess.Popen([ self._mysql_load_command ], shell=True)

# Schedule File paths
current_stop_times = "/storage/current_schedule/stop_times.txt"
current_trips = "/storage/current_schedule/trips.txt"


# Create instance
instance = CurrentSchedule(current_stop_times, current_trips)

instance.delete_tmp()
instance.create_data_frames()
instance.merge()
instance.create_line_id()
instance.modify_stop_id()
instance.clean_columns()
instance.create_directory()
instance.export()
instance.mysql_load_data()
#instance.delete_tmp()


