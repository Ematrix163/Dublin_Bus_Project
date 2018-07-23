#!/bin/bash

# Make functions.sh file accessible by this script:
source extract_functions.sh


# If input parameters are less than one echo "parameter required"

if [ $# -lt 1 ] ; then
        echo "Bus LineID required as a parameter"
        exit 1
fi

# Assign parameter one to a variable
LineID=$1

#print a new line:
printf "%s\n\n" ""

echo "Extracting files for bus LineID $LineID..."

# Define file paths:
pathLT="/home/student/data/clean_data/leave17.csv"
path_trips_df="/home/student/data/clean_data/trips17.csv"
pathBusTrips="/home/student/data_analytics/prediction_model/extracted/tmp/bus_"$LineID"_trips.csv"
pathBusLT="/home/student/data_analytics/prediction_model/extracted/tmp/bus_"$LineID"_lt.csv"
pathTripID="/home/student/data_analytics/prediction_model/extracted/tmp/bus_"$LineID"_tripID.csv"
pathMerge="/home/student/data_analytics/prediction_model/extracted/bus_"$LineID"_merge.csv"


# Call function to remove previously exported files
delete_previous_files

# Call function to create the "exported" folder if it doesn't already exist
create_folder

# Call function to export trips file for LineID
export_trips_file

# Call function to export all TripIDs for LineID
export_TripID_file

# Call function to export all TripIDs for LineID
export_LeaveTimes_file

# Add unique columns
add_unique_columns

# Merge files
merge_files

# Drop columns
drop_columns

# Re-order columns
re-order_columns

# Re-order columns
sort_columns

#print a new line:
printf "%s\n\n" ""

# Call the function to print summary info
print_file_sizes

# Delete temporary files
delete_temp_files

# Count the merged files's lines:
wc -l $pathMerge