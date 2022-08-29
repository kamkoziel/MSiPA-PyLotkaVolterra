import numpy as np
from numpy.core._multiarray_umath import ndarray
from scipy.integrate.odepack import odeint
from scipy.integrate.quadpack import  quad
import pylab as p
from src.calculations.LV_Model import LV_Model


class LV_OutsideFactorModel(LV_Model):
    X_f0: ndarray
    X_f1: ndarray
    X_f2: ndarray
    time: ndarray

    def __init__(self, **kwargs):
        super().__init__()

        if ('r' and 's' and 'a' and 'b' and 'K' and 'g' and 'h') in kwargs:
            self.r = kwargs['r']
            self.a = kwargs['a']
            self.b = kwargs['b']
            self.s = kwargs['s']
            self.K = kwargs['K']
            self.g = kwargs['g']
            self.h = kwargs['h']
        else:
            self.r = 2
            self.s = 0.01
            self.a = 0.08
            self.b = 0.1
            self.K = 100
            self.g = 3
            self.h = 0.5

        self.time = np.linspace(0, 1000, 100)
        self.initialCondition = np.array([10, 5])

        self.X_f0 = np.array([0., 0.])
        self.X_f1 = np.array([((self.K*(self.r + self.h))/self.r), 0])
        self.X_f2 = np.array([(self.s + self.g)/(self.a*self.b),
                              - (self.r*self.s+self.g*self.r-self.K*self.a*self.b*self.r-self.K*self.a*self.b*self.h) / (self.K * self.a ** 2 * self.b)])

    def setParamsValues(self,**kwargs):
        self.r = kwargs['r']
        self.s = kwargs['s']
        self.a = kwargs['a']
        self.b = kwargs['b']
        self.K = kwargs['K']
        self.g = kwargs['g']
        self.h = kwargs['h']
        self.X_f2 = np.array([(self.s + self.g) / (self.a * self.b),
                              - (self.r * self.s + self.g * self.r - self.K * self.a * self.b * self.r - self.K * self.a * self.b * self.h) / (self.K * self.a ** 2 * self.b)])

    def updateStabilityPoints(self, r, s, a, b, K, h, g):
        self.setParamsValues(r = r, s = s, a = a, b = b, K = K, h = h, g = g)

        self.X_f1 = np.array([((self.K * (self.r - self.h)) / self.r), 0])
        self.X_f2 = np.array([(self.s + self.g) / (self.a * self.b),
                              - (self.r * self.s + self.g * self.r - self.K * self.a * self.b * self.r - self.K * self.a * self.b * self.h) / (self.K * self.a ** 2 * self.b)])

    def dX_dt(self, X, t=0):
        return np.array([self.r * X[0] * (1 - (X[0] / self.K)) - self.a * X[0] * X[1]+self.h * X[0],
                         -(self.s + self.g) * X[1] + self.b * self.a * X[0] * X[1]])

    def d2X_dt2(self, X, t=0):
        return np.array([[(-(2 * X[0] - self.K) * self.r + self.K * self.a * X[1]) / self.K, - self.a * X[0]],
                         [self.a * self.b * X[1], -self.s-self.g + self.a * self.b * X[0]]])

    def createSimulation(self):
        X, infodict = odeint(self.dX_dt, self.initialCondition, self.time, full_output=True)
        return X

    def getPopulationsData(self):
        X = self.createSimulation()
        victims, predators = X.T
        return victims, predators

    def exportFigToPNG(self,fileName):

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

    def exportTrajectoriesFigToPNG(self, filename):

        f2 = p.figure()

        X0 = self.X_f1
        X = odeint(self.dX_dt, self.initialCondition, self.time)
        p.plot(X[:, 0], X[:, 1], lw=3.5, label='X0=(%.f, %.f)' % (self.initialCondition[0], self.initialCondition[1]))

        ymax = p.ylim(ymin=0)[1]  # get axis limits
        xmax = p.xlim(xmin=0)[1]


        p.title('Trajectories and direction fields')
        p.xlabel('Number of rabbits')
        p.ylabel('Number of foxes')
        p.legend()
        p.grid()
        p.xlim(0, xmax)
        p.ylim(0, ymax)
        f2.savefig(filename)