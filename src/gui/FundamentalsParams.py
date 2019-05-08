from PyQt5.QtWidgets import QSpinBox, QLabel
from PyQt5.QtWidgets import QWidget, QVBoxLayout

"""
    Class responsible for a own modifications gui elements 
    in left panel main widget
"""


class FundamentalParams(QWidget):
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
        self.rSpinBox = QSpinBox()
        self.rSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.rSpinBox.setValue(1)

        self.labelb = QLabel("Śmiertelność ofiar (skuteczność polowań) - a", self)
        self.aSpinBox = QSpinBox()
        self.aSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.aSpinBox.setValue(2)

        self.labelc = QLabel("Śmiertelność drapiezników - s", self)
        self.sSpinBox = QSpinBox()
        self.sSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.sSpinBox.setValue(3)

        self.labeld = QLabel("Część upolowanych ofiar \nprzeznaczona na reprodukcję rapieżników - b", self)
        self.bSpinBox = QSpinBox()
        self.bSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.bSpinBox.setValue(1)

        fundamentalParamsLV = QVBoxLayout(self)
        fundamentalParamsLV.addWidget(self.labela)
        fundamentalParamsLV.addWidget(self.rSpinBox)
        fundamentalParamsLV.addSpacing(20)
        fundamentalParamsLV.addWidget(self.labelb)
        fundamentalParamsLV.addWidget(self.aSpinBox)
        fundamentalParamsLV.addSpacing(20)
        fundamentalParamsLV.addWidget(self.labelc)
        fundamentalParamsLV.addWidget(self.sSpinBox)
        fundamentalParamsLV.addSpacing(20)
        fundamentalParamsLV.addWidget(self.labeld)
        fundamentalParamsLV.addWidget(self.bSpinBox)
        fundamentalParamsLV.addStretch(1)