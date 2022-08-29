from PyQt5.QtWidgets import QSpinBox, QLabel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

class SetTimeWidget(QWidget):
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
        self.startTime = QSpinBox()
        self.startTime.setValue(0)
        self.startTime.setFixedSize(250,30)
        self.startTime.setMinimum(0)
        self.startTime.setStyleSheet("background-color: #2d3847; color: white")
        self.stopTime = QSpinBox()
        self.stopTime.setValue(50)
        self.stopTime.setMaximum(1000)
        self.stopTime.setFixedSize(250,30)
        self.stopTime.setStyleSheet("background-color: #2d3847; color: white")

        # layout of own params gui elements
        HLayout = QHBoxLayout()
        HLayout.addWidget(QLabel("Start symulacji [t(0)]:  "))
        HLayout.addWidget(self.startTime)
        HLayout.addWidget(QLabel("Stop symulacji  [t(n)]:  "))
        HLayout.addWidget(self.stopTime)

        VLayout = QVBoxLayout(self)
        VLayout.addWidget(QLabel("Czas symulacji "))
        VLayout.addSpacing(30)
        VLayout.addLayout(HLayout)
