import ifcopenshell.geom
file = ifcopenshell.open("Haus.ifc")
for wall in file.by_type("IfcWall"):
    print(wall)


