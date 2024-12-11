# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2024-12-11 15:05:59
"""
import arcpy

def Model():  # Model
 
 # Environmental Configuration
    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False   # to show the output files already exist , and not be overwritten.

# to import a toolbox containing various data management tools from ArcGIS .
# Two variables are defined to input dataset like mineral core location and regional plan boundaries.
    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Data Management Tools.tbx")
    Mineral_Core_Location_0_ = "Mineral_Core_Location_0$"
    LUF_Integrated_Regional_Plan_Boundaries = "LUF Integrated Regional Plan Boundaries"


# to convert the an xY table into point features. The output is stored in a geodatabase . 
    # Process: XY Table To Point (XY Table To Point) (management)
    Mineral_Core_Location_0_XYTableToPoint2 = "C:\\Users\\jamim\\OneDrive\\Documents\\ArcGIS\\Projects\\Openbookproject\\Openbookproject.gdb\\Mineral_Core_Location_0_XYTableToPoint2"
    arcpy.management.XYTableToPoint(in_table=Mineral_Core_Location_0_, out_feature_class=Mineral_Core_Location_0_XYTableToPoint2, x_field="Longitude__NAD83_", y_field="Latitude__NAD83_", coordinate_system="GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

# A buffer of 50 kilometers is created around the point features generated in the previous step.
    # Process: Buffer (Buffer) (analysis)
    Mineral_Core_Location_Buffer3 = "C:\\Users\\jamim\\OneDrive\\Documents\\ArcGIS\\Projects\\Openbookproject\\Openbookproject.gdb\\Mineral_Core_Location_Buffer3"
    arcpy.analysis.Buffer(in_features=Mineral_Core_Location_0_XYTableToPoint2, out_feature_class=Mineral_Core_Location_Buffer3, buffer_distance_or_field="50 Kilometers")

# The script performs an intersection analysis between the buffered features and any other features. 

    # Process: Intersect (Intersect) (analysis)
    Mineral_Core_Locat_Intersect2 = "C:\\Users\\jamim\\OneDrive\\Documents\\ArcGIS\\Projects\\Openbookproject\\Openbookproject.gdb\\Mineral_Core_Locat_Intersect2"
    arcpy.analysis.Intersect(in_features=[[Mineral_Core_Location_Buffer3, ""]], out_feature_class=Mineral_Core_Locat_Intersect2)

# finally, the clips the intersected features using the regional plan boundaries.
    # Process: Clip (Clip) (analysis)
    LUFIntegratedRegionalPl_Clip = "C:\\Users\\jamim\\OneDrive\\Documents\\ArcGIS\\Projects\\Openbookproject\\Openbookproject.gdb\\LUFIntegratedRegionalPl_Clip"
    arcpy.analysis.Clip(in_features=Mineral_Core_Locat_Intersect2, clip_features=LUF_Integrated_Regional_Plan_Boundaries, out_feature_class=LUFIntegratedRegionalPl_Clip)


# this check program that is being run, set the Workspace for the ArcPy environment and call the 'Model'function.
if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="C:\\Users\\jamim\\OneDrive\\Documents\\ArcGIS\\Projects\\Openbookproject\\Openbookproject.gdb", workspace="C:\\Users\\jamim\\OneDrive\\Documents\\ArcGIS\\Projects\\Openbookproject\\Openbookproject.gdb"):
        Model()