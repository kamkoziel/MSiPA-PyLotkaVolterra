from PyQt5.QtWidgets import QHBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot
from src.gui.LeftPanel import LeftPanel
from src.gui.PlotTabWidget import PlotTabWidget

from src.calculations.LV_BasicModel import LV_BasicModel

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

        self.leftPanel = LeftPanel()
        self.leftPanel.mainButton.clicked.connect(self.onClick)

        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(self.leftPanel)
        mainLayout.addWidget(self.tabPanel)




    @pyqtSlot()
    def onClick(self):
        self.basicModel= LV_BasicModel()
        self.basicModel.setInitialonditions(self.leftPanel.initNums.VNumber.value(), self.leftPanel.initNums.PNumber.value())
        self.basicModel.setParamsValues(self.leftPanel.fundParams.rSpinBox.value(),self.leftPanel.fundParams.sSpinBox.value(),
                                        self.leftPanel.fundParams.aSpinBox.value(),self.leftPanel.fundParams.bSpinBox.value())
        self.basicModel.setSimulationTime(0,15,1000)
        self.basicModel.exportFigToPNG()



