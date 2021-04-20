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

#biblioteca responsavel por calcular as propriedades de refrigeracao
import CoolProp as CP
from CoolProp.CoolProp import PropsSI

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

		#para colocar fundo animado
		self.movie = QMovie("backgroundAires.gif")
		self.movie.frameChanged.connect(self.repaint)
		self.movie.start()			

		self.widget_2.setVisible(False)
		self.widget.setVisible(False)		

		self.timer = QTimer(self)				

		self.createActions()
		self.createMenus()		

		self.events()
		self.timer.setInterval(200)
		self.timer.start()	

	def events(self):
		self.timer.timeout.connect(self.update)

	def update(self):
		if(self.widget.isVisible()):		
			self.realizaCalculos()

	def createActions(self):
		self.openAct = QAction("&Open Archive", self, shortcut="Ctrl+O", triggered=self.open)
		self.openExport = QAction("&Export Data", self, shortcut="Ctrl+D", enabled=False, triggered=self.export)  
		self.openView = QAction("&View Graph", self, shortcut="Ctrl+P", triggered=self.view)  
		self.openHelp = QAction("&Help", self, shortcut="Ctrl+H", triggered=self.help)
		self.openAbout = QAction("&About", self, shortcut="Ctrl+B", triggered=self.about)

	def open(self):
		self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))  
		self.df = pd.read_excel(self.filename[0], index_col=0,  engine='openpyxl', dtype={'DATE':str, 'TIME':str, 'T01':float, 'T02':float, 'T03':float, 'T04':float, 'T05':float, 'T06':float, 'T07':float, 'T08':float, 'P01':float, 'P02':float,}) 
		if(len(self.df['T01']) > 0):					
			self.widget_2.setVisible(True)
			self.widget.setVisible(True)
			self.widget_2.setStyleSheet("background-image : url(layoutAires.png)")
			self.fileMenu02.setEnabled(True)			
			self.realizaCalculos()
			self.openExport.setEnabled(True)
		else:
			return

	def export(self):
		self.filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))

		data = {'T01': [self.label01.text()], 'T02': [self.label02.text()], 'T03': [self.label03.text()], 'T04': [self.label04.text()], 
		'T05': [self.label05.text()], 'T06': [self.label06.text()], 'T07': [self.label07.text()], 'T08': [self.label08.text()], 
		'P01': [self.label09.text()], 'P02': [self.label10.text()],  'Q_Evap [BTU/h]': [self.label18.text()], 'Q_Evap [kW]': [self.label11.text()],
		'Sub_Resfriamento [K]': [self.label12.text()], 'Super_Aquecimento [K]': [self.label13.text()], 'h1 [kJ/kg]': [self.label14.text()],
		'h3 [kJ/kg]': [self.label15.text()], 'T_sat_Evap [C]': [self.label16.text()], 'T_sat_Liq [C]': [self.label17.text()],
		 'Mass Flow [kg/h]': [self.lineEdit.text()]}

		df = pd.DataFrame(data, columns = ['T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'P01', 'P02', 'Q_Evap [BTU/h]', 'Q_Evap [kW]',
		'Sub_Resfriamento [K]', 'Super_Aquecimento [K]', 'h1 [kJ/kg]', 'h3 [kJ/kg]', 'T_sat_Evap [C]', 'T_sat_Liq [C]', 'Mass Flow [kg/h]'])

		df.to_excel (self.filename[0]+".xlsx", index = False, header=True)			
	
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

	def celsiusToKelvin(self,celsius):
		return(celsius + 273.15)

	def kelvinToCelsius(self,kelvin):
		return(kelvin - 273.15)

	def barToPascal(self,bar):
		return (bar*100000.0)

	def realizaCalculos(self):
		#calculando media e desvio padrao dos dados excel
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

		#calculando capacidade do evap, subresfriamento e superaqueciemnto	
		if(len(self.lineEdit.text()) > 0):	
			if(self.checkBox.isChecked()):
				T_liq = self.celsiusToKelvin(round(np.mean(self.df['T03']),1))
			else:
				T_liq = self.celsiusToKelvin(round(np.mean(self.df['T08']),1))
			T_suc = self.celsiusToKelvin(round(np.mean(self.df['T04']),1))
			P_suc_comp = self.barToPascal( round(np.mean(self.df['P02']),1) + 1.02)
			P_liq_comp = self.barToPascal(round(np.mean(self.df['P01']),1) + 1.02)

			T_sat_evap = PropsSI('T', 'P', P_suc_comp, 'Q', 1, 'R134a')			
			self.label16.setText(str(round(self.kelvinToCelsius(T_sat_evap),2)))

			T_sat_liq = PropsSI('T', 'P', P_liq_comp, 'Q', 1, 'R134a')			
			self.label17.setText(str(round(self.kelvinToCelsius(T_sat_liq),2)))

			h1 = PropsSI('H', 'P', P_suc_comp, 'Q', 1, 'R134a')
			self.label14.setText(str(round(h1/1000.,2)))		

			h3 = PropsSI('H', 'T', T_liq, 'Q', 0, 'R134a')
			self.label15.setText(str(round(h3/1000.,2)))	

			subResfriamento = T_sat_liq - T_liq
			self.label12.setText(str(round(subResfriamento,2)))		

			superAquecimento = T_suc - T_sat_evap
			self.label13.setText(str(round(superAquecimento,2)))

			Q_evap = float(self.lineEdit.text())*((h1-h3)/1000.0)/3600.
			self.label11.setText(str(round(Q_evap,2)))		
			self.label18.setText(str(round(Q_evap*3412)))

		else:
			self.label11.setText("?")
			self.label12.setText("?")
			self.label13.setText("?")
			self.label14.setText("?")
			self.label15.setText("?")
			self.label16.setText("?")
			self.label17.setText("?")
			self.label18.setText("?")

	#funcao que anima gif
	def paintEvent(self, event):
		currentFrame = self.movie.currentPixmap()
		frameRect = currentFrame.rect()
		frameRect.moveCenter(self.rect().center())
		if frameRect.intersects(event.rect()):
			painter = QPainter(self)
			painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	main = MainWindow()
	main.show()

	sys.exit(app.exec_())
