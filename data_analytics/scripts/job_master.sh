#!/bin/bash


extract_lineIDs="/home/student/data_analytics/scripts/extract_lineIDs.sh"
extract_bus_line="/home/student/data_analytics/scripts/extract_bus_line.sh"
temp_path="/home/student/data_analytics/prediction_model/extracted/tmp"
lineID_file="$temp_path/bus_lineIDs.txt"
merge_done="$temp_path/merge_done.txt"

# Make directory (-p does not output error if it already exists)
mkdir -p $temp_path

# If LineID_file exists, remove it
if [ -f $lineID_file ]; then
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

    count=0

    echo "testing:"
    for elem in "${a[@]}"; do

        echo "Element in array: $elem"

        # If element is found in the merge_finished file then:

        if [ "$(fgrep '$elem' $merge_done)" -ge 1 ]; then
            echo "Found $elem in file"
            count=$(($count+1))
            echo "count: $count"
            if [ $count -ge 5 ]; then
                exit
            fi
        else
            echo "Extracting bus line"
            bash $extract_bus_line $elem
            echo "$elem" >> $merge_done

        fi
    echo "done"
    done
    # Print out all elements in array
    # echo "${a[@]}"

fi

#
exit
