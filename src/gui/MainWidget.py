from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QGroupBox
from PyQt5.QtWidgets import QSpinBox, QLabel, QPushButton, QStackedWidget
from plots.plotCanvas import *
from gui.ownModGui import ownModGuiElements
from gui.initialNumberGuiElements import initialNumber
from lvModel.ParamsCalc import LVmodel
from PyQt5.QtCore import pyqtSlot

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

        self.labela = QLabel("Rozrodczosc ofiar - a", self)
        self.aSpinBox = QSpinBox()
        self.aSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.aSpinBox.setValue(1)

        self.labelb = QLabel("Śmiertelność ofiar - b", self)
        self.bSpinBox = QSpinBox()
        self.bSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.bSpinBox.setValue(2)

        self.labelc = QLabel("Śmiertelność drapiezników - c", self)
        self.cSpinBox = QSpinBox()
        self.cSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.cSpinBox.setValue(3)

        self.labeld = QLabel("Śmiertelność ofiar - d", self)
        self.dSpinBox = QSpinBox()
        self.dSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.dSpinBox.setValue(1)

        self.makeModelButton = QPushButton("&Wykonaj")
        self.makeModelButton.resize(150, 60)
        self.makeModelButton.setStyleSheet("background-color: #2d3847; color: white;")

        self.m = PlotCanvas(self, width=5, height=4)
        self.m.move(0, 0)

        fundamentalParamsLV = QVBoxLayout()
        fundamentalParamsLV.setContentsMargins(20, 10, 10, 20)
        fundamentalParamsLV.addWidget(self.labela)
        fundamentalParamsLV.addWidget(self.aSpinBox)
        fundamentalParamsLV.addSpacing(20)
        fundamentalParamsLV.addWidget(self.labelb)
        fundamentalParamsLV.addWidget(self.bSpinBox)
        fundamentalParamsLV.addSpacing(20)
        fundamentalParamsLV.addWidget(self.labelc)
        fundamentalParamsLV.addWidget(self.cSpinBox)
        fundamentalParamsLV.addSpacing(20)
        fundamentalParamsLV.addWidget(self.labeld)
        fundamentalParamsLV.addWidget(self.dSpinBox)
        fundamentalParamsLV.addStretch(1)

        firstGroup = QGroupBox(" Parametry podstawowe ")
        firstGroup.setMaximumHeight(300)
        firstGroup.setMaximumWidth(self.leftPanelWidth)
        firstGroup.setLayout(fundamentalParamsLV)

        self.ownParamsGUIElements = ownModGuiElements()
        self.initialNumber = initialNumber()

        # self.makeModelButton.clicked.connect(self.onClick())

        self.ownModWidget = QStackedWidget()
        self.ownModWidget.addWidget(self.ownParamsGUIElements)
        self.initialNumberWidget = QStackedWidget()
        self.initialNumberWidget.addWidget(self.initialNumber)

        ownParamsVLayot = QVBoxLayout()
        ownParamsVLayot.addWidget(self.ownModWidget)
        initialNumberVLayot = QVBoxLayout()
        initialNumberVLayot.addWidget(self.initialNumberWidget)

        ownParamsGroup = QGroupBox(" Parametry modyfikacji ")
        ownParamsGroup.setMaximumHeight(200)
        ownParamsGroup.setMaximumWidth(self.leftPanelWidth)
        ownParamsGroup.setLayout(ownParamsVLayot)

        initialNumberGroup = QGroupBox(" Liczebność początkowa ")
        initialNumberGroup.setMaximumHeight(200)
        initialNumberGroup.setMaximumWidth(self.leftPanelWidth)
        initialNumberGroup.setLayout(initialNumberVLayot)

        leftPanel = QVBoxLayout()
        leftPanel.addWidget(initialNumberGroup)
        leftPanel.addWidget(firstGroup)
        leftPanel.addWidget(ownParamsGroup)
        leftPanel.addSpacing(200)
        leftPanel.addWidget(self.makeModelButton)

        mainLayout = QHBoxLayout(self)
        mainLayout.addLayout(leftPanel)
        mainLayout.addWidget(self.m)

        self.makeModelButton.clicked.connect(self.onClick)

    @pyqtSlot()
    def onClick(self):
        self.modelLV = LVmodel(self.initialNumber.victimNumber.value(), self.initialNumber.predatorsNumber.value())
        self.modelLV.setFundamParams(self.aSpinBox.value())
        print(self.modelLV.victimsReproduc)