#!/usr/bin/env python

import sys
import time

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QKeyEvent, QPixmap

from matplotlib.ticker import MaxNLocator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFrame
from PyQt5.QtGui import QIcon, QPixmap

Ui_Help, _ = uic.loadUiType("help.ui")

class Help(QDialog, Ui_Help):

	def __init__(self, parent=None):

		QDialog.__init__(self, parent=parent)
		Ui_Help.__init__(self)
		self.setupUi(self)		
		
		self.timer = QTimer(self)

		self.value = 1
		self.pushButton1.clicked.connect(self.decrementa)
		self.pushButton2.clicked.connect(self.incrementa)

		self.events()

		self.timer.setInterval(300)
		self.timer.start()

	def events(self):
		self.timer.timeout.connect(self.update)

	def update(self):
		if(self.value == 1):
			self.pushButton1.setEnabled(False)
		else:
			self.pushButton1.setEnabled(not False)

		if(self.value == 2):
			self.pushButton2.setEnabled(False)
		else:
			self.pushButton2.setEnabled(not False)

		if(self.value == 1):	
			self.label1.setPixmap(QPixmap('Image_Help/Image2.png'))
			self.labelText.setText("Na Coleta dos Dados se deve serguir o padrão da figura:")
		elif(self.value == 2):	
			self.label1.setPixmap(QPixmap('Image_Help/Image1.png'))
			self.labelText.setText("O arquivo excel gerado deve seguir a estrura da figura abaixo:")
		
		self.label1.adjustSize()

	def incrementa(self):
		if(self.value > 2):
			self.value = 2
		self.value += 1

	def decrementa(self):		
		if(self.value > 1):
			self.value -= 1
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Help()
    main.show()

    sys.exit(app.exec_())