from pyqtrecipeeditorcontroller import PyQtRecipeEditorController
from PyQt_recipe_editor_mainwindow import Ui_MainWindow
from pyqt_recipe_editor_view import RecipeEditorView
from PyQt5 import QtCore, QtGui, QtWidgets
import time 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RecipeEditorView(MainWindow) #Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()

    PyQtRecEdt = PyQtRecipeEditorController(database = [], view=ui)


    sys.exit(app.exec_()) 