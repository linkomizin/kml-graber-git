import xml.etree.ElementTree as ET
from xml.dom import minidom

#XML_FILE = ('gp.xml')
#tree = ET.parse(XML_FILE)

tree = ET.parse('gps.xml')
root = tree.getroot()
# root.tag
# root.attrib
#print (root)
#print (type(root))


#type(root)

def prettify(elem):
    # """Return a pretty-printed XML string for the Element.
    # """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml()


# for achild in root.iter():
#     print(achild.keys)
#     for ggchi in achild.iterfind('./Document/'):
#         print (ggchi.keys)
#         for placem in ggchi.findall('name'):
#             print (placem.tag, placem.text)

print (prettify(root))

#for child in root.iter('.//'):
#    print('Tag: ', child.tag, 'text: ', child.text)
#    for gchild in child:
#        print('Tag:', gchild.tag,  'text:', gchild.text)

#(child.tag, child.text, child.attrib, child.keys, child.items)






