import os
# filename, file_extension = os.path.splitext('/Users/akira/Documents/code/py/kml-graber-git/gps.kml')
# print(filename)

# print (file_extension)


for file in os.listdir("/Users/akira/Documents/code/py/kml-graber-git/"):
    if file.endswith(".kml"):
        print(os.path.join("/", file))