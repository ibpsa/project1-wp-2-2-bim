import ifcopenshell as ios
from ifcopenshell import geom as geom

file_path='house.ifc'#put your ifc file path here

def print_space_boundaries(space):
    name=space.Name
    id=space.GlobalId
    print('boundaries of space id='+id+' name='+name+':')
    for rel in space.BoundedBy: #get IfcRelSpaceBoundary that connects IfcSpace and its boundaries(may be IfcWall, IfcDoor, IfdWindow, IfcSlab, etc.)
        elem=rel.RelatedBuildingElement
        if elem:
            el_name=elem.Name
            el_id=elem.GlobalId
            el_type=elem.is_a()
            print('\t'+el_type+' id='+el_id+' name='+el_name+':')

ifc_file=ios.open(file_path)
#get spaces by type
spaces=ifc_file.by_type('IfcSpace')
for space in spaces:
    print_space_boundaries(space)