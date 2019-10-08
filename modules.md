**Modules for Space Boundary Extraction**
- M1: IFC4 file &rightarrow; MVDXMLChecker &rightarrow; IFC4 file, Report (txt) | Checking IFC file for content regarding requirements (e.g. IfcSpaces)
- M2: IFC4 file &rightarrow; Boundary Representation Creation &rightarrow; BREP (OCC-Shape, .STEP, .BREP, ...) | Creation of explicit geometry linked to GUID
- M3: BREP &rightarrow; Shape Checker &rightarrow; Report | Are BREPS valid (watertightness, face  normals, manifoldness, self-intersections)
- M4: BREP, Report &rightarrow; Shape Fixer &rightarrow; BREP | Valid BREPS 
- M5: ... e.g. Fixing relations between building elements, Spatial Data Structure, Neighbour-Search, Topology extraction, Clipping, Projection, ...
