from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QHBoxLayout, QWidget
from src.plots.plotCanvas import PlotCanvas
from src.plots.plotPopulationEvolution import PlotPopulationEvolution

from src.gui.TabWidget import tabWidget

class PlotTabWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setStyleSheet("background: #2d3847; color: white;")

        self.plot1 = tabWidget()
        self.plot2 = tabWidget()
        self.plot3 = tabWidget()

        self.tabs = QTabWidget()
        self.tabs.resize(300, 200)
        self.tabs.setStyleSheet("""QTabBar::tab{background-color: #2d3847; 
                                            color: white; 
                                            padding: 5; 
                                            height: 50; 
                                            width: 200; 
                                            border-style: solid;
                                            border-width: 1; 
                                            border-color: #2d3847; }
                                    QTabBar::tab:selected {background-color: #192028; color: white;}
                                    QTabBar::tab:hover {background-color: #151B21; color: white;}""")

        self.tabs.addTab(self.plot1, "Podstawowy model \n Lotki-Volterry")
        self.tabs.addTab(self.plot2, "Model Lotki-Volterry \nz ograniczoną pojemnością środowiska \ndla ofiar")
        self.tabs.addTab(self.plot3, "Model Lotki-Volterry \nz ograniczoną pojemnością środowiska \ndla ofiar i czynnikami zewnętrznymi")


        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
