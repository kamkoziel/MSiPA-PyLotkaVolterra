from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy
from PyQt5.QtWidgets import  QAction, qApp, QDialog, QFileDialog
from PyQt5.QtGui import QIcon
from src.gui.MainWidget import *
from src.gui.SubwindowsWidgets.SaveDataWidget import SaveDataWidget
import os
import csv

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

        addData = QAction(QIcon('data.png'), 'AddData',self)
        addData.setStatusTip('Add set of data from file')
        addData.triggered.connect(self.AddDataToPlots)
        saveData = QAction(QIcon('save.png'), 'Save Data', self)
        saveData.triggered.connect(self.openSaveDialog)

        self.statusBar().showMessage('Ready')
        self.statusBar().setStyleSheet("background-color: #2d3847; color: white")

        self.MainGui = MainWidget()
        self.statusBar().showMessage(str(self.MainGui.leftPanel.fundParams.rSpinBox.value()))
        self.setCentralWidget(self.MainGui)

        menubar = self.menuBar()
        self.menuBar().setStyleSheet("background-color: #2d3847; color: white;")
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(saveFile)
        fileMenu.addAction(addData)
        fileMenu.addAction(exitAct)
        dataMenu = menubar.addMenu('&Data')
        dataMenu.addAction(addData)
        dataMenu.addAction(saveData)

        self.show()

    @pyqtSlot()
    def AddDataToPlots(self):
        dataToPlotY = []
        dataToPlotX = []
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home','CSV (*.csv)' )
        if fname:
            with open(fname[0], newline = '') as dataFile:
                data_reader = csv.reader(dataFile,delimiter = ';')
                for row in data_reader:
                    dataToPlotY.append(row[0])
                    dataToPlotX.append(row[1])

            self.MainGui.tabPanel.plot1.plotPhaze.AddDataToFig(dataToPlotY,dataToPlotX,fname)
        else:
            print('Brak pliku')

    @pyqtSlot()
    def openSaveDialog(self):
        SaveDataWidget(self, self.MainGui.basicModel, self.MainGui.LCModel, self.MainGui.OFModel)

