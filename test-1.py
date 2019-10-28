from fastkml import kml
import pandas as pd
import plotly.graph_objects as go

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
            coordinat = ((str(f2[count].geometry))[6:]).replace('(','').replace(')','').replace(' ',',')
            latitude, longitude = coordinat.split(',', 1)
            s = (f2[count].name)

            if s.find('БС 0'):
                signal = ['0']
            print (signal)
            for yes_signail in s:
                if s.find('dBm'):
                    signal = (s.replace('dBm', ''))
                    bs_signal, signal = (signal.split('-', (1)))
                    yes_signal = ('-' + signal)
                    print(yes_signal)
            for signal in s:
                if s.find('БС 0'):
                    signal = ['0']
                    print (signal)

                #signal = str(['-'+([s.split('-',[1])])-' dBm'])
            # print (signal)
                
            #d = {'latitude':pd.array([latitude]), 'longitude':pd.array([longitude]), 'signal':pd.array(signal)}
            #df = pd.DataFrame(d,index=[count])
            
            # print (f2[count].name, coordinat)
            #coordinates =  str(f2[count].geometry)
        #coordinates = (coordinates[6:])
        #print (coordinates.replace('(','').replace(')','').replace(' ',','))
# quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')
#fig = go.Figure(go.Densitymapbox(lat=df.latitude, lon=df.longitude, z=df.signal, radius=10))
#fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()




        