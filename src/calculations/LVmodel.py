import numpy as np
from scipy.integrate.odepack import odeint
#from numpy import array
#from numpy.core._multiarray_umath import ndarray
from sympy import *
import pylab as p


class LVmodel():
    #initialCondition: np.ndarray

    def __init__(self,r = 1, s = 0.1,a = 1.5,b = 0.75):
        # self.r  # victims reproduce                               a
        # self.s  # predators death                                 c
        # self.a  # hunting efficiency                              b
        # self.b  # part of huntedVictims for predatorReproduce     d

        self.r, self.s, self.a, self.b = r,s,a,b
        self.time = np.linspace(0, 1000, 100)
        self.initialCondition = np.array([10, 5])

        # stability points where right side of expr is equal 0
        self.X_f0 = np.array([0., 0.])
        self.X_f1 = np.array([self.s / (self.b * self.a), self.r / self.a])
        # all(dX_dt(X_f0) == zeros(2)) and all(dX_dt(X_f1) == zeros(2))  # => True

        #self.A_f0 = d2X_dt2(X_f0)



    def setParamsValues(self,r,s,a,b):
        self.r = r
        self.s = s
        self.a = a
        self.b = b

    def updateStabilityPoints(self,r,s,a,b):
        self.setParamsValues(r,s,a,b)
        self.X_f1 = np.array([self.s / (self.b * self.a), self.r / self.a])

    def dX_dt(self, X, t=0):
        return np.array([self.r * X[0] - self.a * X[0] * X[1],
                      -self.s * X[1] + self.b * self.a * X[0] * X[1]])

    def d2X_dt2(self, X, t=0):
        """ Return the Jacobian matrix evaluated in X. """
        return np.array([[self.r - self.a * X[1], - self.a * X[0]],
                      [self.a * self.b * X[1], -self.s + self.a * self.b * X[0]]])

    def setSimulationTime(self, start=0, stop=1000, samplesNumber=1000):
        """
        py:method:: def setSimulationTime(self,start = 0, stop =1000, samplesNumber = 1000)

        method set the time of simulation its important when we creating a plots od ODE resolve

        :param int start: start point of simulation
        :param int stop: end point of simulation
        :param int samplesNumber: number of element
        :return: ndarray
        """
        self.time = np.linspace(start, stop, samplesNumber)
        return self.time

    def setInitialonditions(self, V=10, P=5):
        self.initialCondition = np.array([V, P])
        return self.initialCondition

    def createSimulation(self):
        X, infodict = odeint(self.dX_dt, self.initialCondition, self.time, full_output=True)
        return X

    def makeDataForSimulationPlot(self):
        X = self.createSimulation()
        victims, predators = X.T
        return victims, predators

    def exportFigToPNG(self):
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
        f1.savefig('rabbits_and_foxes_1.png')


        # jackMatrix.subs([(V, zeroPoints[0][0]), (P, zeroPoints[0][1])]).eigenvals()
