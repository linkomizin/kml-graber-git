from fastkml import kml
import pandas as pd
import plotly.graph_objects as go
from pprint import pprint
import os




class My_read_kml ():


    def read_file ():

        if __name__ == '__main__':
            # files=[]
            # for file in os.listdir("/Users/akira/Documents/code/py/kml-graber-git/"):
            #     if file.endswith(".kml"):
            #         files.append(file)
            #         print(os.path.join(file))

            # fname = "gps.kml"
            fileName = ""

            with open(fileName,"rb") as kmlFile:
                k = kml.KML()
                file = kmlFile.read()
                k.from_string(file)
                features =list(k.features())
                f2 = list(features[0].features())
                a = 0

                sorce_all = []
                all_signal = []
                num_point = []
                coordinat_all = []
                latitude_all = []
                longitude_all = []
                signal_all = []

                while a < len(f2) - 1:
                    a = a + 1
                    s = f2[a].name


                    num_point.append(a)
                    if "dBm" in s:

                        signal = (s.replace('dBm',''))

                        de, signal = (signal.split("-",(1)))
                        de = 0
                        signal_y = ('-' + signal)
                        signal_all.append(signal_y)


                    else :
                        if 'БС 0' in s:

                            signal_n = ('0')

                            signal_all.append(signal_n)


                    coordinat = ((str(f2[a].geometry))[6:]).replace('(', '').replace(')', '').replace(' ', ',')
                    longitude, latitude = coordinat.split(',', 1)

                    latitude_all.append(latitude)
                    longitude_all.append(longitude)

                    point =[num_point, signal_all, latitude_all, longitude_all]

            allio = {"num_point": num_point, "signal_all": signal_all, "latitude_all": latitude_all, "longitude_all": longitude_all}
            # pprint(allio)



            df = pd.DataFrame(allio, index=[num_point])

            fig = go.Figure(go.Densitymapbox(lat=df.latitude_all, lon=df.longitude_all, z=df.signal_all, radius=10))
            fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            fig.show()
