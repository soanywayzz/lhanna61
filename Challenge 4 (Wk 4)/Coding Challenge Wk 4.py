# For this coding challenge, I want you to find a particular tool that you like in arcpy. It could be a tool that
# you have used in GIS before or something new. Try browsing the full tool list to get some insight here
# (click Tool Reference on the menu list to the left).
# Set up the tool to run in Python, add some useful comments, and importantly, provide some example
# data in your repository (try to make it open source, such as Open Streetmap, or RI GIS. You can add it as a zip
# file to your repository.
# My only requirements are:
# Comment your code well.
# Ensure that the code will run with only a single change to a single variable (i.e. a base folder location).


# STEP ONE:
# import appropriate tools/extensions.

import os
import arcpy
arcpy.CheckOutExtension("Spatial")

print "Extensions have been imported."
#STEP TWO:
# Set arcpy/GIS to allow files to be overwritten (this is done so if/when the script is rerun, it will
# automatically delete the previous runs version.
arcpy.env.overwriteOutput = True

# STEP THREE:
#                              ***change file path location here *** (in between quotations).
##          *****NOTE: If any crashes take place, please make sure that there are no spaces in your folder names*****
##   ADDITIONAL NOTE: Copy all working/data files into the file path you are setting up as your mainDirectory location.


mainDirectory = raw_input(r"Enter your file path here: ") ## This allows the user to paste in their own file path
# where their data is stored-- without them having to figure out where to change the link.

outputDirectory = os.path.join(mainDirectory, "outputs")
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)


# Clip Tool: Set Variables
in_features = os.path.join(mainDirectory, "HUC12_RI_09.shp")
clip_features = os.path.join(mainDirectory, "towns.shp")
out_feature_class = os.path.join(outputDirectory, "Clipped.shp")


# Run Clip Tool
arcpy.Clip_analysis(in_features, clip_features, out_feature_class)

# Confirm Operation is Completed

print "Clipping Completed"
