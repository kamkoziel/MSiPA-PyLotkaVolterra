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

    def __init__(self,r = 1, s = 0.1,a = 1.5,b = 0.75, K=100):

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
        return np.array([self.r * X[0]*(1- (X[0]*self.K )) - self.a * X[0] * X[1],
                      -self.s * X[1] + self.b * self.a * X[0] * X[1]])

    # TODO  |
    #      \/
    #   start refractoring form here
    #  first Jakobian in wxMaxima -> begin is, have to finish
    def d2X_dt2(self, X, t=0):
        """ Return the Jacobian matrix evaluated in X. """
        return np.array([[(-(2*X[0]-self.K)*self.r+self.K*self.a*X[1])/self.K, - self.a * X[0]],
                      [self.a * self.b * X[1], -self.s + self.a * self.b * X[0]]])


