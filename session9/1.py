# lecture 7
temp_file = open("temp.txt" , "w")
#or put the address of the directory of the file_obj
""" to check the address:
''' import os
    os getw


    "r" mode is read-only mode and ...
    look at the table of different modes
    the default value of file = is sys.stdout // using help.print
"""
print("first line", file = temp_file)
print("second line", file = temp_file)
print("third line", file = temp_file)

temp_file.close()
