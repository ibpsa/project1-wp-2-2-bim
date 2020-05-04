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
from OCC.Display.SimpleGui import init_display


def brep_to_occ(file, guids, settings):
    guid_to_shape = {}
    for g in guids:
        s = product_to_shape(file.by_guid(g), settings)
        if s != None:
            guid_to_shape[g] = s
    return guid_to_shape


def product_to_shape(p, settings):
    if p.Representation is not None:
        try:
            return ifcopenshell.geom.create_shape(settings, p).geometry
        except:
            print(ifcopenshell.get_log)
            return None
    else:
        return None


def visualize_products(guid_to_shape):
    display, start_display, add_menu, add_function_to_menu = init_display()
    for key in guid_to_shape:
        display.DisplayShape(guid_to_shape[key], update=True)
    display.FitAll()
    start_display()
