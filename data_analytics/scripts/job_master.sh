#!/bin/bash


extract_lineIDs="/home/student/data_analytics/scripts/extract_lineIDs.sh"
extract_bus_line="/home/student/data_analytics/scripts/extract_bus_line.sh"
temp_path="/home/student/data_analytics/prediction_model/extracted/tmp/"
lineID_file="$temp_path/bus_lineIDs.txt"
merge_done="$temp_path/merge_done.txt"

# Make directory (-p does not output error if it already exists)
mkdir -p $temp_path

if [ -f $lineID_file ]; then
        rm -f $lineID_file;
fi

if [ ! -f $merge_done ]; then
        touch $merge_done
fi

# Run the extract_lineIDs.sh script (as another process)
bash $extract_lineIDs ; reply=$?
echo "REPLY=${reply}"

# if output is not equal to zero print "Error", else
if [ $reply -ne 0 ]; then
    echo "Error"
    exit 1

# Create an array with bus LineIDs, for each elem in array execute extract_bus_line.sh
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
    for elem in "${a[@]}";
    do
        # If element already in the $merge_done file, skip
        if ack -w $elem $merge_done; then
            echo "Bus LineID "$elem"has already been processed"
            true
        else
            # Execute script to extract bus line:
            echo "Extracting bus line ID "$elem"..."
            bash $extract_bus_line $elem >> extraction_output.log 2>&1
            # prepend LineID to $merge done file
            printf "\n$elem" >> $merge_done
            echo -en "\e[1A"; echo -e "\e[0K\rBus LineID "$elem"extracted"
            ((count++))
        fi


        #if [ $count -eq 2 ]; then
        #echo "Count is two"
        #exit
        #fi

    done
    # Print out all elements in array
    # echo "${a[@]}"

fi

#
exit
