##Python Midterm: use arcpy and python.
##Output Requirements: provide example data and the code used.
##Goal: write code that manipulates a dataset across three different proesses
## (ex: extracting, modifying and exporting data.)


# Setup: Step One
# import appropriate tools.
import os
import arcpy
arcpy.CheckOutExtension("Spatial")

# Setup: Step Two
# set arcpy/GIS to allow files to be overwritten (this is done so if/when the script is rerun, it will
# automatically delete the previous runs version.
arcpy.env.overwriteOutput = True

# Setup: Step Three
# ***change file path location here *** (after equals sign).
mainDirectory = r"C:\Users\lauren_hanna\Desktop\Python\Midterm"

# Setup: Step Four
# set up folder structure by creating an "outputs" folder and a "temporary" folder.
outputDirectory = os.path.join(mainDirectory, "outputs")
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

outputTemp = os.path.join(mainDirectory, "temporary")
if not os.path.exists(outputTemp):
    os.mkdir(outputTemp)

arcpy.AddMessage(r'Setup Steps 1-4 are complete')

## Project Output Explanation: The purpose of this specific script (below) is to set the perform a constraint analysis
## on the watersheds in Rhode Island and calculate the area. The tools that will be used are:
## 1: Clip
## 2: Dissolve
## 3: Calculate: Add Filed and Set Expression so that the number reflects Hectares

### Files Needed To Perform this are: HUC 12 Watersheds and Towns.shp



#############################################
## Clip HUC 12 Watersheds dataset to Towns.shp

# Step One:
# Clip Tool: Set Variables
in_features = "HUC12_RI_09.shp"
clip_features = "towns.shp"
out_feature_class = os.path.join(outputDirectory, "Clipped.shp")

# StepTwo:
# Run Clip Tool
arcpy.Clip_analysis(in_features, clip_features, out_feature_class)

# Step Three:
# Confirm Operation is Completed
if arcpy.Exists(out_feature_class):
    print "TOOL ONE: Clip Steps 1-3 are complete"

#############################################
## At this point, we need to dissolve the clipped watersheds (output created from previous step).

# Step One:
# Dissolve Tool: Set Variables
in_features = os.path.join(outputDirectory, "Clipped.shp")
out_feature_class = os.path.join(outputDirectory, "Dissolved.shp")
dissolve_field = ["HUC_12"]

# Step Two:
# Run Dissolve Tool
arcpy.Dissolve_management(in_features, out_feature_class, dissolve_field)

# Step Three:
# Confirm Operation is Completed
if arcpy.Exists(out_feature_class):
    print "TOOL TWO: Dissolved Steps 1-3 are complete"

#############################################
## At this time, we are now able to calculate the % of urban cover for the watersheds.
## To complete this step, we will need to perform the Add Field & Calculate Field functions.
## For this data output, the LARGEST watershed area (in Hectares) should be 14,770.

# Step One:
# Add Field
in_table = os.path.join(outputDirectory, "Dissolved.shp")
field_name = "Basin_Area"
field_type = "DOUBLE"

# Step Two:
# Run Tool
arcpy.AddField_management(in_table, field_name, field_type)

# Step Three:
# Calculate Filed (just added in previous step)
arcpy.CalculateField_management(in_table, field_name, "!SHAPE.AREA@hectares!", "PYTHON_9.3")

# Step Three:
# Confirm Operation is Completed
print "TOOL THREE: Add Field & Calculate Steps 1-4 are complete"


#############################################
## Sorry this took me so long-- I really don't get how/why anymore!
print "1"
print "2"
print "3"
print "..."
print "and just like that..."
print " "
print " "
print "Midterm is complete!!!!!"
