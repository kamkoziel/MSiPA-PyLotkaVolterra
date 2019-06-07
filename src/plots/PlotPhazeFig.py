from PyQt5.QtWidgets import QSizePolicy

from src.plots.plotCanvas import PlotCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from src.calculations.LV_Model import LV_Model
from src.calculations.LV_BasicModel import LV_BasicModel

import numpy as np

class PlotPhazeFig(PlotCanvas):

    def __init__(self, parent=None, width=5, height=3, dpi=100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)



    def plot(self, V, P, V0=10, P0=5, PS1 =0, PS2=0, modelLV: LV_Model = LV_BasicModel()):
        self.figure.clear()

        if len(self.figure.get_axes()) != 0:
            self.figure.delaxes()

        self.ax = self.figure.add_subplot(111)
        self.ax.plot(V, P,'g-' , label='X0=(%.f, %.f)' % (V0, P0))
        self.ax.plot(V0, P0, 'b.')
        self.ax.plot(PS1, PS2, 'r*')

        ymax = self.ax.set_ylim(bottom=0)[1] # get axis limits
        xmax = self.ax.set_xlim(left=0)[1]
        nb_points = 25

        x = np.linspace(0, xmax, nb_points)
        y = np.linspace(0, ymax, nb_points)

        X1, Y1 = np.meshgrid(x, y)  # create a grid
        DX1, DY1 = modelLV.dX_dt([X1, Y1])  # compute growth rate on the gridt
        M = (np.hypot(DX1, DY1))  # Norm of the growth rate
        M[M == 0] = 1.  # Avoid zero division errors
        DX1 /= M  # Normalize each arrows
        DY1 /= M

        self.ax.set_title('Wykres fazowy  i trajektorie')
        self.ax.quiver(X1, Y1, DX1, DY1, M, pivot='mid')
        self.ax.set_xlabel('Liczebność ofiar')
        self.ax.set_ylabel('Liczebność drapieżników')
        self.ax.legend(loc='upper right')
        self.ax.grid()

        self.draw()

    def AddDataToFig(self, dataY = 10,dataX = 10, label = "label" ):

        if len(self.figure.get_axes()) > 0:
            cx = self.figure.get_axes()
            cx[0].plot(dataY,dataX,'g*', label=label)
            self.draw()
