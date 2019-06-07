from PyQt5.QtWidgets import  QWidget, QPushButton, QLabel, QComboBox, QRadioButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFileDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from src.calculations.LV_BasicModel import LV_BasicModel
from src.calculations.LV_LimitedCaptionModel import LV_LimitedCaptionModel
from src.calculations.LV_OutsideFactorModel import LV_OutsideFactorModel
from src.calculations.LV_Model import LV_Model
import xlsxwriter
import numpy as np
class SaveDataWidget(QDialog):


    def __init__(self, parent = None, *args):
        super(SaveDataWidget, self).__init__(parent)

        if len(args) == 3:
            self.modelLV = args[0]
        else:
            self.modelLV = args[0]
            print("Load data to method error...")

        self.modelsForSelect = args

        self.initUI()

    def initUI(self):
        self.setGeometry(500,500,400,150)

        customElementsLayout = QVBoxLayout(self)
        customElementsLayout.addWidget(QLabel("Wybierz dane do zapisu:"))

        self.radioButton = QRadioButton("Model podstawowy Lotki Voltery",self)
        self.radioButton.setChecked(True)
        self.radioButton.number = 0
        self.radioButton.toggled.connect(self.onClicked)
        customElementsLayout.addWidget(self.radioButton)

        self.radioButton = QRadioButton("Model z ograniczoną pojemnością", self)
        self.radioButton.number = 1
        self.radioButton.toggled.connect(self.onClicked)
        customElementsLayout.addWidget(self.radioButton)

        self.radioButton = QRadioButton("Model z z czynnikime zewnętrznym", self)
        self.radioButton.number = 2
        self.radioButton.toggled.connect(self.onClicked)
        customElementsLayout.addWidget(self.radioButton)

        self.aproveButton = QPushButton("Potwierdź")
        self.aproveButton.clicked.connect(self.aproveSave)
        self.cancelButton = QPushButton("Anuluj")
        self.cancelButton.clicked.connect(self.closeWidget)


        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(self.aproveButton)
        buttonsLayout.addWidget(self.cancelButton)

        customElementsLayout.addLayout(buttonsLayout)

        self.setModal(True)
        self.setWindowTitle('Logowanie')
        self.show()

    def onClicked(self):
        self.radioButton = self.sender()
        if self.radioButton.isChecked():
            self.modelLV = self.modelsForSelect[self.radioButton.number]
            print("Number is %s" % (self.radioButton.number))

    @pyqtSlot()
    def closeWidget(self):
        self.close()

    @pyqtSlot()
    def aproveSave(self):
        if self.modelLV != None:

            data1,data2 = self.modelLV.getPopulationsData()
            data = np.zeros((len(data1), 3))
            fileDialog = QFileDialog.getSaveFileName()

            workbook = xlsxwriter.Workbook(fileDialog[0])
            worksheet = workbook.add_worksheet()

            row=0
            time = self.modelLV.getSimulationTime()
            while(row<len(data1)):
                data[row][0] = time[row]
                data[row][1] = data1[row]
                data[row][2] = data2[row]
                row += 1

            row = 1
            col = 0
            worksheet.write(0, 0,"Time")
            worksheet.write(0, 1, "Victims")
            worksheet.write(0, 2, "Predators")

            for time, vic, predo in data:
                worksheet.write(row, col, time)
                worksheet.write(row, col+1, vic)
                worksheet.write(row, col + 2, predo)
                row += 1

            timeForChart = '=Sheet1!$A$2:$A$' + str(row)
            victimsForChart = '=Sheet1!$B$2:$B$' + str(row)
            predatorsForChart = '=Sheet1!$C$2:$c$' + str(row)

            chart = workbook.add_chart({'type': 'scatter', 'subtype': 'smooth'})
            chart.add_series({
                'categories': timeForChart ,
                'values':  victimsForChart,
                'name': '=Sheet1!$B$1' })
            chart.add_series({
                'categories': timeForChart,
                'values': predatorsForChart,
                'name': '=Sheet1!$C$1'})

            worksheet.insert_chart('E6', chart)
            workbook.close()

        else:
            print("Brak modelu danych")

        self.close()






