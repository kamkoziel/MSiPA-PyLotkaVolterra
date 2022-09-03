from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot
from gui.ParamsPanel import ParamsPanel
from gui.PlotsTabWidget import PlotsTabWidget
from gui.SetTimeWidget import SetTimeWidget

from calculations.LV_BasicModel import LV_BasicModel
from calculations.LV_LimitedCaptionModel import LV_LimitedCaptionModel
from calculations.LV_OutsideFactorModel import LV_OutsideFactorModel


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

        self.tabPanel = PlotsTabWidget()

        self.leftPanel = ParamsPanel()
        self.leftPanel.submit.clicked.connect(self.onClick)

        self.time_widget = SetTimeWidget()

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.tabPanel)
        v_layout.addWidget(self.time_widget)

        layout = QHBoxLayout(self)
        layout.addWidget(self.leftPanel)
        layout.addLayout(v_layout)

    @pyqtSlot()
    def onClick(self):
        self.basicModel = LV_BasicModel()
        self.basicModel.setInitialConditions(self.leftPanel.init_values.victims,
                                             self.leftPanel.init_values.predators)
        self.basicModel.setParamsValues(r=self.leftPanel.basic_params.r,
                                        s=self.leftPanel.basic_params.s,
                                        a=self.leftPanel.basic_params.a,
                                        b=self.leftPanel.basic_params.b)
        self.basicModel.setSimulationTime(self.time_widget.get_start_time(), self.time_widget.get_stop_time(),
                                          (self.time_widget.get_stop_time() - self.time_widget.get_start_time()) * 100)

        victims_model, predators_model = self.basicModel.getPopulationsData()

        self.tabPanel.basic_model_plot.plotPopulation.plot(self.basicModel.time, victims_model, predators_model)
        self.tabPanel.basic_model_plot.plotPhaze.plot(victims_model, predators_model,
                                                      self.basicModel.initialCondition[0],
                                                      self.basicModel.initialCondition[1],
                                                      self.basicModel.X_f1[0],
                                                      self.basicModel.X_f1[1],
                                                      self.basicModel)

        self.LCModel = LV_LimitedCaptionModel()
        self.LCModel.setInitialConditions(self.leftPanel.init_values.victims,
                                          self.leftPanel.init_values.predators)
        self.LCModel.setParamsValues(r=self.leftPanel.basic_params.r,
                                     s=self.leftPanel.basic_params.s,
                                     a=self.leftPanel.basic_params.a,
                                     b=self.leftPanel.basic_params.b,
                                     K=self.leftPanel.limited_params.CaptionLimitSpinBox.value())

        self.LCModel.setSimulationTime(self.time_widget.get_start_time(), self.time_widget.get_stop_time(),
                                       (self.time_widget.get_stop_time() - self.time_widget.get_start_time()) * 100)

        victims_model, predators_model = self.LCModel.getPopulationsData()

        self.tabPanel.limited_model_plot.plotPopulation.plot(self.LCModel.time, victims_model, predators_model)
        self.tabPanel.limited_model_plot.plotPhaze.plot(victims_model, predators_model, self.LCModel.initialCondition[0],
                                                        self.LCModel.initialCondition[1],
                                                        self.LCModel.X_f2[0],
                                                        self.LCModel.X_f2[1],
                                                        self.LCModel)

        self.OFModel = LV_OutsideFactorModel()
        self.OFModel.setInitialConditions(self.leftPanel.init_values.victims,
                                          self.leftPanel.init_values.predators)
        self.OFModel.setParamsValues(r=self.leftPanel.basic_params.r,
                                     s=self.leftPanel.basic_params.s,
                                     a=self.leftPanel.basic_params.a,
                                     b=self.leftPanel.basic_params.b,
                                     K=self.leftPanel.limited_params.CaptionLimitSpinBox.value(),
                                     g=self.leftPanel.outside_factor_params.victims_factor.value(),
                                     h=self.leftPanel.outside_factor_params.predators_factor.value())

        self.OFModel.setSimulationTime(self.time_widget.get_start_time(), self.time_widget.get_stop_time(),
                                       (self.time_widget.get_stop_time() - self.time_widget.get_start_time()) * 100)

        victims_model, predators_model = self.OFModel.getPopulationsData()

        self.tabPanel.factor_model_plot.plotPopulation.plot(self.OFModel.time, victims_model, predators_model)
        self.tabPanel.factor_model_plot.plotPhaze.plot(victims_model, predators_model, self.OFModel.initialCondition[0],
                                                       self.OFModel.initialCondition[1],
                                                       self.OFModel.X_f2[0],
                                                       self.OFModel.X_f2[1],
                                                       self.OFModel)
