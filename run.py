from pyqtrecipeeditorcontroller import PyQtRecipeEditorController
from databasepersistence import DatabasePersistence
from PyQt_recipe_editor_mainwindow import Ui_MainWindow
from pyqt_recipe_editor_view import RecipeEditorView
from PyQt5 import QtCore, QtGui, QtWidgets
import time 

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RecipeEditorView(MainWindow) #Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    database = DatabasePersistence()
    PyQtRecEdt = PyQtRecipeEditorController(database = database, view=ui) 


    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()
