import pandas as pd
import os, sys

def prepare_trip_file():
    file_dir = "/home/student/data/db_historic/rt_trips_2017_I_DB.txt"
    # read trips 2016 .txt file into dataframe16
    trips17 = pd.read_csv(file_dir, delimiter=';')

    # THIS cell removes all rows where suppressed is equal to 1, then counts to check there are no rows with this values left
    suppressed_is_1 = trips17['suppressed'] == 1
    is_suppressed = trips17[suppressed_is_1]
    print(
    "Number of rows in trips17 where suppressed column has value 1 (before they are removed): ", is_suppressed.shape[0])

    trips17 = trips17[trips17.suppressed != 1]

    suppressed_is_1 = trips17['suppressed'] == 1
    is_suppressed = trips17[suppressed_is_1]
    print("Number of rows in trips17 where suppressed column has value 1: ", is_suppressed.shape[0])
    print()

    # Drop Columns
    print("Drop Columns")
    trips17 = trips17.drop('datasource', axis=1)
    trips17 = trips17.drop('basin', axis=1)
    trips17 = trips17.drop('tenderlot', axis=1)
    trips17 = trips17.drop('justificationid', axis=1)
    trips17 = trips17.drop('lastupdate', axis=1)
    trips17 = trips17.drop('note', axis=1)

    print("Change data type:")
    # THIS CELL WILL change datatype of dayofservice from string to datetime format
    trips17['dayofservice'] =  pd.to_datetime(trips17['dayofservice'], dayfirst=True)

    trips17.shape

    #CREATE CSV of trips16
    print("Create CSV:")
    trips17.to_csv('trips17_test.csv', index=False, header=False)

def prepare_leave_times_file():

    lt_file = "/home/student/data/db_historic/rt_leavetimes_2017_I_DB.txt"
