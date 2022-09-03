from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpinBox, QLabel


class InitNumberWidget(QWidget):
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
        self.__victims_amount = QSpinBox()
        self.__victims_amount.setValue(10)
        self.__victims_amount.setMaximum(1000)
        self.__victims_amount.setStyleSheet("background-color: #2d3847; color: white")
        self.__predators_amount = QSpinBox()
        self.__predators_amount.setValue(5)
        self.__predators_amount.setMaximum(1000)
        self.__predators_amount.setStyleSheet("background-color: #2d3847; color: white")

        # layout of own params gui elements
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel(" Początkowa liczebność drapieżników "))
        self.layout.addWidget(self.__predators_amount)
        self.layout.addSpacing(20)
        self.layout.addWidget(QLabel(" Początkowa liczebność ofiar "))
        self.layout.addWidget(self.__victims_amount)

    @property
    def victims(self):
        return self.__victims_amount.value()

    @property
    def predators(self):
        return self.__predators_amount.value()
