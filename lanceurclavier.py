#!/usr/bin/python
from PyQt4 import QtWebKit
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread
import json
import sys
#import lanceur2
import clavier
#import trav
#import alist
from PyQt4.QtCore import QTimer
import time
#from PyQt4.QtGui import QApplication
import time
from PyQt4.QtCore import QObject, pyqtSignal, SIGNAL
     
class lazyworker(QtCore.QObject):
	def doWork(self):
		self.i = 0
		print self.i
		for self.i in range(0,10):
			time.sleep(0.1)
			self.emit(SIGNAL("update(int)"), self.i)
		print self.i




#alexT.starting(self)
#class string():

    



class MainDialog(QtGui.QFrame, clavier.Ui_Frame):


	def __init__(self,parent=None):
		

		super(MainDialog,self).__init__(parent)
		
        	
		self.setupUi(self)
		tl = lazyworker()
		self.connect(tl, SIGNAL("update(int)"), self.updateUI)
        	self.test = tl.doWork()
		#timer = QTimer()
		#self.pushButton_4.clicked.connect(self.BConnectClicked)
		self.PB.clicked.connect(self.pbcliked)
		#self.pbmontrer.clicked.connect(self.BConnectClicked)
		#self.BDisconect.clicked.connect(self.BDisconectClicked)
		#self.BConectRafr.clicked.connect(self.BConectRafrClicked)
	
	def updateUI(self, prog):
        	print prog

	def pbcliked(self):
        	#test = self.LETerminal.text()
        	print "entrer"
        	tl = lazyworker()
        	tl.doWork()

		
		

	

#app=QtGui.QApplication(sys.argv) 
#Frame = MainDialog()
#ui = Ui_Frame()
#ui.setupUi(Frame)
#Frame.show()
#app.exec_()
#sys.exit(app.exec_())

app=QtGui.QApplication(sys.argv) 
form=MainDialog()
form.show()
app.exec_()


