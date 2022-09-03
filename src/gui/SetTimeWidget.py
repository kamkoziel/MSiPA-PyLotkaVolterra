from PyQt5.QtWidgets import QSpinBox, QLabel, QWidget, QHBoxLayout, QVBoxLayout


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
        self.__start_time = QSpinBox()
        self.__start_time.setValue(0)
        self.__start_time.setFixedSize(250, 30)
        self.__start_time.setMinimum(0)
        self.__start_time.setStyleSheet("background-color: #2d3847; color: white")
        self.__stop_time = QSpinBox()
        self.__stop_time.setValue(50)
        self.__stop_time.setMaximum(1000)
        self.__stop_time.setFixedSize(250, 30)
        self.__stop_time.setStyleSheet("background-color: #2d3847; color: white")

        # layout of own params gui elements
        __h_layout = QHBoxLayout()
        __h_layout.addWidget(QLabel("Start symulacji [t(0)]:  "))
        __h_layout.addWidget(self.__start_time)
        __h_layout.addWidget(QLabel("Stop symulacji  [t(n)]:  "))
        __h_layout.addWidget(self.__stop_time)

        __layout = QVBoxLayout(self)
        __layout.addWidget(QLabel("Czas symulacji "))
        __layout.addSpacing(30)
        __layout.addLayout(__h_layout)

    def get_stop_time(self):
        return self.__stop_time.value()

    def get_start_time(self):
        return self.__start_time.value()
