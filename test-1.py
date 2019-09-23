from fastkml import kml
import plotly.express as px

def name_bs(element):
    """ Prints the name of every child node of the given element, recursively """
    if not getattr(element, 'features', None):
        return
    for feature in element.features():
        name_bs(feature)

if __name__ == '__main__':

    fname = "gps.xml"

    
    with open(fname,"rb") as kmlFile:
        k = kml.KML()
        file = kmlFile.read()
        k.from_string(file)
        features =list(k.features())
        f2 = list(features[0].features())
        count_all = len(f2)
        count = 0
        while count <= (count_all - 20):
            count
            count = 1 + count
            print (f2[count].name, f2[count].geometry)
        coordinates =  str(f2[count].geometry)
        coordinates = (coordinates[6:])
        print (coordinates.replace('(','').replace(')','').replace(' ',','))