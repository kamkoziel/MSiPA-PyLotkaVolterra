from PyQt5.QtWidgets import QSpinBox, QLabel, QPushButton
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox
from src.gui.InitNumberWidget import InitNumberSpinBoxes
from src.gui.BasicModelParamsWidget import BasicParams
from src.gui.LimitCaptionModelParamsWidget import CaptionLimitWidget
from src.gui.OutsideFactorModelParamsWidget import OutsideFactorParamsWidget
"""
    Class responsible for a own modifications gui elements 
    in left panel main widget
"""


class LeftPanel(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 700
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self):

        self.initNums = InitNumberSpinBoxes()
        initNumsGroup = QGroupBox()
        initNumsGroup.setLayout(self.initNums.initNumbersLayout)
        initNumsGroup.setTitle("Waruki początkowe")

        self.fundParams = BasicParams()
        basicParamsGroup = QGroupBox()
        basicParamsGroup.setLayout(self.fundParams.basicModelParamsLayout)
        basicParamsGroup.setTitle("Parametry modelu podstawowego")

        self.limitCaption = CaptionLimitWidget()
        limitedCaptionGroup = QGroupBox()
        limitedCaptionGroup.setLayout(self.limitCaption.initNumVLay)
        limitedCaptionGroup.setTitle("Parametry modelu ograniczonej pojemności środowiska")

        self.outFactor = OutsideFactorParamsWidget()
        outFactorGroup = QGroupBox()
        outFactorGroup.setLayout(self.outFactor.initNumVLay)
        outFactorGroup.setTitle("Parametry modelu własnego - z czynnikiem zewnętrznym")

        self.mainButton = QPushButton("Wykonaj")
        self.mainButton.resize(150, 100)
        self.mainButton.setStyleSheet("background-color: #2d3847; color: white;")

        leftPanVlay = QVBoxLayout(self)
        leftPanVlay.setContentsMargins(10, 10, 10, 20)
        leftPanVlay.addWidget(initNumsGroup)
        leftPanVlay.addWidget(basicParamsGroup)
        leftPanVlay.addWidget(limitedCaptionGroup)
        leftPanVlay.addWidget(outFactorGroup)
        leftPanVlay.addSpacing(80)
        leftPanVlay.addWidget(self.mainButton)
