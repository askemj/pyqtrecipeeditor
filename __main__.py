from pyqtrecipeeditorcontroller import PyQtRecipeEditorController
from PyQtRecipeEditorUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    PyQtRecEdt = PyQtRecipeEditorController(database = [], view=ui)

    sys.exit(app.exec_())