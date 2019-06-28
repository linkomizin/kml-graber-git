import xml.etree.ElementTree as ET

tree = ET.parse('gps.xml')
root = tree.getroot()
gis = '{http://www.opengis.net/kml/2.2}'
# print (gis)
# print(root)
# print(len(root))
# for placemark in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark/'):
    # print ( placemark, '\t')

# for point in root.findall('.//'+gis+'coordinates'):
#     print(point.text)
for placemark in root.findall('.//'+gis+'Placemark'):
    inPlacemark = placemark.findall('.//'+gis+'name')


    for point in placemark.findall('.//'+gis+'Point'):
        inPoint = point.find('.//'+gis+'coordinates')
        print(placemark., inPoint)


# for elem in root:‭
# print(elem.find‭('‬item‭')‬.get‭('‬name‭'))



#     print()
#     print(len(kml))
#     for document in kml.findall('{http://www.opengis.net/kml/2.2}Placemark/'):
#             print (document.text, document.tag)



#for point in kml.findall('{http://www.opengis.net/kml/2.2}Placemark/'):

        #print(serc.tag)


#search = root.findall('{http://www.opengis.net/kml/2.2}Placemark')
#print(search)
#print("---!!!----", len(search))
# for country in root.findall('country'):
# ...   rank = country.find('rank').text
# ...   name = country.get('name')
# ...   print(name, rank)
#
#root.tag
#for child in root:
#    print('Tag:', child.tag, 'Attributes:', child.attrib)
#    for grandchild in child:
#        print('\ttag:', grandchild.tag, 'attrib:', grandchild.attrib)
