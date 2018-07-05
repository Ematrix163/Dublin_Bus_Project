#!/bin/bash

#

if [ $# -lt 1 ] ; then
        echo "Bus LineID required as a parameter"
        exit 1
fi

LineID=$1

echo "Creating files for bus LineID $LineID"

# Define file paths:
pathLT="/home/student/data/clean_data/leave17.csv"
path_trips_df="/home/student/data/clean_data/trips17.csv"
pathBusTrips="/home/student/data_analytics/bus_lines/bus_"$LineID"_trips.csv"
pathBusLT="/home/student/data_analytics/bus_lines/bus_"$LineID"_lt.csv"
pathTripID="/home/student/data_analytics/bus_lines/bus_"$LineID"_tripID.csv"

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

    now=$(date +%Y%m%d%H%M%S)
    printf '%(%a %b %d %T %Z %Y)T:%s\n' -1 $(hostname)
    echo "$LineID files created - $now"
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
# awk -F -v LineID="$LineID" 'BEGIN { if ($3 == LineID) print $0 }' $path_trips_df | sort -S 50% --parallel=4 -t',' -k1,1 -k2,2n -k4,4n >> $pathBusTrips
awk -F',' '{ if ($3 ==LineID) print $0 }' LineID="$LineID" $path_trips_df | sort -S 50% --parallel=4 -t',' -k1,1 -k2,2n -k4,4n >> $pathBusTrips
echo "File created: $pathBusTrips"

# Find all trip ids and create temporary file
awk -F',' '{ print $2 }' $pathBusTrips >> $pathTripID
echo "File created: $pathTripID"

# Copy the first line of the full leavetimes file to the LineID only
head -n 1 $pathLT >> $pathBusLT
# Use tripID file to search for each trip ID in the bus's leavetimes bus line file, create bus's leavetimes file
LC_ALL=C grep -f $pathTripID $pathLT | sort -t',' -k1,1 -k2,2n -k3,3 | sed '$ d' >> $pathBusLT
echo "File created: $pathBusLT"

# Call function to delete temporary files
delete_temp_files

# Invoke the function to print summary info:
print_file_sizes

# 4084264
