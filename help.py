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

		if(self.value == 14):
			self.pushButton2.setEnabled(False)
		else:
			self.pushButton2.setEnabled(not False)

		if(self.value == 1):	
			self.label1.setPixmap(QPixmap('Image_Help/Image1.png'))
			self.labelText.setText("Para utilizar o software eh necessario acessar o menu: Tools -> Select Serial Ports -> Porta Serial Detectada ")
		elif(self.value == 2):	
			self.label1.setPixmap(QPixmap('Image_Help/Image2.png'))
			self.labelText.setText(" Com o Menu de Opcoes desbloqueado, Pode-se escolher as opcoes de envio de dados disponivel. ")
		elif(self.value == 3):	
			self.label1.setPixmap(QPixmap('Image_Help/Image3.png'))
			self.labelText.setText("No Passo seguinte se Escolhe se o Dispositvo eh o Emissor ou o Receptor.")
		elif(self.value == 4):	
			self.label1.setPixmap(QPixmap('Image_Help/Image4.png'))
			self.labelText.setText("Para a Opcao de Envio em ASCII o dispositivo Emissor deve escolher Escolher a Taxa de Envio e uma das opcoes de envio disponivel, pode ser escolhido entre digitar a informacao via linha de comando ou carregar um arquivo. ")
		elif(self.value == 5):	
			self.label1.setPixmap(QPixmap('Image_Help/Image5.png'))
			self.labelText.setText("Entrada em Texto via Linha de Comando.")
		elif(self.value == 6):	
			self.label1.setPixmap(QPixmap('Image_Help/Image6.png'))
			self.labelText.setText("Entrada via Arquivo de Texto.")
		elif(self.value == 7):	
			self.label1.setPixmap(QPixmap('Image_Help/Image7.png'))
			self.labelText.setText("Exemplo de Visualizacao ao Abrir um arquivo de texto.")
		elif(self.value == 8):	
			self.label1.setPixmap(QPixmap('Image_Help/Image8.png'))
			self.labelText.setText("Usando as teclas: Ctrl+G eh possivel visualizar o sinal binario. Para Ocultar o Grafico usar: Ctrl+K. Essas mesmas funcionalidades podem ser acessada no menu Tools.")
		elif(self.value == 9):	
			self.label1.setPixmap(QPixmap('Image_Help/Image9.png'))
			self.labelText.setText("Usando as teclas: Ctrl+P eh possivel visualizar a barra de personalizacao onde eh possivel escolher os sinais a serem visualizados e etc. Para Ocultar: Ctrl+L. Essas mesmas funcionalidades podem ser acessada no menu Tools.")
		elif(self.value == 10):	
			self.label1.setPixmap(QPixmap('Image_Help/Image10.png'))
			self.labelText.setText("Para a Opcao de Recepcao em ASCII o dispositivo Receptor deve escolher Escolher a Taxa de Recebimento. A funcionalidade de deteccao de Erro so sera liberada caso o receptor tenha recebido alguma mensagem. As funcionalidades de visualizacao de sinal tambem sao validas para o receptor.")
		elif(self.value == 11):	
			self.label1.setPixmap(QPixmap('Image_Help/Image11.png'))
			self.labelText.setText("Para a Opcao de Envio de Imagem o Emissor deve Selecionar a Taxa de envio e selecionar uma imagem. Para tanto dois menus sao desbloqueados (File e View), um para a procura da imagem a ser carregada e outro referente a visualizacao da imagem.")
		elif(self.value == 12):	
			self.label1.setPixmap(QPixmap('Image_Help/Image12.png'))
			self.labelText.setText("Ao ser carregada a Imagem por meio do menu: File ou pela tecla de atalho: Ctrl+O, o binario respectivo a cada canal RGB sera mostrado. Eh possivel escolher o canal RGB para a visualizacao.")
		elif(self.value == 13):	
			self.label1.setPixmap(QPixmap('Image_Help/Image13.png'))
			self.labelText.setText("As opcoes de visualizacao grafica tambem sao validas para imagem (Ctrl+G e Ctrl+P). Tambem eh possivel ocultar a imagem atraves do atalho: Ctrl+U e voltar a visualizar: Ctrl+I ou usar o menu: View para acessar as mesmas funcionalidades.")
		elif(self.value == 14):	
			self.label1.setPixmap(QPixmap('Image_Help/Image14.png'))
			self.labelText.setText("Para a Opcao de Recebimento da Imagem o Receptor deve Selecionar a Taxa de recepcao. As opcoes de visualizacao grafica tambem sao validas para o recptor (Ctrl+G e Ctrl+P). Tambem eh possivel ocultar a imagem atraves do atalho: Ctrl+U e voltar a visualizar: Ctrl+I ou usar o menu: View para acessar as mesmas funcionalidades. A funcionalidade de deteccao de Erro so sera liberada caso o receptor tenha recebido alguma mensagem.")
		self.label1.adjustSize()

	def incrementa(self):
		if(self.value > 14):
			self.value = 14
		self.value += 1

	def decrementa(self):		
		if(self.value > 1):
			self.value -= 1
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Help()
    main.show()

    sys.exit(app.exec_())