
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QHBoxLayout, QWidget
from src.plots.plotCanvas import PlotCanvas
from src.plots.plotPopulationEvolution import PlotPopulationEvolution
from src.plots.PlotPhazeFig import PlotPhazeFig


class tabWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.plotPopulation = PlotPopulationEvolution()
        self.plotPhaze = PlotPhazeFig()

        self.tabLay = QHBoxLayout(self)
        self.tabLay.addWidget(self.plotPopulation)
        self.tabLay.addWidget(self.plotPhaze)
