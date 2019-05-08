from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QGroupBox
from PyQt5.QtWidgets import QSpinBox, QLabel, QPushButton, QStackedWidget
from src.plots.plotCanvas import *
from PyQt5.QtCore import pyqtSlot
from src.gui.LeftPanel import LeftPanel
from src.gui.PlotTabWidget import PlotTabWidget

from src.calculations.LVmodel import LVmodel

"""
    Class responsible for a main widget 
    in application window 
    Contains: 
        -left panel fundamental params gui elements
        -left panel own params gui elements from ownModGui


"""

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 650
        self.leftPanelWidth = 250

        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tabPanel = PlotTabWidget()
        #self.m.move(0, 0)

        self.leftPanel = LeftPanel()
        self.leftPanel.mainButton.clicked.connect(self.onClick)

        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(self.leftPanel)
        mainLayout.addWidget(self.tabPanel)




    #@pyqtSlot()
    def onClick(self):
        self.basicModel= LVmodel()
        self.basicModel.setInitialonditions(self.leftPanel.initNums.VNumber.value(), self.leftPanel.initNums.PNumber.value())
        self.basicModel.setParamsValues(self.leftPanel.fundParams.aSpinBox.value(),self.leftPanel.fundParams.bSpinBox.value(),
                                        self.leftPanel.fundParams.dSpinBox.value(),self.leftPanel.fundParams.cSpinBox.value())
        self.basicModel.setSimulationTime(0,15,1000)
        self.basicModel.exportFigToPNG()



