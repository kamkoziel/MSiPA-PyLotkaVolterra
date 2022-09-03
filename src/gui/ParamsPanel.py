from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QPushButton
from gui.InitNumberWidget import InitNumberWidget
from gui.BasicParamsWidget import BasicParamsWidget
from gui.LimitedCaptionsParamsWidget import LimitedCaptionsParamsWidget
from gui.OutsideFactorParamsWidget import OutsideFactorParamsWidget




class ParamsPanel(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 700
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self):
        self.init_values = InitNumberWidget()
        init_values_group = QGroupBox()
        init_values_group.setLayout(self.init_values.layout)
        init_values_group.setTitle("Waruki początkowe")

        self.basic_params = BasicParamsWidget()
        basic_params_group = QGroupBox()
        basic_params_group.setLayout(self.basic_params.layout)
        basic_params_group.setTitle("Parametry modelu podstawowego")

        self.limited_params = LimitedCaptionsParamsWidget()
        limited_params_group = QGroupBox()
        limited_params_group.setLayout(self.limited_params.layout)
        limited_params_group.setTitle("Parametry modelu ograniczonej pojemności środowiska")

        self.outside_factor_params = OutsideFactorParamsWidget()
        outside_factor_params_group = QGroupBox()
        outside_factor_params_group.setLayout(self.outside_factor_params.layout)
        outside_factor_params_group.setTitle("Parametry modelu własnego - z czynnikiem zewnętrznym")

        self.submit = QPushButton("Wykonaj")
        self.submit.resize(150, 100)
        self.submit.setStyleSheet("background-color: #2d3847; color: white;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 20)
        layout.addWidget(init_values_group)
        layout.addWidget(basic_params_group)
        layout.addWidget(limited_params_group)
        layout.addWidget(outside_factor_params_group)
        layout.addSpacing(80)
        layout.addWidget(self.submit)
