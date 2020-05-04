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

import ifcopenshell.geom
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Common
from OCCUtils.face import Face
from OCCUtils.Topology import Topo
from OCC.Extend.DataExchange import write_stl_file, read_stl_file


def simplify(model, guids):
    products_guid_brep = {}

    opening_settings = ifcopenshell.geom.settings()
    opening_settings.set(opening_settings.USE_PYTHON_OPENCASCADE, True)
    opening_settings.set(opening_settings.SEW_SHELLS, True)
    opening_settings.set(opening_settings.DISABLE_OPENING_SUBTRACTIONS, True)

    window_guids = {}  # key: door, value: [opening, wall]
    opening_geoms = {}  # opening: shape
    wall_geoms = {}  # wall: shape

    for g in guids:
        p = model.by_guid(g)
        if p.Representation is not None and not p.is_a("IfcSpace") and p.FillsVoids:

            opening = p.FillsVoids[0].RelatingOpeningElement
            wall = opening.VoidsElements[0].RelatingBuildingElement
            window_guids[g] = [opening.GlobalId, wall.GlobalId]

            shp_opening = ifcopenshell.geom.create_shape(opening_settings, opening).geometry
            opening_geoms[opening.GlobalId] = shp_opening

            if (wall.GlobalId not in wall_geoms):
                shp_wall = ifcopenshell.geom.create_shape(opening_settings, wall).geometry
                wall_geoms[wall.GlobalId] = shp_wall

    for key, value in list(window_guids.items()):
        products_guid_brep[key] = BRepAlgoAPI_Common(opening_geoms[value[0]], wall_geoms[value[1]]).Shape()

    return products_guid_brep


def eliminate_non_planar_faces(guid_to_shape):
    non_planar = []
    for guid, shape in guid_to_shape.items():
        faces = Topo(shape).faces()
        for face in faces:
            F = Face(face)
            if not F.is_planar():
                non_planar.append(guid)
                break

    for guid in non_planar:
        filename = str(guid) + ".stl"
        write_stl_file(guid_to_shape[guid], filename, mode="ascii", linear_deflection=0.95, angular_deflection=0.95)
        guid_to_shape[guid] = read_stl_file(filename)

    return guid_to_shape
