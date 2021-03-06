from fastkml import kml

def print_child_features(element):
    """ Prints the name of every child node of the given element, recursively """
    if not getattr(element, 'features', None):
        return
    for feature in element.features():
        print (feature.name)
        print_child_features(feature)



if __name__ == '__main__':

    fname = "gps.xml"

    k = kml.KML()
    with open(fname,"rb") as kmlFile:
        file = kmlFile.read()
        k.from_string(file)
        print_child_features(k)

def coordinates(element):
    if not getattr(element, 'features', None):
        return

    for features in element.features():
        for f2 in features[0].features:
            
            print(f2)

coordinates(k)



