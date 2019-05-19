from PyQt5.QtWidgets import QSizePolicy

from src.plots.plotCanvas import PlotCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotPopulationEvolution(PlotCanvas):

    def __init__(self, parent=None, width=5, height=3, dpi=100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)

    def plot(self, time, V, P):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(time, V, 'b-', label='Victims')
        ax.plot(time, P, 'r-', label='Predators')
        ax.grid()
        ax.legend(loc='upper right')
        ax.set_xlabel("Time")
        ax.set_ylabel('Population')
        ax.set_title('PyQt Matplotlib Example')

        self.draw()