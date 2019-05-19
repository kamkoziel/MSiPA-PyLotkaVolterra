import numpy as np
from numpy.core._multiarray_umath import ndarray
from scipy.integrate.odepack import odeint
import pylab as p
from src.calculations.LV_BasicModel import LV_BasicModel
"""
TODO generowanie wykresu fazowego

"""

class LV_LimitedCaptionModel(LV_BasicModel):
    X_f0: ndarray
    X_f1: ndarray
    X_f2: ndarray

    #initialCondition: np.ndarray

    def __init__(self,r = 1, s = 0.1,a = 1.5,b = 0.75, K=900):

        self.r, self.s, self.a, self.b ,self.K = r,s,a,b,K
        self.time = np.linspace(0, 1000, 100)
        self.initialCondition = np.array([10, 5])

        # stability points where right side of expr is equal 0
        self.X_f0 = np.array([0., 0.])
        self.X_f1 = np.array([K,0])
        self.X_f2 = np.array([self.s / (self.b * self.a),
                              (self.r*self.s-self.K*self.a*self.b*self.r)/ (self.K*self.a**2*self.b)])


    def setParamsValues(self,r,s,a,b,K):
        self.r = r
        self.s = s
        self.a = a
        self.b = b
        self.K = K

    #not important propably for drop
    def switch_state_point(self,pointNum):
        switcher = {
            0: self.X_f0,
            1: self.X_f1,
            2: self.X_f2
        }
        return switcher.get(pointNum % 3,"nothing")

    def updateStabilityPoints(self,r,s,a,b,K):

        self.setParamsValues(r,s,a,b,K)

        self.X_f1 = np.array([K, 0])
        self.X_f2 = np.array([self.s / (self.b * self.a),
                              (self.r * self.s - self.K * self.a * self.b * self.r) / (self.K * self.a ** 2 * self.b)])

    def dX_dt(self, X, t=0):
        return np.array([self.r * X[0]*(1 - (X[0]/self.K)) - self.a * X[0] * X[1],
                      -self.s * X[1] + self.b * self.a * X[0] * X[1]])


    def d2X_dt2(self, X, t=0):
        """ Return the Jacobian matrix evaluated in X. """
        return np.array([[(-(2*X[0]-self.K)*self.r+self.K*self.a*X[1])/self.K, - self.a * X[0]],
                      [self.a * self.b * X[1], -self.s + self.a * self.b * X[0]]])

    def createSimulation(self):
        X, infodict = odeint(self.dX_dt, self.initialCondition, self.time, full_output=True)
        return X

    def makeDataForSimulationPlot(self):
        X = self.createSimulation()
        victims, predators = X.T
        return victims, predators

    def exportFigToPNG(self,fileName):
        X = self.createSimulation()
        rabbits, foxes = self.makeDataForSimulationPlot()
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

        # -------------------------------------------------------
        # plot trajectories
        # for v, col in zip(values, vcolors):
        X0 = self.X_f1  # starting point
        X = odeint(self.dX_dt, self.initialCondition, self.time)  # we don't need infodict here
        p.plot(X[:, 0], X[:, 1], lw=3.5, label='X0=(%.f, %.f)' % (self.initialCondition[0], self.initialCondition[1]))
        # p.plot(X0[0], X0[1], 'b.')
        # p.plot(self.X_f2[0], self.X_f2[1], 'r.')

        # -------------------------------------------------------
        # define a grid and compute direction at each point
        ymax = p.ylim(ymin=0)[1]  # get axis limits
        xmax = p.xlim(xmin=0)[1]
        nb_points = 30

        # x = np.linspace(0, xmax, nb_points)
        # y = np.linspace(0, ymax, nb_points)
        #
        # X1, Y1 = p.meshgrid(x, y)  # create a grid
        # DX1, DY1 = self.dX_dt([X1, Y1])  # compute growth rate on the gridt
        # M = (p.hypot(DX1, DY1))  # Norm of the growth rate
        # M[M == 0] = 1.  # Avoid zero division errors
        # DX1 /= M  # Normalize each arrows
        # DY1 /= M

        p.title('Trajectories and direction fields')
        #p.quiver(X1, Y1, DX1, DY1, M, pivot='mid')
        p.xlabel('Number of rabbits')
        p.ylabel('Number of foxes')
        p.legend()
        p.grid()
        p.xlim(0, xmax)
        p.ylim(0, ymax)
        f2.savefig(filename)
