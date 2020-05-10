## in order to complete challenge...
## ***Copied from class 11 lecture***

import os
import arcpy
arcpy.CheckOutExtension("spatial")
print "Spatial Extentions checked out" # **Probably don't need this since it won't print in ArcMap**

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "PythonFinal_ToolboxChallenge" # What the toolbox will be called in ArcMap
        self.alias = "PythonFinal_ToolboxChallenge"
        self.tools = [Clip_analysis, Dissolve_management, Union] # Name of the tools in the toolbox

print "tools have been established" # **Probably remove, see above for explanation**

################################
#Step One: Setup first tool

class Clip_analysis(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clip_analysis Tool" # **Name of tool that will display in ArcMap**
        self.description = "clip area" # **Description of what the tool will do**
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = [] # **Creates list to store the parameters of the tool**
        input_string = arcpy.Parameter(name="input_string", # **Same as variable name**
                                       displayName="clipped_files", # **What will be displayed on ArcMap **
                                       # "Please enter files you want to analyze"**
                                       datatype="DEFeatureClass", # **Add shape file here
                                       parameterType="Required", # **Required|Optional|Derived, almost always Required**
                                       direction="Output") # **Provide location of clipped file                                                          # you want them to set an output location for the clipped file.**
        params.append(input_string)
        clip_shp = arcpy.Parameter(name="clip_shp",  # **File needing to be clipped
                                      displayName="Enter shapefile to clip area by:",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Input")
        params.append(clip_shp)
        clip_output = arcpy.Parameter(name="clip_output", # **Need an output location
                                      displayName="Enter output destination for the clipped shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Output")
        params.append(clip_output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # **This is where you'll put the actual code to run the tool. All Python arcpy stuff, just like we've been doing!**

        input_string = parameters[0].valueAsText # **Extracts input_string (shapefile you want to clip) from params list**
        clip_shp = parameters[1].valueAsText # **Extracts clip_shp (clipping area) from the params list**
        clip_output = parameters[2].valueAsText # **Extracts clip_output (clipped shapefile name/location) from list**

        in_features = input_string
        clip_features = clip_shp
        out_feature_class = clip_output
        xy_tolerance = ""

        # Execute Clip
        arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)
        arcpy.AddMessage("clipping is complete") # **Need to use arcpy.AddMessage() in order to display text in ArcMap**
        return
print "step one complete"





##########################################################
## Step Two: Dissolve Area

class Dissolve_management(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Dissolve_management Tool" # **Name of tool that will display in ArcMap**
        self.description = "dissolve area(s)/boundaries" # **Description of what the tool will do**
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = [] # **Creates list to store the parameters of the tool**
        input_string2 = arcpy.Parameter(name="input_string2", # **Same as variable name**
                                       displayName="dissolved_files", # **What will be displayed on ArcMap **
                                       # "Please enter files you want to analyze"**
                                       datatype="DEFeatureClass", # **Add shape file here -- previously clipped file
                                       parameterType="Required",# **Required|Optional|Derived, almost always Required**
                                       direction="Output") # **Provide location of dissolved file                                                          # you want them to set an output location for the clipped file.**
        params.append(input_string2)
        dissolved_shp = arcpy.Parameter(name="dissolved_shp",  # **File needing to be clipped
                                      displayName="Enter previously clipped file to area area by:",
                                      datatype="DEFeatureDataset", # ** This will be a specific column/field within
                                   # the attribute table
                                      parameterType="Required",
                                      direction="Input")
        params.append(dissolved_shp)
        dissolved_output= arcpy.Parameter(name="dissolved_output", # **Need an output location
                                      displayName="Enter output destination for the clipped shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Output")
        params.append(dissolved_output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # **This is where you'll put the actual code to run the tool. All Python arcpy stuff, just like we've been doing!**

        input_string2 = parameters[0].valueAsText # **shapefile you want to dissolve
        dissolve_shp = parameters[1].valueAsText # **Extracts dissolve_shp (dissolving area) from the params list**
        dissolve_output = parameters[2].valueAsText # ** dissolve_output (dissolved based on column name/location) from list**

        in_features = input_string2
        out_feature_class = dissolve_shp
        dissolved_field = dissolve_output


        # Execute Clip
        arcpy.Dissolve_management(in_features, out_feature_class, dissolved_field)
        arcpy.AddMessage("dissolved is complete") # **Need to use arcpy.AddMessage() in order to display text in ArcMap**
        return
print "step two complete"


################################
#Step Three: Union Tool

class Union(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Union Tool" # **Name of tool that will display in ArcMap**
        self.description = "union" # **Description of what the tool will do**
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = [] # **Creates list to store the parameters of the tool**
        input_string3 = arcpy.Parameter(name="input_string3", # **Same as variable name**
                                       displayName="union_shp", # **What will be displayed on ArcMap **
                                       # "Please enter files you want to analyze"**
                                       datatype="DEFeatureClass", # **Add shape file here
                                       parameterType="Required", # **Required|Optional|Derived, almost always Required**
                                       direction="Output") # **Provide location of union file                                                          # you want them to set an output location for the clipped file.**
        params.append(input_string3)
        union_shp = arcpy.Parameter(name="union_shp",  # **File needing the union tool
                                      displayName="Enter shapefile to buffer area by:",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Input")
        params.append(union_shp)
        union_output = arcpy.Parameter(name="union_output", # **Need an output location
                                      displayName="Enter output destination for the clipped shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Output")
        params.append(union_output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # **This is where you'll put the actual code to run the tool. All Python arcpy stuff, just like we've been doing!**

        input_string3 = parameters[0].valueAsText # **Extracts input_string (shapefile you want to clip) from params list**
        union_shp = parameters[1].valueAsText # **Extracts clip_shp (clipping area) from the params list**
        union_output = parameters[2].valueAsText # **Extracts clip_output (clipped shapefile name/location) from list**

        in_features = input_string3
        join_attributes = union_shp
        out_features = union_output

        # Execute Clip
        arcpy.Clip_analysis(in_features, out_features, join_attributes)
        arcpy.AddMessage("clipping is complete") # **Need to use arcpy.AddMessage() in order to display text in ArcMap**
        return
print "step three complete"

print "final is done!"
print "Thank you for a great semester!"
