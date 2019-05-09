from PyQt5.QtWidgets import QSizePolicy

from src.plots.plotCanvas import PlotCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotPopulationEvolution(PlotCanvas):

    def __init__(self, parent=None, width=5, height=3, dpi=100, victims = [10,100,100], predators = [20,200,200], time = [1,2,3] ):

        self.time = time
        self.victims = victims
        self.predators = predators

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.plot()



    def plot(self):
        ax = self.figure.add_subplot(111)
        ax.plot(self.time, self.victims, 'r-', label='Victims')
        ax.plot(self.time, self.predators, 'r-', label='Predators')
        ax.grid()
        ax.legend(loc='best')
        ax.set_xlabel("Time")
        ax.set_ylabel('Population')
        ax.set_title('PyQt Matplotlib Example')

        self.draw()
