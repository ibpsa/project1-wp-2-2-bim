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

def print_object_properties(obj):
    print('properties of '+obj.is_a()+' id='+obj.GlobalId+':')
    for rel in obj.IsDefinedBy:
        if not rel.is_a('IfcRelDefinesByProperties'): continue
        prop_def=rel.RelatingPropertyDefinition
        print('\t'+prop_def.is_a()+' id='+prop_def.GlobalId+' name='+prop_def.Name+':')
        if prop_def.is_a('IfcElementQuantity'):
            for quantity in prop_def.Quantities:
                if quantity.is_a('IfcQuantityArea'):
                    print('\t\t'+' name='+quantity.Name+' area='+str(quantity.AreaValue))
                elif quantity.is_a('IfcQuantityVolume'):
                    print('\t\t'+' name='+quantity.Name+' volume='+str(quantity.VolumeValue))
                else:continue #there are more types
        elif prop_def.is_a('IfcPropertySet'):
            for property in prop_def.HasProperties:
                if property.is_a('IfcPropertySingleValue'):
                    value=property.NominalValue.wrappedValue if property.NominalValue else None
                    print('\t\t'+' name='+property.Name+' value='+str(value))
                else:continue #there are more types
        else:continue #there are more types

ifc_file=ios.open(file_path)
#get spaces by type
spaces=ifc_file.by_type('IfcSpace')
for space in spaces:
    print_space_boundaries(space)
    print_object_properties(space)