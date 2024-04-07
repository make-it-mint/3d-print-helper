import sys, os, json
from PyQt6 import QtCore, QtGui, QtWidgets
from ui import *



        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    #main_ui = MainApp()
    #main_ui.setup_ui(main_window)
    
    sys.exit(app.exec())