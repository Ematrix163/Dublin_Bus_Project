# -*- coding: utf-8 -*

from current_schedule import CurrentSchedule




# Create instance
instance = CurrentSchedule()


# Delete temporary files
instance.delete_gtfs_files()

# Create required folders:
instance.create_directory()

# Download GTFS current schedule files from DublinBus
instance.download()

# Unzip downloaded files
instance.unzip()

# Create dataframes
instance.create_data_frames()

# Merge dataframes
instance.merge()

#perform cleaning operations

instance.create_line_id()
instance.modify_stop_id()
instance.clean_columns()

#
instance.export()
instance.mysql_load_data()
instance.delete_gtfs_files()
