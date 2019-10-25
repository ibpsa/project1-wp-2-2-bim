**Modules for Space Boundary Extraction**
- M1: IFC file &rightarrow; MVDXMLChecker &rightarrow; Report (txt) | Checking IFC file for content regarding requirements (e.g. IfcSpaces), maybe modifications to the original IFC file necessary; some checking rules are only available in IFC4
- M2: IFC file &rightarrow; Boundary Representation Creation &rightarrow; BREP (OCC-Shape, .STEP, .BREP, ...) | Creation of explicit geometry linked to GUID ### [BREPtoOCC](https://github.com/ibpsa/project1-wp-2-2-bim/blob/master/Code/Module%202%20-%20BREP-Creation.py)
- M3: BREP &rightarrow; Shape Checker &rightarrow; Report | Are BREPS valid (watertightness, face  normals, manifoldness, self-intersections)
- M4: BREP, Report &rightarrow; Shape Fixer &rightarrow; BREP | Valid BREPS 
- M5: ... e.g. Fixing relations between building elements, Spatial Data Structure, Neighbour-Search, Topology extraction, Clipping, Projection, ...

**Input**
- IFC4 or IFC2x3 Files
- IfcSpaces
- Planar faces
- No hybrid modelling of walls

**Output**
- 2nd Level Space Boundary (horizontal, vertical) - Linking between IfcSpace and IfcBuildingElement using IfcRelSpaceBoundary, IfcPhysicalOrVirtualEnum (physical, virtual), IfcInternalOrExternalEnum (internal, external)
- Geometry of Space Boundary according to one of the representation types of IFC (parametric, direct or indirect representation, etc.)
