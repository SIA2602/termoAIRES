#!/usr/bin/env python

import sys
import time
import numpy as np

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

Ui_View, _ = uic.loadUiType("view.ui")

class View(QDialog, Ui_View):

	def __init__(self, data, parent = None):

		QDialog.__init__(self, parent=parent)
		Ui_View.__init__(self)
		self.setupUi(self)				
		
		self.timer = QTimer(self)				

		self.events()
		
		self.y = data	
		self.x = np.arange(0, len(self.y['T01']), 1).tolist()	

		self.createGraph()

		self.timer.setInterval(300)
		self.timer.start()

	def events(self):
		self.timer.timeout.connect(self.update)

	def update(self):
		self.plot()

	def printColor(self, comboBox):
		if(comboBox.currentText() == 'blue'):
			return 'b'
		if(comboBox.currentText() == 'cian'):
			return 'c'
		elif(comboBox.currentText() == 'yellow'):
			return 'y'
		elif(comboBox.currentText() == 'pink'):
			return 'm'
		elif(comboBox.currentText() == 'green'):
			return 'g'
		elif(comboBox.currentText() == 'red'):
			return 'r'
		elif(comboBox.currentText() == 'white'):
			return 'white'
		elif(comboBox.currentText() == 'purple'):
			return 'purple'
		elif(comboBox.currentText() == 'orange'):
			return 'orange'
		elif(comboBox.currentText() == 'lime'):
			return 'lime'
		elif(comboBox.currentText() == 'deeppink'):
			return 'deeppink'
		return 'white'

	def linesWidth(self):		
		self.label9.setNum(self.horizontalSlider1.value()/20.)
		return self.horizontalSlider1.value()/20.

	def createGraph(self):  		     
		self.figure = plt.figure()
		self.figure.subplots_adjust(left=0.070, bottom=0.085, right=0.99, top=0.97, hspace=0.13)
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar(self.canvas, self)
		self.graphLayout.addWidget(self.canvas)
		self.graphLayout.addWidget(self.toolbar)
		self.controle = True

	def plot(self):
		self.figure.clear()	

		if(len(self.x) > 0):
			#controle para imprimir a quantidade de bits desajado
			self.horizontalSlider.setMaximum(100)	
			value = (self.x[-1] - 19*self.spinBox.value()/20)*self.horizontalSlider.value()/99
			start = value - self.spinBox.value()/20
			end = start + 21*self.spinBox.value()/20
			#nao deixando ultrapassar o numero maximo de bits para visualizacao
			if(self.spinBox.value()+1 > len(self.y)): self.spinBox.setValue(len(self.y))
			else:				
				self.ax = self.figure.add_subplot(111)
				#ajustando eixo de visualizacao			
				self.ax.set_xlim(start, end)			
				#self.ax.step(self.x, self.y, color=self.printColor(), linewidth=self.linesWidth()) #opcao ativa imprime grafico	
				if(self.T01.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['T01'], color=self.printColor(self.comboBoxT01)) #opcao ativa imprime grafico	
				if(self.T02.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['T02'], color=self.printColor(self.comboBoxT02)) #opcao ativa imprime grafico
				if(self.T03.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['T03'], color=self.printColor(self.comboBoxT03)) #opcao ativa imprime grafico
				if(self.T04.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['T04'], color=self.printColor(self.comboBoxT04)) #opcao ativa imprime grafico
				if(self.T05.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['T05'], color=self.printColor(self.comboBoxT05)) #opcao ativa imprime grafico
				if(self.T06.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['T06'], color=self.printColor(self.comboBoxT06)) #opcao ativa imprime grafico
				if(self.T07.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['T07'], color=self.printColor(self.comboBoxT07)) #opcao ativa imprime grafico
				if(self.T08.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['T08'], color=self.printColor(self.comboBoxT08)) #opcao ativa imprime grafico
				if(self.P01.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['P01'], color=self.printColor(self.comboBoxP01)) #opcao ativa imprime grafico
				if(self.P02.isChecked()):
					self.ax.plot(self.y['TIME'], self.y['P02'], color=self.printColor(self.comboBoxP02)) #opcao ativa imprime grafico			
				self.ax.yaxis.set_major_locator(MaxNLocator(integer=True))
				self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))		
				self.ax.xaxis.grid(color='gray', linestyle='--', linewidth=0.5)
				self.ax.xaxis.grid(self.checkBox3.isChecked())	
				self.ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)			
				self.ax.yaxis.grid(self.checkBox2.isChecked())
				self.ax.set_facecolor((39./256.,40./256.,34./256.))	
				self.figure.set_facecolor((39./256.,40./256.,34./256.))
				color = "white"	
				#self.ax.set_ylabel(self.comboBox3.currentText(), color=color, size=15)
				self.ax.spines['bottom'].set_color(color)
				self.ax.spines['top'].set_color(color)
				self.ax.spines['left'].set_color(color)
				self.ax.spines['right'].set_color(color)
				for t in self.ax.xaxis.get_ticklines(): t.set_color(color)
				for t in self.ax.yaxis.get_ticklines(): t.set_color(color)
				for t in self.ax.xaxis.get_ticklines(): t.set_color(color)
				for t in self.ax.yaxis.get_ticklines(): t.set_color(color)
				for label in self.ax.get_yticklabels():
					label.set_color(color)
				for label in self.ax.get_xticklabels():
					label.set_color(color)	
				self.canvas.draw()	
		else: return
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = View()
    main.show()

    sys.exit(app.exec_())