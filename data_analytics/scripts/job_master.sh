#!/bin/bash


extract_lineIDs="/home/student/data_analytics/scripts/extract_lineIDs.sh"
extract_bus_line="/home/student/data_analytics/scripts/extract_bus_line.sh"
temp_path="/home/student/data_analytics/prediction_model/extracted/tmp/"
lineID_file="$temp_path/bus_lineIDs.csv"
merge_finished="$temp_path/merge_done.csv"

# Make directory (-p does not output error if it already exists)
mkdir -p $temp_path
touch $merge_finished
    if [ -f $lineID_file ]
    then
        rm -f $lineID_file;
    fi

# Run the extract_lineIDs.sh script (as another process)
bash $extract_lineIDs ; reply=$?
echo "REPLY=${reply}"
# if output is not equal to zero print "Error", else
if [ $reply -ne 0 ]; then
    echo "Error"
    exit 1

else
    count=$(wc -l <$lineID_file)
    echo "Total number of LineIDs:$count";
    # Create an array (a) from file
    readarray a < $lineID_file

    # Print first line in array
    printf "line 1: %s\n" "${a[0]}"
    # Delete the LineID file
    rm $lineID_file

    echo "testing:"
    for index in "${a[@]}";
    do
        echo $index
        if grep -F "$index" $merge_finished; then
            echo "Found!"
            exit 1
        else
            bash $extract_bus_line $index
            echo "Horray!"


        fi
    done
    # Print out all elements in array
    # echo "${a[@]}"

fi

#
exit
