# coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys
from fastkml import kml
import pandas as pd
import plotly.graph_objects as go
from pprint import pprint
import os
import csv




class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Привет, мир!")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("закрыть окно")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        #self.button.clicked.connect(self.on_clicked)
        self.button = QtWidgets.QPushButton("Нажми меня")
        self.vbox.addWidget(self.button)
        self.button.clicked.connect(self.on_clicked)

        self.button2 = QtWidgets.QPushButton("Открыть каталог")
        self.vbox.addWidget(self.button2)
        self.button2.clicked.connect(self.open_dir)

        self.label2 = QtWidgets.QLabel("Каталог")
        self.vbox.addWidget(self.label2)

        self.button3 = QtWidgets.QPushButton("Открыть файл")
        self.vbox.addWidget(self.button3)
        self.button3.clicked.connect(self.open_file)

        self.progressBar = QtWidgets.QProgressBar(self)
      
        self.vbox.addWidget(self.progressBar)
       



    def open_dir(self, parent):
        self.dirName = QtWidgets.QFileDialog.getExistingDirectory(parent=window, directory=QtCore.QDir.currentPath())
        # self.dir = QtWidgets.QFileDialog.getExistingDirectoryUrl(parent=window, directory = QtCore.QUrl.fromLocalFile(QtCore.QDir.currentPath()))
        # self.dirName = self.dir.toLocalFile()
        self.label2.setText(self.dirName)

    def open_file(self, parent):
        self.f = QtWidgets.QFileDialog.getOpenFileName(
            parent=window, caption="Выбрать *.kml",
            directory=QtCore.QDir.currentPath(),
            filter="All (*);;KML (*.kml *.xml)"
            )
        self.fileName = self.f[0]
        self.label2.setText(self.fileName)
        
        self.read_kml(self.fileName)

        




    def on_clicked(self):
        self.label.setText("Новая надпись")
        #button = QtWidgets.QPushButton("Нажми меня")
        #self.button.setDisabled(True)

    def read_kml(self, fileName):
        print(fileName)
        with open(fileName, 'rb') as kmlFile:
            k = kml.KML()
            file = kmlFile.read()
            k.from_string(file)
            features =list(k.features())
            f2 = list(features[0].features())
            a = 0


            # списки по каждым данным
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
                self.progressBar.setValue(a)

                if "dBm" in s:

                    signal = (s.replace('dBm','').replace(' ', ''))

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

                
            point = [[num_point], [signal_all], [latitude_all], [longitude_all]]

            allio = {"num_point": num_point, "signal_all": signal_all, "latitude_all": latitude_all, "longitude_all": longitude_all}
            # pprint(allio)

            

            with open('test.csv', 'wt') as fout:
                cout = csv.DictWriter(fout, ['num_point', 'signal_all', 'latitude_all', 'longitude_all'] )
                cout.writeheader()
                cout.writerow(allio)
                


            with open('dict.csv', 'w') as f:
                

                w = csv.writer(f)
                w.writerow(allio.keys())
                for toi in zip(num_point, signal_all, latitude_all, longitude_all):
                    w.writerow(toi)


            
            with open('mifile.txt', 'w') as mi:
                mi.write(str(allio))

            df = pd.DataFrame(allio, index=[num_point])

            fig = go.Figure(go.Densitymapbox(lat=df.latitude_all, lon=df.longitude_all, z=df.signal_all, radius=10))
            fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            fig.show()

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=df["num_point"],
                    y=df["signal_all"],
                    mode="lines",
                    name="signal"
                )    
            )
            
            fig.show()





if __name__ == "__main__" :

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
        # Создаем экземпляр класса
    window.setWindowTitle("ООП-стиль создания окна")
    window.resize(300, 70)
    window.show() # Отображаем окно
    #button.show()

    sys.exit(app.exec_()) # Запускаем цикл обработки событий

