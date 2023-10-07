import arcpy
import os

gdb_path = r"D:\SEM_III\Programming_3\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["ESTAB", "NAME", "ZIP"]

# Use a search cursor to establish read-only access to the feature class
with arcpy.da.SearchCursor(fc_path, fields_list) as s_cursor:
    for row in s_cursor:
        estb_year = int(row[0])
        if estb_year > 2000:
            print("The name of the Hotel is {} , and it was established in year {}. ".format(row[1], row[0]))

print("Process Completed")