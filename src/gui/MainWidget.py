from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QGroupBox
from PyQt5.QtWidgets import QSpinBox, QLabel, QPushButton, QStackedWidget
from plots.plotCanvas import *
from PyQt5.QtCore import pyqtSlot
from src.gui.LeftPanel import LeftPanel
from src.gui.PlotTabWidget import PlotTabWidget

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

        self.m = PlotTabWidget()
        #self.m.move(0, 0)

        self.leftPanel = LeftPanel()

        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(self.leftPanel)
        mainLayout.addWidget(self.m)


    @pyqtSlot()
    def onClick(self):
        self.modelLV = LVmodel(self.initialNumber.victimNumber.value(), self.initialNumber.predatorsNumber.value())
        self.modelLV.setFundamParams(self.aSpinBox.value())
        print(self.modelLV.victimsReproduc)