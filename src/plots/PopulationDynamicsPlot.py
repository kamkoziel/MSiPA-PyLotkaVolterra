from PyQt5.QtWidgets import QSizePolicy

from .PlotCanvas import PlotCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PopulationDynamicsPlot(PlotCanvas):

    def __init__(self, parent=None, width=5, height=3, dpi=100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)

    def plot(self, time, V, P):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(time, V, 'b-', label='Ofiary')
        ax.plot(time, P, 'r-', label='Drapieżniki')
        ax.grid()
        ax.legend(loc='upper right')
        ax.set_xlabel("Czas")
        ax.set_ylabel('Liczebność populacji')
        ax.set_title('Liczebność populacji modelu Lotki - Voltery')

        self.draw()

    def AddDataToFig(self, dataY = 10,dataX = 10, label = "label" ):

        if len(self.figure.get_axes()) > 0:
            cx = self.figure.get_axes()
            cx[0].plot(dataY,dataX,'g*', label=label)
            self.draw()