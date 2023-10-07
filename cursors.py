"""
S
"""

import arcpy
import os

gdb_path = r"D:\SEM_III\Programming_3\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = 'MajorAttractions'
fc_path = os.path.join(gdb_path,fc_name)

fields_list = ["ESTAB","ZIP","NAME"]

# use the search cursor to establish a read only access to the feature class

#s_cursor = arcpy.da.SearchCursor(fc_path,fields_list)

"""for row in s_cursor:
    print("{}, {}, {}".format(row[1],row[0],row[2]))
    #print(row[1],row[0],row[2])

#deleting the cursor
del s_cursor

print("process complete")"""

with arcpy.da.SearchCursor(fc_path,fields_list)as s_cursor:
    for row in s_cursor:
        print("{}, {}, {}".format(row[1],row[0],row[2]))
        #print(row[1],row[0],row[2])

    #deleting the cursor
    del s_cursor

    print("process complete")