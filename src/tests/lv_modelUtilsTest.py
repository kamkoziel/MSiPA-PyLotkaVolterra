from src.calculations.LV_BasicModel import *
from src.utils.LV_ModelUtils import ModelUtils

if __name__ == '__main__':
    LVModel = LV_BasicModel()
    LVModel.setParamsValues(0.4,0.02,0.003, 0.001)
    LVModel.getPopulationsData()
    LVModel.createSimulation()
    LVModel.exportFigToPNG("razDwaTrzy.png")
    testOjc = ModelUtils(LVModel)
    testOjc.SaveModelData()