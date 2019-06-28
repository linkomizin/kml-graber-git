import xml.etree.ElementTree as ET
import re

from xml.dom import minidom

tree = ET.parse('gps.xml')
root = tree.getroot()

# def prettify(elem):
#     """Return a pretty-printed XML string for the Element.
#     """
#     rough_string = ET.tostring(elem, 'utf-8')
#     reparsed = minidom.parseString(rough_string)
#     return reparsed.toprettyxml()
PPP = ("{http://www.opengis.net/kml/2.2}")
# print ('|-> ',root.tag, ' |<>| ')

for root_2 in root.findall('./' + PPP + 'Document/' + PPP + 'Placemark/'):
    # print ('|--> ', root_2.tag, '  ', root_2.attrib)
    for root_3 in root_2.findall('.'):

        coord = root_3.findall(PPP + 'coordinates')
        print ('|--> ',root_3.tag, coord)
        for root_4 in root_3:
            print('---++|->  ', root_4.text)

    # for troot in root.findall('./Document/Placemark'):
# for troot in root.findall('./' + PPP + 'Document/' + PPP + 'Placemark/'):
#     mark_name = troot.find('name')

    # print ('|-> ', mark_name)
    #mark = troot.get('Placemark')

    #point = troot.get('Point')
    # for get_coordinates in troot.findall('.'):

        # for get_coo in get_coordinates:

            # print ('<> ' , get_coordinates.tag)
            # coordinates = get_coordinates.iterfind('coordinates')
            # print('|---> ', mark_name, coordinates)

# print (prettify(root))



