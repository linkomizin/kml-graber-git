from fastkml import kml
k = kml.KML()
# kml_file = 'gps.xml'
gis = '{http://www.opengis.net/kml/2.2}'
# kml_file = urlopen("http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml")

with open(r"gps.xml", "rb") as file_kml:
    # file_kml.encoding= "UTF-8"
    doc= file_kml.read()
    k.from_string(doc)
    features = list(k.features())
    print (len(features))

    # print (features[0].features())

    f2 = list(features[0].features())
    print (len(f2))

    # k._features.0._fetures.000



    print (f2[0].geometry)


    # print (f2[0].description)

