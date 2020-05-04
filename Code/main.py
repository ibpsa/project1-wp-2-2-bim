'''
Copyright (c) 2020 International Building Performance Simulation Association.  All rights reserved.


Developed by: Eric Fichter
              E3D, RWTH Aachen University
              www.e3d.rwth-aachen.de

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal with
the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to
do so, subject to the following conditions:
* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimers.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimers in the documentation
  and/or other materials provided with the distribution.
* Neither the names of <NAME OF DEVELOPMENT GROUP>, <NAME OF INSTITUTION>,
  nor the names of its contributors may be used to endorse or promote products
  derived from this Software without specific prior written permission.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE
SOFTWARE.
'''

import sys
import logging
import ifcopenshell
from validation import validate
from filtering import filter
from shape_generation import brep_to_occ, visualize_products
from simplify import simplify, eliminate_non_planar_faces
from OCC.Extend.DataExchange import write_stl_file
from OCC.Core.BRepCheck import BRepCheck_Analyzer

if __name__ == "__main__":

    for fn in sys.argv[1:]:
        print("File", fn)

        f = ifcopenshell.open(fn)

        # Validation
        print("Validation")
        logger = logging.getLogger('validate')
        logger.setLevel(logging.DEBUG)
        validate(f, logger)

        # Filtering
        print("Filtering")
        good_classes = ["IfcBuildingElement"]
        bad_classes = ["IfcStair", "IfcRailing"]
        guids = filter(f, good_classes, bad_classes)

        # Shape Generation
        print("Shape Generation")
        settings = ifcopenshell.geom.settings()
        settings.set(settings.USE_PYTHON_OPENCASCADE, True)
        guid_to_shape = brep_to_occ(f, guids, settings)
        # visualize_products(guid_to_shape)

        # Simplification
        print("Simplification")
        guid_to_simplified_shape = simplify(f, guids)
        for guid, shape in guid_to_simplified_shape.items():
            guid_to_shape[guid] = shape

        # Triangulation
        print("Triangulation")
        guid_to_shape = eliminate_non_planar_faces(guid_to_shape)
        # visualize_products(guid_to_shape)

        # Export, e.g. stl
        print("Export")
        # guid = guids[0]
        # shape = guid_to_shape[guid]
        # write_stl_file(shape, str(guid) + ".stl", mode="ascii", linear_deflection=0.9, angular_deflection=0.5)

        # Shape Checking
        print("Shape Checking")
        for guid, shape in guid_to_simplified_shape.items():
            a = BRepCheck_Analyzer(shape, True)
            if not a.IsValid():
                print("Shape", guid, "not valid!")
