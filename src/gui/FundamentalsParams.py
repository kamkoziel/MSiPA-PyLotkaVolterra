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
        #elements declarations
        self.victimNumber = QSpinBox()
        self.victimNumber.setValue(0)
        self.victimNumber.setStyleSheet("background-color: #2d3847; color: white")
        self.predatorsNumber = QSpinBox()
        self.predatorsNumber.setValue(0)
        self.predatorsNumber.setStyleSheet("background-color: #2d3847; color: white")

        #layout of own params gui elements
        ownParamsGroupVWidget = QVBoxLayout(self)
        ownParamsGroupVWidget.addWidget(QLabel(" Początkowa liczebność drapieżników "))
        ownParamsGroupVWidget.addWidget(self.predatorsNumber)
        ownParamsGroupVWidget.addSpacing(20)
        ownParamsGroupVWidget.addWidget(QLabel(" Początkowa liczebność ofiar "))
        ownParamsGroupVWidget.addWidget(self.victimNumber)