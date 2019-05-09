
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QHBoxLayout, QWidget
from src.plots.plotCanvas import PlotCanvas
from src.plots.plotPopulationEvolution import PlotPopulationEvolution



class tabWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.plot2 = PlotPopulationEvolution()
        self.plot22 = PlotPopulationEvolution()

        self.tabLay = QHBoxLayout(self)
        self.tabLay.addWidget(self.plot2)
        self.tabLay.addWidget(self.plot22)
