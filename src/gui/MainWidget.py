from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot
from src.gui.LeftPanel import LeftPanel
from src.gui.PlotTabWidget import PlotTabWidget
from src.gui.SetTimeWidget import SetTimeWidget

from src.calculations.LV_BasicModel import LV_BasicModel
from src.calculations.LV_LimitedCaptionModel import LV_LimitedCaptionModel
from src.calculations.LV_OutsideFactorModel import LV_OutsideFactorModel

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

        self.timeWidget = SetTimeWidget()

        VLayout = QVBoxLayout()
        VLayout.addWidget(self.tabPanel)
        VLayout.addWidget(self.timeWidget)

        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(self.leftPanel)
        mainLayout.addLayout(VLayout)




    @pyqtSlot()
    def onClick(self):
        self.basicModel= LV_BasicModel()
        self.basicModel.setInitialConditions(self.leftPanel.initNums.VNumber.value(), self.leftPanel.initNums.PNumber.value())
        self.basicModel.setParamsValues(self.leftPanel.fundParams.rSpinBox.value(),self.leftPanel.fundParams.sSpinBox.value(),
                                        self.leftPanel.fundParams.aSpinBox.value(),self.leftPanel.fundParams.bSpinBox.value())
        self.basicModel.setSimulationTime(self.timeWidget.startTime.value(),self.timeWidget.stopTime.value(),
                                          (self.timeWidget.stopTime.value()-self.timeWidget.startTime.value())*100)

        self.basicModel.exportFigToPNG('bModel.png')
        self.basicModel.exportTrajectoriesFigToPNG('bModel_tr.png')


        self.LCModel = LV_LimitedCaptionModel()
        self.LCModel.setInitialConditions(self.leftPanel.initNums.VNumber.value(),
                                          self.leftPanel.initNums.PNumber.value())
        self.LCModel.setParamsValues(self.leftPanel.fundParams.rSpinBox.value(),
                                        self.leftPanel.fundParams.sSpinBox.value(),
                                        self.leftPanel.fundParams.aSpinBox.value(),
                                        self.leftPanel.fundParams.bSpinBox.value(),
                                        self.leftPanel.limitCaption.CaptionLimitSpinBox.value())

        self.LCModel.setSimulationTime(self.timeWidget.startTime.value(), self.timeWidget.stopTime.value(),
                                       (self.timeWidget.stopTime.value()-self.timeWidget.startTime.value())*100)

        self.LCModel.exportFigToPNG('lcModel.png')
        self.LCModel.exportTrajectoriesFigToPNG('lcModel_tr.png')


        self.OFModel = LV_OutsideFactorModel()
        self.OFModel.setInitialConditions(self.leftPanel.initNums.VNumber.value(),
                                          self.leftPanel.initNums.PNumber.value())
        self.OFModel.setParamsValues(self.leftPanel.fundParams.rSpinBox.value(),
                                     self.leftPanel.fundParams.sSpinBox.value(),
                                     self.leftPanel.fundParams.aSpinBox.value(),
                                     self.leftPanel.fundParams.bSpinBox.value(),
                                     self.leftPanel.limitCaption.CaptionLimitSpinBox.value(),
                                     self.leftPanel.outFactor.victimsFactor.value(),
                                     self.leftPanel.outFactor.predatorsFactor.value())

        self.OFModel.setSimulationTime(self.timeWidget.startTime.value(), self.timeWidget.stopTime.value(),
                                       (self.timeWidget.stopTime.value() - self.timeWidget.startTime.value()) * 100)

        self.OFModel.exportFigToPNG('ofModel.png')
        self.OFModel.exportTrajectoriesFigToPNG('ofModel_tr.png')


