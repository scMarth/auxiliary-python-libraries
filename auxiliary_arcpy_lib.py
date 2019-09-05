"""
auxiliary_arcpy_lib.py : some useful arcpy functions
"""

import arcpy, os, shutil

def convert_xy_spatial_ref(longitude_x, latitude_y, input_sr, output_sr):
    """
    Converts some x,y or long,lat coordinates from the one spatial reference to another.
    input_sr is the input factory code spatial reference
    output_sr is the output factory code spatial reference
    """
    point = arcpy.Point(longitude_x, latitude_y)
    sr_in = arcpy.SpatialReference(input_sr)
    point_geometry = arcpy.PointGeometry(point, sr_in)

    sr_out = arcpy.SpatialReference(output_sr)
    projected = point_geometry.projectAs(sr_out)

    return [projected.firstPoint.X, projected.firstPoint.Y]

def create_fgdb(path, fgdb_name):
    """
    Creates a file geodatabase called 'fgdb_name.gdb' in 'path'. If it already exists,
    delete it and create a new one.
    """
    fgdb_path = path + '\\' + fgdb_name + '.gdb'

    if os.path.exists(fgdb_path):
        shutil.rmtree(fgdb_path)

    arcpy.CreateFileGDB_management(path, fgdb_name)

def delete_fc(fc_path):
    """
    Deletes the feature class given by 'fc_path' if it exists
    """
    if arcpy.Exists(fc_path):
        arcpy.Delete_management(fc_path)

def delete_features_in_fc(fc_path):
    """
    Deletes the features in the feature class given by 'fc_path' if it exists.
    This doesn't delete the actual feature class.
    """
    if arcpy.Exists(fc_path):
        arcpy.DeleteFeatures_management(fc_path)

def create_fc_text_attributes_from_fields(fgdb_path, feature_class_name, fields):
    """
    Creates text attribute fields for feature class 'feature_class_name' in fgdb at
    path 'fgdb_path'. Assumes that the shape is the first item in 'fields'
    """
    arcpy.env.workspace = fgdb_path

    for field in fields[1:]:
        arcpy.AddField_management(feature_class_name, field, 'TEXT', field_alias=field, field_is_nullable='NULLABLE')

def create_fc_with_text_attribute_fields(fgdb_path, fc_name, geometry_type, template, has_m, has_z, spatial_ref, fields):
    """
    Creates a feature class given the following parameters:

        fgdb_path       : this is the path to the file geodatabase that holds the feature
        fc_name         : this is the name of the feature class
        geometry_type   : this is the type of the geometry e.g. 'POINT' or 'POLYGON'
        template
        has_m           : if no m, use string 'DISABLED'
        has_z           : if no z, use string 'DISABLED'
        spatial_ref
        fields

        NOTE: field names should not have spaces, since arcpy automatically replaces them with underscores!
    """
    arcpy.CreateFeatureclass_management(fgdb_path, out_name=fc_name, geometry_type=geometry_type, template=template, has_m=has_m, has_z=has_z, spatial_reference=spatial_ref)
    create_fc_text_attributes_from_fields(fgdb_path, fc_name, fields)