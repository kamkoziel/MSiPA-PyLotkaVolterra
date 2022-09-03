import numpy as np
from numpy.core._multiarray_umath import ndarray
from scipy.integrate.odepack import odeint
import pylab as p
from calculations.LV_Model import LV_Model


class LV_LimitedCaptionModel(LV_Model):
    X_f0: ndarray
    X_f1: ndarray
    X_f2: ndarray

    # initialCondition: np.ndarray

    def __init__(self, **kwargs):
        super().__init__()

        if ('r' and 's' and 'a' and 'b' and 'K') in kwargs:
            self.r = kwargs['r']
            self.a = kwargs['a']
            self.b = kwargs['b']
            self.s = kwargs['s']
            self.K = kwargs['K']
        else:
            self.r = 2
            self.s = 0.01
            self.a = 0.08
            self.b = 0.1
            self.K = 100

        self.time = np.linspace(0, 1000, 100)
        self.initialCondition = np.array([10, 5])

        self.X_f0 = np.array([0., 0.])
        self.X_f1 = np.array([self.K, 0])
        self.X_f2 = np.array([self.s / (self.b * self.a),
                              -(self.r * self.s - self.K * self.a * self.b * self.r) / (self.K * self.a ** 2 * self.b)])

    def setParamsValues(self, **kwargs):
        self.r = kwargs['r']
        self.s = kwargs['s']
        self.a = kwargs['a']
        self.b = kwargs['b']
        self.K = kwargs['K']
        self.X_f2 = np.array([self.s / (self.b * self.a),
                              -(self.r * self.s - self.K * self.a * self.b * self.r) / (self.K * self.a ** 2 * self.b)])

    def updateStabilityPoints(self, r, s, a, b, K):

        self.setParamsValues(r=r, s=s, a=a, b=b, K=K)
        self.X_f1 = np.array([K, 0])
        self.X_f2 = np.array([self.s / (self.b * self.a),
                              (self.r * self.s - self.K * self.a * self.b * self.r) / (self.K * self.a ** 2 * self.b)])

    def dX_dt(self, X, t=0):
        return np.array([self.r * X[0] * (1 - (X[0] / self.K)) - self.a * X[0] * X[1],
                         -self.s * X[1] + self.b * self.a * X[0] * X[1]])

    def d2X_dt2(self, X, t=0):
        return np.array([[(-(2 * X[0] - self.K) * self.r + self.K * self.a * X[1]) / self.K, - self.a * X[0]],
                         [self.a * self.b * X[1], -self.s + self.a * self.b * X[0]]])

    def createSimulation(self):
        X, infodict = odeint(self.dX_dt, self.initialCondition, self.time, full_output=True)
        return X

    def getPopulationsData(self):
        X = self.createSimulation()
        victims, predators = X.T
        return victims, predators

    def exportFigToPNG(self, fileName):
        X = self.createSimulation()
        rabbits, foxes = self.getPopulationsData()
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

        ymax = p.ylim(ymin=0)[1]
        xmax = p.xlim(xmin=0)[1]
        nb_points = 30

        p.title('Trajectories and direction fields')
        p.xlabel('Number of rabbits')
        p.ylabel('Number of foxes')
        p.legend()
        p.grid()
        p.xlim(0, xmax)
        p.ylim(0, ymax)
        f2.savefig(filename)
