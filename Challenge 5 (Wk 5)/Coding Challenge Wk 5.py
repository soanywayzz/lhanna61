## For this coding challenge, I want you to practice the heatmap generation that we went through in class, but this
## time obtain your own input data, and I want you to generate heatmaps for TWO species.

## You can obtain species data from a vast array of different sources, for example:

## obis - Note: You should delete many columns (keep species name, lat/lon) as OBIS adds some really long
## strings that don't fit the Shapefile specification.
## GBIF
## Maybe something on RI GIS
## Or just Google species distribution data
## My requirements are:

## The two input species data must be in a SINGLE CSV file, you must process the input data to separate out
## the species (Hint: You can a slightly edited version of our CSV code from a previous session to do this), I
## recommend downloading the species data from the same source so the columns match.
## Only a single line of code needs to be altered (workspace environment) to ensure code runs on my
## computer, and you provide the species data along with your Python code.
## The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
## You leave no trace of execution, except the resulting heatmap files.
## You provide print statements that explain what the code is doing, e.g. Fishnet file generated.



import arcpy
import csv
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'C:\Users\lauren_hanna\Desktop\Python\Week5' #place the folder to which you would like your pulled
# from and written to
# An empty species list should be created in order to populate a loop reader from imported csv
list_of_species = []

with open("data_csv.csv") as species_csv: #Gray Seal Data ## CHANGE HERE IF NEEDED
    csv_reader = csv.reader(species_csv, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count != 0:
            if row[0] not in list_of_species:
                list_of_species.append(row[0])
        if line_count == 0:
            print "Columns: " + str(row)
            line_count += 1
        line_count += 1

print list_of_species
print("Processed List" + str(line_count) + "Processed Lines") # different ways to code print statements
print "First part is complete" # different ways to code print statements

# Loop through the csv and if the species name are the same the code will break out according to species count
for y in list_of_species:
    with open("data_csv.csv") as species_csv:
        csv_reader = csv.reader(species_csv, delimiter=',')
        file = open(y[1:3] + ".csv", "w")
        file.write("Name,Long,Lat\n")
        for row in csv_reader:
            if row[0] == y:

                string = ",".join(row)
                string = string + "\n"
                file.write(string)
        file.close() # tip given to avoid errors

# While still under the initial species loop, I am creating a shp file for each of the split species csv files.
for y in list_of_species:
    in_Table = y[1:3] + ".csv"
    x_coords = "Long"
    y_coords = "Lat"
    out_Layer = "new_data"
    saved_Layer = y[1:3] + ".shp"

    spRef = arcpy.SpatialReference(4326) #this is the PyCharm code number for WGS 1984
    print "so far so good"
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")
    arcpy.CopyFeatures_management(lyr, saved_Layer)

    if arcpy.Exists(saved_Layer):
        print "Created shape file successfully!"
    else:
        print "Error"


# Next, identify the spatial coordinates of each shp file in order to produce fishnets
    desc = arcpy.Describe(y[1:3] + ".shp")
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

    print("Extent:\n YMin: {0},\n YMax: {1},\n XMin: {2},\n XMax: {3}".format(desc.extent.YMin, desc.extent.YMax,
                                                                              desc.extent.XMin, desc.extent.XMax))

print "CSV Nonsense is COMPLETE"

# Creating fishnets still within the initial loop therefore for each shape file there will be a fishnet.
arcpy.env.outputCoordinateSystem = spRef
outFeatureClass = y[1:3] + "_Fishnet.shp"

originCoordinate = str(XMin) + " " + str(YMin)
yAxisCoordinate = str(XMin) + " " + str(YMin + 10)
cellSizeWidth = "2"
cellSizeHeight = "2"
numRows = ""
numColumns = ""
oppositeCorner = str(XMax) + " " + str(YMax)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,cellSizeWidth, cellSizeHeight,
                               numRows, numColumns,oppositeCorner, labels, templateExtent, geometryType)

# Making sure the files were created
if arcpy.Exists(outFeatureClass):
    print "Created Fishnet file successfully!"

# Join the fishnet with the distribution in order to produce a heatmap again all under the same loop so that the
# program will run through twice for each species.
    target_features = y[1:3] + "_Fishnet.shp"
    join_features = y[1:3] + ".shp"
    out_feature_class = y[1:3] + "_FINALheatmap.shp"
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)

# To make sure the heatmap was created
    if arcpy.Exists(out_feature_class):
        print "Heatmap file(s) are officially complete!!"
# Deleting the intermediate files with proof that they were created by the if acpy.exists commands.
print "Deleting Unnecessary Files Now"
arcpy.Delete_management(target_features)
arcpy.Delete_management(join_features)

print "Files Successfully Deleted"
print "Pat Yourself On The Back!!"