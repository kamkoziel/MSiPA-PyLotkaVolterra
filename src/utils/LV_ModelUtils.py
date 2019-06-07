import numpy as np
from src.calculations.LV_BasicModel import *
import os




class ModelUtils():

    def __init__(self, LV_Model: LV_BasicModel):
        self.LV_Model = LV_Model

    def SaveModelData(self):
        dataToSave = self.LV_Model.getPopulationsData()
        print(dataToSave)