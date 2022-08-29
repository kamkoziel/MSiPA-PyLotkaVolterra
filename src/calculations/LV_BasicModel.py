import numpy as np
from scipy.integrate.odepack import odeint
from src.calculations.LV_Model import LV_Model
import pylab as p



class LV_BasicModel(LV_Model):
    #initialCondition: np.ndarray

    def __init__(self, **kwargs):
        super().__init__()

        # self.r  # victims reproduce
        # self.s  # predators death
        # self.a  # hunting efficiency
        # self.b  # part of huntedVictims for predatorReproduce

        if ('r' and 's' and 'a' and 'b') in kwargs:
            self.r: np.float64 = kwargs['r']
            self.a: np.float64 = kwargs['a']
            self.b: np.float64 = kwargs['b']
            self.s: np.float64 = kwargs['s']
        else:
            self.r: np.float64 = 2
            self.s: np.float64 = 0.01
            self.a: np.float64 = 0.08
            self.b: np.float64 = 0.1

        self.time = np.linspace(0, 1000, 100, dtype = np.float64)
        self.initialCondition = np.array([10, 5])

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
        return np.array([self.r * X[0] - self.a * X[0] * X[1],
                    -self.s * X[1] + self.b * self.a * X[0] * X[1]], dtype = np.float64)

    def d2X_dt2(self, X, t=0):
        return np.array([[self.r - self.a * X[1], - self.a * X[0]],
                      [self.a * self.b * X[1], -self.s + self.a * self.b * X[0]]])

    def createSimulation(self):
        X, infodict = odeint(self.dX_dt, self.initialCondition, self.time, full_output=True, Dfun = self.d2X_dt2, )
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

        X0 = self.X_f1
        X = odeint(self.dX_dt, self.initialCondition , self.time)
        p.plot(X[:, 0], X[:, 1], lw=3.5, label='X0=(%.f, %.f)' % (self.initialCondition[0], self.initialCondition[1]))
        p.plot(X0[0],X0[1],'b.')
        p.plot(self.X_f1[0], self.X_f1[1], 'r.')

        ymax = p.ylim(ymin=0)[1]
        xmax = p.xlim(xmin=0)[1]
        nb_points = 30

        x = np.linspace(0, xmax, nb_points)
        y = np.linspace(0, ymax, nb_points)

        X1, Y1 = p.meshgrid(x, y)
        DX1, DY1 = self.dX_dt([X1, Y1])
        M = (p.hypot(DX1, DY1))
        M[M == 0] = 1.
        DX1 /= M
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
