#!/bin/bash

# File paths
pathDf="/home/student/data/db_historic/rt_trips_2017_I_DB.txt"
pathLine="/home/student/data_analytics/individual_bus_lines/route66_trips.csv"
pathLT="/home/student/data/db_historic/rt_leavetimes_2017_I_DB.txt"
pathTripID="/home/student/data_analytics/individual_bus_lines/bus66_tripID.csv"
pathBus66LT="/home/student/data_analytics/individual_bus_lines/bus66_lt.csv"

# Use awk to search column 4 for the bus line and append to $pathLine
head -n 1 $pathDf >> $pathLine
awk -F';' '{ if ($4 == "66") print $0 }' $pathDf >> $pathLine

echo "Bus line trips file created, row count:"

# Count lines in files
countDf="$(wc -l $pathDf | awk '{print $1}')"
countLine="$(wc -l $pathLine | awk '{print $1}')"

printf "%'.f\n" $countLine;

echo "Rows in trips data file:";
printf "%'.f\n" $countDf;


# Find all trip ids
awk -F';' '{ print $3 }' $pathLine >> $pathTripID
echo "created bus66_TripID.csv"

grep -f $pathTripID $pathLT | sort -t';' -k2,2 > bus66_lt.csv

# Count lines in files
count66LT="$(wc -l $pathBus66LT | awk '{print $1}')"

echo "Created bus66_lt.csv, row count:";
printf "%'.f\n" $count66LT;
