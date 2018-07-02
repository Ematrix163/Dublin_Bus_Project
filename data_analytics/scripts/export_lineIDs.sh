#!/bin/bash

pathDf="/home/student/data/db_historic/rt_trips_2017_I_DB.txt"

# Use awk to sort pathDf and append values to bus_lines.csv
awk -F";" '!_[$4]++' $pathDf | cut -d';' -f4 | grep . >> bus_lines.csv

