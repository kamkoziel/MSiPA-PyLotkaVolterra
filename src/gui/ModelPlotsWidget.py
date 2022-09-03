from PyQt5.QtWidgets import QHBoxLayout, QWidget
from plots.plotPopulationEvolution import PlotPopulationEvolution
from plots.PlotPhazeFig import PlotPhazeFig


class ModelPlotsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.plotPopulation = PlotPopulationEvolution()
        self.plotPhaze = PlotPhazeFig()

        self.tabLay = QHBoxLayout(self)
        self.tabLay.addWidget(self.plotPopulation)
        self.tabLay.addWidget(self.plotPhaze)
