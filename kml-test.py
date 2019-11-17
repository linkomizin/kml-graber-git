import pandas as pd
quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.graph_objects as go
fig = go.Figure(go.Densitymapbox(lat=quakes.Latitude, lon=quakes.Longitude, z=quakes.Magnitude, radius=10))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()



# from fastkml import kml

# if __name__ == '__main__':

#     fname = "gps.xml"

#     with open(fname,"rb") as kmlFile:
#         k = kml.KML()
#         file = kmlFile.read()
#         k.from_string(file)
#         features =list(k.features())
#         f2 = list(features[0].features())
#         print (len(f2))


        # print (s)
        # count_all = len(f2) - 1
        # count = 0
        # while count <= count_all:
        #     count
        #     count = count - 1
        #     # coordinat = ((str(f2[count].geometry))[6:]).replace('(','').replace(')','').replace(' ',',')
        #     # latitude, longitude = coordinat.split(',', 1)
        #     s = (f2[count].name)
            
            



                    # print(len(yes_signal))


                #signal = str(['-'+([s.split('-',[1])])-' dBm'])
            # print (signal)
                
            #d = {'latitude':pd.array([latitude]), 'longitude':pd.array([longitude]), 'signal':pd.array(signal)}
            #df = pd.DataFrame(d,index=[count])
            
            # print (f2[count].name, coordinat)
            #coordinates =  str(f2[count].geometry)
        #coordinates = (coordinates[6:])
        #print (coordinates.replace('(','').replace(')','').replace(' ',','))
# quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')
# fig = go.Figure(go.Densitymapbox(lat=df.latitude, lon=df.longitude, z=df.signal, radius=10))
# fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()




#             if s.find('dBm'):
#                 signal = (s.replace('dBm', ''))    
#             s.find('dBm')
#                 signal = (s.replace('dBm', ''))
                
#                 bs_signal, signal = (signal.split('-', (1)))
#                 yes_signal = ('-' + signal)
#             else:
#                 continue
            # print(a," : --- " ,yes_signal)
            
            # if s.find('БС 0'):
            #     no_signal = ['0']
            #     print (a," : --- " ,no_signal)
            # else:
            #     continue
                
                
        
#                except ValueError:
 #                   pass