from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QAction, qApp, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from gui.MainWidget import MainWidget
from gui.SubwindowsWidgets.SaveDataWidget import SaveDataWidget
import csv


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui: MainWidget
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 650
        self.title = 'PiSA - Model Lotki-Volterry'
        self.setStyleSheet("background-color: #192028; color: white")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        addData = QAction(QIcon('data.png'), 'AddData', self)
        addData.setStatusTip('Add set of data from file')
        addData.triggered.connect(self.add_data2plot)
        saveData = QAction(QIcon('save.png'), 'Save Data', self)
        saveData.setStatusTip('Save data to .xlsx file')
        saveData.triggered.connect(self.save_data)

        self.statusBar().showMessage('Ready')
        self.statusBar().setStyleSheet("background-color: #2d3847; color: white")

        self.gui = MainWidget()
        self.statusBar().showMessage(str(self.gui.leftPanel.basic_params.r))
        self.setCentralWidget(self.gui)

        menubar = self.menuBar()
        self.menuBar().setStyleSheet("background-color: #2d3847; color: white;")
        fileMenu = menubar.addMenu('&File')

        fileMenu.addAction(exitAct)
        dataMenu = menubar.addMenu('&Data')
        dataMenu.addAction(saveData)

        self.show()

    @pyqtSlot()
    def add_data2plot(self):
        dataToPlotY = []
        dataToPlotX = []
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', 'CSV (*.csv)')
        if fname:
            with open(fname[0], newline='') as dataFile:
                data_reader = csv.reader(dataFile, delimiter=';')
                for row in data_reader:
                    dataToPlotY.append(row[0])
                    dataToPlotX.append(row[1])

            self.gui.tabPanel.basic_model_plot.plotPhaze.AddDataToFig(dataToPlotY, dataToPlotX, fname)
        else:
            print('Brak pliku')

    @pyqtSlot()
    def save_data(self):
        SaveDataWidget(self, self.gui.basicModel, self.gui.LCModel, self.gui.OFModel)
