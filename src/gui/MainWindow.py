from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy
from PyQt5.QtWidgets import  QAction, qApp, QDialog
from PyQt5.QtGui import QIcon
from gui.MainWidget import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.width=1000
        self.height=650
        self.title = 'PiSA - Model Lotki-Volterry'
        self.setStyleSheet("background-color: #192028; color: white")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        saveFile = QAction(QIcon('save.png'), '&Save', self)
        saveFile.setStatusTip('Save application')
        saveFile.triggered.connect(qApp.quit)
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar().showMessage('Ready')
        self.statusBar().setStyleSheet("background-color: #2d3847; color: white")

        menubar = self.menuBar()
        self.menuBar().setStyleSheet("background-color: #2d3847; color: white;")
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitAct)

        self.MainGui = MainWidget()
        self.setCentralWidget(self.MainGui)

        self.show()


