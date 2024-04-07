from PyQt6 import QtCore, QtGui, QtWidgets
import math, sys
import re
import subprocess
from settings import *
from serial.tools.list_ports import comports as list_comports

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.slicer_path = self.get_slicer_path()

        self.setWindowTitle("My App")
        self.resize(500,400)

        layout = QtWidgets.QVBoxLayout()
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(f"background-color:{BACKGROUND_COLOR}")


        self.cb_profile = QtWidgets.QComboBox()
        self.cb_profile.setFont(BASIC_FONT_LARGE)
        self.cb_profile.addItem("Prusa Mini")
        self.cb_profile.addItem("Prusa MK3")
        self.cb_profile.addItem("Prusa MK4")


        bt_filepath = QtWidgets.QPushButton("Dateipfad auswählen")
        bt_filepath.setFont(BASIC_FONT_LARGE)
        bt_filepath.clicked.connect(self.select_file)

        self.txt_filepath = QtWidgets.QTextEdit("Keine Datei ausgewählt")
        self.txt_filepath.setFont(BASIC_FONT_MID)
        self.txt_filepath.setReadOnly(True)

        self.bt_search_usb = QtWidgets.QPushButton("USB Stick suchen")
        self.bt_search_usb.setFont(BASIC_FONT_LARGE)
        self.bt_search_usb.clicked.connect(self.find_usb_drive)

        bt_slice = QtWidgets.QPushButton("SLICEN")
        bt_slice.setFont(BASIC_FONT_LARGE)
        bt_slice.clicked.connect(self.start_slicing)

        bt_exe_path = QtWidgets.QPushButton("Slicer Pfad")
        bt_exe_path.setFont(BASIC_FONT_LARGE)
        bt_exe_path.clicked.connect(self.set_slicer_path)

        bt_close = QtWidgets.QPushButton("Beenden")
        bt_close.setFont(BASIC_FONT_LARGE)
        bt_close.clicked.connect(self.close)
        
        layout.addWidget(self.cb_profile)
        layout.addWidget(bt_filepath)
        layout.addWidget(self.txt_filepath)
        layout.addWidget(self.bt_search_usb)
        layout.addWidget(bt_slice)
        layout.addWidget(bt_exe_path)
        layout.addWidget(bt_close)

        
        self.setCentralWidget(widget)

        self.show()


    def start_slicing(self):
        save_path = QtWidgets.QFileDialog.getSaveFileName(self, 'GCode Speichern',filter="(*.gcode)")
        print(save_path[0])
        #TODO Slice bash command


    def find_usb_drive(self):
        comports = [comport.device for comport in list_comports()]
        print(comports)

    def get_slicer_path(self):
        f = open("slicerpath.txt", "r")
        return f.read()

    def set_slicer_path(self): 
        dialog = QtWidgets.QFileDialog.getOpenFileName(self, "Slicerpfad auswählen", filter="EXE (*.exe)")
        f = open("slicerpath.txt", "w")
        f.write(dialog[0])
        f.close()
        self.slicer_path = dialog[0]

    def select_file(self):
        dialog = QtWidgets.QFileDialog.getOpenFileName(self, "Dateipfad auswählen", filter="3D Models (*.stl)")
        #print(dialog)
        self.txt_filepath.setText(dialog[0])

    def close(self):
        sys.exit()