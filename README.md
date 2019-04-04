
![enter image description here](https://ibpsa.github.io/project1/assets/IBPSA-project1.png)

## [IPBSA Project 1 - Repository](https://github.com/ibpsa/project1)  

### IBPSA Project 1 WP 2.2 - Geometry Processing

This repository is the coding repository of IBPSA Project 1 Work Package 2.2 (BIM).

**Link list**
  
Internal links  

  
External links     
* [IPBSA Project 1 - WP 2.2 Repository](https://github.com/ibpsa/project1/tree/master/wp_2_2_bim)  
* [IfcStatistics site](https://ibpsa-project-1.e3d.rwth-aachen.de/IfcStats/). For access contact fichter@e3d.rwth-aachen.de. Scans all files from IFC_Files folder. Supported file formats .ifc and .ifczip (please only one .ifc file per .ifczip archive). Maximum file size 100 MB.
* [UDK Code Repository](https://github.com/UdK-VPT/BIM2Modelica)

**Tools and libraries** 
IFC-Parser and BRep creator: IfcOpenShell (Python)  
Geometry kernel: OpenCascade (PythonOCC)  
 1. Operating system: Windows/Linux/MacOS  
 2. Python: 3.X, recommended is Python 3.5 or Python 3.6  
 3. IfcOpenShell: v. 0.6 - [Link](https://github.com/IfcOpenShell/IfcOpenShell)  
 4. PythonOCC: v. 0.18.1 (OpenCascade) - [Link](https://github.com/tpaviot/pythonocc) 

**Installation of IfcOpenShell and PythonOCC**  
 1. Install Conda  
 2. Run `conda install -c conda-forge -c dlr-sc -c pythonocc -c oce pythonocc-core==0.18.1`
 3. Get IfcOpenShell. Build it using cmake or use the prebuilt versions: 
    - [Prebuilt for Linux (64bit for Python 3.6)](https://s3.amazonaws.com/ifcopenshell-builds/ifcopenshell-python-36-v0.6.0-33cbcc2-linux64.zip)   
     - [Prebuilt for Windows (64 bit for Python 3.6)](https://s3.amazonaws.com/ifcopenshell-builds/ifcopenshell-python-36-v0.6.0-33cbcc2-win64.zip)  
 4. Add IfcOpenShell folder to Python packages

**IFC test files**    
[Single objects for testing the BRep creation](https://github.com/IfcOpenShell/files)
