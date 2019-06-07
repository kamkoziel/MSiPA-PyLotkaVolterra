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
        self.VNumber.setMaximum(1000)
        self.VNumber.setStyleSheet("background-color: #2d3847; color: white")
        self.PNumber = QSpinBox()
        self.PNumber.setValue(5)
        self.PNumber.setMaximum(1000)
        self.PNumber.setStyleSheet("background-color: #2d3847; color: white")

        #layout of own params gui elements
        self.initNumbersLayout = QVBoxLayout(self)
        self.initNumbersLayout.addWidget(QLabel(" Początkowa liczebność drapieżników "))
        self.initNumbersLayout.addWidget(self.PNumber)
        self.initNumbersLayout.addSpacing(20)
        self.initNumbersLayout.addWidget(QLabel(" Początkowa liczebność ofiar "))
        self.initNumbersLayout.addWidget(self.VNumber)