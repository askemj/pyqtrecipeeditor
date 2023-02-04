# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt-recipe-editor-ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tablewidget import IngredientsTableWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 81, 17))
        self.label_6.setObjectName("label_6")
        self.inpRecNotes = QtWidgets.QTextEdit(self.centralwidget)
        self.inpRecNotes.setGeometry(QtCore.QRect(20, 230, 421, 91))
        self.inpRecNotes.setObjectName("inpRecNotes")

        ### Ingredient table widget 
        ###self.inpIngredients = IngredientsTableWidget(self.centralwidget)
        ###self.inpIngredients.setGeometry(QtCore.QRect(20, 330, 691, 192))
        #
        # self.inpIngredients = QtWidgets.QTableWidget(self.centralwidget)
        # self.inpIngredients.setGeometry(QtCore.QRect(20, 330, 691, 192))
        # self.inpIngredients.setObjectName("inpIngredients")
        # self.inpIngredients.setColumnCount(5)
        # self.inpIngredients.setRowCount(8)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setVerticalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setVerticalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setVerticalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setVerticalHeaderItem(6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setVerticalHeaderItem(7, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.inpIngredients.setHorizontalHeaderItem(4, item)
        # #
        self.inpTags = QtWidgets.QListWidget(self.centralwidget)
        self.inpTags.setGeometry(QtCore.QRect(460, 110, 256, 211))
        self.inpTags.setObjectName("inpTags")
        item = QtWidgets.QListWidgetItem()
        self.inpTags.addItem(item)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(460, 80, 81, 17))
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 421, 89))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.inpRecTitle = QtWidgets.QLineEdit(self.layoutWidget)
        self.inpRecTitle.setObjectName("inpRecTitle")
        self.gridLayout.addWidget(self.inpRecTitle, 0, 1, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.inpNServings = QtWidgets.QLineEdit(self.layoutWidget)
        self.inpNServings.setObjectName("inpNServings")
        self.gridLayout.addWidget(self.inpNServings, 1, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 3)
        self.inpPrepTime = QtWidgets.QLineEdit(self.layoutWidget)
        self.inpPrepTime.setObjectName("inpPrepTime")
        self.gridLayout.addWidget(self.inpPrepTime, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 4, 1, 1)
        self.inpTotTime = QtWidgets.QLineEdit(self.layoutWidget)
        self.inpTotTime.setObjectName("inpTotTime")
        self.gridLayout.addWidget(self.inpTotTime, 2, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)
        self.btnValidate = QtWidgets.QPushButton(self.centralwidget)
        self.btnValidate.setGeometry(QtCore.QRect(394, 530, 80, 25))
        self.btnValidate.setObjectName("btnValidate")
        self.btnLoadFromDB = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadFromDB.setGeometry(QtCore.QRect(259, 530, 131, 25))
        self.btnLoadFromDB.setObjectName("btnLoadFromDB")
        self.btnInsertInDB = QtWidgets.QPushButton(self.centralwidget)
        self.btnInsertInDB.setGeometry(QtCore.QRect(478, 530, 111, 25))
        self.btnInsertInDB.setObjectName("btnInsertInDB")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(593, 530, 80, 25))
        self.btnExit.setObjectName("btnExit")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(170, 530, 80, 25))
        self.btnClear.setObjectName("btnClear")
        self.disHUD = QtWidgets.QTextBrowser(self.centralwidget)
        self.disHUD.setGeometry(QtCore.QRect(200, 20, 501, 31))
        self.disHUD.setAutoFillBackground(False)
        self.disHUD.setObjectName("disHUD")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 81, 17))
        self.label_9.setObjectName("label_9")
        self.inpRecType = QtWidgets.QComboBox(self.centralwidget)
        self.inpRecType.setGeometry(QtCore.QRect(110, 170, 331, 25))
        self.inpRecType.setObjectName("inpRecType")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Recipe editor"))
        self.label_6.setText(_translate("MainWindow", "Recipe notes:"))
        # item = self.inpIngredients.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "Ny række"))
        # item = self.inpIngredients.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "Ny række"))
        # item = self.inpIngredients.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "Ny række"))
        # item = self.inpIngredients.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "Ny række"))
        # item = self.inpIngredients.verticalHeaderItem(4)
        # item.setText(_translate("MainWindow", "Ny række"))
        # item = self.inpIngredients.verticalHeaderItem(5)
        # item.setText(_translate("MainWindow", "Ny række"))
        # item = self.inpIngredients.verticalHeaderItem(6)
        # item.setText(_translate("MainWindow", "Ny række"))
        # item = self.inpIngredients.verticalHeaderItem(7)
        # item.setText(_translate("MainWindow", "Ny række"))
        # item = self.inpIngredients.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "Quantity"))
        # item = self.inpIngredients.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "Unit"))
        # item = self.inpIngredients.horizontalHeaderItem(2)
        # item.setText(_translate("MainWindow", "Name"))
        # item = self.inpIngredients.horizontalHeaderItem(3)
        # item.setText(_translate("MainWindow", "Function"))
        # item = self.inpIngredients.horizontalHeaderItem(4)
        # item.setText(_translate("MainWindow", "Category"))
        __sortingEnabled = self.inpTags.isSortingEnabled()
        self.inpTags.setSortingEnabled(False)
        item = self.inpTags.item(0)
        item.setText(_translate("MainWindow", "Ny post"))
        self.inpTags.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "Tags"))
        self.label_2.setText(_translate("MainWindow", "Recipe title:"))
        self.label_3.setText(_translate("MainWindow", "Number of Servings:"))
        self.label_4.setText(_translate("MainWindow", "Preparation/total  time:"))
        self.label_5.setText(_translate("MainWindow", "/"))
        self.label_7.setText(_translate("MainWindow", "Recipe ID"))
        self.btnValidate.setText(_translate("MainWindow", "Validate"))
        self.btnLoadFromDB.setText(_translate("MainWindow", "Load from Database"))
        self.btnInsertInDB.setText(_translate("MainWindow", "Insert in Database"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.label_9.setText(_translate("MainWindow", "Recipe Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())