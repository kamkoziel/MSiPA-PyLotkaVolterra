from PyQt5.QtWidgets import QSpinBox, QLabel, QPushButton
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from src.gui.InitNumberSpinBoxes import InitNumberSpinBoxes
from src.gui.BasicParams import BasicParams
from src.gui.CaptionLimit import CaptionLimitWidget
from src.gui.OutsideFactorParamsWidget import OutsideFactorParamsWidget
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
        self.fundParams = BasicParams()
        self.limitCaption = CaptionLimitWidget()
        self.outFactor = OutsideFactorParamsWidget()
        self.mainButton = QPushButton("Wykonaj")
        self.mainButton.resize(150, 100)
        self.mainButton.setStyleSheet("background-color: #2d3847; color: white;")

        leftPanVlay = QVBoxLayout(self)
        leftPanVlay.setContentsMargins(10, 10, 10, 20)
        leftPanVlay.addWidget(self.initNums)
        leftPanVlay.addWidget(self.fundParams)
        leftPanVlay.addWidget(self.limitCaption)
        leftPanVlay.addWidget(self.outFactor)
        leftPanVlay.addWidget(self.mainButton)
