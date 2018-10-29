### IBPSA Project 1 WP 2.2 - Geometry Processing

This repository is the coding repository of IBPSA Project 1 Work Package 2.2 (BIM).

**Link list**
  
Internal links  
[Tasks and definitions](https://github.com/e3dEF/IBPSA-WP-2.2/blob/master/Tasks%20and%20definitions.md)  
  
External links     
[IPBSA Project 1 - WP 2.2 Repository](https://github.com/ibpsa/project1/tree/master/wp_2_2_bim)

**Tools and libraries**  
 1. Operating system: Windows/Linux/MacOS  
 2. Python: 3.X, recommended is Python 3.5  
 3. IfcOpenShell: v. 0.6 - [Link](https://github.com/IfcOpenShell/IfcOpenShell)  
 4. PythonOCC: v. 0.18.1 (OpenCascade) - [Link](https://github.com/tpaviot/pythonocc) 

**Installation of IfcOpenShell and PythonOCC**  
 1. Install Conda  
 2. Run `conda install -c conda-forge -c dlr-sc -c pythonocc -c oce pythonocc-core==0.18.1`
 3. Get IfcOpenShell. Build it using cmake or use the prebuilt versions: 
    - [Prebuilt for Linux (64bit for Python 3.5)](https://s3.amazonaws.com/ifcopenshell-builds/ifcopenshell-python-35-v0.6.0-5526f42-linux64.zip)   
     - [Prebuilt for Windows (64 bit for Python 3.5)](https://s3.amazonaws.com/ifcopenshell-builds/ifcopenshell-python-35-v0.6.0-5526f42-win64.zip)  
 4. Add IfcOpenShell folder to Python packages
