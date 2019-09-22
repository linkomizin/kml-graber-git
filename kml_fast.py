from fastkml import kml

def print_child_features(element):
    """ Prints the name of every child node of the given element, recursively """
    if not getattr(element, 'features', None):
        return
    for feature in element.features():
        print (feature.name)
        print_child_features(feature)

def print_geometry(element):
    if not getattr(element, 'features', None):
        return
    for feature in element.features():

        print (feature.coordinates)
        print_geometry(feature)


    # for feature in element.features():
    #     for pointo in element.Placemark():
    #         print (pointo.geometry)
    #         print_geometry(pointo)


if __name__ == '__main__':

    fname = "gps.xml"

    k = kml.KML()
<<<<<<< HEAD
=======
    # g = kml.Geometry()

>>>>>>> af0bea7358cc57f2d1a5716b7c3e248c169f1a38
    with open(fname,"rb") as kmlFile:
        k.from_string(kmlFile.read())
        # print_child_features(k)
        print_geometry(k)

    # print_child_features(k)

    # print_coordinates(f)