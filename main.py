import sys

from PyQt6 import QtWidgets

from ui import MainWindow

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	# main_ui = MainApp()
	# main_ui.setup_ui(main_window)

	sys.exit(app.exec())
