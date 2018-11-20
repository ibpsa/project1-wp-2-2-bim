IfcOpenShell offers functions to change the schema version that is used for IFC files on runtime. Anyway some IFC entities have been removed from IFC2x3 to IFC4 and some attributed have been added in IFC4. Due to this, you can't simply mix up the two file formats.  
The following commands can be used in python:

`IfcFile = ifcopenshell.open('testfile.ifc')`  
`IfcFile.schema # return ifc file schema`  
`IfcFile.schema = 'IFC2x3' # sets the ifc file schema manual (IFC2X3 or IFC4)`  

In general, this discussion is helpful regarding cross compability of IFC versions:  
https://github.com/IndustryFoundationClasses/Questions/issues/10


