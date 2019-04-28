from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget
from src.plots.plotCanvas import PlotCanvas

class PlotTabWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setStyleSheet("background: #2d3847; color: white;")

        self.plot1 = PlotCanvas(self)
        self.plot2 = PlotCanvas()
        self.plot3 = PlotCanvas()
        self.plot4 = PlotCanvas(self, width=5, height=4)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.resize(300, 200)
        self.tabs.setStyleSheet("""QTabBar::tab{background-color: #2d3847; 
                                            color: white; 
                                            padding: 5; 
                                            height: 20; 
                                            width: 80; 
                                            border-style: solid;
                                            border-width: 1; 
                                            border-color: #2d3847; }
                                    QTabBar::tab:selected {background-color: #192028; color: white;}
                                    QTabBar::tab:hover {background-color: #151B21; color: white;}""")

        # Add tabs
        self.tabs.addTab(self.plot1, "Tab 1")
        self.tabs.addTab(self.plot2, "Tab 2")
        self.tabs.addTab(self.plot3, "Tab 3")
        self.tabs.addTab(self.plot4, "Tab 4")

        self.layout = QVBoxLayout(self)
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
