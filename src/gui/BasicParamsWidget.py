from PyQt5.QtWidgets import QLabel, QDoubleSpinBox, QWidget, QVBoxLayout


class BasicParamsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self):
        self.__rSpinBox = QDoubleSpinBox()
        self.__rSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.__rSpinBox.setValue(0.30)
        self.__rSpinBox.setMinimum(0.001)
        self.__rSpinBox.setMaximum(10)
        self.__rSpinBox.setDecimals(3)

        self.__aSpinBox = QDoubleSpinBox()
        self.__aSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.__aSpinBox.setValue(0.008)
        self.__aSpinBox.setSingleStep(0.001)
        self.__aSpinBox.setMinimum(0.001)
        self.__aSpinBox.setDecimals(3)

        self.__sSpinBox = QDoubleSpinBox()
        self.__sSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.__sSpinBox.setValue(0.01)
        self.__sSpinBox.setSingleStep(0.001)
        self.__sSpinBox.setMinimum(0.001)
        self.__sSpinBox.setDecimals(3)

        self.__bSpinBox = QDoubleSpinBox()
        self.__bSpinBox.setStyleSheet("background-color: #2d3847; color: white")
        self.__bSpinBox.setValue(0.300)
        self.__bSpinBox.setSingleStep(0.001)
        self.__bSpinBox.setMinimum(0.001)
        self.__bSpinBox.setDecimals(3)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("Rozrodczosc ofiar - r", self))
        self.layout.addWidget(self.__rSpinBox)
        self.layout.addSpacing(20)
        self.layout.addWidget(QLabel("Śmiertelność ofiar (skuteczność polowań) - a", self))
        self.layout.addWidget(self.__aSpinBox)
        self.layout.addSpacing(20)
        self.layout.addWidget(QLabel("Śmiertelność drapiezników - s", self))
        self.layout.addWidget(self.__sSpinBox)
        self.layout.addSpacing(20)
        self.layout.addWidget(QLabel("Część upolowanych ofiar \nprzeznaczona na reprodukcję rapieżników - b", self))
        self.layout.addWidget(self.__bSpinBox)

    @property
    def a(self):
        return self.__aSpinBox.value()

    @property
    def b(self):
        return self.__bSpinBox.value()

    @property
    def s(self):
        return self.__sSpinBox.value()

    @property
    def r(self):
        return self.__rSpinBox.value()
