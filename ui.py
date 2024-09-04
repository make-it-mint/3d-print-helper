from PyQt6 import QtCore, QtGui, QtWidgets
import math, sys, os, time, winsound
from settings import *
from os import listdir
from os.path import isfile, join

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.slicer_path = self.get_slicer_path()
    

        self.setWindowTitle("3DPrintHelper")
        self.resize(500,400)

        layout = QtWidgets.QVBoxLayout()
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(f"background-color:{BACKGROUND_COLOR}")


        self.cb_profile = QtWidgets.QComboBox()
        self.cb_profile.setFont(BASIC_FONT_LARGE)
        config_files = [f for f in listdir("config_files/") if isfile(join("config_files/", f))]
        for file in config_files:
            self.cb_profile.addItem(file)



        bt_filepath = QtWidgets.QPushButton("Dateipfad auswählen")
        bt_filepath.setFont(BASIC_FONT_LARGE)
        bt_filepath.clicked.connect(self.select_file)
        self.print_file_stl = None

        self.txt_filepath = QtWidgets.QTextEdit("Keine Datei ausgewählt")
        self.txt_filepath.setFont(BASIC_FONT_MID)
        self.txt_filepath.setReadOnly(True)


        bt_slice = QtWidgets.QPushButton("Slicen")
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
        layout.addWidget(bt_slice)
        layout.addWidget(bt_exe_path)
        layout.addWidget(bt_close)

        
        self.setCentralWidget(widget)

        self.show()


    def beep(self, success):
        #einfacher Beep für Erfolg, doppelter Beep für Fehler
        duration = 300  # milliseconds
        freq = 440
        if success:
            winsound.Beep(freq, duration)
        else:
            winsound.Beep(freq, duration)
            time.sleep(.3)
            winsound.Beep(freq, duration)
        
    def start_slicing(self):
        if self.print_file_stl == None:
            self.beep(False)
            return False
        save_path = QtWidgets.QFileDialog.getSaveFileName(self, 'GCode Speichern',filter="(*.gcode)")
        try:
            os.system(f"{self.get_slicer_path()} -g  {self.print_file_stl} -o {save_path[0]} --load config_files/{self.cb_profile.currentText()}")
            self.beep(True)
        except Exception as e:
            self.beep(False)
            print(e)


    def get_slicer_path(self):
        f = open("slicerpath.txt", "r")
        return f.read()
    
    def refactor_path(self, path):
        #cmd kann nicht mit Leerzeichen in Dateipfaden umgehen, deswegen werden die Pfade mit Leerzeichen korrigiert
        path = path.split("/")
        new_path = ''
        for directory in path:
            if ' ' in directory:
                new_path = f'{new_path}/"{directory}"'
            else:
                if len(new_path) == 0:
                    new_path  = f'{directory}'
                else:
                    new_path  = f'{new_path}/{directory}'
        return new_path

    def set_slicer_path(self): 
        dialog = QtWidgets.QFileDialog.getOpenFileName(self, "Slicerpfad auswählen", filter="EXE (*.exe)")
        if dialog[0].endswith("prusa-slicer-console.exe"):
            path = self.refactor_path(dialog[0])
            f = open("slicerpath.txt", "w")
            f.write(path)
            f.close()
            self.slicer_path = path
            self.beep(True)
        else:
            self.beep(False)

    def select_file(self):
        print_file = QtWidgets.QFileDialog.getOpenFileName(self, "Dateipfad auswählen", filter="3D Models (*.stl)")
        if print_file[0].endswith(".stl"):
            self.print_file_stl = self.refactor_path(print_file[0])
            self.txt_filepath.setText(print_file[0])
            self.beep(True)
        else:
            self.beep(False)

    def close(self):
        sys.exit()