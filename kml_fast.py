from fastkml import kml

def print_child_features(element):
    """ Prints the name of every child node of the given element, recursively """
    if not getattr(element, 'features', None):
        return
    for feature in element.features():
        print (feature.name)
        print_child_features(feature)

<<<<<<< HEAD
def print_geometry(element):
    if not getattr(element, 'features', None):
        return
    for feature in element.features():

        # print (feature.geometry)
        print_geometry(feature)


    # for feature in element.features():
    #     for pointo in element.Placemark():
    #         print (pointo.geometry)
    #         print_geometry(pointo)
=======
>>>>>>> 60afe53c7e82dc63cbea5cc20760c22df2da4e2a


if __name__ == '__main__':

    fname = "gps.xml"

    k = kml.KML()
    with open(fname,"rb") as kmlFile:
<<<<<<< HEAD
        k.from_string(kmlFile.read())
        print_child_features(k)
        print_geometry(k)
=======
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

>>>>>>> 60afe53c7e82dc63cbea5cc20760c22df2da4e2a


