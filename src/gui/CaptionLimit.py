from PyQt5.QtWidgets import QSpinBox, QLabel
from PyQt5.QtWidgets import QWidget, QVBoxLayout

"""
    class InitNumberSpinBoxes(QWidget)  

    Class responsible for a own modifications gui elements 
    in left panel main widget

    @params:
        #.VNumber - (QtWidget.QSpinBox) number of victim on begin
        #.@PNumber - (QtWidget.QSpinBox) number of predators on begin

"""


class CaptionLimitWidget(QWidget):
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
        self.CaptionLimitSpinBox = QSpinBox()
        self.CaptionLimitSpinBox.setValue(100)
        self.CaptionLimitSpinBox.setMaximum(1000)
        self.CaptionLimitSpinBox.setStyleSheet("background-color: #2d3847; color: white")

        # layout of own params gui elements
        initNumVLay = QVBoxLayout(self)
        initNumVLay.addWidget(QLabel(" Pojemność środowiska "))
        initNumVLay.addWidget(self.CaptionLimitSpinBox)
        initNumVLay.addSpacing(20)
