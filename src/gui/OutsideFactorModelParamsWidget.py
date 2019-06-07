from PyQt5.QtWidgets import QDoubleSpinBox, QLabel
from PyQt5.QtWidgets import QWidget, QVBoxLayout

"""
    class InitNumberSpinBoxes(QWidget)  

    Class responsible for a own modifications gui elements 
    in left panel main widget

    @params:
        #.VNumber - (QtWidget.QSpinBox) number of victim on begin
        #.@PNumber - (QtWidget.QSpinBox) number of predators on begin

"""


class OutsideFactorParamsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self):
        # elements declarations
        self.victimsFactor = QDoubleSpinBox()
        self.victimsFactor.setValue(4)
        self.victimsFactor.setMaximum(100)
        self.victimsFactor.setMinimum(-100)
        self.victimsFactor.setStyleSheet("background-color: #2d3847; color: white")
        self.predatorsFactor = QDoubleSpinBox()
        self.predatorsFactor.setValue(-1)
        self.predatorsFactor.setMaximum(100)
        self.predatorsFactor.setMinimum(-100)
        self.predatorsFactor.setStyleSheet("background-color: #2d3847; color: white")

        # layout of own params gui elements
        self.initNumVLay = QVBoxLayout(self)
        self.initNumVLay.addWidget(QLabel(" wpływ zew. na ofiary "))
        self.initNumVLay.addWidget(self.victimsFactor)
        self.initNumVLay.addSpacing(20)
        self.initNumVLay.addWidget(QLabel(" wpływ zew. na drapieżniki "))
        self.initNumVLay.addWidget(self.predatorsFactor)


