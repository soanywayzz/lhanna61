## Our coding challenge this week follows from the last exercise that we did in class during Week 6.
##
## Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are interested in
## the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the Landsat 8 imagery. Data
## provided are monthly (a couple are missing due to cloud coverage) during the year 2015 for the State of RI.
##
## Before you start, here is a suggested workflow:
##
## Extract the Step_3_data.zip file into a known location.
## For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
## https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool in
## ArcMap and using "Copy as Python Snippet" for the first calculation.
## The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided. As part of your code
## submission, you should also provide a visualization document (e.g. an ArcMap layout), showing the patterns for an
## area of RI that you find interesting.


import os
import arcpy

arcpy.CheckOutExtension("Spatial")
listMonths = ["02", "04", "05", "07", "10", "11"]

mainDirectory = r"C:\Users\lauren_hanna\Desktop\Python\Week6\Step_3_data_lfs" # Change Filepath Here to Set Up Folders

outputDirectory = os.path.join(mainDirectory, "outputs")
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

print "Directory is Setup"

for month in listMonths:
    print "Extracting Band Information for month ... " + month

    arcpy.env.workspace = os.path.join(mainDirectory, "2015" + month)

    bandFour = arcpy.ListRasters("*", "TIF")
    bandFour = [x for x in bandFour if "B4" in x]
    print "The file for Band 4 is " + str(bandFour) + ""

    band5 = arcpy.ListRasters("*", "TIF")
    band5 = [x for x in band5 if "B5" in x]
    print "The file for Band 5 is " + str(band5) + ""

# Using the equation: nvdi = (nir - vis) / (nir + vis), we're going to calculate the NVDI for each month
    arcpy.gp.RasterCalculator_sa('Float("' + band5[0] + '"-"' + bandFour[0] + '") / Float("' + band5[0] +
                                 '"+"' + bandFour[0] + '")', os.path.join(outputDirectory, "NVDI_2015" + month +
                                                                          ".tif"))
print "NVDI Calculation is NOW Complete"