#!/bin/bash

pathDf="/home/student/data/db_historic/rt_trips_2017_I_DB.txt"
outputPath="/home/student/data_analytics/prediction_model/extracted/tmp"
outputFile="/home/student/data_analytics/prediction_model/extracted/tmp/bus_lineIDs.csv"

# Make directory (-p does not output error if it already exists)
mkdir -p $outputPath

# Use awk to sort pathDf and append values to bus_lines.csv
awk -F";" '!_[$4]++' $pathDf | cut -d';' -f4 | grep . >> $outputFile

sed -i '1d' $outputFile

# Test to make sure file was created properly:
if [ -f $outputFile ] && [ $(wc -l <$outputFile) > 100 ]; then
    echo "Success - LineID file created"
    exit 0
else
    echo "Error - file not created" >&2
    exit 1
fi