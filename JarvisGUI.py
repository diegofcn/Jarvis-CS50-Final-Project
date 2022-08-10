from gui import Ui_Dialog
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import main
import sys


class MainThread(QThread):

    def __int__(self):
        super(MainThread, self).__init__()

    def run(self):
        main.run_jarvis()


startExe = MainThread()


class GuiStart(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_Dialog()
        self.gui.setupUi(self)

        self.gui.pushButtonStart.clicked.connect(self.startTask)
        self.gui.pushButtonQuit.clicked.connect(self.close)

    def startTask(self):
        self.gui.label1 = QtGui.QMovie("..//..//OneDrive//Desktop//Neuer Ordner//Iron_Template_1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("..//..//OneDrive//Desktop//Neuer Ordner//Siri_1.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("..//..//OneDrive//Desktop//Neuer Ordner//__02-____.gif")
        self.gui.label_2.setMovie(self.gui.label3)
        self.gui.label3.start()

        startExe.start()


GuiApp = QApplication(sys.argv)
jarvis_gui = GuiStart()
jarvis_gui.show()
exit(GuiApp.exec_())
