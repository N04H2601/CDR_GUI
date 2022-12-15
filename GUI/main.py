import sys
from PyQt5.QtWidgets import QApplication
from interface import Window

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
