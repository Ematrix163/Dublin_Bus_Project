#!/usr/bin/env bash


schedule_path="/home/student/data_analytics/prediction_model/tmp/dublinBus_schedule_current.csv"
table_name="dublinBus.dublinBus_schedule_current"
log=/home/student/data_analytics/prediction_model/scripts/logs/mysql_load_data.log

mysql -u front_end -p --execute="LOAD DATA INFILE '$schedule_path' INTO TABLE $table_name FIELDS TERMINATED BY ',' IGNORE 1 LINES; SHOW WARNINGS" > $log


