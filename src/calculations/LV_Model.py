from abc import ABCMeta, abstractmethod
import numpy as np

class LV_Model(object):

    __metaclass__ = ABCMeta


    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def setParamsValues(self, **kwargs):
        pass

    @abstractmethod
    def updateStabilityPoints(self, **kwargs):
        pass

    @abstractmethod
    def dX_dt(self, X, t=0):
        pass

    @abstractmethod
    def getPopulationsData(self):
        pass

    def setInitialConditions(self, V=10, P=5):
        self.initialCondition = np.array([V, P])
        return self.initialCondition

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

    def getSimulationTime(self):
        return self.time
