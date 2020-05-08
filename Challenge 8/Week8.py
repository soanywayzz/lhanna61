import arcpy

print "As Barney Stinson, from How I Met Your Mother (TV Show), says... Challenge Accepted..."

def checkFolder(a, b):
    arcpy.env.workspace = a
    rasterList = arcpy.ListRasters("*", b)
    rasterList = [x for x in rasterList if "_BQA.tif" not in x]
    print "The files ending in " + b + " are " + str(rasterList)
    print "The number of files in that folder are " + str(len(rasterList))


checkFolder(r"C:\Users\lauren_hanna\Desktop\Python\Week8", "tif")


print "Challenge Completed Successfully-- I forget what Barney Stinson says in this scenario"