# coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys
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
		
		self.button2 = QtWidgets.QPushButton("Открыть")
		self.vbox.addWidget(self.button2)
		self.button2.clicked.connect(self.open_dir)

		self.label2 = QtWidgets.QLabel(" hh")
		self.vbox.addWidget(self.label2)
		
	def open_dir(self, parent):
		self.dirName = QtWidgets.QFileDialog.getExistingDirectory(parent=window, directory=QtCore.QDir.currentPath())
		self.dir = QtWidgets.QFileDialog.getExistingDirectoryUrl(parent=window, directory = QtCore.QUrl.fromLocalFile(QtCore.QDir.currentPath()))
		self.dirName = self.dir.toLocalFile()
		self.label2.setText(self.dirName)
		
		
	
	def on_clicked(self):
		self.label.setText("Новая надпись")
		#button = QtWidgets.QPushButton("Нажми меня")
		#self.button.setDisabled(True)
		
if __name__ == "__main__" :
	
	app = QtWidgets.QApplication(sys.argv)
	window = MyWindow()
		# Создаем экземпляр класса
	window.setWindowTitle("ООП-стиль создания окна")
	window.resize(300, 70)
	window.show() # Отображаем окно
	
	
	#button.show()
	sys.exit(app.exec_()) # Запускаем цикл обработки событий