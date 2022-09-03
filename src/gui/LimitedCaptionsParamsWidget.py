from PyQt5.QtWidgets import QSpinBox, QLabel, QWidget, QVBoxLayout


class LimitedCaptionsParamsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 100
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self):
        # elements declarations
        self.CaptionLimitSpinBox = QSpinBox()
        self.CaptionLimitSpinBox.setValue(100)
        self.CaptionLimitSpinBox.setMaximum(1000)
        self.CaptionLimitSpinBox.setStyleSheet("background-color: #2d3847; color: white")

        # layout of own params gui elements
        self.__layout = QVBoxLayout(self)
        self.__layout.addWidget(QLabel(" Pojemność środowiska "))
        self.__layout.addWidget(self.CaptionLimitSpinBox)


    @property
    def layout(self) -> 'QLayout':
        return self.__layout
