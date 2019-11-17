from fastkml import kml
import pandas as pd
import plotly.graph_objects as go

# def name_bs(element):
#     """ Prints the name of every child node of the given element, recursively """
#     if not getattr(element, 'features', None):
#         return
#     for feature in element.features():
#         name_bs(feature)
#         if a == (len(f2) - 1):
#             break
# def signal_y():

# 	signal = (s.replace('dBm',''))

# 	df, signal = (signal.split("-",(1)))
# 	df = 0
# 	yes_signal = ('-' + signal)
# 	# print (a," : --- " , yes_signal)


def signal_n():
	no_signal = ['0']
	# print (a," : --- " , no_signal)



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
            if "dBm" in s:
                # signal_y()
                signal = (s.replace('dBm',''))

                de, signal = (signal.split("-",(1)))
                de = 0
                y_signal = ('-' + signal)
            else:
                s.find('БС 0')
                signal_n()            
                continue
            coordinat = ((str(f2[len(f2) - 1].geometry))[6:]).replace('(','').replace(')','').replace(' ',',')
            latitude, longitude = coordinat.split(',', 1)
            d = {'latitude':pd.array([latitude]), 'longitude':pd.array([longitude]), 'signal':pd.array([y_signal])}
            df = pd.DataFrame(d,index=[len(f2) -1 ])
        fig = go.Figure(go.Densitymapbox(lat=df.latitude, lon=df.longitude, z=df.signal, radius=10))
        fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.show()