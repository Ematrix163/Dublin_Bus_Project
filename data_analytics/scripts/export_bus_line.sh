#!/bin/bash

# Define file paths:
pathLT="/home/student/data/db_historic/rt_leavetimes_2017_I_DB.txt"
path_trips_df="/home/student/data/db_historic/rt_trips_2017_I_DB.txt"
pathBusTrips="/home/student/data_analytics/bus_lines/bus66_trips.csv"
pathBusLT="/home/student/data_analytics/bus_lines/bus66_lt.csv"
pathTripID="/home/student/data_analytics/bus_lines/bus66_tripID.csv"

# Create function for printing file sizes:
print_file_sizes () {

    # Create file size variables:
    FileSize_trips_df=$(du -h $path_trips_df)
    FileSize_LT=$(du -h $pathLT)
    FileSize_BusTrips=$(du -h $pathBusTrips)
    FileSize_BusLT=$(du -h $pathBusLT)

    # Print the file sizes
    echo "File sizes:"
    echo "$FileSize_LT"
    echo "$FileSize_trips_df"
    echo "$FileSize_BusLT"
    echo "$FileSize_BusTrips"
}

# Function to delete all files that have previously been made by this script:

delete_files () {

    if [ -f $pathBusLT ]
    then
        rm -f $pathBusLT;
    fi

    if [ -f $pathBusTrips ]
    then
        rm -f $pathBusTrips;
    fi

    echo "Deleted previous files"
}

# Function to delete temporary files
delete_temp_files () {

    if [ -f $pathTripID ]
    then
        rm -f $pathTripID;
        echo "Temporary file removed";

    else
        echo "Temporary file not removed";

    fi
}

# Call function to remove previously exported files
delete_files

echo "Exporting bus line files ..."
# Use awk to search column 4 for the bus line and append to $pathLine
head -n 1 $path_trips_df >> $pathBusTrips
awk -F';' '{ if ($4 == "66") print $0 }' $path_trips_df | sort -t';' -k2,2n >> $pathBusTrips
echo "File created: $pathBusTrips"

# Find all trip ids and create temporary file
awk -F';' '{ print $3 }' $pathBusTrips >> $pathTripID
echo "File created: $pathTripID"

# Use tripID file to search for each trip ID in the bus's leavetimes bus line file, create bus's leavetimes file
LC_ALL=C grep -f $pathTripID $pathLT | sort -t';' -k2,2n -k3,3n > $pathBusLT
echo "File created: $pathBusLT"

# Call function to delete temporary files
delete_temp_files

# Invoke the function to print file sizes:
print_file_sizes