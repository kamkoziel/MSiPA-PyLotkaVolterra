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

        #TODO nie spojne nazyw pól z nazwami parametór równanie- popraw
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

        fundamentalParamsLV = QVBoxLayout(self)
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