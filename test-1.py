from fastkml import kml
#mport pandas as pd
#mport plotly.graph_objects as go

# def name_bs(element):
#     """ Prints the name of every child node of the given element, recursively """
#     if not getattr(element, 'features', None):
#         return
#     for feature in element.features():
#         name_bs(feature)
#         if a == (len(f2) - 1):
#             break
def signal_y():

	signal = (s.replace('dBm',''))

	df, signal = (signal.split("-",(1)))
	df = 0
	yes_signal = ('-' + signal)
	print (a," : --- " , yes_signal)





    # except ValueError:
    #     pass


def signal_n():
	no_signal = ['0']
	print (a," : --- " , no_signal)
#     for no_signal in s:
#         try:
#             if s.find('БС 0'):

#                 no_signal = ['0']
#             else:
#                 continue

#             # print (no_signal)

#         except ValueError:
#                pass



if __name__ == '__main__':

    fname = "gps.xml"

    with open(fname,"rb") as kmlFile:
        k = kml.KML()
        file = kmlFile.read()
        k.from_string(file)
        features =list(k.features())
        f2 = list(features[0].features())
        a = 0
        while a < len(f2) - 1:
            a = a + 1
            s = f2[a].name
            if "dBm" in s:#s.find("dBm"):
                signal_y()
            else:
                s.find('БС 0')
                signal_n()
            
                continue

            # print (a," : --- " ,(signal_y())