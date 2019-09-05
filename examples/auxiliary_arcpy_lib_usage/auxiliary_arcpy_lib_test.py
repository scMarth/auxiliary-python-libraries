import arcpy, sys, os
sys.path.insert(0, os.path.dirname(__file__) + '/../../')

from auxiliary_arcpy_lib import *

longitude = -121.6515268
latitude = 36.6735302

longitude2, latitude2 = convert_xy_spatial_ref(longitude, latitude, 4326, 102644)

print('long: {} ; lat: {}'.format(longitude, latitude))
print('long: {} ; lat: {}'.format(longitude2, latitude2))

# create a file geodatabase in the same directory as this script
workspace = os.path.dirname(__file__)

create_fgdb(workspace, 'test')

fields = [ \
    'SHAPE@XY', \
    'First_Name', \
    'Last_Name' \
]
spatial_reference = arcpy.SpatialReference(102644) # WKID for NAD 1983
create_fc_with_text_attribute_fields(workspace + '\\'  'test' + '.gdb', 'featureClassName', 'POINT', None, 'DISABLED', 'DISABLED', spatial_reference, fields)

x = 0
y = 0

data = [ \
    ['Bob', 'Dole'], \
    ['Crash', 'Bandicoot'], \
    ['Coco', 'Bandicoot'] \
]

fc = workspace + r'\test.gdb\featureClassName'
with arcpy.da.InsertCursor(fc, fields) as cursor:
    for record in data:
        x += 1
        y += 1
        xy = (x,y)
        cursor.insertRow(( \
            xy, \
            record[0], \
            record[1] \
        ))

create_fc_with_text_attribute_fields(workspace + '\\'  'test' + '.gdb', 'featureClassName2', 'POINT', None, 'DISABLED', 'DISABLED', spatial_reference, fields)

x = 0
y = 0

data = [ \
    ['Bob', 'Dole'], \
    ['Crash', 'Bandicoot'], \
    ['Coco', 'Bandicoot'] \
]

fc = workspace + r'\test.gdb\featureClassName2'
with arcpy.da.InsertCursor(fc, fields) as cursor:
    for record in data:
        x += 1
        y += 1
        xy = (x,y)
        cursor.insertRow(( \
            xy, \
            record[0], \
            record[1] \
        ))

create_fc_with_text_attribute_fields(workspace + '\\'  'test' + '.gdb', 'featureClassName3', 'POINT', None, 'DISABLED', 'DISABLED', spatial_reference, fields)

x = 0
y = 0

data = [ \
    ['Bob', 'Dole'], \
    ['Crash', 'Bandicoot'], \
    ['Coco', 'Bandicoot'] \
]

fc = workspace + r'\test.gdb\featureClassName3'
with arcpy.da.InsertCursor(fc, fields) as cursor:
    for record in data:
        x += 1
        y += 1
        xy = (x,y)
        cursor.insertRow(( \
            xy, \
            record[0], \
            record[1] \
        ))

delete_fc(workspace + r'\test.gdb\featureClassName3') # delete the 3rd feature class
delete_features_in_fc(workspace + r'\test.gdb\featureClassName2') # delete the features within the second feature class