#!/usr/bin/env bash


path_trips_df="/home/student/data/clean_data/trips17.csv"

# AWK finds rows with unique values for column 3 and column 2, sorts it and displays only the unique ones
unique_TID="$(awk -F"," '!unique[$3, $2]++' $path_trips_df | sort -u | uniq -c | sort -n )"

echo "$unique_TID"

