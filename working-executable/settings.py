from PyQt6 import QtGui, QtWidgets

BACKGROUND_COLOR = "rgb(62, 110, 145)"
BASIC_FONT_LARGE = QtGui.QFont('Arial', 28)
BASIC_FONT_MID = QtGui.QFont('Arial', 18)

SIZE_POLICY = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
SIZE_POLICY.setHorizontalStretch(1)
SIZE_POLICY.setVerticalStretch(1)