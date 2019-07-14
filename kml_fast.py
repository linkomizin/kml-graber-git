from fastkml import kml

def print_child_features(element):
    """ Prints the name of every child node of the given element, recursively """
    if not getattr(element, 'features', None):
        return
    for feature in element.features():
        print (feature.name)
        print_child_features(feature)

# def print_coordinates(element):
#     if not getattr(element, 'features', None):
#         return
#     for feature in element.features():
#         print (feature.Point)
#         print_child_features(feature)
#         for point in feature.features():
#             for coord in point.features():
#                 print (coord.coordinates)
#                 print_coordinates(coord)


if __name__ == '__main__':

    fname = "gps.xml"

    k = kml.KML()
    with open(fname,"rb") as kmlFile:
        k.from_string(kmlFile.read())

    print_child_features(k)
    # print_coordinates(f)