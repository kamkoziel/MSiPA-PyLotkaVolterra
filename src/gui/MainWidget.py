from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot
from src.gui.LeftPanel import LeftPanel
from src.gui.PlotTabWidget import PlotTabWidget
from src.gui.SetTimeWidget import SetTimeWidget

from src.calculations.LV_BasicModel import LV_BasicModel
from src.calculations.LV_LimitedCaptionModel import LV_LimitedCaptionModel
from src.calculations.LV_OutsideFactorModel import LV_OutsideFactorModel

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
        self.basicModel.setParamsValues(r=self.leftPanel.fundParams.rSpinBox.value(),s=self.leftPanel.fundParams.sSpinBox.value(),
                                        a=self.leftPanel.fundParams.aSpinBox.value(),b=self.leftPanel.fundParams.bSpinBox.value())
        self.basicModel.setSimulationTime(self.timeWidget.startTime.value(),self.timeWidget.stopTime.value(),
                                          (self.timeWidget.stopTime.value()-self.timeWidget.startTime.value())*100)

        V,P = self.basicModel.getPopulationsData()

        self.tabPanel.plot1.plotPopulation.plot(self.basicModel.time ,V, P )
        self.tabPanel.plot1.plotPhaze.plot(V, P,
                                           self.basicModel.initialCondition[0],
                                           self.basicModel.initialCondition[1],
                                           self.basicModel.X_f1[0],
                                           self.basicModel.X_f1[1],
                                           self.basicModel)


        self.LCModel = LV_LimitedCaptionModel()
        self.LCModel.setInitialConditions(self.leftPanel.initNums.VNumber.value(),
                                          self.leftPanel.initNums.PNumber.value())
        self.LCModel.setParamsValues(r= self.leftPanel.fundParams.rSpinBox.value(),
                                       s= self.leftPanel.fundParams.sSpinBox.value(),
                                       a= self.leftPanel.fundParams.aSpinBox.value(),
                                       b= self.leftPanel.fundParams.bSpinBox.value(),
                                       K= self.leftPanel.limitCaption.CaptionLimitSpinBox.value())

        self.LCModel.setSimulationTime(self.timeWidget.startTime.value(), self.timeWidget.stopTime.value(),
                                       (self.timeWidget.stopTime.value()-self.timeWidget.startTime.value())*100)

        V, P = self.LCModel.getPopulationsData()

        self.tabPanel.plot2.plotPopulation.plot(self.LCModel.time, V, P)
        self.tabPanel.plot2.plotPhaze.plot(V, P, self.LCModel.initialCondition[0],
                                           self.LCModel.initialCondition[1],
                                           self.LCModel.X_f2[0],
                                           self.LCModel.X_f2[1],
                                           self.LCModel)


        self.OFModel = LV_OutsideFactorModel()
        self.OFModel.setInitialConditions(self.leftPanel.initNums.VNumber.value(),
                                          self.leftPanel.initNums.PNumber.value())
        self.OFModel.setParamsValues(r= self.leftPanel.fundParams.rSpinBox.value(),
                                     s= self.leftPanel.fundParams.sSpinBox.value(),
                                     a= self.leftPanel.fundParams.aSpinBox.value(),
                                     b= self.leftPanel.fundParams.bSpinBox.value(),
                                     K= self.leftPanel.limitCaption.CaptionLimitSpinBox.value(),
                                     g= self.leftPanel.outFactor.victimsFactor.value(),
                                     h= self.leftPanel.outFactor.predatorsFactor.value())

        self.OFModel.setSimulationTime(self.timeWidget.startTime.value(), self.timeWidget.stopTime.value(),
                                       (self.timeWidget.stopTime.value() - self.timeWidget.startTime.value()) * 100)

        V, P = self.OFModel.getPopulationsData()

        self.tabPanel.plot3.plotPopulation.plot(self.OFModel.time, V, P)
        self.tabPanel.plot3.plotPhaze.plot(V, P, self.OFModel.initialCondition[0],
                                           self.OFModel.initialCondition[1],
                                           self.OFModel.X_f2[0],
                                           self.OFModel.X_f2[1],
                                           self.OFModel)

