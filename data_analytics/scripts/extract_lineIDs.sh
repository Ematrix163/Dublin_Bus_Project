#!/bin/bash

pathDf="/home/student/data/db_historic/rt_trips_2017_I_DB.txt"
pathLineID="/home/student/data_analytics/prediction_model/bus_lineIDs.csv"
# Use awk to sort pathDf and append values to bus_lines.csv
awk -F";" '!_[$4]++' $pathDf | cut -d';' -f4 | grep . >> $pathLineID

sed -i '1d' $pathLineID

