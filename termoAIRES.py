#!/usr/bin/env python3

#Temperaturas
#T01 = Entrada do Evaporador (Ar quente)
#T02 = Saida do Evaporador (Ar resfriado)
#T03 = Descarga Compressor
#T04 = Succao Compressor
#T05 = Da descarga do compressor para a entrada do condesador 
#T06 = Entrada do condensador (Ar temperatura ambiente)
#T07 = Saida do Condesador (Ar aquecido)
#T08 = Ponto para medicao de subresfriamento no condensador

#Pressoes
#P01 = Pressao na descarga
#P02 = Pressao na succao

import sys, os
import pandas as pd
import numpy as np

from PyQt5 import QtGui, QtCore

from PyQt5 import uic
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QPushButton, QVBoxLayout, QAction, QMenu, QFileDialog 

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from help import Help
from view import View

Ui_MainWindow, QtBaseClass = uic.loadUiType("termoAIRES.ui")

class MainWindow(QMainWindow, Ui_MainWindow):
	
	def __init__(self, parent=None):        
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)		
		self.setupUi(self) 		

		self.widget_2.setStyleSheet("background-image : url(layoutAires.png)")

		self.timer = QTimer(self)	

		self.test = [1,2,3]	

		self.createActions()
		self.createMenus()		

		self.events()
		self.timer.setInterval(200)
		self.timer.start()	

	def events(self):
		self.timer.timeout.connect(self.update)

	def update(self):
		return

	def createActions(self):
		self.openAct = QAction("&Open Archive", self, shortcut="Ctrl+O", triggered=self.open)
		self.openExport = QAction("&Export Data", self, shortcut="Ctrl+D", triggered=self.export)  
		self.openView = QAction("&View Graph", self, shortcut="Ctrl+P", triggered=self.view)  
		self.openHelp = QAction("&Help", self, shortcut="Ctrl+H", triggered=self.help)
		self.openAbout = QAction("&About", self, shortcut="Ctrl+B", triggered=self.about)

	def open(self):
		self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))  
		self.df = pd.read_excel(self.filename[0], index_col=0, dtype={'DATE':str, 'TIME':str, 'T01':float, 'T02':float, 'T03':float, 'T04':float, 'T05':float, 'T06':float, 'T07':float, 'T08':float, 'P01':float, 'P02':float,}) 
		if(len(self.df['T01']) > 0):
			self.fileMenu02.setEnabled(True)
			self.realizaCalculos()
		else:
			return

	def export(self):
		return	
	
	def view(self):
		View(self.df).exec_()

	def help(self):		
		Help().exec_()		

	def about(self):
		return
		
	def createMenus(self):
		self.fileMenu01 = QMenu("&Menu", self)
		self.fileMenu01.addSeparator()
		self.fileMenu01.addAction(self.openAct)        
		self.fileMenu01.addSeparator() 
		self.fileMenu01.addAction(self.openExport)        
		self.fileMenu01.addSeparator()

		self.fileMenu02 = QMenu("&View", self)
		self.fileMenu02.addSeparator()
		self.fileMenu02.addAction(self.openView)        
		self.fileMenu02.addSeparator()
		self.fileMenu02.setEnabled(False)

		self.fileMenu03 = QMenu("&Help", self)
		self.fileMenu03.addSeparator()
		self.fileMenu03.addAction(self.openHelp)        
		self.fileMenu03.addSeparator()   
		self.fileMenu03.addAction(self.openAbout)        
		self.fileMenu03.addSeparator()   

		self.menuBar().addMenu(self.fileMenu01)
		self.menuBar().addMenu(self.fileMenu02)	
		self.menuBar().addMenu(self.fileMenu03)	

	def realizaCalculos(self):
		self.label01.setText(str(round(np.mean(self.df['T01']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['T01']),1)))
		self.label02.setText(str(round(np.mean(self.df['T02']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['T02']),1)))
		self.label03.setText(str(round(np.mean(self.df['T03']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['T03']),1)))
		self.label04.setText(str(round(np.mean(self.df['T04']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['T04']),1)))
		self.label05.setText(str(round(np.mean(self.df['T05']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['T05']),1)))
		self.label06.setText(str(round(np.mean(self.df['T06']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['T06']),1)))
		self.label07.setText(str(round(np.mean(self.df['T07']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['T07']),1)))
		self.label08.setText(str(round(np.mean(self.df['T08']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['T08']),1)))
		self.label09.setText(str(round(np.mean(self.df['P01']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['P01']),1)))
		self.label10.setText(str(round(np.mean(self.df['P02']),1)) + " " + str(u'\u00B1') + " " + str(round(np.std(self.df['P02']),1)))

if __name__ == '__main__':
	app = QApplication(sys.argv)

	main = MainWindow()
	main.show()

	sys.exit(app.exec_())
