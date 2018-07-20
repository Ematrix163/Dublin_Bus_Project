#!/bin/bash


extract_lineIDs="/home/student/data_analytics/scripts/extract_lineIDs.sh"
extract_file="/home/student/data_analytics/prediction_model/extraction_job_master/bus_lineIDs.csv"
# Run the extract_lineIDs.sh script (as another process)
bash $extract_lineIDs ; reply=$?
echo "REPLY=${reply}"
# if output is not equal to zero print "Error", else
if [ $reply -ne 0 ]; then
    echo "Error"
    exit 1

else
    count=$(wc -l <$extract_file)
    echo "Total number of LineIDs:$count";
    # Create an array (a) from file
    readarray a < $extract_file
    # Print first line in array
    printf "line 1: %s\n" "${a[0]}"
    # Delete the LineID file
    rm $extract_file
    # Print out all elements in array
    # echo "${a[@]}"
fi
exit $reply
