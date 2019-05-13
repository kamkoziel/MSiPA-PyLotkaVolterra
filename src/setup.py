import sys
from PyQt5.QtWidgets import QApplication
from src.gui.MainWindow import App

# TODO
#  - zmiana nazw klas i plikow
#  - wyswietlanie wykresow w oknie
#  - oznaczenie punktu stabilnosci na wykresie
#  - dokumentacja (Sphinx)
#  - analiza wyników
#  - sprawozdanie + prezentacja

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())