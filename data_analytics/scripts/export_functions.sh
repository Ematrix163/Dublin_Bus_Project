#!/bin/bash

create_folder() {
    # Make directory (-p does not output error if it already exists)
    mkdir -p /home/student/data_analytics/prediction_model/extracted

}

export_trips_file() {

    # Use awk to search column 4 for the bus line and append to $pathLine
    head -n 1 $path_trips_df >> $pathBusTrips
    # awk -F -v LineID="$LineID" 'BEGIN { if ($3 == LineID) print $0 }' $path_trips_df | sort -S 50% --parallel=4 -t',' -k1,1 -k2,2n -k4,4n >> $pathBusTrips
    awk -F',' '{ if ($3 ==LineID) print $0 }' LineID="$LineID" $path_trips_df | sort -S 50% --parallel=4 -t',' -k1,1 -k2,2n -k4,4n >> $pathBusTrips
    echo "File created: $pathBusTrips"

}

export_TripID_file() {

    # Find all trip ids and create temporary file
    awk -F',' '{ print $2 }' $pathBusTrips >> $pathTripID
    echo "File created: $pathTripID"

}

export_LeaveTimes_file() {

# Copy the first line of the full leavetimes file to the LineID only
head -n 1 $pathLT >> $pathBusLT
# Use tripID file to search for each trip ID in the bus's leavetimes bus line file, create bus's leavetimes file
LC_ALL=C grep -f $pathTripID $pathLT | sort -t',' -k1,1 -k2,2n -k3,3n | sed '$ d' >> $pathBusLT

echo "File created: $pathBusLT"

}

# Create function for printing file sizes:
print_file_sizes () {

    # Create file size variables:
    FileSize_trips_df=$(du -h $path_trips_df)
    FileSize_LT=$(du -h $pathLT)
    FileSize_BusTrips=$(du -h $pathBusTrips)
    FileSize_BusLT=$(du -h $pathBusLT)
    FileSize_Merge=$(du -h $pathMerge)

    # Print the file sizes
    echo "File sizes:"
    echo "$FileSize_LT"
    echo "$FileSize_trips_df"
    echo "$FileSize_BusLT"
    echo "$FileSize_BusTrips"
    echo "$FileSize_Merge"

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

    if [ -f $pathMerge ]
    then
        rm -f $pathMerge;
    fi

    echo "Previous files deleted"

}

# Function to delete temporary files
delete_temp_files () {
    # Counter for tracking deleted files
    counter=0

    if [ -f $pathTripID ]
    then
        rm -f $pathTripID;
        # Increase counter by one
        counter=$((counter+1));
    fi

    if [ -f $pathBusLT ]
    then
        rm -f $pathBusLT;
        # Increase counter by one
        counter=$((counter+1));
    fi

    if [ $counter>0 ]
    then
        echo "Temporary files deleted ($counter x)";

    else
        echo "Temporary files not removed";

    fi
}

# Function add the columns that make the data unique (DayOfService, TripID)
add_unique_columns () {

    echo "Adding primary keys to CSV files"
    awk -F',' 'BEGIN {OFS = FS} {$10 = $1 $2; print;}' $pathBusLT > tmp && mv tmp $pathBusLT
    awk -F',' 'BEGIN {OFS = FS} {$10 = $1 $2; print;}' $pathBusTrips > tmp && mv tmp $pathBusTrips

}

# Function to merge CSVs
merge_files () {

    echo "Merging files"
    sort -t , -k 10,10 $pathBusLT > sort1.csv
    sort -t , -k 10,10 $pathBusTrips > sort2.csv
    join -t',' -j1 10 -j2 10 sort1.csv sort2.csv -a1 > $pathMerge
    echo "Copy header from last line of file"
    header=$(tail -n 1 $pathMerge)

    # Append header to file
    sed -i "1 s/^.*$/$header/" $pathMerge
    # Remove the last line of file (sorted header)
    head -n -1 $pathMerge > tmp && mv tmp $pathMerge
    echo "File created: $pathMerge"

}

# Function to drop unnecessary columns
drop_columns () {

echo "Dropping columns"
cut -d, -f2-10,13-15 $pathMerge > tmp && mv tmp $pathMerge

}

# Function to re-order columns
re-order_columns () {

echo "Re-ordering columns"
awk -F',' 'BEGIN {OFS = FS} {print $10, $12, $11, $1, $2, $3, $4, $5, $6, $7, $8}' $pathMerge > tmp && mv tmp $pathMerge

}

# Function to sort columns
sort_columns () {
    echo "Sorting columns"
    sort -t',' -k2,2n -k3,3 -k4,4 -k5,5n -k6,6n $pathMerge > tmp && mv tmp $pathMerge

}

