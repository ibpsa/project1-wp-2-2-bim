import ifcopenshell.geom


def module_2_brep_to_occ(file, guids):
    settings = ifcopenshell.geom.settings()
    settings.set(settings.USE_PYTHON_OPENCASCADE, True)
    guid_to_shape = {}
    for g in guids:
        s = product_to_shape(file.by_guid(g), settings)
        if s != None:
            guid_to_shape[g] = s
    return guid_to_shape


def product_to_shape(p, settings):
    if p.is_a("IfcOpeningElement") or p.is_a("IfcSite") or p.is_a("IfcAnnotation"):
        return None
    if p.Representation is not None:
        try:
            return ifcopenshell.geom.create_shape(settings, p).geometry
        except:
            print(ifcopenshell.get_log)
            return None
    else:
        return None


# create input
file = ifcopenshell.open("h.ifc")
guids = []
for p in file.by_type("IfcWall"):
    guids.append(p.GlobalId)

# create occ shapes from guid list of specific file
guid_to_shape = module_2_brep_to_occ(file, guids)

# result
for key in guid_to_shape:
    print(key, guid_to_shape[key])

# def visualize_products(guid_to_shape):
#     shapes = []
#     for key in guid_to_shape:
#         shapes.append(guid_to_shape[key])
#     if isinstance(shapes, list):
#         for shape in shapes:
#             ifcopenshell.geom.utils.display_shape(shape)
#     else:
#         ifcopenshell.geom.utils.display_shape(shapes)
# pyocc_viewer = ifcopenshell.geom.utils.initialize_display()
# visualize_products(guid_to_shape)
# pyocc_viewer.FitAll()
# ifcopenshell.geom.utils.main_loop()
