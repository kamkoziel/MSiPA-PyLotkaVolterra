from PyQt5.QtWidgets import QSpinBox, QLabel, QDoubleSpinBox
from PyQt5.QtWidgets import QWidget, QVBoxLayout

"""
    Class responsible for a own modifications gui elements 
    in left panel main widget
"""


class BasicParams(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self):

        #TODO ewentualnie nazwy pol _spinBox do zmiany
        self.labela = QLabel("Rozrodczosc ofiar - r", self)
        self.rSpinBox = QDoubleSpinBox()
        self.rSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.rSpinBox.setValue(2)
        self.rSpinBox.stepBy(0.1)

        self.labelb = QLabel("Śmiertelność ofiar (skuteczność polowań) - a", self)
        self.aSpinBox = QDoubleSpinBox()
        self.aSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.aSpinBox.setValue(0.5)
        self.aSpinBox.stepBy(0.1)

        self.labelc = QLabel("Śmiertelność drapiezników - s", self)
        self.sSpinBox = QDoubleSpinBox()
        self.sSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.sSpinBox.setValue(0.3)
        self.sSpinBox.stepBy(0.1)

        self.labeld = QLabel("Część upolowanych ofiar \nprzeznaczona na reprodukcję rapieżników - b", self)
        self.bSpinBox = QDoubleSpinBox()
        self.bSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.bSpinBox.setValue(0.8)
        self.bSpinBox.stepBy(0.1)

        self.basicModelParamsLayout = QVBoxLayout(self)
        self.basicModelParamsLayout.addWidget(self.labela)
        self.basicModelParamsLayout.addWidget(self.rSpinBox)
        self.basicModelParamsLayout.addSpacing(20)
        self.basicModelParamsLayout.addWidget(self.labelb)
        self.basicModelParamsLayout.addWidget(self.aSpinBox)
        self.basicModelParamsLayout.addSpacing(20)
        self.basicModelParamsLayout.addWidget(self.labelc)
        self.basicModelParamsLayout.addWidget(self.sSpinBox)
        self.basicModelParamsLayout.addSpacing(20)
        self.basicModelParamsLayout.addWidget(self.labeld)
        self.basicModelParamsLayout.addWidget(self.bSpinBox)
