from PyQt5.QtWidgets import QSpinBox, QLabel
from PyQt5.QtWidgets import QWidget, QVBoxLayout

"""
    Class responsible for a own modifications gui elements 
    in left panel main widget
    
    params:
        @VNumber - (QtWidget.QSpinBox) number of victim on begin
        @PNumber - (QtWidget.QSpinBox) number of predators on begin
    
"""


class InitNumberSpinBoxes(QWidget):
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
        self.VNumber = QSpinBox()
        self.VNumber.setValue(10)
        self.VNumber.setStyleSheet("background-color: #2d3847; color: white")
        self.PNumber = QSpinBox()
        self.PNumber.setValue(5)
        self.PNumber.setStyleSheet("background-color: #2d3847; color: white")

        #layout of own params gui elements
        initNumVLay = QVBoxLayout(self)
        initNumVLay.addWidget(QLabel(" Początkowa liczebność drapieżników "))
        initNumVLay.addWidget(self.PNumber)
        initNumVLay.addSpacing(20)
        initNumVLay.addWidget(QLabel(" Początkowa liczebność ofiar "))
        initNumVLay.addWidget(self.VNumber)