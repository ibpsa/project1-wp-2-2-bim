import ifcopenshell.geom

def product_to_shape(products,settings):
    product_shapes = []
    for product in products:
        if product.is_a("IfcOpeningElement") or product.is_a("IfcSite") or product.is_a("IfcAnnotation"): continue
        if product.Representation is not None:
            try:
                shape = ifcopenshell.geom.create_shape(settings, product).geometry
                product_shapes.append(shape)
            except:
                print(ifcopenshell.get_log)
    return product_shapes

def visualize_products(shapes):

    if isinstance(shapes, list):
        for shape in shapes:
            ifcopenshell.geom.utils.display_shape(shape)
    else:
        ifcopenshell.geom.utils.display_shape(shapes)


filename = "../ifc_files/misc/AC20-FZK-Haus.ifc"
file = ifcopenshell.open(filename)
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_PYTHON_OPENCASCADE, True)
pyocc_viewer = ifcopenshell.geom.utils.initialize_display()

products = file.by_type("IfcProduct")
shape_list = product_to_shape(products,settings)
visualize_products(shape_list)

# Allow for user interaction
pyocc_viewer.FitAll()
ifcopenshell.geom.utils.main_loop()