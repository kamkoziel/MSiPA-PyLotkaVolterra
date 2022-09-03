from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget
from .ModelPlotsWidget import ModelPlotsWidget


class PlotsTabWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setStyleSheet("background: #2d3847; color: white;")

        self.__basic_model_plot = ModelPlotsWidget()
        self.__limited_model_plot = ModelPlotsWidget()
        self.__factor_model_plot = ModelPlotsWidget()

        __tabs = QTabWidget()
        __tabs.resize(300, 200)
        __tabs.setStyleSheet("""QTabBar::tab{background-color: #2d3847; 
                                            color: white; 
                                            padding: 5; 
                                            height: 50; 
                                            width: 200; 
                                            border-style: solid;
                                            border-width: 1; 
                                            border-color: #2d3847; }
                                    QTabBar::tab:selected {background-color: #192028; color: white;}
                                    QTabBar::tab:hover {background-color: #151B21; color: white;}""")

        __tabs.addTab(self.__basic_model_plot, "Podstawowy model \n Lotki-Volterry")
        __tabs.addTab(self.__limited_model_plot,
                         "Model Lotki-Volterry \nz ograniczoną pojemnością środowiska \ndla ofiar")
        __tabs.addTab(self.__factor_model_plot,
                         "Model Lotki-Volterry \nz ograniczoną pojemnością środowiska \ndla ofiar i czynnikami "
                         "zewnętrznymi")

        self.__layout = QVBoxLayout(self)
        self.__layout.addWidget(__tabs)

    @property
    def layout(self) -> 'QLayout':
        return self.__layout

    @property
    def basic_model_plot(self):
        return self.__basic_model_plot

    @property
    def limited_model_plot(self):
        return self.__limited_model_plot

    @property
    def factor_model_plot(self):
        return self.__factor_model_plot