**Modules for Space Boundary Extraction**
- M1: IFC4 file &rightarrow; MVDXMLChecker &rightarrow; Report (txt) | Checking IFC file for content regarding requirements (e.g. IfcSpaces), maybe modifications to the original IFC4 file necessary
- M2: IFC4 file &rightarrow; Boundary Representation Creation &rightarrow; BREP (OCC-Shape, .STEP, .BREP, ...) | Creation of explicit geometry linked to GUID
- M3: BREP &rightarrow; Shape Checker &rightarrow; Report | Are BREPS valid (watertightness, face  normals, manifoldness, self-intersections)
- M4: BREP, Report &rightarrow; Shape Fixer &rightarrow; BREP | Valid BREPS 
- M5: ... e.g. Fixing relations between building elements, Spatial Data Structure, Neighbour-Search, Topology extraction, Clipping, Projection, ...

**Input**
- IFC4
- IfcSpaces
- Planar faces
- No hybrid modelling of walls

**Output**
- 2nd Level Space Boundary (horizontal, vertical) - Linking between IfcSpace and IfcBuildingElement using IfcRelSpaceBoundary, IfcPhysicalOrVirtualEnum (physical, virtual), IfcInternalOrExternalEnum (internal, external)
- Geometry of Space Boundary according to one of the representation styles of IFC
