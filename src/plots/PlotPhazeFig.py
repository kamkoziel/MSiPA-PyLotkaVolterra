from PyQt5.QtWidgets import QSizePolicy

from src.plots.plotCanvas import PlotCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np


class PlotPhazeFig(PlotCanvas):

    def __init__(self, parent=None, width=5, height=3, dpi=100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)


    def plot(self, V, P, V0=10, P0=5):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.plot(V, P, lw=3.5, label='X0=(%.f, %.f)' % (V0, P0))
        # ax.plot(X0[0], X0[1], 'b.')
        # ax.plot(self.X_f1[0], self.X_f1[1], 'r.')

        # ymax = ax.ylim(ymin=0)[1]  # get axis limits
        # xmax = ax.xlim(xmin=0)[1]
        # nb_points = 30
        #
        # x = np.linspace(0, xmax, nb_points)
        # y = np.linspace(0, ymax, nb_points)
        #
        # X1, Y1 = ax.meshgrid(x, y)  # create a grid
        # DX1, DY1 = self.dX_dt([X1, Y1])  # compute growth rate on the gridt
        # M = (ax.hypot(DX1, DY1))  # Norm of the growth rate
        # M[M == 0] = 1.  # Avoid zero division errors
        # DX1 /= M  # Normalize each arrows
        # DY1 /= M

        ax.set_title('Trajectories and direction fields')
        #ax.quiver(X1, Y1, DX1, DY1, M, pivot='mid')
        ax.set_xlabel('Number of rabbits')
        ax.set_ylabel('Number of foxes')
        ax.legend(loc='upper right')
        ax.grid()
        # ax.xlim(0, xmax)
        # ax.ylim(0, ymax)

        self.draw()