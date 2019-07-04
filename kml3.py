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
"""for placemark in root.findall('.//'+gis+'Placemark'):
    # print(placemark)
    for point in placemark.findall(gis+'Point/'):
        #print ('-> ',point.tag, point.attrib, point.text)
        print ('-> ', point.text)
        for coord in point.findall('.//'+gis+'coordinates'):
            print(coord.text)
            """
def pointo():
    for placemark in root.findall('.//'+gis+'Placemark'):
        for point in placemark.findall(gis+'Point/'):
        #print ('-> ',point.tag, point.attrib, point.text)
            print ('-> ', point.text)
print(pointo())

        # inPoint = point.find('.//'+gis+'coordinates')
        # print(placemark, inPoint)
        # print(point.tag)
        # print(placemark.find('name').text, point.find('coordinates').text)

        # for inCoord in point.iterfind('.//'+gis+'coordinates/'):
            # print("\ttag:  ",inCoord.text)
            # print(p.find('Name').text, p.find('Value').text)

# print("%s | %s" % (p.find('Name').text, p.find('Value').text))
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
