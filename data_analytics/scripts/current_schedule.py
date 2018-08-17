# -*- coding: utf-8 -*

import pandas as pd
import os
import shutil
import string
import unittest
import subprocess
import signal
import warnings
import requests


import zipfile
import sys


# The current schedule class is for methods that relate to the current schedule data
class CurrentSchedule:

    _mysql_load_command = "bash /home/student/data_analytics/scripts/mysql_load_data.sh"
    _output_file = "dublinBus_schedule_current.csv"
    _download_URL_path = '/home/student/data_analytics/tmp/'
    _schedule_file = _download_URL_path+'google_transit_dublinbus.zip'
    _gtfs_stops_file = _download_URL_path+'stop_times.txt'
    _gtfs_trips_file = _download_URL_path+'trips.txt'


    # This method automatically initializes the class variables when an class instance is created
    def __init__(self):
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
        self._df_one = pd.read_csv(self._gtfs_stops_file)
        self._df_two = pd.read_csv(self._gtfs_trips_file)

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
        self._df_merged = self._df_merged[~self._df_merged['stop_id'].isin(['gen:'])]

    def clean_columns(self):
        self._df_merged['trip_headsign'] = self._df_merged['trip_headsign'].str.replace(',', ' ')

    def create_directory(self):
        try:
            os.mkdir(self._download_URL_path)
        except OSError:
            print ("ERROR - Creation of output directory %s failed" % self._download_URL_path)
            raise
        else:
            print("Successfully created output directory %s " % self._download_URL_path)

    def export(self):
        self._df_merged.index.name = 'pkey'
        self._df_merged.to_csv(self._download_URL_path+self._output_file, index=True)
        print("Created merged csv file %s" % self._download_URL_path+self._output_file)
        print(self._df_merged.shape)

    # Calls a shell script to get mysql to truncate table and load data in file
    def mysql_load_data(self):
        process = subprocess.Popen([ self._mysql_load_command ], stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        stdout = process.communicate()[0]
        print ('STDOUT:{}'.format(stdout))
        # os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        print("loading data finished")

    def download(self):
        print("Downloading starting...")
        url = 'http://www.transportforireland.ie/transitData/google_transit_dublinbus.zip'

        req = requests.get(url, allow_redirects=True)
        open(self._schedule_file, 'wb').write(req.content)
        print("Downloaded status:", req.status_code)
        return req.status_code


    def unzip(self):
        print('Unzipping file')
        print(self._download_URL_path)
        if os.path.exists(self._schedule_file):
            with zipfile.ZipFile(self._schedule_file, "r") as zip_ref:
                zip_ref.extractall(self._download_URL_path)


    # Delete gtfs files
    def delete_gtfs_files(self):

        ## If file exists, delete it ##
        if os.path.isdir(self._download_URL_path):
            shutil.rmtree(self._download_URL_path, ignore_errors=True)
            print("Removed files in folder %s" % self._download_URL_path)
        else:  ## Show an error ##
            print("Note: %s Do not need to remove any temporary files" % self._download_URL_path)


if __name__ == '__main__':
    unittest.main()
