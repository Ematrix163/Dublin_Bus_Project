#!/usr/bin/env bash


schedule_path="/home/student/data_analytics/tmp/dublinBus_schedule_current.csv"
table_name="dublinBus.dublinBus_schedule_current"
log=/home/student/data_analytics/scripts/logs/mysql_load_data.log

echo "Truncating table $table_name"
mysql -u front_end -p'password' dublinBus -e "TRUNCATE $table_name"
echo "Loading data into $table_ename"
mysql -u front_end -p'password' --execute="LOAD DATA INFILE '$schedule_path' INTO TABLE $table_name FIELDS TERMINATED BY ',' IGNORE 1 LINES; SHOW WARNINGS"
echo "End of script"
exit

