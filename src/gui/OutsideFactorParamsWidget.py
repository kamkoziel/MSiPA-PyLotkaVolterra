from PyQt5.QtWidgets import QDoubleSpinBox, QLabel, QWidget, QVBoxLayout


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
        self.victims_factor = QDoubleSpinBox()
        self.victims_factor.setValue(4)
        self.victims_factor.setMaximum(100)
        self.victims_factor.setMinimum(-100)
        self.victims_factor.setStyleSheet("background-color: #2d3847; color: white")
        self.predators_factor = QDoubleSpinBox()
        self.predators_factor.setValue(-1)
        self.predators_factor.setMaximum(100)
        self.predators_factor.setMinimum(-100)
        self.predators_factor.setStyleSheet("background-color: #2d3847; color: white")

        # layout of own params gui elements
        self._layout = QVBoxLayout(self)
        self._layout.addWidget(QLabel(" wpływ zew. na ofiary "))
        self._layout.addWidget(self.victims_factor)
        self._layout.addSpacing(20)
        self._layout.addWidget(QLabel(" wpływ zew. na drapieżniki "))
        self._layout.addWidget(self.predators_factor)

    @property
    def layout(self) -> 'QLayout':
        return self._layout

