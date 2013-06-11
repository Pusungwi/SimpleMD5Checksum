#Title : SimpleMD5Checksum
#Version : 0.1
#Author : Yi 'Pusungwi' Yeon Jae
#Description : Simple creating md5 checksum to use PyQt4 script

import sys
import hashlib
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()

		#global init
		self.tTextBox = None
		self.cTextBox = None

		self.initUI()

	def initUI(self):
		self.setToolTip('This is a <b>QWidget</b> example')

		tText = QtGui.QLabel('Target Text')
		cText = QtGui.QLabel('Checksum (MD5)')

		self.tTextBox = QtGui.QLineEdit()
		self.tTextBox.textChanged.connect(self.makeMD5checksum)

		self.cTextBox = QtGui.QLineEdit()

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(tText, 1, 0)
		grid.addWidget(self.tTextBox, 1, 1)

		grid.addWidget(cText, 2, 0)
		grid.addWidget(self.cTextBox, 2, 1)

		self.setLayout(grid)

		self.setGeometry(300, 300, 500, 150)
		self.setWindowTitle('md5check')
		
	def makeMD5checksum(self):
		targetText = self.tTextBox.text()
		tmpChecksum = hashlib.md5(targetText.encode()).hexdigest()

		#DEBUG CODE
		#print('result : ' + tmpChecksum)
		self.cTextBox.setText(tmpChecksum)

	def closeWidget(self):
		reply = QtGui.QMessageBox.question(self, 'Message', 'Are you sure to quit?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.Yes:
			self.hide()
			QtCore.QCoreApplication.instance().quit()
		else:
			QtGui.QMessageBox.information(self, 'Message', 'GOOD')

def main():
	app = QtGui.QApplication(sys.argv)

	w = Example()
	w.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
