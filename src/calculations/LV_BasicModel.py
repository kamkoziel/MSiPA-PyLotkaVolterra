import numpy as np
from scipy.integrate.odepack import odeint
from src.calculations.LV_Model import LV_Model
import pylab as p



class LV_BasicModel(LV_Model):
    #initialCondition: np.ndarray

    def __init__(self, **kwargs):
        super().__init__()

        # self.r  # victims reproduce                               a
        # self.s  # predators death                                 c
        # self.a  # hunting efficiency                              b
        # self.b  # part of huntedVictims for predatorReproduce     d

        if ('r' and 's' and 'a' and 'b') in kwargs:
            self.r = kwargs['r']
            self.a = kwargs['a']
            self.b = kwargs['b']
            self.s = kwargs['s']
        else:
            self.r = 2
            self.s = 0.01
            self.a = 0.08
            self.b = 0.1

        self.time = np.linspace(0, 1000, 100)
        self.initialCondition = np.array([10, 5])
        # stability points where right side of expr is equal 0
        self.X_f0 = np.array([0., 0.])
        self.X_f1 = np.array([self.s / (self.b * self.a), self.r / self.a])

    def setParamsValues(self, **kwargs):
        self.r = kwargs['r']
        self.s = kwargs['s']
        self.a = kwargs['a']
        self.b = kwargs['b']
        self.X_f1 = np.array([self.s / (self.b * self.a), self.r / self.a])

    def updateStabilityPoints(self,**kwargs):
        self.setParamsValues(r=kwargs['r'],s=kwargs['s'],a=kwargs['a'],b=kwargs['b'])
        self.X_f1 = np.array([self.s / (self.b * self.a), self.r / self.a])

    def dX_dt(self, X, t=0):
        # return np.array([self.a * X[0] - self.b * X[0] * X[1],
        #              -self.c * X[1] + self.e * self.a * X[0] * X[1]])
        return np.array([self.r * X[0] - self.a * X[0] * X[1],
                    -self.s * X[1] + self.b * self.a * X[0] * X[1]])

    def d2X_dt2(self, X, t=0):
        """ Return the Jacobian matrix evaluated in X. """
        return np.array([[self.r - self.a * X[1], - self.a * X[0]],
                      [self.a * self.b * X[1], -self.s + self.a * self.b * X[0]]])

    def createSimulation(self):
        X, infodict = odeint(self.dX_dt, self.initialCondition, self.time, full_output=True)
        return X

    def getPopulationsData(self):
        X = self.createSimulation()
        victims, predators = X.T
        return victims, predators

    def exportFigToPNG(self,fileName: str):
        X = self.createSimulation()
        rabbits, foxes = X.T
        f1 = p.figure()
        p.plot(self.time, rabbits, 'r-', label='Rabbits')
        p.plot(self.time, foxes, 'b-', label='Foxes')
        p.grid()
        p.legend(loc='best')
        p.xlabel('time')
        p.ylabel('population')
        p.title('Evolution of fox and rabbit populations')
        f1.savefig(fileName)

    def exportTrajectoriesFigToPNG(self, filename: str):
        f2 = p.figure()

        X0 = self.X_f1  # starting point
        X = odeint(self.dX_dt, self.initialCondition , self.time)  # we don't need infodict here
        p.plot(X[:, 0], X[:, 1], lw=3.5, label='X0=(%.f, %.f)' % (self.initialCondition[0], self.initialCondition[1]))
        p.plot(X0[0],X0[1],'b.')
        p.plot(self.X_f1[0], self.X_f1[1], 'r.')

        # -------------------------------------------------------
        # define a grid and compute direction at each point
        ymax = p.ylim(ymin=0)[1]  # get axis limits
        xmax = p.xlim(xmin=0)[1]
        nb_points = 30

        x = np.linspace(0, xmax, nb_points)
        y = np.linspace(0, ymax, nb_points)

        X1, Y1 = p.meshgrid(x, y)  # create a grid
        DX1, DY1 = self.dX_dt([X1, Y1])  # compute growth rate on the gridt
        M = (p.hypot(DX1, DY1))  # Norm of the growth rate
        M[M == 0] = 1.  # Avoid zero division errors
        DX1 /= M  # Normalize each arrows
        DY1 /= M

        p.title('Trajectories and direction fields')
        p.quiver(X1, Y1, DX1, DY1, M, pivot='mid')
        p.xlabel('Number of rabbits')
        p.ylabel('Number of foxes')
        p.legend()
        p.grid()
        p.xlim(0, xmax)
        p.ylim(0, ymax)
        f2.savefig(filename)
